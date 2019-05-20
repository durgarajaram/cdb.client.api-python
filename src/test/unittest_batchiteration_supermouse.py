"_alarmhandler test module"
#pylint: disable-msg=R0904

import unittest
from test import _constants

from cdb import CdbPermanentError
from cdb import CdbTemporaryError
from test import _constants
from cdb import BatchIterationSuperMouse

class TestBatchIterationSuperMouse(unittest.TestCase):
    "Test the _batchiteration_supermouse module."

    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._bi = BatchIterationSuperMouse()

    def test_str(self):
        "Test BatchIteration __str__."
        self.assertEquals(self._bi.__str__(), _constants.BISM_STR)

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
        # mock service returns the xml, it gets parsed and compared to the dictionary in _constants
        self.assertEquals(self._bi.get_datarecord(1),
                          _constants.BI_DATARECORD)
        # set the iteration number to 2 to get NOSUCHRECORD xml output : <error>    </error>
        # which should throw an exception
        self.assertRaises(CdbPermanentError,self._bi.get_datarecord,2)

    def test_set_datacards(self):
        # if ok, the server would return a static XML message, the client strips it off the <ok> </ok> tags
        self._bi.set_url("ok")
        self.assertEquals(self._bi.set_datacards("a comment","reco-mock-data","mc-mock-data"), _constants.BISM_SET_DATACARDS_OK)
        # now try to mimic an exception
        self._bi.set_url("error")
        self.assertRaises(CdbPermanentError,self._bi.set_datacards,"comment", "reco", "mc")

