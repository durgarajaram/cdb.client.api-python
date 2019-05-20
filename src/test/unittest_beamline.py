"_beamline test module."
#pylint: disable-msg=R0904
#pylint: disable-msg=C0103

import unittest
from datetime import datetime

from test import _constants
from test.suds import _xml
from cdb import Beamline
from cdb import CdbPermanentError
from cdb import CdbTemporaryError
from cdb._beamline import _get_float
from cdb._beamline import _get_int
from cdb._beamline import _get_long


class TestBeamline(unittest.TestCase):
    "Test the _beamline module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._bl = Beamline()
        self.maxDiff = None
    def test_str(self):
        "Test Beamline __str__."
        self.assertEquals(self._bl.__str__(), _constants.BL_STR)
        
    def test_get_status(self):
        "Test Beamline get_status"
        self._bl.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._bl.get_status)
        self._bl.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._bl.get_status)
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_status(),
                          _constants.STATUS_OK)

    def test_get_all_beamlines(self):
        "Test Beamline get_all_beamlines."
        self._bl.set_url("error")
        self.assertRaises(CdbPermanentError, self._bl.get_all_beamlines)
        self._bl.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bl.get_all_beamlines)
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_all_beamlines(), _constants.BL_RUNS)
        self.assertEquals(self._bl.get_all_beamlines(), _constants.BL_RUNS)
        
    def test_get_all_beamlines_xml(self):
        "Test Beamline get_all_beamlines_xml."
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_all_beamlines_xml(), _xml.BL_RUNS)
        
    def test_get_beamline_for_run(self):
        "Test Beamline get_beamline_for_run."
        _run_number = 666
        self._bl.set_url("error")
        self.assertRaises(CdbPermanentError, self._bl.get_beamline_for_run,
                          _run_number)
        self._bl.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bl.get_beamline_for_run,
                          _run_number)
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamline_for_run(_run_number),
                          _constants.BL_RUN)
        
    def test_get_beamline_for_run_xml(self):
        "Test Beamline get_beamline_for_run_xml."
        _run_number = 666
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamline_for_run_xml(_run_number),
                          _xml.BL_RUN)
        
    def test_get_beamlines_for_dates(self):
        "Test Beamline get_beamlines_for_dates."
        _start_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        _stop_time = datetime.strptime("2029-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._bl.set_url("error")
        self.assertRaises(CdbPermanentError, self._bl.get_beamlines_for_dates,
                          _start_time)
        self._bl.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bl.get_beamlines_for_dates,
                          _start_time)
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamlines_for_dates(_start_time),
                          _constants.BL_DATES)
        self.assertEquals(self._bl.get_beamlines_for_dates(_start_time,
                          _stop_time), _constants.BL_DATES)
        self.assertEquals(self._bl.get_beamlines_for_dates
                         (_start_time, None), _constants.BL_DATES)
    
    def test_get_beamlines_for_dates_xml(self):
        "Test Beamline get_beamlines_for_dates_xml."
        _start_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        _stop_time = datetime.strptime("2029-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamlines_for_dates_xml(_start_time),
                          _xml.BL_DATES)
        self.assertEquals(self._bl.get_beamlines_for_dates_xml(_start_time,
                          _stop_time), _xml.BL_DATES)
        self.assertEquals(self._bl.get_beamlines_for_dates_xml
                         (_start_time, None), _xml.BL_DATES)  
            
    def test_get_beamlines_for_pulses(self):
        "Test Beamline get_beamlines_for_pulses."
        _start_pluse = 1
        _end_pulse = 2
        self._bl.set_url("error")
        self.assertRaises(CdbPermanentError, self._bl.get_beamlines_for_pulses,
                          _start_pluse, _end_pulse)
        self._bl.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bl.get_beamlines_for_pulses,
                          _start_pluse, _end_pulse)
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamlines_for_pulses(_start_pluse,
                          _end_pulse), _constants.BL_PULSES)
        self.assertEquals(self._bl.get_beamlines_for_pulses(_start_pluse
                          ), _constants.BL_PULSES)

    def test_get_beamlines_for_pulses_xml(self):
        "Test Beamline get_beamlines_for_pulses_xml."
        _start_pluse = 1
        _end_pulse = 2
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamlines_for_pulses_xml(_start_pluse,
                          _end_pulse), _xml.BL_PULSES)
        self.assertEquals(self._bl.get_beamlines_for_pulses_xml(_start_pluse),
                           _xml.BL_PULSES)
        
    def test_get_beamline_for_tag(self):
        "Test Beamline get_beamlines_for_tag."
        _tag = 1
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamline_for_tag(_tag),
                           _constants.BL_TAG)

    def test_list_tags(self):
        "Test Beamline list_tags."
        self._bl.set_url("beamline")
        self.assertEquals(self._bl.list_tags(), _constants.BL_TAGS)
        
    def test_get_float(self):
        "Test Beamline _get_float."
        self.assertEquals(_get_float(""), None)

    def test_get_int(self):
        "Test Beamline _get_int."
        self.assertEquals(_get_int(""), None)

    def test_get_long(self):
        "Test Beamline _get_long."
        self.assertEquals(_get_long(""), None)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestBeamline))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

