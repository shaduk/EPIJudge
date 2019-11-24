from test_framework import generic_test


def h_index(citations):
    # TODO - you fill in here.
    length = len(citations)
    citations.sort()
    for i in range(length):
        if(citations[i] >= length - i):
            return length - i
    return 0

if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
