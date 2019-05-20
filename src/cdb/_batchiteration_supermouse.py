"BatchIteration module."

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._batchiteration import BatchIteration
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError

__all__ = ["BatchIterationSuperMouse"]


class BatchIterationSuperMouse(BatchIteration):

    """
The BatchIteration class is used to retrieve MAUS data cards indexed by batch iteration number.

A couple of methods are provided for diagnostics. It is possible to retrieve a
list of ...
TODO set methods

        """

    def __init__(self, url="",
                 wsdl_dir="/cdb/batchIterationSuperMouse?wsdl"):
        """
Construct an BatchIteration object.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(BatchIterationSuperMouse, self).__init__(url, wsdl_dir)
        #self._alh_handler = _AlarmHandlerHandler()
        self._help = self._base_help + "\n\tget_datarecord(int iteration_number) \
        \n\tget_reco_datacards(int iteration_number)\
        \n\tget_mc_datacards(int iteration_number) \
        \n\tget_comment(int iteration_number) \
        \n\tset_datacards(int iteration_number, string comment, string reco_datacards, string mc_datacards)"

    def __str__(self):
        return "BatchIterationSuperMouse" + self._help
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl
@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(BatchIterationSuperMouse, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(BatchIterationSuperMouse, self).get_status()

    def set_datacards(self, comment, recocards, mccards):
        """
        :param comment:
        :param recocards:
        :param mccards:
        """
        xml = str(self._server.setDataCards(comment,recocards,mccards))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()