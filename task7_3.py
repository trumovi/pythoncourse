import unittest
import os
import shutil

def Path(path):
    os.makedirs(path, exist_ok=True)
    file_name = path + "\\troy.txt"
    with open(file_name, "w") as d:
        d.write("Everybody's always talkin' at me\nEverybody's tryin' to get in my head\nI wanna listen to my own heart talkin'\nI need to count on myself instead")

class ThirdTask(unittest.TestCase):
    def setUp(self) -> None:
        Path("C:\\Users\\Ольга\\pythoncourse\\task")

    def test_equality(self):
        with open('C:\\Users\\Ольга\\pythoncourse\\task\\troy.txt', 'r') as to_check:
            text = to_check.read()
            self.assertEqual(text, "Everybody's always talkin' at me\nEverybody's tryin' to get in my head\nI wanna listen to my own heart talkin'\nI need to count on myself instead")

    def tearDown(self) -> None:
        shutil.rmtree('C:\\Users\\Ольга\\pythoncourse\\task')


if __name__ == '__main__':
    unittest.main()