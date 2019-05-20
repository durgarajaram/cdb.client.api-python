"_alarmhandler test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import BatchIteration
from cdb import CdbPermanentError
from cdb import CdbTemporaryError

class TestBatchIteration(unittest.TestCase):
    "Test the _batchiteration module."

    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._bi = BatchIteration()

    def test_str(self):
        "Test BatchIteration __str__."
        self.assertEquals(self._bi.__str__(), _constants.BI_STR)

    def test_get_status(self):
        "Test BatchIteration get_status"
        self._bi.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._bi.get_status)
        self._bi.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._bi.get_status)
        self._bi.set_url("ok")
        self.assertEquals(self._bi.get_status(),
                          _constants.STATUS_OK)

    def test_get_datarecord(self):
        "Test BatchIteration get_datarecord."
        _tag = "spam"
        self._bi.set_url("error")
        self.assertRaises(CdbPermanentError, self._bi.get_datarecord, _tag)
        self._bi.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bi.get_datarecord, _tag)
        self._bi.set_url("ok")
        # mock service returns the xml (from suds/_xml.py), it gets parsed and compared to the dictionary in _constants
        self.assertEquals(self._bi.get_datarecord(1),
                          _constants.BI_DATARECORD)
        # set the iteration number to 2 to get NOSUCHRECORD xml output : <error>    </error>
        # which should throw an exception
        self.assertRaises(CdbPermanentError,self._bi.get_datarecord,2)

    def test_get_reco_datacards(self):
        _tag="spam"
        self._bi.set_url("error")
        self.assertRaises(CdbPermanentError, self._bi.get_datarecord, _tag)
        self._bi.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bi.get_datarecord, _tag)
        self._bi.set_url("ok")
        self.assertEquals(self._bi.get_reco_datacards(1),
                          _constants.BI_RECORECORD)

    def test_get_mc_datacards(self):
        _tag="spam"
        self._bi.set_url("error")
        self.assertRaises(CdbPermanentError, self._bi.get_datarecord, _tag)
        self._bi.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bi.get_datarecord, _tag)
        self._bi.set_url("ok")
        self.assertEquals(self._bi.get_mc_datacards(1),
                          _constants.BI_MCRECORD)

    def test_get_comment(self):
        _tag="spam"
        self._bi.set_url("error")
        self.assertRaises(CdbPermanentError, self._bi.get_datarecord, _tag)
        self._bi.set_url("warn")
        self.assertRaises(CdbTemporaryError, self._bi.get_datarecord, _tag)
        self._bi.set_url("ok")
        self.assertEquals(self._bi.get_comment(1),
                          _constants.BI_COMMENT)