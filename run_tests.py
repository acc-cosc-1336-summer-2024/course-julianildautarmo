import unittest

from tests.homework.c_decisions import tests_decisions #change this line per test

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions) #chance this line per test
unittest.TextTestRunner(verbosity=2).run(suite)

'''when I run this it only shows ran 2 tests rather than 2+5 totalling to 7. It all works, but why doesn't it say it ran 2 sets of tests, 1 of 2 tests and 1 of 5 tests'''