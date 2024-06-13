import unittest

from src.examples.e_functions.value_return_functions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
'''
    def test_get_radnom(self):
        random = get_random(1,100)
        
        self.assertEqual(True,random >=1 and random<=100)'''