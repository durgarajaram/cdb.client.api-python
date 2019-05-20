"MCSerialNumber module."

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._mcserialnumber import MCSerialNumber
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError

__all__ = ["MCSerialNumberSuperMouse"]


class MCSerialNumberSuperMouse(MCSerialNumber):

    """
The MCSerialNumber class is used to retrieve MAUS data cards indexed by batch iteration number.

A couple of methods are provided for diagnostics. It is possible to retrieve a
list of ...
TODO set methods

        """

    def __init__(self, url="",
                 wsdl_dir="/cdb/mcSerialNumberSuperMouse?wsdl"):
        """
Construct an MCSerialNumber object.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(MCSerialNumberSuperMouse, self).__init__(url, wsdl_dir)
        self._help = self._base_help + "\n\tget_datacards(int serial_number) \
        \n\tget_comment(int serial_number) \
        \n\tset_datacards(int serial_number, string datacards, string software_version, string comment)"

    def __str__(self):
        return "MCSerialNumberSuperMouse" + self._help
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl
@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(MCSerialNumberSuperMouse, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(MCSerialNumberSuperMouse, self).get_status()

    def set_datacards(self, datacards, sw_version, comment):
        """
        :param serialNumber:
        :param comment:
        :param datacards:
        :param sw_version:
        """
        xml = str(self._server.setDataCards(datacards, sw_version, comment))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_comment(self, serialNumber, comment):
        xml = str(self._server.setComment(serialNumber, comment))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()