"_target test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import Target
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestTarget(unittest.TestCase):
    "Test the _target module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._target = Target()
        self._name = 'ISIS'

    def test_str(self):
        "Test Target __str__."
        self.assertEquals(self._target.__str__(), _constants.T_STR)
        
    def test_get_status(self):
        "Test Target get_status"
        self._target.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._target.get_status)
        self._target.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._target.get_status)
        self._target.set_url("ok")
        self.assertEquals(self._target.get_status(),
                          _constants.STATUS_OK)

    def test_get_current_blob(self):
        "Test Target get_current_blob."
        self._target.set_url("error")
        self.assertRaises(CdbPermanentError, self._target.get_current_blob,
                          self._name)
        self._target.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._target.get_current_blob,
                          self._name)
        self._target.set_url("ok")
        self.assertEquals(self._target.get_current_blob(self._name),
                          _constants.T_BLOB_CURRENT)
        self.assertEquals(self._target.get_current_blob(self._name),
                          _constants.T_BLOB_CURRENT)

    def test_get_blob_for_date(self):
        "Test Target get_blob_for_date."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._target.set_url("error")
        self.assertRaises(CdbPermanentError, self._target.get_blob_for_date,
                          self._name, _timestamp)
        self._target.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._target.get_blob_for_date,
                          self._name, _timestamp)
        self._target.set_url("ok")
        self.assertEquals(self._target.get_blob_for_date(self._name,
                          _timestamp), _constants.T_BLOB_FOR_DATE)

    def test_get_blob_for_run(self):
        "Test Target get_blob_for_run."
        _run = 1
        self._target.set_url("error")
        self.assertRaises(CdbPermanentError, self._target.get_blob_for_run,
                          self._name, _run)
        self._target.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._target.get_blob_for_run,
                          self._name, _run)
        self._target.set_url("ok")
        self.assertEquals(self._target.get_blob_for_run(self._name, _run),
                          _constants.T_BLOB_FOR_RUN)
        
    def test_get_target_names(self):
        "Test Target get_target_names."
        self.assertEquals(self._target.get_target_names(),
                          _constants.T_TARGET_NAMES)
        self.assertEquals(self._target.get_target_names(),
                          _constants.T_TARGET_NAMES)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestTarget))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

