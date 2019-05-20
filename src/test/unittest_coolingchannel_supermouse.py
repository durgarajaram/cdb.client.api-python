"_coolingchannel_supermouse test module."
# pylint: disable-msg=R0904
# pylint: disable-msg=C0103

import unittest
import copy
from datetime import datetime

import _constants
from cdb import CoolingChannelSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError
from cdb._coolingchannel import _get_float
from cdb._coolingchannel import _get_int


class TestCoolingchannelSuperMouse(unittest.TestCase):
    "Test the _coolingchannel_supermouse module."
    
    def setUp(self):  # pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._cc = CoolingChannelSuperMouse()
        self.maxDiff = None
    def test_str(self):
        "Test CoolingchannelSuperMouse __str__."
        self.assertEquals(self._cc.__str__(), _constants.CC_SM_STR)
        
    def test_get_status(self):
        "Test CoolingchannelSuperMouse get_status"
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
        "Test CoolingchannelSuperMouse get_all_coolingchannels."
        self._cc.set_url("error")
        self.assertRaises(CdbPermanentError, self._cc.get_all_coolingchannels)
        self._cc.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._cc.get_all_coolingchannels)
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_all_coolingchannels(), _constants.CC_ALL)
        self.assertEquals(self._cc.get_all_coolingchannels(), _constants.CC_ALL)
    
    def test_get_coolingchannel_for_run(self):
        "Test CoolingchannelSuperMouse get_coolingchannel_for_run."
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
        "Test CoolingchannelSuperMouse get_coolingchannels_for_tag."
        self._cc.set_url("ok")
        self.assertEquals(self._cc.get_coolingchannel_for_tag(3),
                           _constants.CC_TAG_3)

    def test_list_tags(self):
        "Test CoolingchannelSuperMouse list_tags."
        self._cc.set_url("coolingchannel")
        self.assertEquals(self._cc.list_tags(), _constants.CC_TAGS)

    def test_set_coolingchannel(self):
        "Test CoolingchannelSuperMouse set_coolingchannel."
        self._cc.set_url("ok")
        self.assertEquals(self._cc.set_coolingchannel(_constants.CC_1),
                          _constants.STATUS_OK)    
        self.assertEquals(self._cc.set_coolingchannel(_constants.CC_2),
                          _constants.STATUS_OK)  
        self.assertRaises(CdbPermanentError, self._cc.set_coolingchannel,
                          _constants.CC_ERROR_1)
        self.assertRaises(CdbPermanentError, self._cc.set_coolingchannel,
                          _constants.CC_ERROR_2)
        self.assertRaises(CdbPermanentError, self._cc.set_coolingchannel,
                          _constants.CC_ERROR_3)
                
    def test_set_coolingchannel_tag(self):
        "Test CoolingchannelSuperMouse set_coolingchannel_tag."
        self.assertEquals(self._cc.set_coolingchannel_tag('1',
                          _constants.CC_1), _constants.STATUS_OK)    
        self.assertEquals(self._cc.set_coolingchannel_tag('1',
                          _constants.CC_2), _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, self._cc.set_coolingchannel_tag,
                           '1', _constants.CC_ERROR_1)
        self.assertRaises(CdbPermanentError, self._cc.set_coolingchannel_tag,
                           '1', _constants.CC_ERROR_2)
        self.assertRaises(CdbPermanentError, self._cc.set_coolingchannel_tag,
                           '1', _constants.CC_ERROR_3) 

    def test_set_coolingchannel_csv_tag(self):
        "Test CoolingchannelSuperMouse set_coolingchannel_csv_tag."
        print 'BURP'
        self.assertEquals(
          self._cc.set_coolingchannel_csv_tag(copy.deepcopy(_constants.CC_CSV)),
          _constants.STATUS_OK)
        self.assertRaises(CdbPermanentError, 
                          self._cc.set_coolingchannel_csv_tag,
                          _constants.CC_CSV_ERROR_1)
        self.assertRaises(CdbPermanentError, 
                          self._cc.set_coolingchannel_csv_tag,
                          _constants.CC_CSV_ERROR_2)
        self.assertRaises(CdbPermanentError, 
                          self._cc.set_coolingchannel_csv_tag,
                          _constants.CC_CSV_ERROR_3)
        test_tag, test_data = self._cc._coolingchannel_csv(_constants.CC_CSV)
        self.assertEqual(test_tag, "0_to_240FlipP2")
        self.assertEqual(test_data[0]['polarity'], '-1')
        self.assertEqual(test_data[0]['name'], 'SS1')
        self.assertEqual(test_data[0]['coils'][0],
            {'name':'SS1-M1', 'vlim':6.0, 'ilim':300.0, 'rate':23.66,
            'iset':270.3, 'stability':0.0, 'calibration':1.0})
        self.assertEqual(len(test_data[0]['coils']), 5)


    def test_get_float(self):
        "Test CoolingchannelSuperMouse _get_float."
        self.assertEquals(_get_float(""), None)

    def test_get_int(self):
        "Test CoolingchannelSuperMouse _get_int."
        self.assertEquals(_get_int(""), None)

    def test_set_coolingchannel_absorber(self):
        self._cc.set_url('ok')
        self.assertEquals(self._cc.set_absorber(5624, _constants.CC_ABS),_constants.STATUS_OK)
        broken_absorbers=copy.deepcopy(_constants.CC_ABS)
        broken_absorbers[0].pop('name')
        self.assertRaises(CdbPermanentError, self._cc.set_absorber, 5624, broken_absorbers) # missing key.
        # server errors:
        self._cc.set_url('warn')
        self.assertRaises(CdbTemporaryError, self._cc.set_absorber, 5624, _constants.CC_ABS)
        self._cc.set_url('error')
        self.assertRaises(CdbPermanentError, self._cc.set_absorber, 5624, _constants.CC_ABS)

    def test_set_coolingchannel_absorber_tag(self):
        self._cc.set_url('ok')
        # pass a value of tag dict only (i.e absorber list only):
        self.assertEquals(self._cc.set_absorber_tag('navi_tag', _constants.CC_ABS_TAG['navi_tag']),_constants.STATUS_OK)
        broken_absorber_tag=copy.deepcopy(_constants.CC_ABS_TAG)
        broken_absorber_tag['navi_tag'][0].pop('name')  # name of first absorber in the tag
        self.assertRaises(CdbPermanentError, self._cc.set_absorber_tag, 'navi_tag', broken_absorber_tag['navi_tag'])  # missing key.
        # server errors:
        self._cc.set_url('warn')
        self.assertRaises(CdbTemporaryError, self._cc.set_absorber_tag, 'navi_tag', _constants.CC_ABS)  # absorbe list only
        self._cc.set_url('error')
        self.assertRaises(CdbPermanentError, self._cc.set_absorber_tag, 'navi_tag', _constants.CC_ABS)  # absorber list only

def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestCoolingchannelSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

