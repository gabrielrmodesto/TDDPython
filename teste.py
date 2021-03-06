import unittest
from codigo import *

class ClasseDeTeste(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(),'Hello World')

    def teste_lista(self):
        self.assertEqual(10, len(cria_lista(10)))
    
    def test_fib(self):
        self.assertEqual(987, fib(1000)[-1])

if __name__ == '__main__':
    unittest.main()