import unittest

from src.examples.d_repetition.repetition import sum_of_powers_for, test_config

class Test_Config(unittest.TestCase):

    '''def test_configuration(self):
        self.assertEqual(True, test_config())'''

    def test_sum_of_powers_for_w_value_3(self): 
        self.assertEqual(14, sum_of_powers_for(3))