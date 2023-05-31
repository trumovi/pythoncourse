import unittest

from oppp import TFIDF


class TestTFIDF(unittest.TestCase):

    def setUp(self):
        self.object = TFIDF(['text_1.txt', 'text_2.txt'])
        self.tfidf = self.object.count_tfidf('text_3.txt')
        self.tfidfs = [('это', 0.0), ('тестовый', 0.0), ('файл', 0.0), ('с', 0.0), ('текст', 0.06931471805599453),
                       ('для', 0.06931471805599453), ('проверка', 0.0), ('подсчёт', 0.0), ('tfidf', 0.0)]

    def test_texts_upload(self):
        self.assertIsNotNone(self.object.get_texts())

    def test_tfidf(self):
        for i in range(len(self.tfidfs)):
            with self.subTest(i=i):
                self.assertEqual(self.tfidfs[i][1], self.tfidf[i][1])


if __name__ == '__main__':
    unittest.main()
