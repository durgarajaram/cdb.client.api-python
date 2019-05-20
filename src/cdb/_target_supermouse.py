"TargetSuperMouse module."

from base64 import b64encode
from xml.sax import parseString

from cdb._target import Target

__all__ = ["TargetSuperMouse"]


class TargetSuperMouse(Target):

    """
The TargetSuperMouse class is used to store and retrieve target data.

    """

    def __init__(self, url=""):
        """
Construct a TargetSuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(TargetSuperMouse, self).__init__(url,
                                                 "/cdb/targetSuperMouse?wsdl")
       
    def __str__(self):
        _help_super = (
        "\n\tadd_blob(string name, string data)")
        return "TargetSuperMouse" + self._help + _help_super
        
    def add_blob(self, name, data):
        """
Set the target data.

The data is converted to a byte array thus enabling the user to pass in the
data in a zipped format if so required.

@param name: a string containing the target name
@param data: a string containing a target data set

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

     """
        xml = str(self._server.addBlob(str(name), b64encode(data)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

