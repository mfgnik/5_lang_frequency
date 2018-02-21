import collections

def load_data(filepath):
    text = []
    with open(filepath, 'r', encoding='utf-8') as our_file:
        for line in our_file:
            text.extend(line.split())
    return text


def get_most_frequent_words(text):
    amount_of_words = 10
    counter = collections.Counter()
    for word in text:
        counter[word] += 1
    return counter.most_common(amount_of_words)

if __name__ == '__main__':
    file_path = input()
    print(*(word[0] for word in get_most_frequent_words(load_data(file_path))))
