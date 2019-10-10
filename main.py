from anki import get_anki_words
from wiktionary import request_wiki
from kindl import process_clippings
import os
import pprint

def generate_anki_flat_file(kindl_filepath, anki_filepath = None, outfilename = 'New Words.txt'):
    """

    :param kindl_filepath: full path to My Clippings.txt file
    :param anki_filepath (optional): file path to All Decks.txt file from Anki
    :param outfilename: output filename
    :return: None
    """
    f_out = open(outfilename, 'w+')
    all_clippings, all_sentences = process_clippings(kindl_filepath)
    if anki_filepath:
        all_anki = get_anki_words(anki_filepath)
        print([x for x in all_clippings if x not in all_anki])
        all_clippings = [x for x in all_clippings if x not in all_anki]

        print("After removing words from existing Anki decks:", len(all_clippings))

# /pprint.pprint(all_anki)
    i=0
    for word in all_clippings:
        if word:
            i+=1
            print(f'{i} Fetching definition for {word}')
            en_word = request_wiki(word)
            if en_word is None and word[-1] =='s':
                en_word = request_wiki(word[:-1])
            if not en_word is None and en_word != '':
                f_out.writelines(f'{word};{en_word}\n')

    f_out.close()
    print(f'Finished. Import {outfilename} to Anki')


if __name__=="__main__":
    kindl_filepath = './My Clippings.txt'
    anki_filepath = os.path.join(os.curdir, 'All Decks.txt')
    generate_anki_flat_file(kindl_filepath, anki_filepath)