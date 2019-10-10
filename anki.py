import os
import re
import string
def get_anki_words(filepath):
    all = []
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            all = f.readlines()
            a_ = [x.split('\t')[0] for x in all]
            b_ = [x.split('\t')[1] for x in all if len(x.split('\t'))>1]
            all = a_ + b_
            all = [x.replace('\n', ' ') for x in all]
            all = [x.replace('"', '') for x in all]
            all = [x.replace('&nbsp', ' ') for x in all]
            all = [re.sub('<[^>]*>', ' ', x) for x in all]
            all = [x.lower() for x in all]


            all = [x.rstrip(string.punctuation + string.whitespace) for x in all]
            all = [x.lstrip(string.punctuation + string.whitespace) for x in all]
            all = list(dict.fromkeys(all))
            print("Unique words in Anki:", len(all))
    return all

if __name__ == '__main__':
    filepath = os.path.join(os.curdir, 'All Decks.txt')
    print(filepath)
    get_anki_words(filepath)
