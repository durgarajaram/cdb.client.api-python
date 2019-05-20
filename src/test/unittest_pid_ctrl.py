"_pid_ctrl test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import PIDCtrl
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestPIDCtrl(unittest.TestCase):
    "Test the _pid_ctrl module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._pid_ctrl = PIDCtrl()

    def test_str(self):
        "Test PIDCtrl __str__."
        self.assertEquals(self._pid_ctrl.__str__(), _constants.C_STR)
        
    def test_get_status(self):
        "Test PIDCtrl get_status"
        self._pid_ctrl.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._pid_ctrl.get_status)
        self._pid_ctrl.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._pid_ctrl.get_status)
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.get_status(),
                          _constants.STATUS_OK)

    def test_get_pid_ctrls(self):
        "Test PIDCtrl get_pid_ctrls"
        self._pid_ctrl.set_url("error")
        self.assertRaises(CdbPermanentError, self._pid_ctrl.get_pid_ctrls)
        self._pid_ctrl.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._pid_ctrl.get_pid_ctrls)
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.get_pid_ctrls(),
                          _constants.C_CONTROLS)
        self.assertEquals(self._pid_ctrl.get_pid_ctrls(),
                          _constants.C_CONTROLS)

    def test_get_pid_ctrls_for_crate(self):
        "Test PIDCtrl get_pid_ctrls_for_crate."
        _crate = 1
        self._pid_ctrl.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._pid_ctrl.get_pid_ctrls_for_crate, _crate)
        self._pid_ctrl.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._pid_ctrl.get_pid_ctrls_for_crate, _crate)
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.get_pid_ctrls_for_crate(_crate),
                          _constants.C_CONTROLS_FOR_CRATE)

    def test_get_pid_ctrls_for_channel(self):
        "Test PIDCtrl get_pid_ctrls_for_channel."
        _crate = 1
        _slot = 1
        _channel = 1
        self._pid_ctrl.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._pid_ctrl.get_pid_ctrls_for_channel,
                          _crate, _slot, _channel)
        self._pid_ctrl.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._pid_ctrl.get_pid_ctrls_for_channel,
                          _crate, _slot, _channel)
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.get_pid_ctrls_for_channel
                          (_crate, _slot, _channel),
                          _constants.C_CONTROLS_FOR_CRATE)
        
    def test_get_previous_settings(self):
        "Test PIDCtrl get_previous_settings."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._pid_ctrl.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._pid_ctrl.get_previous_settings, _timestamp)
        self._pid_ctrl.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._pid_ctrl.get_previous_settings, _timestamp)
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.get_previous_settings(_timestamp),
                          _constants.C_CONTROLS_FOR_PREVIOUS)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestPIDCtrl))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

