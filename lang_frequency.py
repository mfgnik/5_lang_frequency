import collections
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def file_to_list(f):
    return f.split()


def get_most_frequent_words(list_of_words):
    amount_of_words = 10
    counter = collections.Counter(list_of_words)
    return dict(counter.most_common(amount_of_words)).keys()

if __name__ == '__main__':
    file_path = ' '.join(sys.argv[1:])
    print(*get_most_frequent_words(file_to_list(load_data(file_path))))
