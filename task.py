import xml.etree.ElementTree as ET

class Wordform:
    def __init__(self, text, grammems):
        self.text = text
        self.grammems = grammems

class Sentence:
    def __init__(self, text, words):
        self.text = text
        self.words = words

    def __getitem__(self, id):
        return self.words[id]

    def __len__(self):
        return len(self.words)



class Corpus:
    def __init__(self, filename):
        self.sentences = []
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
            self.sentences.append(sentence)

    def __getitem__(self, id):
        return self.sentences[id]

    def __len__(self):
        return len(self.sentences)

    def get_wordform(self, sent_id, word_id):
        print(self.sentences[sent_id].words[word_id])

    def get_grammems(self, sent_id, word_id):
        print(self.sentences[sent_id].words[word_id].grammems)

    def print_sentence(self, sent_id):
        print(self.sentences[sent_id].text)


# corpus = Corpus("annot.opcorpora.no_ambig.xml")
# corpus.get_wordform(73, 2)
# corpus.get_grammems(23, 4)
# corpus.print_sentence(98)
