"BatchIteration module."

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError

__all__ = ["BatchIteration"]


class BatchIteration(_CdbBase):

    """
The BatchIteration class is used to retrieve MAUS data cards indexec by batch iteration number.

A couple of methods are provided for diagnostics. It is possible to retrieve a
list of ...


        """

    def __init__(self, url="",
                 wsdl_dir="/cdb/batchIteration?wsdl"):
        """
Construct an BatchIteration object.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(BatchIteration, self).__init__(url, wsdl_dir)
        #self._bitn_handler = _BatchIterationHandler()
        self._help = self._base_help + "\n\tget_datarecord(int iteration_number) \
        \n\tget_reco_datacards(int iteration_number)\
        \n\tget_mc_datacards(int iteration_number) \
        \n\tget_comment(int iteration_number)"

    def __str__(self):
        return "BatchIteration" + self._help
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl
xception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(BatchIteration, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(BatchIteration, self).get_status()

    def get_datarecord(self, iteration):
        #assert isinstance(iteration, object)
        xml = self._server.getDataRecord(iteration)
        return self._get_parsed_data(xml)

    def get_reco_datacards(self, iteration):
        xml = self._server.getRecoDataCards(iteration)
        #xml='<batchiteration><error>Problem issuing query SELECT recocards FROM batchiteration WHERE iteration=1;</error></batchiteration>'
        return self._get_parsed_data(xml)

    def get_mc_datacards(self, iteration):
        xml = self._server.getMCDataCards(iteration)
        return self._get_parsed_data(xml)

    def get_comment(self, iteration):
        xml = self._server.getComment(iteration)
        return self._get_parsed_data(xml)

    def _get_parsed_data(self, xml):
        bitn_handler = _BatchIterationHandler()
        parseString(xml, bitn_handler)
        return bitn_handler.getData()


class _BatchIterationHandler(ContentHandler):

    " ContentHandler for batch iteration number data. "

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
        elif name == 'batchiteration':
            self.data = {}
        elif name == 'recodatacards':
            self._message = ""
        elif name == 'mcdatacards':
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
        elif name == 'batchiteration':
            pass
        elif name == 'recodatacards':
            self._data['reco'] = self._message
        elif name == 'mcdatacards':
            self._data['mc'] = self._message
        elif name == 'comment':
            self._data['comment'] =  self._message

    def getData(self):
        return self._data
