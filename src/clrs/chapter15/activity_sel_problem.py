"""
Greedy solutions to the activity-selection problem.
"""

from __future__ import annotations


class Activity:
    """
    Represents an activity with a start and finish time.
    """

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return "[Activity] {0} - {1}".format(self.start, self.end)

    def is_after_me(self, a: Activity) -> bool:
        """
        Return True if the activity can be scheduled after this activity.
        """
        return a.start >= self.end


def create_activities() -> list[Activity]:
    """
    Create the CLRS activity-selection example dataset.
    """
    activities = []

    activities.append(Activity(1, 4))
    activities.append(Activity(5, 9))
    activities.append(Activity(3, 9))
    activities.append(Activity(2, 14))
    activities.append(Activity(7, 11))
    activities.append(Activity(8, 12))
    activities.append(Activity(5, 7))
    activities.append(Activity(3, 5))
    activities.append(Activity(12, 16))
    activities.append(Activity(0, 6))
    activities.append(Activity(6, 10))

    return activities


def do_activity_selection_rec(activities: list[Activity]) -> list[Activity]:
    """
    Return an optimal activity set using the recursive greedy algorithm.
    """

    if not activities:
        return []

    first_activity = activities[0]
    next_activity = None

    for i in range(1, len(activities)):
        if first_activity.is_after_me(activities[i]):
            next_activity = activities[i]
            break

    if next_activity is not None:
        next_activity_index = activities.index(next_activity)
        return [first_activity] + do_activity_selection_rec(
            activities[next_activity_index:]
        )

    return [first_activity]


def do_activity_selection_iter(activities: list[Activity]) -> list[Activity]:
    """
    Return an optimal activity set using the iterative greedy algorithm.
    """

    if not activities:
        return []

    sol = [activities[0]]

    for i in range(1, len(activities)):
        if sol[-1].is_after_me(activities[i]):
            sol.append(activities[i])

    return sol


def main():
    activities = create_activities()
    activities_sorted_by_end = sorted(activities, key=lambda a: a.end)

    print("Activity selection with recursion")
    sol = do_activity_selection_rec(activities_sorted_by_end)
    print(", ".join(str(a) for a in sol))

    print("\nActivity selection with iteration")
    sol = do_activity_selection_iter(activities_sorted_by_end)
    print(", ".join(str(a) for a in sol))


if __name__ == "__main__":
    main()
