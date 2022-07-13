import unittest

from src.fish import Fish

class test_fish(unittest.TestCase):

    def setUp(self):
        self.fish = Fish('stupid')

    def test_fish_name(self):
        actual = self.fish.name
        self.assertEqual('stupid', actual)


    