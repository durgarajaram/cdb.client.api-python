"__init__ test module"
#pylint: disable-msg=R0904

import unittest

from test import _constants


class TestInit(unittest.TestCase):
    "Test the __init__ module."

    def test_imports(self):
        "Test __init__ imports."
        from cdb import CdbError #pylint: disable-msg=W0612
        from cdb import CdbPermanentError #pylint: disable-msg=W0612
        from cdb import CdbTemporaryError #pylint: disable-msg=W0612
        from cdb import AlarmHandler #pylint: disable-msg=W0612
        from cdb import Beamline #pylint: disable-msg=W0612
        from cdb import Cabling #pylint: disable-msg=W0612
        from cdb import Calibration #pylint: disable-msg=W0612
        from cdb import PIDCtrl #pylint: disable-msg=W0612
        from cdb import Geometry #pylint: disable-msg=W0612
        from cdb import Target #pylint: disable-msg=W0612
        from cdb import StateMachine #pylint: disable-msg=W0612
        from cdb import DataQuality #pylint: disable-msg=W0612
        from cdb import MCSerialNumber #pylint: disable-msg=W0612
        self.assertEqual(dir(), _constants.CLASS_LIST)

def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestInit))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

