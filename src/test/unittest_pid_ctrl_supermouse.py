"_pid_ctrl_supermouse test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import PIDCtrlSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestPIDCtrlSuperMouse(unittest.TestCase):
    "Test the _pid_ctrl_supermouse module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._pid_ctrl = PIDCtrlSuperMouse()

    def test_str(self):
        "Test PIDCtrlSuperMouse __str__."
        self.assertEquals(self._pid_ctrl.__str__(), _constants.C_SM_STR)
        
    def test_get_status(self):
        "Test PIDCtrlSuperMouse get_status"
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
        "Test PIDCtrlSuperMouse get_pid_ctrls"
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
        "Test PIDCtrlSuperMouse get_pid_ctrls_for_crate."
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
        "Test PIDCtrlSuperMouse get_pid_ctrls_for_channel."
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
        "Test PIDCtrlSuperMouse get_previous_settings."
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
        
    def test_set_parameter(self):
        "Test PIDCtrlSuperMouse set_parameter."
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.set_parameter(1, 2, 3, 'a', 'b'),
                          _constants.STATUS_OK)

    def test_update_parameter(self):
        "Test PIDCtrlSuperMouse update_parameter."
        self._pid_ctrl.set_url("ok")
        self.assertEquals(self._pid_ctrl.update_parameter(4, 5, 6, 'c', 'd'),
                          _constants.STATUS_OK)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestPIDCtrlSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

