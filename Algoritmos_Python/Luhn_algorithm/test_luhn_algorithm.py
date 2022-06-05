import unittest

from luhn_algorithm import verificacion

class LuhnAlgorithmTests(unittest.TestCase):

    def test_one(self):
        self.assertIs(verificacion(374386966075351), True)

    def test_two(self):
        self.assertIs(verificacion(6060712580972374), True)

    def test_three(self):
        self.assertIs(verificacion(7069807093165969179), True)

    def test_four(self):
        self.assertIs(verificacion(601286592634), True)

    def test_five(self):
        self.assertIs(verificacion(600186592634), False)

    def test_six(self):
        self.assertIs(verificacion('60121s6590134'), False)

    def test_seven(self):
        self.assertIs(verificacion(''), False)

if __name__ == '__main__':
    unittest.main()
