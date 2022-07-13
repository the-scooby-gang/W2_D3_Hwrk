import unittest

from src.bear import Bear

class Test_Bear(unittest.TestCase):
   
    def setUp(self):
        self.bear = Bear('Yogi', 'Grizzly')

    def test_bear_has_name(self):
        actual = self.bear.name
        self.assertEqual("Yogi", actual)

    def test_bear_type(self):
        actual = self.bear.type
        self.assertEqual('Grizzly', actual)

    def test_stomach_size(self):
        self.assertEqual(0, self.bear)
        

    





