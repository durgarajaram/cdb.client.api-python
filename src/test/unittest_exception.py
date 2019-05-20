"_exception test module"
#pylint: disable-msg=R0904

import unittest

from test import _constants
from cdb import CdbError

class TestException(unittest.TestCase):
    "Test the _exception module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._exception = CdbError(_constants.EXCEPT_STR)

    def test_str(self):
        "Test Exception __str__."
        self.assertEquals(self._exception.__str__(), _constants.EXCEPT_STR)
        self._exception.get_exception()

        
def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestException))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

