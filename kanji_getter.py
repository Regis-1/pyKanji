import requests
import urllib.parse
from bs4 import BeautifulSoup

url_wiki = 'https://en.wikipedia.org/wiki/List_of_kanji_by_stroke_count'
url_jisho_pre = 'https://jisho.org/search/'
url_jisho_post = '20%23kanji'
page = requests.get(url_wiki)

#checking for status other than 200 [HTTP OK STATUS]
if page.status_code != 200:
    print('Error with opening the site.')
    quit()
    
soup = BeautifulSoup(page.content, 'lxml')
results = soup.find_all('a', 'extiw')

#copying kanji to list
kanji = []
for result in results:
    kanji.append(str(result.string))

del results

#deleting two unnecessary elements from list
del kanji[len(kanji)-2:len(kanji)]
print('Kanji download successfull.')

f = open('kanji_meanings.txt', 'w', encoding='utf-8')
n = 0
#getting meaning for each kanji from jisho.org website
for k in kanji:
    n += 1
    print('Kanji ', n, ' being processed...')
    url_jisho = url_jisho_pre + urllib.parse.quote(k, encoding='utf-8') + url_jisho_post
    page = requests.get(url_jisho)

    if page.status_code != 200:
        print('Page error for ', k, 'kanji')
        quit()

    soup = BeautifulSoup(page.content, 'lxml')
    result = soup.find('div', 'kanji-details__main-meanings')
    if result is None:
        continue
    meaning = str(result.string).strip()
    end_string = k + ' - ' + meaning + '\n'
    f.write(end_string)

f.close()
print('\nGetting and saving meaning of kanji done.')
print('The file is ready!')
