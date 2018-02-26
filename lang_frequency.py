import collections
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_text:
        return file_with_text.read()


def get_most_frequent_words(list_of_words):
    amount_of_words = 10
    counter = collections.Counter(list_of_words.split())
    return dict(counter.most_common(amount_of_words))


if __name__ == '__main__':
    file_path = ' '.join(sys.argv[1:])
    print(*(word for word in get_most_frequent_words(load_data(file_path))))
