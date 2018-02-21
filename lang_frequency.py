import collections

def load_data(filepath):
    text = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            text.extend(line.split())
    return text


def get_most_frequent_words(text):
    c = collections.Counter()
    for word in text:
        c[word] += 1
    return c.most_common(10)

if __name__ == '__main__':
    file_path = input()
    print(*(x[0] for x in get_most_frequent_words(load_data(file_path))))
