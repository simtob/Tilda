from Labboration8 import *
import unittest


class Test(unittest.TestCase):

    def testa(self):
        self.assertEqual(syntaxcontrol("C"), "Syntaxen stämmer!")
        self.assertEqual(syntaxcontrol("P29"), "Syntaxen stämmer!")
        self.assertEqual(syntaxcontrol("Ag3"), "Syntaxen stämmer!")
        self.assertEqual(syntaxcontrol("Fe12"), "Syntaxen stämmer!")
        self.assertEqual(syntaxcontrol("Xx5"), "Syntaxen stämmer!")
        self.assertEqual(syntaxcontrol("a"), ("Den är inte en storbokstav: " + "a"))
        self.assertEqual(syntaxcontrol("8"), "Den är inte en storbokstav: 8")
        self.assertEqual(syntaxcontrol("Cr0"), "För litet tal:0")
        self.assertEqual(syntaxcontrol("Pb1"), "För litet tal:1")
        self.assertNotEqual(syntaxcontrol("XW02"), "Syntaxen stämmer inte!")

if __name__ == '__main__':
    unittest.main()