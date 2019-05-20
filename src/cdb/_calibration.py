"Calibration module."

from base64 import b64decode
from xml.sax import parseString
from xml.sax import SAXParseException
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError


__all__ = ["Calibration"]


class Calibration(_CdbBase):

    """
The Calibration class is used to retrieve calibration data.

For the tracker, data is described by its location with reference to to bank,
board and channel. For the detectors, calibration data is associated with a
detector and a calibration type. Old versions of the data are stored for
diagnostic purposes. Data can be retrieved for a given time using
get_calibration_for_date and for a given run using get_calibration_for_run.


    """

    def __init__(self, url="",
                 wsdl_dir="/cdb/calibration?wsdl"):
        """
Construct a Calibration.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(Calibration, self).__init__(url, wsdl_dir)
        self._calibration_handler = _CalibrationHandler()
        # add Trackers (issue #1667)
        self._detectors = ["Ckov A", "Ckov B", "EMR", "KL", "Scalers", "TOF0",
        "TOF1", "TOF2", "Trigger", "Trigger request","Trackers"]
        self._help = (self._base_help + 
        "\n\tget_calibration_for_date(string device, datetime timestamp, \
        \n\t\tstring calibration_type) \
        \n\tget_calibration_for_id(int id) \
        \n\tget_calibration_for_run(string device, int run_number, \
        \n\t\tstring calibration_type) \
        \n\tget_current_calibration(string device, string calibration_type) \
        \n\tget_ids(datetime start_time, datetime stop_time) \
        \n\tlist_devices()")

    def __str__(self):
        return "Calibration" + self._help

    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl

@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(Calibration, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(Calibration, self).get_status()

    def get_calibration_for_date(self, device, timestamp,
                                 calibration_type=None):
        """
Get the calibration data of the given device, where the name of the device may be
that of a detector or tracker, that was valid at the given timestamp.

@param device: a string containing the name of the detector or tracker 
@param timestamp: a datetime in UTC 
@param calibration_type: a string containing the type of the calibration. Only
used for detectors. May be None.

@return for the trackers: a list of dictionaries. For the detectors: a string
containing a calibration data set.
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        timestamp = _get_string_from_date(timestamp)
        if self._detectors.__contains__(device):
            _data = b64decode(self._server.getDetectorCalibrationForDate(device,
                        calibration_type, timestamp))
            try:
                # check for error or warning tag
                parseString(_data, self._status_handler)
            except SAXParseException:
                pass # no tag found so as expected could not parse data
            return _data
        else:
            xml = str(self._server.getCalibrationForDate(str(device),
                                                         timestamp))
            return self._parse_calibration_xml(xml)

    def get_calibration_for_run(self, device, run_number,
                                calibration_type=None):
        """
Get the calibration data of the given device, where the name of the device may be
that of a detector or tracker, that was valid for the given run number.

@param device: a string containing the name of the detector or tracker
@param run_number:  a long containing the number of a run
@param calibration_type: a string containing the type of the calibration. Only
used for detectors. May be None.

@return for the trackers: a list of dictionaries. For the detectors: a string
containing a calibration data set.

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        if self._detectors.__contains__(device):
            _data = b64decode(self._server.getDetectorCalibrationForRun(device,
                        calibration_type, run_number))
            try:
                # check for error or warning tag
                parseString(_data, self._status_handler)
            except SAXParseException:
                pass # no tag found so as expected could not parse data
            return _data
        else:
            xml = str(self._server.getCalibrationForRun(device, run_number))
            return self._parse_calibration_xml(xml)
    
    def get_current_calibration(self, device, calibration_type=None):
        """
Get the calibration data of the given device, where the name of the device may be
that of a detector or tracker.

@param device: a string containing the name of the tracker
@param calibration_type: a string containing the type of the calibration. Only
used for detectors. May be None.

@return for the trackers: a list of dictionaries. For the detectors: a string
containing a calibration data set.
    
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        if self._detectors.__contains__(device):
            _data = b64decode(self._server.getCurrentDetectorCalibration(device,
                        calibration_type))
            try:
                # check for error or warning tag
                parseString(_data, self._status_handler)
            except SAXParseException:
                pass # no tag found so as expected could not parse data
            return _data
        else:
            xml = str(self._server.getCurrentCalibration(device))
            return self._parse_calibration_xml(xml)
        
    def get_calibration_for_id(self, id_):
        """
Get the calibration data for a detector for the given id.

@param id_:  an int containing the id

@return a string containing a calibration data set

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        _data = b64decode(self._server.getDetectorCalibrationForId(id_))
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
        return self._parse_calibration_xml(xml)
        
    def get_ids(self, start_time, stop_time=None):
        """
Return a list of ids of the detector calibration data sets that were valid during the given time
period.

N.B. if the stop_time is None then only the ids that were valid at the
start_time will be returned.

@param start_time: a datetime in UTC
@param stop_time: a datetime in UTC. May be None. 

@return a dictionary containing the calibration ids data set:<pre>
    key - id
    value - dictionary with id specific data\n
    id specific data dictionary:
        key - valid_from
            a datetime from when the data id was valid
        key - created
            a datetime of when the data id was created
        key - device
            a string containing the name of the detector
        key - calibration_type
            a string containing the type of the calibration</pre>
               
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
        xml = str(self._server.getCalibrationIds(start_time, stop_time))
        parseString(xml, self._calibration_handler)
        return self._calibration_handler.get_ids()

    def _parse_calibration_xml(self, xml):
        """ Parser for calibration data. """
        parseString(xml, self._calibration_handler)
        return self._calibration_handler.get_data()


class _CalibrationHandler(ContentHandler):
    " ContentHandler for calibration data. "

    def __init__ (self):
        ContentHandler.__init__(self)
        self._device_type = ""
        self._board = ""
        self._bank = ""
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
    
    def startElement(self, name, attrs): #pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            self._message = ""
        elif name == 'warning':
            self._message = ""
        elif name == 'calibration':
            self._reset()
            self._device_type = str(attrs.get('type', ""))
        elif name == 'device':
            self._data.append(str(attrs.get('name', "")))
        elif name == 'board':
            self._board = int(attrs.get('number', ""))
        elif name == 'bank':
            self._bank = int(attrs.get('number', ""))
        elif name == 'channel':
            if self._device_type == "TRACKER":
                self._add_tracker(attrs)
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

    def _add_tracker(self, attrs):
        """ Populate a dictionary with data from the xml. """
        _cable_data = {}
        _cable_data["bank"] = self._board
        _cable_data["board"] = self._bank
        _cable_data["channel"] = int(attrs.get('number', ""))
        _cable_data["adc_pedestal"] = float(attrs.get('adcPedestal', ""))
        _cable_data["adc_gain"] = float(attrs.get('adcGain', ""))
        _cable_data["tdc_pedestal"] = float(attrs.get('tdcPedestal', ""))
        _cable_data["tdc_slope"] = float(attrs.get('tdcSlope', ""))
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
        _id['calibration_type'] = str(attrs.get('type', ''))
        self._ids[str(attrs.get('name', ''))] = _id    

    def _reset(self):
        """ Reset self values. """
        self._device_type = ""
        self._board = ""
        self._bank = ""
        self._data = []
        self._ids = {}
        self._message = ""


