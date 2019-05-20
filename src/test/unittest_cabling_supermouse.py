"_cabling_supermouse test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import CablingSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestCablingSuperMouse(unittest.TestCase):
    "Test the _cabling_supermouse module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._cabling = CablingSuperMouse()

    def test_str(self):
        "Test CablingSuperMouse __str__."
        self.assertEquals(self._cabling.__str__(), _constants.CAB_SM_STR)
        
    def test_get_status(self):
        "Test CablingSuperMouse get_status"
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.get_status)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cabling.get_status)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_status(),
                          _constants.STATUS_OK)

    def test_get_current_cabling(self):
        "Test CablingSuperMouse get_current_cabling"
        _device = "Controls"
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError, self._cabling.get_current_cabling,
                          _device)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cabling.get_current_cabling,
                          _device)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_current_cabling(_device),
                          _constants.CAB_CABLING_CONTROLS)
        self.assertEquals(self._cabling.get_current_cabling("tracker 1"),
                          _constants.CAB_CABLING_TRACKER)

    def test_get_cabling_for_run(self):
        "Test CablingSuperMouse get_cabling_for_run."
        _device = "Controls"
        _run = 1
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.get_cabling_for_run, _device, _run)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cabling.get_cabling_for_run, _device, _run)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_cabling_for_run(_device, _run),
                          _constants.CAB_CABLING_CONTROLS)

    def test_get_cabling_for_date(self):
        "Test CablingSuperMouse get_cabling_for_date."
        _device = "Controls"
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.get_cabling_for_date, _device,
                          _timestamp)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cabling.get_cabling_for_date, _device,
                          _timestamp)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_cabling_for_date
                          (_device, _timestamp),
                          _constants.CAB_CABLING_CONTROLS)
        
    def test_list_devices(self):
        "Test CablingSuperMouse list_devices."
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.list_devices)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cabling.list_devices)
        self._cabling.set_url("cabling")
        self.assertEquals(self._cabling.list_devices(),
                          _constants.CAB_DEVICES)
        
    def test_add_control(self):
        "Test CablingSuperMouse add_control."
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.add_control(1, 2, 3, 'x11'),
                          _constants.STATUS_OK)
        
    def test_update_control(self):
        "Test CablingSuperMouse update_control."
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.update_control(1, 2, 3, 'x12'),
                          _constants.STATUS_OK)

    def test_set_tracker(self):
        "Test CablingSuperMouse set_tracker."
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.set_tracker('Tracker 1',
                          _constants.CAB_SET_TRACKER),
                          _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, self._cabling.set_tracker,
                          'Tracker 1', _constants.CAB_SET_TRACKER_ERROR)
        
    def test_set_detector(self):
        "Test CablingSuperMouse set_detector."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.set_detector('device', _timestamp,
                          "data"),
                          _constants.STATUS_OK)
        
def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestCablingSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

