"Cabling module."

from base64 import b64decode
from xml.sax import parseString
from xml.sax import SAXParseException
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError


__all__ = ["Cabling"]


class Cabling(_CdbBase):

    """
The Cabling class is used to retrieve cabling data.

For the control system a channel is described by its location with reference to
a crate and module. For the trackers a channel is described by its location with
reference to computer id and geo number. Each channel has data associated with
it. For the detectors, cabling data is associated with a detector. Old versions
of the data are stored for diagnostic purposes. Data can be retrieved for a
given time using get_cabling_for_date and for a given run using
get_cabling_for_run.


    """

    def __init__(self, url="",
                 wsdl_dir="/cdb/cabling?wsdl"):
        """
Construct a Cabling.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(Cabling, self).__init__(url, wsdl_dir)
        self._cabling_handler = _CablingHandler()
        self._detectors = ["Ckov A", "Ckov B", "EMR", "KL", "Scalers", "TOF0",
        "TOF1", "TOF2", "Trigger", "Trigger request", "DAQ","Trackers"]
        self._help = (self._base_help + 
        "\n\tget_cabling_for_date(string device, datetime timestamp) \
        \n\tget_cabling_for_id(int id) \
        \n\tget_cabling_for_run(string device, int run_number) \
        \n\tget_current_cabling(string device) \
        \n\tget_ids(datetime start_time, datetime stop_time) \
        \n\tlist_devices()")

    def __str__(self):
        return "Cabling" + self._help

    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl

@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(Cabling, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(Cabling, self).get_status()

    def get_cabling_for_date(self, device, timestamp):
        """
Get the cabling data of the given device, where the name of the device may be
that of a detector, tracker or control, that was valid at the given timestamp.

@param device: a string containing the name of the detector, tracker or control
@param timestamp: a datetime in UTC

@return for the controls and trackers: a list of dictionaries. For the detectors: a string
containing a calibration data set.
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        if self._detectors.__contains__(device):
            _data = b64decode(self._server.getDetectorCablingForDate(device,
                        timestamp))
            try:
                # check for error or warning tag
                parseString(_data, self._status_handler)
            except SAXParseException:
                pass # no tag found so as expected could not parse data
            return _data
        else:
            timestamp = _get_string_from_date(timestamp)
            xml = str(self._server.getCablingForDate(str(device), timestamp))
        return self._parse_cabling_xml(xml)

    def get_cabling_for_run(self, device, run_number):
        """
Get the cabling data of the given device, where the name of the device may be
that of a detector, tracker or control, that was valid for the given run number.

@param device: a string containing the name of the detector, tracker or control
@param run_number:  a long containing the number of a run

@return for the controls and trackers: a list of dictionaries. For the detectors: a string
containing a calibration data set.

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        if self._detectors.__contains__(device):
            _data = b64decode(self._server.getDetectorCablingForRun(device,
                        run_number))
            try:
                # check for error or warning tag
                parseString(_data, self._status_handler)
            except SAXParseException:
                pass # no tag found so as expected could not parse data
            return _data
        else:
            xml = str(self._server.getCablingForRun(device, run_number))
            return self._parse_cabling_xml(xml)

    def get_current_cabling(self, device):
        """
Get the cabling data of the given device, where the name of the device may be
that of a detector, tracker or control.

@param device: a string containing the name of the detector, tracker or control

@return for the controls and trackers: a list of dictionaries. For the detectors: a string
containing a calibration data set.
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        if self._detectors.__contains__(device):
            _data = b64decode(self._server.getCurrentDetectorCabling(device))
            try:
                # check for error or warning tag
                parseString(_data, self._status_handler)
            except SAXParseException:
                pass # no tag found so as expected could not parse data
            return _data
        else:
            xml = str(self._server.getCurrentCabling(device))
            return self._parse_cabling_xml(xml)
    
    def get_cabling_for_id(self, id_):
        """
Get the cabling data for a detector for the given id.

@param id_:  an int containing the id

@return a string containing a calibration data set

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        _data = b64decode(self._server.getDetectorCablingForId(id_))
        try:
            # check for error or warning tag
            parseString(_data, self._status_handler)
        except SAXParseException:
            pass # no tag found so as expected could not parse data
        return _data    

    def list_devices(self):
        """
Get a list of known devices. These are the device names that are recognised by this API.

