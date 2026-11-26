def count_lines_and_words_from_text_file(filename):
    res = {}
    with open(filename) as f:
        txt = f.read()
        lines = txt.splitlines()
        res["line_count"] = len(lines)
        res["word_count"] = len(txt.split(' '))
        f.close()
    return res

print(count_lines_and_words_from_text_file('../data/obama_speech.txt'))