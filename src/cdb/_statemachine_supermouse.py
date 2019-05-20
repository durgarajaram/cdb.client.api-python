"StateMachineSuperMouse module."

from xml.sax import parseString

from cdb._statemachine import StateMachine
from cdb._exceptions import CdbPermanentError

__all__ = ["StateMachineSuperMouse"]

class StateMachineSuperMouse(StateMachine):
    
    """
The StateMachineSuperMouse class is used to set and retrieve state machine settings.

The state of an individual system can be retrieved using get_current_state and
the state of the entire system can be retrieved with get_current_state_machine.
Old versions of the data are stored for diagnostic purposes. Data can be
retrieved for a given time using get_state_machine_for_date and for a given run
using get_state_machine_for_run.

    """
    
    def __init__(self, url=""):
        """
Construct a StateMachineSuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """

        super(StateMachineSuperMouse,
              self).__init__(url, "/cdb/stateMachineSuperMouse?wsdl")

    def __str__(self):
        _help_super = "\n\tset_state(string system, string state) \
        \n\tset_pv_data(string system, string state, list pv_data)" 
        return "StateMachineSuperMouse" + self._help + _help_super

    def set_state(self, system, state):
        """
Set the state of the given system to the given state.

@param system: a string containing the system name
@param state: a string containing the state to set

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = str(self._server.setState(str(system), str(state)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_pv_data(self, system, state, pv_data):
        """
Set the pv data of the given system and state.

@param system: a string containing the system name
@param state: a string containing the state to set
@param pv_data: a list of dictionaries containing the pv data:<pre>
    key - 'name'
    value - a string containing the name of the PV
    key - 'hihi'
    value - a float containing the hihi value of the alarm
    key - 'hi'
    value - a float containing the hi value of the alarm
    key - 'lo'
    value - a float containing the lolo value of the alarm    
    key - 'lolo'
    value - a float containing the lo value of the alarm   
    key - 'units'
    value - a string containing the alarm units
    key - 'auto_sms'
    value - a boolean flag 
    key - 'mode'
    value - a string containing the archiver mode
    key - 'frequency'
    value - a float containing the archiver frequency
    key - 'deadband'
    value - a float containing the archiver deadband
    key - 'transition'
    value - a float containing the archiver transition</pre>
    
@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        _pv_xml = "<pvdata>"
        for _pv in pv_data:
            try:
                _pv_xml = (_pv_xml + "<pv" 
                          + " name='" + str(_pv["name"]) + "'"
                          + " hihi='" + str(_pv["hihi"]) + "'"
                          + " hi='" + str(_pv["hi"]) + "'"
                          + " lo='" + str(_pv["lo"]) + "'"
                          + " lolo='" + str(_pv["lolo"]) + "'"
                          + " units='" + str(_pv["units"]) + "'"
                          + " autosms='" + str(_pv["auto_sms"]) + "'"
                          + " mode='" + str(_pv["mode"]) + "'"
                          + " transition='" + str(_pv["transition"]) + "'")
                
            except KeyError, exception:
                raise CdbPermanentError("Missing value for " + str(exception))
            # only one of frequency or deadband need to be set
            try:
                _pv_xml = (_pv_xml + " frequency='" + str(_pv["frequency"])
                           + "'")
            except KeyError, exception:
                try:
                    _pv["deadband"]
                except KeyError, exception:
                    raise CdbPermanentError(
                        "One of 'frequency' or 'deadband' must be set")
            try:
                _pv_xml = (_pv_xml + " deadband='" + str(_pv["deadband"]) + "'")
            except KeyError, exception:
                pass
            _pv_xml = _pv_xml + "/>"  
 
        _pv_xml = _pv_xml + "</pvdata>"
        xml = str(self._server.setPVData(str(system), str(state), _pv_xml))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()
    