@return a list of device names
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = str(self._server.listDevices())
        return self._parse_cabling_xml(xml)

    def get_ids(self, start_time, stop_time=None):
        """
Return a list of ids of the detector cabling data sets that were valid during the given time
period.

N.B. if the stop_time is None then only the ids that were valid at the
start_time will be returned.

@param start_time: a datetime in UTC
@param stop_time: a datetime in UTC. May be None. 

@return a dictionary containing the cabling ids data set:<pre>
    key - id
    value - dictionary with id specific data\n
    id specific data dictionary:
        key - valid_from
            a datetime from when the data id was valid
        key - created
            a datetime of when the data id was created
        key - device
            a string containing the name of the detector</pre>
               
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        start_time = _get_string_from_date(start_time)
        if stop_time == None:
            stop_time = start_time
        else:
            stop_time = _get_string_from_date(stop_time)
        xml = str(self._server.getCablingIds(start_time, stop_time))
        parseString(xml, self._cabling_handler)
        return self._cabling_handler.get_ids()    

    def _parse_cabling_xml(self, xml):
        """ Parser for cabling data. """
        parseString(xml, self._cabling_handler)
        return self._cabling_handler.get_data()


class _CablingHandler(ContentHandler): #pylint: disable-msg=R0902
    " ContentHandler for cabling data. "

    def __init__ (self):
        ContentHandler.__init__(self)
        self._device_type = ""
        self._vlsb_computer_id = ""
        self._vlsb_geo_number = ""
        self._crate = ""
        self._module = ""
        self._data = []
        self._ids = {}
        self._message = ""

    def get_data(self):
        """
        Get a list containing the parsed xml.

        @return the list containing the parsed xml

        """
        return self._data

    def get_ids(self):
        """
        Get a dictionary containing the parsed xml.

        @return the dictionary containing the parsed xml

        """
        return self._ids
   
    def startElement(self, name, attrs):
        #pylint: disable-msg=R0912
        #pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            self._message = ""
        elif name == 'warning':
            self._message = ""
        elif name == 'cabling':
            self._reset()
            self._device_type = str(attrs.get('type', ""))
        elif name == 'vlsbComputerId':
            self._vlsb_computer_id = int(attrs.get('number', ""))
        elif name == 'vlsbGeoNumber':
            self._vlsb_geo_number = int(attrs.get('number', ""))
        elif name == 'vlsbChannel':
            if self._device_type == "TRACKER":
                self._add_vlsb_channel(attrs)
        elif name == 'crate':
            self._crate = int(attrs.get('number', ""))
        elif name == 'module':
            self._module = int(attrs.get('number', ""))            
        elif name == 'channel':
            if self._device_type == "CONTROL":
                self._add_control_channel(attrs)
        elif name == 'device':
            self._data.append(str(attrs.get('name', "")))
        elif name == 'ids':
            self._reset()
        elif name == 'id':
            self._add_id(attrs)
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

    def _add_vlsb_channel(self, attrs):
        """ Populate a dictionary with data from the xml. """
        _cable_data = {}
        _cable_data["vlsb_computer_id"] = self._vlsb_computer_id
        _cable_data["vlsb_geo_number"] = self._vlsb_geo_number
        _cable_data["vlsb_channel"] = int(attrs.get('number', ""))
        _cable_data["tracker_no"] = int(attrs.get('trackerNumber', ""))
        _cable_data["station"] = int(attrs.get('station', ""))
        _cable_data["plane"] = int(attrs.get('plane', ""))
        _cable_data["channel"] = int(attrs.get('channel', ""))
        self._data.append(_cable_data)

    def _add_control_channel(self, attrs):
        """ Populate a dictionary with data from the xml. """
        _cable_data = {}
        _cable_data["crate"] = self._crate
        _cable_data["module"] = self._module
        _cable_data["channel"] = int(attrs.get('number', ""))
        _cable_data["name"] = str(attrs.get('name', ""))
        self._data.append(_cable_data)

    def _add_id(self, attrs):
        """ Populate a dictionary with data from the xml. """
        _id = {}
        _id['id'] = str(attrs.get('name', ''))
        _id['valid_from'] = (
            _get_date_from_string(attrs.get('validFrom', '')))
        _id['created'] = (
            _get_date_from_string(attrs.get('created', '')))
        _id['device'] = str(attrs.get('device', ''))
        self._ids[str(attrs.get('name', ''))] = _id    

    def _reset(self):
        """ Reset self values. """
        self._device_type = ""
        self._vlsb_computer_id = ""
        self._vlsb_geo_number = ""
        self._crate = ""
        self._module = ""
        self._data = []
        self._ids = {}
        self._message = ""

