def count_lines_and_words_from_text_file(filename):
    res = {}
    with open(filename) as f:
        txt = f.read()
        f.close()
        lines = txt.splitlines()
        res["line_count"] = len(lines)
        res["word_count"] = len(txt.split(' '))
    return res

# print(count_lines_and_words_from_text_file('../data/obama_speech.txt'))
# print(count_lines_and_words_from_text_file('../data/michelle_obama_speech.txt'))
# print(count_lines_and_words_from_text_file('../data/donald_speech.txt'))
# print(count_lines_and_words_from_text_file('../data/melina_trump_speech.txt'))

import json

def most_spoken_languages(filename, qty):
    languages = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
        f.close()
    
    for c in countries:
        for language in c['languages']:
            if not any(len(t) > 1 and t[1] == language for t in languages):
                languages.append((1, language))
            else:
                for i, (count, name) in enumerate(languages):
                    if name == language:
                        languages[i] = (count+1, name)
                        break


    return sorted(languages, reverse=True)[:qty]


print(most_spoken_languages('../data/countries_data.json', 10))
print(most_spoken_languages('../data/countries_data.json', 3))