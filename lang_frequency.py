import collections
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_text:
        return file_with_text.read()


def get_most_frequent_words(text):
    amount_of_words = 10
    list_of_words = [word for word in text.lower().split() if word.isalpha()]
    counter = collections.Counter(list_of_words)
    return counter.most_common(amount_of_words)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        print(*(word for word, _ in get_most_frequent_words(load_data(file_path))))
    except FileNotFoundError:
        print('No file')
    except IndexError:
        print('You did not write the name of file')
