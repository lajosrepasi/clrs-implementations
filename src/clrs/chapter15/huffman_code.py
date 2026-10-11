"""
Huffman coding for lossless text compression.
"""

from typing import Any, cast

from clrs.chapter06.priority_queue import MinPriorityQueue
from clrs.chapter10.binary_tree import Node
from clrs.chapter10.my_queue import Queue
from clrs.chapter11.hash_table_chaining import HashTableChaining as HashTable

END_OF_SEQ = "*"


class HuffmanNode(Node):
    """
    Represents a node in a Huffman coding tree.
    """

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        self.codes: HashTable = HashTable()

    def is_leaf(self) -> bool:
        """
        Return True if the node has no children.
        """
        return self.right is None and self.left is None

    def build_codes(self, root, code_so_far) -> None:
        """
        Generate Huffman codes for all leaf nodes.
        """
        if self.left is not None:
            assert isinstance(self.left, HuffmanNode)
            self.left.build_codes(root, code_so_far + "0")

        if self.right is not None:
            assert isinstance(self.right, HuffmanNode)
            self.right.build_codes(root, code_so_far + "1")

        if self.is_leaf():
            root.codes[self.value] = code_so_far if code_so_far else "0"


def calc_freq(s: str) -> HashTable:
    """
    Count character frequencies in a string.
    """
    ht = HashTable()

    for c in s:
        c_key = ord(c)
        if c_key in ht:
            ht[c_key] = ht[c_key] + 1
        else:
            ht[c_key] = 1

    return ht


def build_mpq(freqs: HashTable) -> MinPriorityQueue[int, HuffmanNode]:
    """
    Build a min-priority queue from character frequencies.
    """
    mpq = MinPriorityQueue()

    for c in freqs:
        mpq.insert(freqs[c], c)

    return mpq


def construct_tree(mpq: MinPriorityQueue[int, HuffmanNode]) -> Any:
    """
    Construct a Huffman tree from a priority queue.
    """
    for _ in range(len(mpq) - 1):
        x_freq, x = cast(tuple[int, Any], mpq.extract_minimum())
        y_freq, y = cast(tuple[int, Any], mpq.extract_minimum())
        node = HuffmanNode(x_freq + y_freq)

        if isinstance(x, int):
            x = HuffmanNode(x)

        if isinstance(y, int):
            y = HuffmanNode(y)

        node.set_left(x)
        node.set_right(y)

        mpq.insert(node.value, node)

    _, root = cast(tuple[int, Any], mpq.extract_minimum())

    if isinstance(root, int):
        root = HuffmanNode(root)

    return root


def printer(node: HuffmanNode) -> Any | int:
    """
    Return a printable representation of a Huffman node.
    """
    if node.left is None and node.right is None:
        return chr(node.value)
    else:
        return node.value


def huffman_tree(s: str) -> HuffmanNode:
    """
    Build a Huffman tree for a string.
    """
    freqs = calc_freq(s)
    mpq = build_mpq(freqs)
    tree = construct_tree(mpq)

    assert isinstance(tree, HuffmanNode)

    return tree


def huffman_encode(s: str) -> tuple[list[int], HuffmanNode]:
    """
    Encode a string using Huffman coding.
    """
    s += END_OF_SEQ

    tree = huffman_tree(s)
    tree.build_codes(tree, "")

    encoded = []
    binary_str = ""

    for c in s:
        code = tree.codes[ord(c)]
        binary_str += code

        if len(binary_str) >= 8:
            encoded.append(int(binary_str[:8], 2))
            binary_str = binary_str[8:]

    if len(binary_str) > 0:
        binary_str += "0" * (8 - len(binary_str))
        encoded.append(int(binary_str, 2))

    return encoded, tree


def huffman_decode(encoded: list[int], tree: HuffmanNode) -> str:
    """
    Decode Huffman-encoded data.
    """

    def to_bin_str(n):

        bin_str = bin(n)[2:]

        if len(bin_str) < 8:
            bin_str = "0" * (8 - len(bin_str)) + bin_str

        return bin_str

    def add_to_buffer(next_to_process):
        bin_str = to_bin_str(encoded[next_to_process])
        for bin_c in bin_str:
            buffer_to_process.enqueue(bin_c)

        next_to_process += 1
        return next_to_process

    buffer_to_process = Queue(16)

    decoded = ""

    next_to_process = 0
    next_to_process = add_to_buffer(next_to_process)

    current_node: HuffmanNode = tree

    while True:
        if current_node.is_leaf():
            decoded_char = chr(current_node.value)
            if decoded_char == END_OF_SEQ:
                break

            decoded += decoded_char
            current_node = tree

        if buffer_to_process.empty():
            next_to_process = add_to_buffer(next_to_process)

        next_step = buffer_to_process.dequeue()

        if next_step == "0":
            assert isinstance(current_node.left, HuffmanNode)
            current_node = current_node.left
        else:
            assert isinstance(current_node.right, HuffmanNode)
            current_node = current_node.right

    return decoded


def main():
    s = "OneShot is a puzzle-adventure game. The player controls Niko, a catlike child who is placed in an unfamiliar sunless world.[2] The game exclusively shows Niko's viewpoint, employing a top-down perspective,[3] while the player is separate, referred to by the name provided in their user account. Throughout the game, the player can make Niko sleep, causing the program to close; upon reopening, a short dream sequence is played showing Niko's old life with their mother"

    print('To compress "{0}", len: {1}'.format(s, len(s)))
    encoded, tree = huffman_encode(s)
    print("Compressed {0}, len: {1}".format(encoded, len(encoded)))
    print("Compressed pecentage: {:.2f}%".format((len(encoded) / len(s)) * 100))
    decoded = huffman_decode(encoded, tree)
    print("Decoded: " + decoded)
    print("Is equals: " + str(decoded == s))
    assert decoded == s


if __name__ == "__main__":
    main()
