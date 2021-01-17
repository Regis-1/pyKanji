import codecs

f = codecs.open('kanji_meanings.txt', 'r', 'utf-8')

kanji = {}
for line in f.readlines():
    separate = line.split('-')
    kanji[(separate[0])[:1]] = ((separate[1])[1:]).strip()


while True:
    usr_word = input('Your kanji word: ')
    print()
    if usr_word == 'q':
        break
    
    for c in usr_word:
        try:
            print(c, ' - ', kanji[c])
        except:
            continue

    print('-'*50)
