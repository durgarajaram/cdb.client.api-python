"_coolingchannel_supermouse test module."
# pylint: disable-msg=R0904
# pylint: disable-msg=C0103

import unittest
import copy
from datetime import datetime

import _constants
from cdb import DataQualitySuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError

class TestDataqualitySuperMouse(unittest.TestCase):
    "Test the _coolingchannel_supermouse module."
    
    def setUp(self):  # pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._dq = DataQualitySuperMouse()
        self.maxDiff = None
    def test_str(self):
        "Test DataqualitySuperMouse __str__."
        self.assertEquals(self._dq.__str__(), _constants.DQ_SM_STR)

    def test_get_status(self):
        "Test Coolingchannel get_status"
        self._dq.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._dq.get_status)
        self._dq.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._dq.get_status)
        self._dq.set_url("ok")
        self.assertEquals(self._dq.get_status(),
                          _constants.STATUS_OK)

    def test_set_reconstruction_flags(self):

        self._dq.set_url("error")
        self.assertRaises(CdbPermanentError,self._dq.set_reconstruction_flags, 7272, 'MAUS-v1.0.0', 1, 'AFC01')

        self._dq.set_url("warn")
        self.assertRaises(CdbTemporaryError,self._dq.set_reconstruction_flags, 7272, 'MAUS-v1.0.0', 1, 'AFC01')

        self._dq.set_url("ok")
        self.assertEquals(self._dq.set_reconstruction_flags(7272, 'MAUS-v1.0.0', 1, 'AFC01'), _constants.STATUS_OK)



def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestDataqualitySuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

