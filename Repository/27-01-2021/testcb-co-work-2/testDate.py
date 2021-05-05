import unittest
import verif

class TestStringsMethods(unittest.TestCase):
    # check if date value is null
    def test_null(self):
        self.assertFalse(verif.creditCard('4785478565874125', None, '451'))
    # date should contain 16 numbers
    def test_date(self):
        self.assertFalse(verif.creditCard('4875', '06/2O24', '451'))
    # date should be in format 'mm/yyyy'
    def test_date(self):
        self.assertFalse(verif.creditCard('4785478565874125', '12-2042', '451'))
    # cvv should be 3 numbers 
    def test_cvv(self):
        self.assertFalse(verif.creditCard('4785478565874125', '06/24', 'a45'))


if __name__ == '__main__':
    unittest.main()
    