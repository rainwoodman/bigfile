import sys
import os

from numpy.testing import Tester

# need an install to run these tests

from sys import argv

tester = Tester()
result = tester.test(extra_argv=['-w', 'tests'] + argv[1:])
if not result:
    raise Exception("Test Failed")
