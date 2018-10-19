import unittest
from codigo import *

class ClasseDeTeste(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(),'Hello World')

if __name__ == '__main__':
    unittest.main()