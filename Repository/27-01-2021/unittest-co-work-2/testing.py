import unittest
import verif


class TestFonc(unittest.TestCase):
    def test(self):
        self.assertEqual(verif.historique('1492'), 'Découverte de l\'Amérique')
        self.assertEqual(verif.historique('1515'), 'Bataille de Marignan')
        self.assertEqual(verif.historique('2O10'), 'Ne correspond à rien')
    
    def test_wrong(self):
        with self.assertRaises(TypeError):
            self.assertEqual(verif.historique(1095))



if __name__ == '__main__':
    unittest.main()