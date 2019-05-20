"_coolingchannel test module."
# pylint: disable-msg=R0904
# pylint: disable-msg=C0103

import unittest
from datetime import datetime

from test import _constants
from cdb import MCSerialNumber
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestMCSerialNumber(unittest.TestCase):
    "Test the _mcserialnumber module."
    
    def setUp(self):  # pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._mc = MCSerialNumber()
        self.maxDiff = None
    def test_str(self):
        "Test MCSerialNumber __str__."
        self.assertEquals(self._mc.__str__(), _constants.MC_STR)
        
    def test_get_status(self):
        "Test Coolingchannel get_status"
        self._mc.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._mc.get_status)
        self._mc.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._mc.get_status)
        self._mc.set_url("ok")
        self.assertEquals(self._mc.get_status(),
                          _constants.STATUS_OK)
    #def test_get_comment(self):
#
#        self.assertEquals(self._mc.get_comment(1), _constants.MC_COMMENT)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestMCSerialNumber))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

