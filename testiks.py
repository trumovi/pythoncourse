import unittest
from task import Corpus


class Testik(unittest.TestCase):
    def setUp(self):
        self.corpus = Corpus("annot.opcorpora.no_ambig.xml")

    def test_corpus_not_empty(self):
        self.assertIsNotNone(self.corpus)

    def test_sentence_not_empty(self):
        sentence = self.corpus.__getitem__(736)
        self.assertNotEqual(len(sentence), 0)


if __name__ == '__main__':
    unittest.main()