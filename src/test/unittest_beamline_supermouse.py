"_beamline_supermouse test module."
#pylint: disable-msg=R0904
#pylint: disable-msg=C0103

import unittest
from datetime import datetime

from test import _constants
from test.suds import _xml
from cdb import BeamlineSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError
from cdb._beamline import _get_float
from cdb._beamline import _get_int
from cdb._beamline import _get_long


class TestBeamlineSuperMouse(unittest.TestCase):
    "Test the _beamline_supermouse module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._bl = BeamlineSuperMouse()
        self.maxDiff = None
    def test_str(self):
        "Test BeamlineSuperMouse __str__."
        self.assertEquals(self._bl.__str__(), _constants.BL_SM_STR)
        
    def test_get_status(self):
        "Test BeamlineSuperMouse get_status"
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
        "Test BeamlineSuperMouse get_all_beamlines."
        self._bl.set_url("error")
        self.assertRaises(CdbPermanentError, self._bl.get_all_beamlines)
        self._bl.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bl.get_all_beamlines)
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_all_beamlines(), _constants.BL_RUNS)
        self.assertEquals(self._bl.get_all_beamlines(), _constants.BL_RUNS)
        
    def test_get_all_beamlines_xml(self):
        "Test BeamlineSuperMouse get_all_beamlines_xml."
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_all_beamlines_xml(), _xml.BL_RUNS)
        
    def test_get_beamline_for_run(self):
        "Test BeamlineSuperMouse get_beamline_for_run."
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
        "Test BeamlineSuperMouse get_beamline_for_run_xml."
        _run_number = 666
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamline_for_run_xml(_run_number),
                          _xml.BL_RUN)
        
    def test_get_beamlines_for_dates(self):
        "Test BeamlineSuperMouse get_beamlines_for_dates."
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
        "Test BeamlineSuperMouse get_beamlines_for_dates_xml."
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
        "Test BeamlineSuperMouse get_beamlines_for_pulses."
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
        "Test BeamlineSuperMouse get_beamlines_for_pulses_xml."
        _start_pluse = 1
        _end_pulse = 2
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamlines_for_pulses_xml(_start_pluse,
                          _end_pulse), _xml.BL_PULSES)
        self.assertEquals(self._bl.get_beamlines_for_pulses_xml(_start_pluse),
                           _xml.BL_PULSES)
        
    def test_get_beamline_for_tag(self):
        "Test BeamlineSuperMouse get_beamlines_for_tag."
        _tag = 1
        self._bl.set_url("ok")
        self.assertEquals(self._bl.get_beamline_for_tag(_tag),
                           _constants.BL_TAG)

    def test_list_tags(self):
        "Test BeamlineSuperMouse list_tags."
        self._bl.set_url("beamline")
        self.assertEquals(self._bl.list_tags(), _constants.BL_TAGS)
        
    def test_set_start_run(self):
        "Test BeamlineSuperMouse set_start_run."
        self._bl.set_url("ok")
        self.assertEquals(self._bl.set_start_run(_constants.BL_START_RUN),
                          _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, self._bl.set_start_run,
                          _constants.BL_START_RUN_ERROR)
        self.assertRaises(CdbPermanentError, self._bl.set_start_run,
                          _constants.BL_START_RUN_ERROR_LDC)
                
    def test_set_end_run(self):
        "Test BeamlineSuperMouse set_start_run."
        self._bl.set_url("ok")
        self.assertEquals(self._bl.set_end_run(_constants.BL_END_RUN,
                          _constants.BL_END_RUN_SCALAR,
                          _constants.BL_END_RUN_ISIS_BEAM),
                          _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, self._bl.set_end_run,
                          _constants.BL_END_RUN_ERROR,
                          _constants.BL_END_RUN_ERROR,
                          _constants.BL_END_RUN_ERROR)

    def test_set_beamline(self):
        "Test BeamlineSuperMouse set_beamline."
        self._bl.set_url("ok")
        self.assertEquals(self._bl.set_beamline(_constants.BL_BEAMLINE_1,
                          _constants.BL_BEAMLINE_MAGNETS),
                          _constants.STATUS_OK)    
        self.assertEquals(self._bl.set_beamline(_constants.BL_BEAMLINE_2,
                          _constants.BL_BEAMLINE_MAGNETS),
                          _constants.STATUS_OK)  
        self.assertRaises(CdbPermanentError, self._bl.set_beamline,
                          _constants.BL_BEAMLINE_ERROR_1,
                          _constants.BL_BEAMLINE_MAGNETS)
        self.assertRaises(CdbPermanentError, self._bl.set_beamline,
                          _constants.BL_BEAMLINE_ERROR_2,
                          _constants.BL_BEAMLINE_MAGNETS)
        self.assertRaises(CdbPermanentError, self._bl.set_beamline,
                          _constants.BL_BEAMLINE_1,
                          _constants.BL_BEAMLINE_MAGNETS_ERROR)
        
    def test_set_beamline_tag(self):
        "Test BeamlineSuperMouse set_beamline_tag."
        self.assertEquals(self._bl.set_beamline_tag('1',
                          _constants.BL_BEAMLINE_1,
                          _constants.BL_BEAMLINE_MAGNETS),
                          _constants.STATUS_OK)    
        self.assertEquals(self._bl.set_beamline_tag('1',
                          _constants.BL_BEAMLINE_2,
                          _constants.BL_BEAMLINE_MAGNETS),
                          _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, self._bl.set_beamline_tag, '1',
                          _constants.BL_BEAMLINE_ERROR_1,
                          _constants.BL_BEAMLINE_MAGNETS)
        self.assertRaises(CdbPermanentError, self._bl.set_beamline_tag, '1',
                          _constants.BL_BEAMLINE_ERROR_2,
                          _constants.BL_BEAMLINE_MAGNETS)
        
    def test_get_float(self):
        "Test BeamlineSuperMouse _get_float."
        self.assertEquals(_get_float(""), None)

    def test_get_int(self):
        "Test BeamlineSuperMouse _get_int."
        self.assertEquals(_get_int(""), None)

    def test_get_long(self):
        "Test BeamlineSuperMouse _get_long."
        self.assertEquals(_get_long(""), None)


def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestBeamlineSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

