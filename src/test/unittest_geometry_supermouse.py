"_geometry test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import GeometrySuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestGeometrySuperMouse(unittest.TestCase):
    "Test the _geometry module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._geo = GeometrySuperMouse()
    def test_str(self):
        "Test GeometrySuperMouse __str__."
        self.assertEquals(self._geo.__str__(), _constants.G_SM_STR)
        
    def test_get_status(self):
        "Test GeometrySuperMouse get_status"
        self._geo.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._geo.get_status)
        self._geo.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._geo.get_status)
        self._geo.set_url("ok")
        self.assertEquals(self._geo.get_status(),
                          _constants.STATUS_OK)

    def test_get_current_gdml(self):
        "Test GeometrySuperMouse get_current_gdml."
        self._geo.set_url("error")
        self.assertRaises(CdbPermanentError, self._geo.get_current_gdml)
        self._geo.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._geo.get_current_gdml)
        self._geo.set_url("ok")
        self.assertEquals(self._geo.get_current_gdml(),
                          _constants.G_GDML_CURRENT)
        self.assertEquals(self._geo.get_current_gdml(),
                          _constants.G_GDML_CURRENT)

    def test_get_gdml_for_id(self):
        "Test GeometrySuperMouse get_gdml_for_id."
        _id = 1
        self._geo.set_url("error")
        self.assertRaises(CdbPermanentError, self._geo.get_gdml_for_id, _id)
        self._geo.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._geo.get_gdml_for_id, _id)
        self._geo.set_url("ok")
        self.assertEquals(self._geo.get_gdml_for_id(_id),
                          _constants.G_GDML_FOR_ID)

    def test_get_gdml_for_run(self):
        "Test GeometrySuperMouse get_gdml_for_run."
        _run = 1
        self._geo.set_url("error")
        self.assertRaises(CdbPermanentError, self._geo.get_gdml_for_run, _run)
        self._geo.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._geo.get_gdml_for_run, _run)
        self._geo.set_url("ok")
        self.assertEquals(self._geo.get_gdml_for_run(_run),
                          _constants.G_GDML_FOR_RUN)
        
    def test_get_ids(self):
        "Test GeometrySuperMouse get_ids."
        _start_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        _stop_time = datetime.strptime("2029-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._geo.set_url("error")
        self.assertRaises(CdbPermanentError, self._geo.get_ids, _start_time)
        self._geo.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._geo.get_ids, _start_time)
        self._geo.set_url("ok")
        self.assertEquals(self._geo.get_ids(_start_time), _constants.G_IDS)
        self.assertEquals(self._geo.get_ids(_start_time, _stop_time),
                           _constants.G_IDS)

    def test_set_gdml(self):
        "Test GeometrySuperMouse set_gdml."
        self._geo.set_url("ok")
        _valid_from_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self.assertEquals(self._geo.set_gdml('ab%$2f', 
                          _valid_from_time, 'blah', 'v1.5'), 
                          _constants.STATUS_OK)

    def test_set_corrections(self):
        self._geo.set_url("ok")
        gid=12
        ret = self._geo.set_corrections(_constants.G_CORR, gid, "test correction setting")
        self.assertEquals(ret, u'Geometry Corrections stored')

        
def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestGeometrySuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

