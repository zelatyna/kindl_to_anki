import os
import pprint
import re
DELIM = '=========='

def format_clippings(clippings):
    clippings = map(lambda x: x.lower(), clippings)
    #remove special chars
    clippings = map(lambda x: re.sub('[?!;:,\.\"()]', '', x) , clippings)
    #remove duplicates
    clippings = list(dict.fromkeys(clippings))
    return clippings

def word_sentence_split(clippings, max_len = 2):
    word_clippings = [x for x in clippings if len(x.split(' '))<= max_len]
    sentence_clippings = [x for x in clippings if len(x.split(' '))> max_len]

    return word_clippings, sentence_clippings

def process_clippings(filepath):
    """
    Process clippings file and returns cleaned list of highlighted words
    :param filepath: File path to My Clippings.txt coppied from Kindl
    :return:
    """
    clippings = []
    word_clippings = []
    sentence_clippings = []
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            all = ''.join(f.readlines())
            highlights = all.split(DELIM)
            print("Number of Clippings:", len(highlights))
            for h in highlights:
                #split each highlight by new line and remove empty string
                parts = [elem for elem in h.split('\n') if elem != '']
                if len(parts)>=3:
                    clippings.append(parts[2])

        clippings = format_clippings(clippings)
        print("Number of higlights:", len(clippings))
        # pprint.pprint(clippings)
        word_clippings, sentence_clippings = word_sentence_split(clippings)
        print("Words to translate:", len(word_clippings))
        print("Sentences in clippings:", len(sentence_clippings))
        # pprint.pprint(sentence_clippings)
    else:
        print("My Clippings.txt file does not exist in provided dir:", filepath)
            # print(all)
            # print(len(all))
    return  word_clippings, sentence_clippings

if __name__ == '__main__':
    filepath = os.path.join(os.curdir, 'My Clippings.txt')
    print(filepath)
    process_clippings(filepath)