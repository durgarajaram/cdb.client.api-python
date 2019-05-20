"DataQualitySuperMouse module."

from xml.sax import parseString

from cdb._dataquality import DataQuality
from cdb._exceptions import CdbPermanentError

__all__ = ["DataQualitySuperMouse"]

class DataQualitySuperMouse(DataQuality):
    
    """
The DataQualitySuperMouse class is used to set and retrieve data quality
data (flags).

    """
    
    def __init__(self, url=""):
        """
Construct a DataQualitySuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """

        super(DataQualitySuperMouse, self).__init__(url,
            "/cdb/dataQualitySuperMouse?wsdl")

    def __str__(self):
        _help_super = "\n\tset_reconstruction_flags(string flags)"
        return "DataQualitySuperMouse" + self._help + _help_super


    def set_reconstruction_flags(self, run_number, maus_version, batch_iteration_number, flags):
        """
Store the flags keyed by run number, b.i.n and MAUS version.

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        return_xml = str(self._server.setReconstructionFlags(run_number, maus_version, batch_iteration_number, flags))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()
