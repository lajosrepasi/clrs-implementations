"""
B-tree implementation based on CLRS Chapter 18.

Nodes are persisted to disk as JSON files to simulate
the DISK-READ and DISK-WRITE operations used in the textbook.
"""

from __future__ import annotations

import os
import pathlib
import uuid
from math import floor
from typing import Any, cast

import jsonpickle

from clrs.chapter10.my_queue import Queue
from clrs.chapter11.hash_table_chaining import HashTableChaining as HashTable

DATA_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/data"


class KV:
    """
    Key-value pair stored inside a B-tree node.
    """

    def __init__(self, key: Any, value: Any) -> None:
        self.k: Any = key
        self.v: Any = value

    def __str__(self) -> str:
        return "[{0}: {1}]".format(self.k, self.v)


class Node:
    """
    A B-tree node containing keys and child references.
    """

    def __init__(self, btree: BTree):
        self.leaf: bool = True
        self.kvs: list[KV] = []
        self.children: list[Node | str] = []
        self.btree: BTree = btree
        self.id: str = str(uuid.uuid4())[:8]

    def __getstate__(self) -> dict[str, Any]:
        state = self.__dict__.copy()

        if len(self.children) > 0:
            state["children"] = [
                (c if type(c) == str else c.get_name()) for c in state["children"]
            ]

        if "btree" in state:
            del state["btree"]

        return state

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__dict__.update(state)

    def __len__(self) -> int:
        return len(self.kvs)

    def is_full(self) -> bool:
        return len(self) == 2 * self.btree.min_degree - 1

    def split_child(self, i: int) -> None:
        """
        Split the i-th full child of this node.
        """
        node_to_split = self.children[i]
        new_node = Node(self.btree)
        assert isinstance(node_to_split, Node)
        new_node.leaf = node_to_split.leaf

        min_degree = self.btree.min_degree

        kv_index_to_move_up = floor(min_degree - 0.5)
        kv_to_move_up = node_to_split.kvs[kv_index_to_move_up]

        new_node.children = node_to_split.children[kv_index_to_move_up + 1 :]
        new_node.kvs = node_to_split.kvs[kv_index_to_move_up + 1 :]

        node_to_split.children = node_to_split.children[: kv_index_to_move_up + 1]
        node_to_split.kvs = node_to_split.kvs[:kv_index_to_move_up]

        self.kvs.insert(i, kv_to_move_up)
        self.children.insert(i + 1, new_node.get_name())

        self.btree.disk_write(self)
        self.btree.disk_write(node_to_split)
        self.btree.disk_write(new_node)

    def insert_non_full(self, kv: KV) -> None:
        """
        Insert a key-value pair into a non-full subtree.
        """
        i = len(self) - 1

        if self.leaf:
            while i >= 0 and self.kvs[i].k > kv.k:
                i -= 1

            self.kvs.insert(i + 1, kv)
            self.btree.disk_write(self)
        else:
            while i >= 0 and self.kvs[i].k > kv.k:
                i -= 1

            i += 1

            node_to_continue = self.btree.disk_read(self, i)
            assert isinstance(node_to_continue, Node)

            if node_to_continue.is_full():
                self.split_child(i)

                if self.kvs[i].k < kv.k:
                    i += 1

            self.btree.disk_read(self, i)
            ith_child = self.children[i]
            assert isinstance(ith_child, Node)
            ith_child.insert_non_full(kv)
            self.children[i] = ith_child.get_name()

    def get_name(self) -> str:
        return self.id

    def add_child(self, node: Node) -> None:
        self.children.append(node.get_name())

    def search(self, key: Any) -> tuple[Node | None, int | None]:
        """
        Search for a key in the subtree rooted at this node.
        """
        found_index = 0
        n = len(self.kvs)

        while found_index < n and self.kvs[found_index].k < key:
            found_index += 1

        if found_index < n and self.kvs[found_index].k == key:
            return (self, found_index)

        if self.leaf:
            return (None, None)

        self.btree.disk_read(self, found_index)

        ith_child = self.children[found_index]
        assert isinstance(ith_child, Node)
        node, found_index = ith_child.search(key)

        return (node, found_index)

    def __str__(self) -> str:
        kvs_str = str([str(kv) for kv in self.kvs])
        return kvs_str


