import json
import math
import os
from collections import Counter

import pymorphy2


class TFIDF:

    def __init__(self, paths: list):
        self._text = []
        self._idf = {}
        self._morph = pymorphy2.MorphAnalyzer()
        for item in paths:
            self._text.append(self._add_file(item)[1])
        if os.path.exists("idf.json"):
            with open('idf.json', 'r', encoding='UTF-8') as d:
                self._idf = json.load(d)
        else:
            for text in self._text:
                self._count_idf(text)

    def _add_file(self, item):
        with open(item, "r", encoding='UTF-8') as d:
            text = d.read()
        for symbol in '.,;:""?!-0123456789()—–«»':
            text = text.replace(symbol, '')
        w = text.lower().split()
        words = [self._morph.parse(word)[0].normal_form for word in w]
        w_count = Counter(words)
        return words, w_count

    def _count_idf(self, text):
        for word in text:
            d = len(self._text)
            di = 0
            for text in self._text:
                if word in text:
                    di += 1
            self._idf[word] = math.log(abs(d) / abs(di))
        with open('idf.json', 'w', encoding="utf-8") as d:
            json.dump(self._idf, d, ensure_ascii=False, indent=4)

    def get_idf(self):
        return self._idf

    def get_texts(self):            # метод используется в тестах
        return self._text

    def count_tfidf(self, item):
        words, word_count = self._add_file(item)
        tfidfs = []
        text_len = len(words)
        for word in word_count:
            tf = word_count[word] / text_len
            idf = self._idf.get(word, 0)
            tfidf = tf * idf
            tfidfs.append((word, tfidf))
        return tfidfs
