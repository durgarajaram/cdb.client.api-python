"CalibrationSuperMouse module."

from base64 import b64encode
from xml.sax import parseString

from cdb._base import _get_string_from_date
from cdb._calibration import Calibration
from cdb._exceptions import CdbPermanentError

__all__ = ["CalibrationSuperMouse"]

class CalibrationSuperMouse(Calibration):
    
    """
The CalibrationSuperMouse class is used to set and retrieve calibration data.

For the control system a channel is described by its location with reference to
a crate and module. For the trackers a channel is described by its location with
reference to board, bank and channel. Each channel has data associated with it.
For detectors calibration data is associated with a detector and a calibration
type. Old versions of the data are stored for diagnostic purposes. Data can be
retrieved for a given time using get_calibration_for_date and for a given run
using get_calibration_for_run.

    """
    
    def __init__(self, url=""):
        """
Construct a CalibrationSuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(CalibrationSuperMouse, self).__init__(url,
            "/cdb/calibrationSuperMouse?wsdl")
       
    def __str__(self):
        _help_super = (
        "\n\tset_tracker(string device, dict data) \
        \n\tset_detector(string device, string calibration_type, \
        \n\t\tdatetime valid_from_time, string data)")
        return "CalibrationSuperMouse" + self._help + _help_super

    def set_tracker(self, device, data):
        """
Update the calibration data for a Tracker. A timestamp is associated with the data.
@param device: a string containing the name of the tracker
@param data: a list of dictionaries containing the calibration data set with the following keys/values:<pre>
    key - board, value - an int representing the board
    key - bank, value - an int the bank
    key - channel, value - an int representing the channel
    key - adc_pedestal, value - a float representing the adc pedestal
    key - adc_gain, value - a float representing the adc gain
    key - tdc_pedestal, value - a float representing the tdc pedestal
    key - tdc_slope, value - a float representing the tdc slope
</pre>

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = "<calibrations>"        
        try:
            if data != None:
                for calibration in data:
                    xml = (xml + "<tracker board='" + str(calibration['board'])
                           + "' bank='" + str(calibration['bank'])
                           + "' channel='" + str(calibration['channel'])
                           + "' adcPedestal='" 
                           + str(calibration['adc_pedestal'])
                           + "' adcGain='" + str(calibration['adc_gain'])
                           + "' tdcPedestal='" 
                           + str(calibration['tdc_pedestal'])
                           + "' tdcSlope='" + str(calibration['tdc_slope'])
                           + "'/>")
            xml = xml + "</calibrations>"
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        return_xml = str(self._server.setTracker(str(device), str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

    def set_detector(self, device, calibration_type, valid_from_time, data):
        """
Set the calibration data set.

The data is converted to a byte array thus enabling the user to pass in the
data in a zipped format if so required.

@param device: a string containing the name of the detector
@param calibration_type: a string containing the type of the calibration
@param valid_from_time: a datetime that should represent the time from which
this data set is considered to be valid
@param data: a string containing a calibration data set

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

     """
        valid_from_time = _get_string_from_date(valid_from_time)
        xml = str(self._server.setDetector(device, calibration_type,
                                           valid_from_time, b64encode(data)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()
 
