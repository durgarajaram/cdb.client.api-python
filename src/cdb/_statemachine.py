"StateMachine module."

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_string_from_date
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError

__all__ = ["StateMachine"]


class StateMachine(_CdbBase):
    
    """
The StateMachine class is used to retrieve state machine data.

The state of an individual system can be retrieved using get_current_state and
the state of the entire system can be retrieved with get_current_state_machine.
Old versions of the data are stored for diagnostic purposes. Data can be
retrieved for a given time using get_state_machine_for_date and for a given run
using get_state_machine_for_run.

    """

    def __init__(self, url="",
                 wsdl_dir="/cdb/stateMachine?wsdl"):
        """
Construct a StateMachine.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(StateMachine, self).__init__(url, wsdl_dir)
        self._state_machine_handler = _StateMachineHandler()
        self._help = self._base_help + "\n\tget_allowed_transitions() \
        \n\tget_current_state(string system) \
        \n\tget_current_state_machine() \
        \n\tget_state_machine_for_date(datetime timestamp) \
        \n\tget_state_machine_for_run(int run_number) \
        \n\tget_pv_data(string system, string state)"
        
    def __str__(self):
        return "StateMachine" + self._help
  
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl

@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(StateMachine, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(StateMachine, self).get_status()

    def get_allowed_transitions(self):
        """
Get a list of the allowed state transition relative to the current state of the state machine.

@return a dictionary containing the machine state data:<pre>
    key - a string containing the system name
    value - a string containing the state</pre>
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getAllowedTransitions()
        return self._parse_state_machine_xml(str(xml))

    def get_current_state(self, system):
        """
Get the current state of the given system.

@param system: a string containing the system name

@return a string containing the current state of the given system

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getCurrentState(system)
        return self._parse_state_machine_xml(str(xml))['state']

    def get_current_state_machine(self):
        """
Get the current state of the entire system.

@return a dictionary containing the machine state data:<pre>
    key - a string containing the system name
    value - a string containing the state</pre>
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getCurrentStateMachine()
        return self._parse_state_machine_xml(str(xml))

    def get_state_machine_for_date(self, timestamp):
        """
Get the state machine data that was valid at the given timestamp.

@param timestamp: a datetime in UTC

@return a dictionary containing the machine state data:<pre>
    key - a string containing the system name
    value - a string containing the state</pre>

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        timestamp = _get_string_from_date(timestamp)
        xml = self._server.getStateMachineForDate(timestamp)
        return self._parse_state_machine_xml(str(xml))
 
    def get_state_machine_for_run(self, run_number):
        """
Get the state machine data that was valid for the given run number.

@param run_number: an int representing the run number

@return a dictionary containing the machine state data:<pre>
    key - a string containing the system name
    value - a string containing the state</pre>

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getStateMachineForRun(str(run_number))
        return self._parse_state_machine_xml(str(xml))

    def get_pv_data(self, system, state):
        """
Get the pv data for the given system and state.

@param system: a string containing the system name
@param state: a string containing the state of the system

@return a list of dictionaries containing the pv data:<pre>
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

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getPVData(str(system), str(state))
        parseString(str(xml), self._state_machine_handler)
        return self._state_machine_handler.get_pv_data()

    def get_pv_data_xml(self, system, state):
        """
        :param system: a string containing the system name
        :param state: a string containing the state of the system
        :return: XML document
        """
        return self._server.getPVData(str(system), str(state))

    def _parse_state_machine_xml(self, xml):
        """ Parser for state_machine data. """
        parseString(xml, self._state_machine_handler)
        return self._state_machine_handler.get_data()


class _StateMachineHandler(ContentHandler):

    " ContentHandler for state_machine data. "

    def __init__ (self):
        ContentHandler.__init__(self)
        self._message = ""
        self._pv_data = []
        self._states = {}
        
    def get_data(self):
        """
        Get a dictionary containing the parsed XML.

        @return the dictionary containing the parsed XML

        """
        return self._states
    
    def get_pv_data(self):
        """
        Get a list containing the parsed XML.

        @return the list containing the parsed XML

        """
        return self._pv_data
       
    def startElement(self, name, attrs): #pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            self._message = ""
        elif name == 'warning':
            self._message = ""
        elif name == 'stateMachine':
            self._states = {}
        elif name == 'system':
            self._set_system(attrs)
        elif name == 'state':
            self._states = {}
            self._message = ""
        elif name == 'pvdata':
            self._pv_data = []
            self._message = ""
        elif name == 'pv':
            self._set_pv_data(attrs)
        return

    def characters(self, message):
        """ Method required for ContentHandler. """
        self._message = self._message + message

    def endElement(self, name): #pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            raise CdbPermanentError(self._message)
        elif name == 'warning':
            raise CdbTemporaryError(self._message)
        elif name == 'state':
            self._states['state'] = str(self._message)

    def _set_system(self, attrs):
        """ Populate a states dictionary with data from the XML. """
        self._states[str(attrs.get('name'))] = str(attrs.get('state'))
        
    def _set_pv_data(self, attrs):
        """ Populate an pv_data dictionary with data from the XML. """
        _pv = {}
        _pv['name'] = str(attrs.get('name'))
        _pv['hihi'] = float(attrs.get('hihi'))
        _pv['hi'] = float(attrs.get('hi'))
        _pv['lolo'] = float(attrs.get('lolo'))
        _pv['lo'] = float(attrs.get('lo'))
        _pv['units'] = str(attrs.get('units'))
        # Note: the server returns 'f' string as False (bug #1746)
        _pv['auto_sms'] = bool(attrs.get('autosms')!='f')
        _pv['mode'] = str(attrs.get('mode'))
        if attrs.get('frequency') != None:
            _pv['frequency'] = float(attrs.get('frequency'))
        if attrs.get('deadband') != None:
            _pv['deadband'] = float(attrs.get('deadband'))
        _pv['transition'] = float(attrs.get('transition'))
        self._pv_data.append(_pv)
      
