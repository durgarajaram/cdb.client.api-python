"MCSerialNumber module."

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError

__all__ = ["MCSerialNumber"]


class MCSerialNumber(_CdbBase):

    """
The SerialNumber class is used to retrieve MAUS data cards indexec by batch iteration number.

A couple of methods are provided for diagnostics. It is possible to retrieve a
list of ...


        """

    def __init__(self, url="",
                 wsdl_dir="/cdb/mcSerialNumber?wsdl"):
        """
Construct an SerialNumber object.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(MCSerialNumber, self).__init__(url, wsdl_dir)
        #self._bitn_handler = _SerialNumberHandler()
        self._help = self._base_help + \
"\n\tget_datacards(int serial_number)\
\n\tget_comment(int serial_number)\
\n\tget_sw_version(int serial_number)"
    def __str__(self):
        return "MCSerialNumber" + self._help
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl
xception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(MCSerialNumber, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(MCSerialNumber, self).get_status()

    def get_datacards(self, serial):
        xml = self._server.getDataCards(serial)
        return self.get_parsed_data(xml)

    def get_comment(self, serial):
        comment = self._server.getComment(serial)
        return self.get_parsed_data(comment)

    def get_sw_version(self, serial):
        ver = self._server.getSWVersion(serial)
        return self.get_parsed_data(ver)

    def get_parsed_data(self, xml):
        bitn_handler = _SerialNumberHandler()
        parseString(xml, bitn_handler)
        return bitn_handler.getData()

class _SerialNumberHandler(ContentHandler):

    " ContentHandler for MC serial number data. "

    def __init__ (self):
        ContentHandler.__init__(self)
        self._data = {}
        self._message = ""

    def startElement(self, name, attrs): #pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            self._message = ""
        elif name == 'warning':
            self._message = ""
        elif name == 'mcserialnumber':
            self.data = {}
        elif name == 'sw_version':
            self._message = ""
        elif name == 'datacards':
            self._message = ""
        elif name == 'comment':
            self._message = ""

    def characters(self, message):
        """ Method required for ContentHandler. """
        self._message = self._message + message

    def endElement(self, name): #pylint: disable-msg=C0103
        """ Method required for ContentHandler.
        """
        if name == 'error':
            raise CdbPermanentError(self._message)
        elif name == 'warning':
            raise CdbTemporaryError(self._message)
        elif name == 'mcserialnumber':
            pass
        elif name == 'datacards':
            self._data['data'] = self._message
        elif name == 'sw_version':
            self._data['softw'] = self._message
        elif name == 'comment':
            self._data['comment'] =  self._message

    def getData(self):
        return self._data
