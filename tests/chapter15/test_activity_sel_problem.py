from clrs.chapter15.activity_sel_problem import (
    Activity,
    do_activity_selection_iter,
    do_activity_selection_rec,
)


def test_activity_is_after_me():
    a1 = Activity(1, 4)
    a2 = Activity(4, 7)
    a3 = Activity(3, 6)

    assert a1.is_after_me(a2)
    assert not a1.is_after_me(a3)


def test_recursive_clrs_example():
    activities = [
        Activity(1, 4),
        Activity(3, 5),
        Activity(0, 6),
        Activity(5, 7),
        Activity(3, 9),
        Activity(5, 9),
        Activity(6, 10),
        Activity(8, 11),
        Activity(8, 12),
        Activity(2, 14),
        Activity(12, 16),
    ]

    result = do_activity_selection_rec(activities)

    assert [(a.start, a.end) for a in result] == [
        (1, 4),
        (5, 7),
        (8, 11),
        (12, 16),
    ]


def test_iterative_clrs_example():
    activities = [
        Activity(1, 4),
        Activity(3, 5),
        Activity(0, 6),
        Activity(5, 7),
        Activity(3, 9),
        Activity(5, 9),
        Activity(6, 10),
        Activity(8, 11),
        Activity(8, 12),
        Activity(2, 14),
        Activity(12, 16),
    ]

    result = do_activity_selection_iter(activities)

    assert [(a.start, a.end) for a in result] == [
        (1, 4),
        (5, 7),
        (8, 11),
        (12, 16),
    ]


def test_recursive_and_iterative_return_same_solution():
    activities = [
        Activity(1, 3),
        Activity(2, 5),
        Activity(4, 7),
        Activity(6, 9),
        Activity(8, 10),
    ]

    rec = do_activity_selection_rec(activities)
    itr = do_activity_selection_iter(activities)

    assert [(a.start, a.end) for a in rec] == [(a.start, a.end) for a in itr]


def test_single_activity():
    activities = [Activity(1, 2)]

    rec = do_activity_selection_rec(activities)
    itr = do_activity_selection_iter(activities)

    assert len(rec) == 1
    assert len(itr) == 1
    assert rec[0].start == 1
    assert itr[0].start == 1


def test_all_activities_compatible():
    activities = [
        Activity(1, 2),
        Activity(2, 3),
        Activity(3, 4),
        Activity(4, 5),
    ]

    rec = do_activity_selection_rec(activities)
    itr = do_activity_selection_iter(activities)

    assert len(rec) == 4
    assert len(itr) == 4
