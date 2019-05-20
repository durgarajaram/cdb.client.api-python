"_coolingchannel test module."
# pylint: disable-msg=R0904
# pylint: disable-msg=C0103

import unittest
from datetime import datetime

from test import _constants
from cdb import DataQuality
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestDataquality(unittest.TestCase):
    "Test the _dataquality module."
    
    def setUp(self):  # pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._dq = DataQuality()
        self.maxDiff = None
    def test_str(self):
        "Test Dataquality __str__."
        self.assertEquals(self._dq.__str__(), _constants.DQ_STR)
        
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
    def test_get_reconstruction_flags(self):
        result = self._dq.get_reconstruction_flags(7233, 'MAUS-v1.0.0', 1)
        self.assertEquals(result, _constants.DQ_DICT)
        # cannot convert string returned for run=0  to int:
        self.assertRaises(CdbPermanentError, self._dq.get_reconstruction_flags,0,'MAUS-v1.0.0', 1)

    def test_get_reconstruction_flags_for_detector(self):

        res = self._dq.get_reconstruction_flags_for_detector('RF1', 7233, 'MAUS-v1.0.0', 1)
        self.assertEquals(res, _constants.DQ_DICT['RF1'])
        # wrong det name:
        self.assertRaises(CdbPermanentError, self._dq.get_reconstruction_flags_for_detector,'RF7',7233,'MAUS-v1.0.0', 1)
        #

def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestDataquality))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

