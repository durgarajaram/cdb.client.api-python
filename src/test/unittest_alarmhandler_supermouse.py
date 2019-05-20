"_alarmhandler_supermouse test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import AlarmHandlerSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError


class TestAlarmHandlerSuperMouse(unittest.TestCase):
    "Test the _alarmhandler_supermouse module."

    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._alh = AlarmHandlerSuperMouse()

    def test_str(self):
        "Test AlarmHandlerSuperMouse __str__."
        self.assertEquals(self._alh.__str__(), _constants.ALH_SM_STR)
        
    def test_get_status(self):
        "Test AlarmHandlerSuperMouse get_status"
        self._alh.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._alh.get_status)
        self._alh.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._alh.get_status)
        self._alh.set_url("ok")
        self.assertEquals(self._alh.get_status(),
                          _constants.STATUS_OK)

    def test_get_tagged_alh(self):
        "Test AlarmHandlerSuperMouse get_tagged_alh."
        _tag = "spam"
        self._alh.set_url("error")
        self.assertRaises(CdbPermanentError, self._alh.get_tagged_alh, _tag)
        self._alh.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._alh.get_tagged_alh, _tag)
        self._alh.set_url("ok")
        self.assertEquals(self._alh.get_tagged_alh(_tag),
                          _constants.ALH_TAGGED_ALH)
        self.assertEquals(self._alh.get_tagged_alh(_tag),
                          _constants.ALH_TAGGED_ALH)

    def test_get_used_alh(self):
        "Test AlarmHandlerSuperMouse get_used_alh."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._alh.set_url("error")
        self.assertRaises(CdbPermanentError, self._alh.get_used_alh, _timestamp)
        self._alh.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._alh.get_used_alh, _timestamp)
        self._alh.set_url("ok")
        self.assertEquals(self._alh.get_used_alh(_timestamp),
                          _constants.ALH_USED_ALH)

    def test_get_used_tags(self):
        "Test AlarmHandlerSuperMouse get_used_tags."
        _start_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        _stop_time = datetime.strptime("2029-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._alh.set_url("error")
        self.assertRaises(CdbPermanentError, self._alh.get_used_tags,
                          _start_time)
        self._alh.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._alh.get_used_tags,
                          _start_time)
        self._alh.set_url("ok")
        self.assertEquals(self._alh.get_used_tags(_start_time, _stop_time),
                          _constants.ALH_USED_TAGS)
    
    def test_list_tags(self):
        "Test AlarmHandlerSuperMouse list_tags."
        self._alh.set_url("error")
        self.assertRaises(CdbPermanentError, self._alh.list_tags)
        self._alh.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._alh.list_tags)
        self._alh.set_url("ok")
        self.assertEquals(self._alh.list_tags(), _constants.ALH_LIST_TAGS)
        
    def test_set_tagged_alh(self):
        "Test AlarmHandlerSuperMouse set_tagged_alh."
        self._alh.set_url("ok")
        self._alh.set_tagged_alh('tag1', _constants.ALH_SET_TAGGED_ALH)
        
    def test_set_tag_in_use(self):
        "Test AlarmHandlerSuperMouse set_tag_in_use."
        self._alh.set_url("ok")
        _creation_time = datetime.strptime("1999-12-31 23:59:59.999999",
                                        "%Y-%m-%d %H:%M:%S.%f")
        self._alh.set_tag_in_use('tag1', _creation_time)
        
        
def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestAlarmHandlerSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

