import unittest
from main import index, final, cow, passit


class TestFunctions(unittest.TestCase):
    def test_index(self):
        assert index() == "Hello, world!"
    def test_cow(self):
        assert cow() == "MOoooOo!"
    def test_final(self):
        assert final() == "Welcome to my final assignment!"
    def test_passit(self):
        assert passit() == 'I hope I will pass for the first time ^^'
