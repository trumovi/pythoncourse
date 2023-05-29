import xml.etree.ElementTree as ET

class Wordform:
    def __init__(self, text, grammems):
        self._text = text
        self.__grammems = grammems

    def get_grammems(self):
        return self.__grammems


class Sentence:
    def __init__(self, text, words):
        self._text = text
        self.__words = words


    def get_word(self, id):
        return self.__words[id]

    def len(self):
        return len(self.__words)


class Corpus:
    def __init__(self, filename):
        self.__sentences = []
        tree = ET.parse(filename)
        root = tree.getroot()
        for sent in root.iter('sentence'):
            source_text = sent.find('source').text
            words = []
            for token in sent.findall('tokens/token'):
                text = token.get('text')
                grammems = [gram.attrib['v'] for gram in token.iter('g')]
                wordform = Wordform(text, grammems)
                words.append(wordform)
            sentence = Sentence(source_text, words)
            self.__sentences.append(sentence)

    def get_item(self, id):
        return self.__sentences[id]

    def len(self):
        return len(self.__sentences)

    def get_wordform(self, sent_id, word_id):
       return self.__sentences[sent_id].get_word(word_id)

    def get_grammems(self, sent_id, word_id):
        return self.__sentences[sent_id].get_word(word_id).get_grammems()

    def get_sentence(self, sent_id):
        return self.__sentences[sent_id]._text


corpus = Corpus("annot.opcorpora.no_ambig.xml")
print(corpus.get_wordform(73, 2))
print(corpus.get_grammems(23, 4))
