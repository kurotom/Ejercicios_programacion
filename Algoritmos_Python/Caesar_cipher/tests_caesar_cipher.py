import unittest

from caesar_cipher import caesar_cipher


class CaesarCipherTests(unittest.TestCase):

    def test_fifty_encrypt(self):
        self.assertEqual(caesar_cipher('hello world', 50, 'encrypt'), 'fcjjm umpjb')

    def test_fifty_decrypt(self):
        self.assertEqual(caesar_cipher('fcjjm umpjb', 50, 'decrypt'), 'hello world')

    def test_onethousand_encrypt(self):
        self.assertEqual(caesar_cipher('python code', 1000, 'encrypt'), 'bkftaz oapq')

    def test_onethousand_decrypt(self):
        self.assertEqual(caesar_cipher('bkftaz oapq', 1000, 'decrypt'), 'python code')

    def test_final_encrypt(self):
        self.assertEqual(caesar_cipher('this is a test', 1000000, 'encrypt'), 'hvwg wg o hsgh')

    def test_final_decrypt(self):
        self.assertEqual(caesar_cipher('hvwg wg o hsgh', 1000000, 'decrypt'), 'this is a test')


if __name__ == '__main__':
    unittest.main()
