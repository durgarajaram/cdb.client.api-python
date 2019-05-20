"_coolingchannel test module."
# pylint: disable-msg=R0904
# pylint: disable-msg=C0103

import unittest
from datetime import datetime

from test import _constants
from cdb import CoolingChannel
from cdb import CdbPermanentError
from cdb import CdbTemporaryError
from cdb._coolingchannel import _get_float
from cdb._coolingchannel import _get_int


class TestCoolingchannel(unittest.TestCase):
    "Test the _coolingchannel module."
    
    def setUp(self):  # pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._cc = CoolingChannel()
        self.maxDiff = None
    def test_str(self):
        "Test Coolingchannel __str__."
        self.assertEquals(self._cc.__str__(), _constants.CC_STR)
        
    def test_get_status(self):
        "Test Coolingchannel get_status"
        self._cc.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cc.get_status)
        self._cc.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cc.get_status)
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_status(),
                          _constants.STATUS_OK)

    def test_get_all_coolingchannels(self):
        "Test Coolingchannel get_all_coolingchannels."
        self._cc.set_url("error")
        self.assertRaises(CdbPermanentError, self._cc.get_all_coolingchannels)
        self._cc.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cc.get_all_coolingchannels)
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_all_coolingchannels(), _constants.CC_ALL)
        self.assertEquals(self._cc.get_all_coolingchannels(), _constants.CC_ALL)
   
    def test_get_coolingchannel_for_run(self):
        "Test Coolingchannel get_coolingchannel_for_run."
        _run_number = 666
        self._cc.set_url("error")
        self.assertRaises(CdbPermanentError, 
                          self._cc.get_coolingchannel_for_run, _run_number)
        self._cc.set_url("warn")
        self.assertRaises(CdbTemporaryError, 
                          self._cc.get_coolingchannel_for_run, _run_number)
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_coolingchannel_for_run(_run_number),
                          _constants.CC_RUN)
        
    def test_get_coolingchannel_for_date(self):
        "Test Coolingchannel get_coolingchannel_for_date."
        _start_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._cc.set_url("error")
        self.assertRaises(CdbPermanentError, 
                          self._cc.get_coolingchannel_for_date, _start_time)
        self._cc.set_url("warn")
        self.assertRaises(CdbTemporaryError, 
                          self._cc.get_coolingchannel_for_date, _start_time)
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_coolingchannel_for_date(_start_time),
                          _constants.CC_DATE)
        self.assertEquals(self._cc.get_coolingchannel_for_date(_start_time),
                          _constants.CC_DATE)
      
    def test_get_coolingchannel_for_tag(self):
        "Test Coolingchannel get_coolingchannels_for_tag."
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_coolingchannel_for_tag(1),
                           _constants.CC_TAG_1)
        self.assertEquals(self._cc.get_coolingchannel_for_tag(2),
                           _constants.CC_TAG_1)
        self.assertEquals(self._cc.get_coolingchannel_for_tag(3),
                           _constants.CC_TAG_3)
        
    def test_list_tags(self):
        "Test Coolingchannel list_tags."
        self._cc.set_url("coolingchannel")
        self.assertEquals(self._cc.list_tags(), _constants.CC_TAGS)
        
    def test_get_float(self):
        "Test Coolingchannel _get_float."
        self.assertEquals(_get_float(""), None)

    def test_get_int(self):
        "Test Coolingchannel _get_int."
        self.assertEquals(_get_int(""), None)

    def test_get_absorber_for_run(self):
        self._cc.set_url("ok")
        run = 5624  # this run number is fixed in the XML the server returns
        self.assertEquals(self._cc.get_absorber_for_run(run), {run:_constants.CC_ABS})

    def test_get_absorber_for_tag(self):
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_absorber_for_tag('navi_tag'), _constants.CC_ABS_TAG)

    def test_list_absorber_tags(self):
        self._cc.set_url("ok")
        self.assertEquals(self._cc.list_absorber_tags(), _constants.CC_LIST_ABS_TAGS)
        self._cc.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._cc.list_absorber_tags)
        self._cc.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._cc.list_absorber_tags)

def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestCoolingchannel))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

