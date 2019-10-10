# Send request to wiktionary and parse data
import bs4
from bs4 import BeautifulSoup
import requests

URL = "https://pl.wiktionary.org/wiki/{}?printable=yes"

def from_dd_to_text(dds):
    text = []
    for dd in dds:
        content = dd.contents
        if len(content) > 0:
            all_text = ''
            for c in content:
                if c.name in ['style']:
                    continue
                if type(c) == bs4.element.Tag:
                    # print(c.text)
                    all_text += c.text
                elif type(c) == bs4.element.NavigableString:
                    all_text += str(c)
            text.append(all_text)
    if len(text) > 1:
        return '\"' + '\n'.join(text) + '\"'
    else:
        return text[0]


def parse_response(response):
    # soup = BeautifulSoup(response.text.replace('>\n<', '><'), 'html.parser')
    soup = BeautifulSoup(response.text, 'html.parser')
    #find the container with meaning in Polish
    dl_mean = soup.find('span', string='znaczenia:').parent.parent.next_sibling.next_sibling.next_sibling.next_sibling
    dds = dl_mean.find_all('dd')
    text = from_dd_to_text(dds)
    return text

def request_wiki(word):
    try:
        response = requests.get(URL.format(word))
        if int(response.status_code == 200):
            return parse_response(response)
    except requests.ConnectionError as e:
        print("something went wrong:", e)

if __name__ == '__main__':
    word = 'moonlit'
    translation = request_wiki(word)
    print(translation)



