"_statemachine_supermouse test module"
#pylint: disable-msg=R0904

import unittest
from datetime import datetime

from test import _constants
from cdb import StateMachineSuperMouse
from cdb import CdbPermanentError
from cdb import CdbTemporaryError

class TestStateMachineSuperMouse(unittest.TestCase):
    "Test the _statemachine_supermouse module."
    
    def setUp(self): #pylint: disable-msg=C0103
        "Set up data for use in tests."
        self._statemachine = StateMachineSuperMouse()

    def test_str(self):
        "Test StateMachineSuperMouse __str__."
        self.assertEquals(self._statemachine.__str__(), _constants.SM_SM_STR)
        
    def test_get_status(self):
        "Test StateMachineSuperMouse get_status"
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_status)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_status)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_status(),
                          _constants.STATUS_OK)

    def test_get_allowed_transitions(self):
        "Test StateMachineSuperMouse get_allowed_transitions."
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_allowed_transitions)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_allowed_transitions)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_allowed_transitions(),
                          _constants.SM_ALLOWED_TRANS)
        self.assertEquals(self._statemachine.get_allowed_transitions(),
                          _constants.SM_ALLOWED_TRANS)

    def test_get_current_state(self):
        "Test StateMachineSuperMouse get_current_state."
        _system = "MICE"
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_current_state, _system)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_current_state, _system)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_current_state(_system),
                          _constants.SM_CURRENT)
        self.assertEquals(self._statemachine.get_current_state(_system),
                          _constants.SM_CURRENT)
        
    def test_get_current_state_machine(self):
        "Test StateMachineSuperMouse get_current_state_machine."
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_current_state_machine)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_current_state_machine)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_current_state_machine(),
                          _constants.SM_CURRENT_SM)
        self.assertEquals(self._statemachine.get_current_state_machine(),
                          _constants.SM_CURRENT_SM)

    def test_get_state_machine_for_date(self):
        "Test StateMachineSuperMouse get_state_machine_for_date."
        _timestamp = datetime.strptime("1999-12-31 23:59:59.999999",
                                "%Y-%m-%d %H:%M:%S.%f")
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_state_machine_for_date,
                          _timestamp)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_state_machine_for_date,
                          _timestamp)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_state_machine_for_date
                          (_timestamp),
                          _constants.SM_FOR_DATE)

    def test_get_state_machine_for_run(self):
        "Test StateMachineSuperMouse get_state_machine_for_run."
        _run = 1
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_state_machine_for_run, _run)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_state_machine_for_run, _run)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_state_machine_for_run(_run),
                          _constants.SM_FOR_RUN)

    def test_get_pv_data(self):
        "Test StateMachine get_pv_datan."
        _system = "MICE"
        _state = "What a state!"
        self._statemachine.set_url("error")
        self.assertRaises(CdbPermanentError,
                          self._statemachine.get_pv_data, _system, _state)
        self._statemachine.set_url("warn")
        self.assertRaises(CdbTemporaryError,
                          self._statemachine.get_pv_data, _system, _state)
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.get_pv_data(_system, _state),
                          _constants.SM_PV_DATA)
                
    def test_set_state(self):
        "Test StateMachineSuperMouse set_state."
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.set_state('cooling', 'off'),
                          _constants.STATUS_OK)
        
    def test_set_pv_data(self):
        "Test StateMachineSuperMouse set_pv_data."
        self._statemachine.set_url("ok")
        self.assertEquals(self._statemachine.set_pv_data('a', 'b',
                          _constants.SM_PV_DATA), _constants.STATUS_OK)
        self._statemachine.set_url("ok")
        self.assertRaises(CdbPermanentError, self._statemachine.set_pv_data,
                          'a', 'b', _constants.SM_PV_DATA_ERROR_1)
        self.assertRaises(CdbPermanentError, self._statemachine.set_pv_data,
                          'a', 'b', _constants.SM_PV_DATA_ERROR_2)

def suite():
    "Add tests to the suite."
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(TestStateMachineSuperMouse))
    return _suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

