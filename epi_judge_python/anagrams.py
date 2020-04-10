from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # TODO - you fill in here.
<<<<<<< HEAD

=======
    print('hello')
>>>>>>> 04f74d412cc80aa1c2d3e7f7fa1ca0fd94743859
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
