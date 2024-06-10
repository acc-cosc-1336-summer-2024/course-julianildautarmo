import unittest

from tests.examples.d_repetition import tests_repetition #change this line per test

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition) #chance this line per test
unittest.TextTestRunner(verbosity=2).run(suite)

