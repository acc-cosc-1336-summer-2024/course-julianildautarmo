import unittest

from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets #change this line per test

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets) #chance this line per test
unittest.TextTestRunner(verbosity=2).run(suite)