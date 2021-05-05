import unittest
import verif

class TestStringsMethods(unittest.TestCase):
    # check if numero value is null
    def test_null(self):
        self.assertFalse(verif.creditCard(None, '06/24', '451'))
    # numero should contain 16 numbers
    def test_length(self):
        self.assertFalse(verif.creditCard('4875', '06/24', '451'))
    # date should be in format 'month/year'
    def test_string(self):
        self.assertFalse(verif.creditCard('47a4785456947854', '12/24', '451'))


if __name__ == '__main__':
    unittest.main()
    