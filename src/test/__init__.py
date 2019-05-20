"cdb test module."

import sys
import unittest

# Allow MAUS to run the tests from the mice.cdb.client.api-python directory
if sys.path[0] != "src/test":
    sys.path.insert(0, "src/test")

from test import unittest__init__
from test import unittest_alarmhandler
from test import unittest_alarmhandler_supermouse
from test import unittest_base
from test import unittest_beamline
from test import unittest_beamline_supermouse
from test import unittest_cabling
from test import unittest_cabling_supermouse
from test import unittest_calibration
from test import unittest_calibration_supermouse
from test import unittest_coolingchannel
from test import unittest_coolingchannel_supermouse
from test import unittest_pid_ctrl
from test import unittest_pid_ctrl_supermouse
from test import unittest_exception
from test import unittest_geometry
from test import unittest_geometry_supermouse
from test import unittest_statemachine
from test import unittest_statemachine_supermouse
from test import unittest_target
from test import unittest_target_supermouse
from test import unittest_dataquality
from test import unittest_dataquality_supermouse

from test import _constants
from . import suds

if __name__ == '__main__':
    SUITE1 = unittest__init__.suite()
    SUITE2 = unittest_base.suite()
    SUITE3 = unittest_alarmhandler.suite()
    SUITE4 = unittest_beamline.suite()
    SUITE5 = unittest_cabling.suite()
    SUITE6 = unittest_calibration.suite()
    SUITE7 = unittest_pid_ctrl.suite()
    SUITE8 = unittest_geometry.suite()
    SUITE9 = unittest_statemachine.suite()
    SUITE10 = unittest_target.suite()
    SUITE11 = unittest_exception.suite()
    SUITE12 = unittest_alarmhandler_supermouse.suite()
    SUITE13 = unittest_beamline_supermouse.suite()
    SUITE14 = unittest_cabling_supermouse.suite()
    SUITE15 = unittest_calibration_supermouse.suite()
    SUITE16 = unittest_pid_ctrl.suite()
    SUITE17 = unittest_geometry_supermouse.suite()
    SUITE18 = unittest_statemachine_supermouse.suite()
    SUITE19 = unittest_target_supermouse.suite()
    SUITE20 = unittest_coolingchannel.suite()
    SUITE21 = unittest_coolingchannel_supermouse.suite()
    SUITE22 = unittest_dataquality.suite()
    SUITE23 = unittest_dataquality_supermouse.suite()
    SUITE24 = unittest_mcserialnumber.suite()
    SUITE25 = unittest_mcserialnumber_supermouse.suite()

    SUITE = unittest.TestSuite()
    SUITE.addTest(SUITE1)
    SUITE.addTest(SUITE2)
    SUITE.addTest(SUITE3)
    SUITE.addTest(SUITE4)
    SUITE.addTest(SUITE5)
    SUITE.addTest(SUITE6)
    SUITE.addTest(SUITE7)
    SUITE.addTest(SUITE8)
    SUITE.addTest(SUITE9)
    SUITE.addTest(SUITE10)
    SUITE.addTest(SUITE11)
    SUITE.addTest(SUITE12)
    SUITE.addTest(SUITE13)
    SUITE.addTest(SUITE14)
    SUITE.addTest(SUITE15)
    SUITE.addTest(SUITE16)
    SUITE.addTest(SUITE17)
    SUITE.addTest(SUITE18)
    SUITE.addTest(SUITE19)
    SUITE.addTest(SUITE20)
    SUITE.addTest(SUITE21)
    SUITE.addTest(SUITE22)
    SUITE.addTest(SUITE23)
    SUITE.addTest(SUITE24)
    SUITE.addTest(SUITE25)
    unittest.TextTestRunner(verbosity=2).run(SUITE)

