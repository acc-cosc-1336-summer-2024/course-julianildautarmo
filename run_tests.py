import unittest

from tests.examples.h_strings import tests_strings #change this line per test

suite = unittest.TestLoader().loadTestsFromModule(tests_strings) #chance this line per test
unittest.TextTestRunner(verbosity=2).run(suite)