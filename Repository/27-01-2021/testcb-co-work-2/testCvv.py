import unittest
import verif

class TestStringsMethods(unittest.TestCase):
    # check if one of the required value is null
    def test_null(self):
        self.assertFalse(verif.creditCard())
    # numero should contain 16 numbers
    def test_numero(self):
        self.assertFalse(verif.creditCard('4875', '06/24', '451'))
    # date should be in format 'month/year'
    def test_date(self):
        self.assertFalse(verif.creditCard('4785478565874125', '1a-12', '451'))
    # cvv should be 3 numbers 
    def test_cvv(self):
        self.assertFalse(verif.creditCard('4785478565874125', '06/24', 'a45'))


if __name__ == '__main__':
    unittest.main()
    