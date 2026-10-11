from clrs.chapter19.disjoint_sets_with_ll import DisjointSetsLL, Item


def test_make_set():
    ds = DisjointSetsLL()

    item = Item(1, "a")

    s = ds.make_set(item)

    assert len(ds.sets) == 1
    assert item.set is s
    assert ds.find_set(item) == item


def test_find_set_singleton():
    ds = DisjointSetsLL()

    item = Item(1, "a")

    ds.make_set(item)

    representative = ds.find_set(item)

    assert representative == item


def test_union_two_singletons():
    ds = DisjointSetsLL()

    a = Item(1, "a")
    b = Item(2, "b")

    ds.make_set(a)
    ds.make_set(b)

    ds.union(a.set, b.set)

    assert ds.are_in_same_set(a, b)
    assert len(ds.sets) == 1


def test_union_three_elements():
    ds = DisjointSetsLL()

    a = Item(1, "a")
    b = Item(2, "b")
    c = Item(3, "c")

    ds.make_set(a)
    ds.make_set(b)
    ds.make_set(c)

    ds.union(a.set, b.set)
    ds.union(a.set, c.set)

    assert ds.are_in_same_set(a, b)
    assert ds.are_in_same_set(a, c)
    assert ds.are_in_same_set(b, c)


def test_disjoint_sets_remain_separate():
    ds = DisjointSetsLL()

    a = Item(1, "a")
    b = Item(2, "b")
    c = Item(3, "c")
    d = Item(4, "d")

    ds.make_set(a)
    ds.make_set(b)
    ds.make_set(c)
    ds.make_set(d)

    ds.union(a.set, b.set)
    ds.union(c.set, d.set)

    assert ds.are_in_same_set(a, b)
    assert ds.are_in_same_set(c, d)

    assert not ds.are_in_same_set(a, c)
    assert not ds.are_in_same_set(a, d)
    assert not ds.are_in_same_set(b, c)


def test_weighted_union_updates_all_set_references():
    ds = DisjointSetsLL()

    a = Item(1, "a")
    b = Item(2, "b")
    c = Item(3, "c")
    d = Item(4, "d")

    ds.make_set(a)
    ds.make_set(b)
    ds.make_set(c)
    ds.make_set(d)

    ds.union(a.set, b.set)
    ds.union(c.set, d.set)

    merged = ds.union(a.set, c.set)

    assert a.set is merged
    assert b.set is merged
    assert c.set is merged
    assert d.set is merged


def test_representative_is_same_for_all_members():
    ds = DisjointSetsLL()

    items = [Item(i, i) for i in range(5)]

    for item in items:
        ds.make_set(item)

    ds.union(items[0].set, items[1].set)
    ds.union(items[0].set, items[2].set)
    ds.union(items[0].set, items[3].set)
    ds.union(items[0].set, items[4].set)

    rep = ds.find_set(items[0])

    for item in items:
        assert ds.find_set(item) == rep
