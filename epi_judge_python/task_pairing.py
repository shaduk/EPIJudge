import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    # TODO - you fill in here.
    sorted_tasks = sorted(task_durations)
    pairs = []
    start, end = 0, len(sorted_tasks) - 1
    while(start < end):
        pairs.append((sorted_tasks[start], sorted_tasks[end]))
        start += 1
        end -= 1
    return pairs


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
