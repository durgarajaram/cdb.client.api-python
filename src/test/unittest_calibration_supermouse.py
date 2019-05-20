"_calibration_supermouse test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import CalibrationSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestCalibrationSuperMouse(unittest.TestCase):
    "Test the _calibration_supermouse module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._calibration = CalibrationSuperMouse()

    def test_str(self):
        "Test CalibrationSuperMouse __str__."
        self.assertEquals(self._calibration.__str__(), _constants.CAL_SM_STR)
        
    def test_get_status(self):
        "Test CalibrationSuperMouse get_status"
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_status)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._calibration.get_status)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_status(),
                          _constants.STATUS_OK)
        
    def test_get_current_calibration(self):
        "Test CalibrationSuperMouse get_current_calibration"
        _device = "tracker 1"
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_current_calibration, _device)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._calibration.get_current_calibration, _device)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_current_calibration(_device),
                          _constants.CAL_CALIBRATION_TRACKER)

    def test_get_calibration_for_run(self):
        "Test CalibrationSuperMouse get_calibration_for_run."
        _device = "tracker 1"
        _run = 1
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_calibration_for_run,
                          _device, _run)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._calibration.get_calibration_for_run,
                          _device, _run)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_calibration_for_run
                          (_device, _run), _constants.CAL_CALIBRATION_TRACKER)

    def test_get_calibration_for_date(self):
        "Test CalibrationSuperMouse get_calibration_for_date."
        _device = "tracker 1"
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_calibration_for_date, _device,
                          _timestamp)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._calibration.get_calibration_for_date, _device,
                          _timestamp)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_calibration_for_date
                          (_device, _timestamp),
                          _constants.CAL_CALIBRATION_TRACKER)
        
    def test_list_devices(self):
        "Test CalibrationSuperMouse list_devices."
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.list_devices)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._calibration.list_devices)
        self._calibration.set_url("calibration")
        self.assertEquals(self._calibration.list_devices(),
                          _constants.CAL_DEVICES)
        
    def test_set_tracker(self):
        "Test CalibrationSuperMouse set_tracker."
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.set_tracker("TRACKER 1",
                          _constants.CAL_SET_TRACKER), _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, self._calibration.set_tracker,
                          "TRACKER 1", _constants.CAL_SET_TRACKER_ERROR)

    def test_set_detector(self):
        "Test CalibrationSuperMouse set_detector."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.set_detector("device",
                          "calibration_type", _timestamp, "value"),
                          _constants.STATUS_OK)
       
def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestCalibrationSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

