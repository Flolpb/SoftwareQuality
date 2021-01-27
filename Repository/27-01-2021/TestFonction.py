import unittest
import Premiere_Fonction


class TestFonc(unittest.TestCase):
    def test(self):
        self.assertEqual(Premiere_Fonction.historique('1492'), 'Découverte de l\'Amérique')
        self.assertEqual(Premiere_Fonction.historique('1515'), 'Bataille de Marignan')
        self.assertEqual(Premiere_Fonction.historique('2006'), 'Coup de Boule de Zizou :(')
        self.assertEqual(Premiere_Fonction.historique('2O10'), 'Ne correspond à rien')
    
    def wrong_test(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Premiere_Fonction.historique(1095), 'Première croisade')



if __name__ == '__main__':
    unittest.main()