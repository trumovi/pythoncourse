import unittest

from oppp import TFIDF


class TestTFIDF(unittest.TestCase):

    def setUp(self):
        self.object = TFIDF(['text_1.txt', 'text_2.txt'])
        self.tfidf = self.object.count_tfidf('text_3.txt')

    def test_texts_upload(self):
        self.assertIsNotNone(self.object.get_texts())

    def test_counts_tfidf(self):
        self.assertIsNotNone(self.tfidf)


if __name__ == '__main__':
    unittest.main()
