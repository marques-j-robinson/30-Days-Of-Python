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


# print(most_spoken_languages('../data/countries_data.json', 10))
# print(most_spoken_languages('../data/countries_data.json', 3))

def most_populated_countries(filename, qty):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    keys_to_keep = ["name", "population"]

    filtered_data = [
        {k: d[k] for k in keys_to_keep if k in d} 
        for d in data
    ]

    return sorted(filtered_data, key=lambda x: x['population'], reverse=True)[:qty]

# print(most_populated_countries('../data/countries_data.json', 10))
# print(most_populated_countries('../data/countries_data.json', 3))


import re

with open('../data/email_exchanges_big.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    f.close()

incoming_email_addresses = []

for line in lines:
    if 'From ' in line:
        match = re.match(r"^[^ ]* ([^ ]*) ", line)
        if match:
            incoming_email_addresses.append(match.group(1))

unique_email_addresses = list(set(incoming_email_addresses))
# print(unique_email_addresses)

def find_most_common_words(input, qty):
    try:
        with open(f"../data/{input}", 'r', encoding="utf-8") as f:
            data = f.read()
            f.close()
    except FileNotFoundError:
        data = input
    
    res = []
    data = " ".join(re.sub(r'[^a-zA-Z0-9 ]', '', data).split())

    for word in re.split(' ', data):
        if (not any(len(t) > 1 and t[1] == word for t in res)):
            count = len(re.findall(rf"\b{word}\b", data))
            res.append((count, word))

    res = sorted(res, key=lambda x: (x[0], x[1]), reverse=True)
    return res[:qty]

# print(find_most_common_words('sample.txt', 10))
# print(find_most_common_words('obama_speech.txt', 10))
# print(find_most_common_words('michelle_obama_speech.txt', 10))
# print(find_most_common_words('donald_speech.txt', 10))
# print(find_most_common_words('melina_trump_speech.txt', 10))

import os
from pathlib import Path
import sys

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from data.stop_words import stop_words

# accept a string or a file
def load_text(source):
    if os.path.isfile(source):
        with open(source, 'r', encoding='utf-8') as f:
            return f.read()
    return source

def clean_text(text):
    text = load_text(text).lower()
    words = re.findall(r'\b[a-z]+\b', text)
    return words

def remove_support_words(words):
    stop_set = set(w.lower() for w in stop_words)
    return [word for word in words if word not in stop_set]

def check_text_similarity(text1, text2):
  words1 = set(remove_support_words(clean_text(text1)))
  words2 = set(remove_support_words(clean_text(text2)))

  if not words1 and not words2:
    return 100.0
  if not words1 or not words2:
    return 0.0

  intersection = words1.intersection(words2)
  union = words1.union(words2)

  similarity = (len(intersection) / len(union)) * 100
  return round(similarity, 2)

michelle_speech = '../data/michelle_obama_speech.txt'
melania_speech = '../data/melina_trump_speech.txt'

score = check_text_similarity(michelle_speech, melania_speech)
# print(f'Text similarity: {score}%')

# print(find_most_common_words('romeo_and_juliet.txt', 10))

import csv

with open('../data/hacker_news.csv', 'r', encoding='utf-8') as f:
    data = csv.DictReader(f)
    word = 'javascript'
    count = 0
    for row in data:
        exists = bool(re.search(rf"\b{re.escape(word)}\b", row['title'], re.I))
        if exists:
            count += 1
    print(count)