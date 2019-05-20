"CablingSuperMouse module."

from base64 import b64encode
from xml.sax import parseString

from cdb._base import _get_string_from_date
from cdb._cabling import Cabling
from cdb._exceptions import CdbPermanentError

__all__ = ["CablingSuperMouse"]

class CablingSuperMouse(Cabling):
    
    """
The CablingSuperMouse class is used to set and retrieve cabling data.

For the control system a channel is described by its location with reference to
a crate and module. For the trackers a channel is described by its location with
reference to computer id and geo number. Each channel has data associated with
it. For the detectors, cabling data is associated with a detector. Old versions
of the data are stored for diagnostic purposes. Data can be retrieved for a
given time using get_cabling_for_date and for a given run using
get_cabling_for_run.

    """
    
    def __init__(self, url=""):
        """
Construct a CablingSuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(CablingSuperMouse, self).__init__(url,
                                                "/cdb/cablingSuperMouse?wsdl")
       
    def __str__(self):
        _help_super = (
        "\n\tadd_control(int crate, int module, int channel, string name) \
        \n\tupdate_control(int crate, int module, int channel, string name) \
        \n\tset_tracker(string device, dict data) \
        \n\tset_detector(string device, datetime valid_from_time, string data)")
        return "CablingSuperMouse" + self._help + _help_super

    def add_control(self, crate, module, channel, name):
        """
Add the cabling data. A timestamp is associated with the data. N.B. There must
NOT already be an entry for the crate, module, channel otherwise an error will
be reported.
    
@param crate: the number of the crate
@param module: the number of the module
@param channel: the number of the channel
@param name: a string containing the name of the device that is connected to the channel

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = str(self._server.addControl(crate, module, channel, name))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()
            
    def update_control(self, crate, module, channel, name):
        """
Update the cabling data. A timestamp is associated with the data. N.B. There
must already be an entry for the crate, module, channel otherwise an error will
be reported.
    
@param crate: the number of the crate
@param module: the number of the module
@param channel: the number of the channel
@param name: a string containing the name of the device that is connected to the channel

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = str(self._server.updateControl(crate, module, channel, name))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_tracker(self, device, data):
        """
Update the cabling data for a Tracker. A timestamp is associated with the data.
@param device: the name of the tracker
@param data: a dictionary containing the cabling data set with the following keys/values:<pre>
    key - vlsb_computer_id, value - an int representing the vlsb computer id
    key - vlsb_geo_number, value - an int representing the vlsb geo number
    key - vlsb_channel, value - an int the vlsb_channel
    key - tracker_no, value - an int representing the tracker no
    key - station, value - an int representing the station
    key - plane, value - an int representing the plane
    key - channel, value - an int representing the channel
</pre>

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = "<cabling>"        
        try:
            if data != None:
                for cabling in data:
                    xml = (xml + "<tracker vlsbComputerId='" 
                           + str(cabling['vlsb_computer_id'])
                           + "' vlsbGeoNumber='" 
                           + str(cabling['vlsb_geo_number'])
                           + "' vlsbChannel='" 
                           + str(cabling['vlsb_channel'])
                           + "' trackerNumber='" 
                           + str(cabling['tracker_no'])
                           + "' station='" + str(cabling['station'])
                           + "' plane='" + str(cabling['plane'])
                           + "' channel='" + str(cabling['channel'])
                           + "'/>")
            xml = xml + "</cabling>"
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        return_xml = str(self._server.setTracker(str(device), str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

    def set_detector(self, device, valid_from_time, data):
        """
Set the cabling data set.

The data is converted to a byte array thus enabling the user to pass in the
data in a zipped format if so required.

@param device: a string containing the name of the detector
@param valid_from_time: a datetime that should represent the time from which
this data set is considered to be valid
@param data: a string containing a cabling data set

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

     """
        valid_from_time = _get_string_from_date(valid_from_time)
        xml = str(self._server.setDetector(device, valid_from_time,
                                           b64encode(data)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()