class BTree:
    """
    A B-tree supporting search and insertion.
    """

    def __init__(self, min_degree: int | None = None) -> None:
        if min_degree is None:
            self.min_degree: int = 2
        else:
            self.min_degree: int = min_degree

        self.root = Node(self)
        self.disk_write(self.root)

        self.cache = HashTable()
        self.cache_lru = Queue(4)

    def search(self, key: Any) -> tuple[Node | None, int | None]:
        if self.root is not None:
            return self.root.search(key)

        return (None, None)

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair into the tree.
        """
        kv = KV(key, value)

        node = self.root

        if self.root.is_full():
            node = self.split_root()

        node.insert_non_full(kv)

    def split_root(self) -> Node:
        """
        Split the root when it becomes full.
        """
        new_root = Node(self)
        new_root.leaf = False
        new_root.add_child(self.root)

        old_root = self.root
        self.root = new_root

        self.disk_write(self.root)
        self.disk_write(old_root)

        self.disk_read(self.root, 0)
        self.root.split_child(0)

        first_child = self.root.children[0]
        assert isinstance(first_child, Node)
        self.root.children[0] = first_child.get_name()
        return new_root

    def disk_read(self, node: Node, i: int) -> Node | str:
        """
        Load the i-th child from disk if necessary.
        """
        to_read = node.children[i]

        if isinstance(to_read, str):
            node_from_cache = self.get_node_from_cache(to_read)
            if node_from_cache is None:
                print("DISK READ:", to_read)
                f = open("{0}/{1}.json".format(DATA_PATH, to_read), "r")
                decoded_node = jsonpickle.decode(f.read(), keys=True)
                assert isinstance(decoded_node, Node)
                decoded_node.btree = self
                node.children[i] = decoded_node

                self.add_node_to_cache(to_read, decoded_node)
            else:
                print("FROM CACHE:", to_read)
                node.children[i] = node_from_cache

        return node.children[i]

    def get_node_from_cache(self, id: Any) -> Node:
        return self.cache[id]

    def add_node_to_cache(self, id: str, node: Node) -> None:
        try:
            self.try_to_add_to_cache(id, node)
        except Exception as e:
            node_to_remove = self.cache_lru.dequeue()
            del self.cache[node_to_remove.id]
            self.try_to_add_to_cache(id, node)

    def try_to_add_to_cache(self, id: str, node: Node) -> None:
        self.cache_lru.enqueue(node)
        self.cache[id] = node

    def disk_write(self, node: Node) -> None:
        """
        Persist a node to disk.
        """
        name = None

        if node == self.root:
            name = "ROOT"
        else:
            name = node.get_name()

        json: str = cast(str, jsonpickle.encode(node, keys=True))
        with open("{0}/{1}.json".format(DATA_PATH, name), "w") as f:
            f.write(json)
            f.close()


def clean() -> None:
    data = os.listdir(DATA_PATH)

    for item in data:
        if item.endswith(".json"):
            os.remove(os.path.join(DATA_PATH, item))


def search_and_print(b_tree: BTree, key: Any, expected_value: Any):
    node, i = b_tree.search(key)
    assert isinstance(node, Node)
    assert i is not None
    v = node.kvs[i].v
    assert v == expected_value
    if node is not None:
        print(v)
    else:
        print(node)


def main():
    clean()
    b_tree = BTree()

    b_tree.insert(5, "thing")
    b_tree.insert(34, "another")
    b_tree.insert(9, "thing2")
    b_tree.insert(234, "data1")
    b_tree.insert(23, "data2")
    b_tree.insert(123, "data3")
    b_tree.insert(99, "data4")
    b_tree.insert(919, "data5")
    b_tree.insert(9191, "data6")

    print("\nSearch:")
    search_and_print(b_tree, 9191, "data6")
    print("\nSearch:")
    search_and_print(b_tree, 99, "data4")


if __name__ == "__main__":
    main()
