"_cabling test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import Cabling
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestCabling(unittest.TestCase):
    "Test the _cabling module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._cabling = Cabling()

    def test_str(self):
        "Test Cabling __str__."
        self.assertEquals(self._cabling.__str__(), _constants.CAB_STR)
        
    def test_get_status(self):
        "Test Cabling get_status"
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
        "Test Cabling get_current_cabling"
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
        _device = "tracker 1"
        self.assertEquals(self._cabling.get_current_cabling(_device),
                          _constants.CAB_CABLING_TRACKER)
        _device = "Ckov A"
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError, self._cabling.get_current_cabling,
                          _device)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cabling.get_current_cabling,
                          _device)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_current_cabling(_device),
                          _constants.CAB_B64)
        
    def test_get_cabling_for_run(self):
        "Test Cabling get_cabling_for_run."
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
        _device = "Ckov A"
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.get_cabling_for_run, _device, _run)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cabling.get_cabling_for_run, _device, _run)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_cabling_for_run(_device, _run),
                          _constants.CAB_B64)
        
    def test_get_cabling_for_date(self):
        "Test Cabling get_cabling_for_date."
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
        _device = "Ckov A"
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
                          (_device, _timestamp), _constants.CAB_B64)

    def test_get_cabling_for_id(self):
        "Test Cabling get_cabling_for_id."
        _id = 1
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.get_cabling_for_id, _id)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cabling.get_cabling_for_id, _id)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_cabling_for_id(_id),
                          _constants.CAB_B64)
                        
    def test_get_ids(self):
        "Test Cabling get_ids."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                       "%Y-%m-%d %H:%M:%S.%f")
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.get_ids, _timestamp)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cabling.get_ids, _timestamp)
        self._cabling.set_url("ok")
        self.assertEquals(self._cabling.get_ids(_timestamp),
                          _constants.CAB_IDS)
        self.assertEquals(self._cabling.get_ids(_timestamp, _timestamp),
                          _constants.CAB_IDS) 
               
    def test_list_devices(self):
        "Test Cabling list_devices."
        self._cabling.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cabling.list_devices)
        self._cabling.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cabling.list_devices)
        self._cabling.set_url("cabling")
        self.assertEquals(self._cabling.list_devices(),
                          _constants.CAB_DEVICES)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestCabling))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

