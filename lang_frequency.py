import collections
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_text:
        return file_with_text.read()


def get_most_frequent_words(text):
    amount_of_words = 10
    list_of_lower = text.lower().split()
    list_of_words = [word for word in list_of_lower if word.isalpha()]
    counter = collections.Counter(list_of_words)
    return counter.most_common(amount_of_words)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        most_frequent_words = get_most_frequent_words(load_data(file_path))
        print('The most frequent words:')
        for word in enumerate((word for word, _ in most_frequent_words), 1):
            print(*word)
    except FileNotFoundError:
        print('No file')
    except IndexError:
        print('You did not write the name of file')
