"_calibration test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import Calibration
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestCalibration(unittest.TestCase):
    "Test the _calibration module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._calibration = Calibration()

    def test_str(self):
        "Test Calibration __str__."
        self.assertEquals(self._calibration.__str__(), _constants.CAL_STR)
        
    def test_get_status(self):
        "Test Calibration get_status"
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
        "Test Calibration get_current_calibration"
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
        _device = "Ckov A"
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_current_calibration, _device)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._calibration.get_current_calibration, _device)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_current_calibration(_device),
                          _constants.CAL_B64)
        
    def test_get_calibration_for_run(self):
        "Test Calibration get_calibration_for_run."
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
        _device = "Ckov A"
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
                          (_device, _run), _constants.CAL_B64)
        
    def test_get_calibration_for_date(self):
        "Test Calibration get_calibration_for_date."
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
        _device = "Ckov A"
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
                          (_device, _timestamp), _constants.CAL_B64)
                
    def test_get_calibration_for_id(self):
        "Test Calibration get_calibration_for_id."
        _id = 1
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_calibration_for_id, _id)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._calibration.get_calibration_for_id, _id)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_calibration_for_id(_id),
                          _constants.CAL_B64)
        
    def test_get_ids(self):
        "Test Calibration get_ids."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                       "%Y-%m-%d %H:%M:%S.%f")
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.get_ids, _timestamp)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._calibration.get_ids,
                           _timestamp)
        self._calibration.set_url("ok")
        self.assertEquals(self._calibration.get_ids(_timestamp),
                          _constants.CAL_IDS)
        self.assertEquals(self._calibration.get_ids(_timestamp, _timestamp),
                          _constants.CAL_IDS) 

    def test_list_devices(self):
        "Test Calibration list_devices."
        self._calibration.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._calibration.list_devices)
        self._calibration.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._calibration.list_devices)
        self._calibration.set_url("calibration")
        self.assertEquals(self._calibration.list_devices(),
                          _constants.CAL_DEVICES)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestCalibration))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

