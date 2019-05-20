"Target module."

from base64 import b64decode
from xml.sax import parseString
from xml.sax import SAXParseException

from cdb._base import _CdbBase
from cdb._base import _get_string_from_date

__all__ = ["Target"]


class Target(_CdbBase):

    """
The Target class is used to retrieve a target data set.

To store target data sets use the TargetSuperMouse class. Previous versions of
the target data sets are also stored. The current target data set can be retrieved
using get_current_blob. The target data set associated with a run can be retrieved
using get_blob_for_run.

    """

    def __init__(self, url="",
                 wsdl_dir="/cdb/target?wsdl"):
        """
Construct a Target.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(Target, self).__init__(url, wsdl_dir)
        self._help = self._base_help + "\n\tget_current_blob(string name) \
        \n\tget_blob_for_run(string name, string run_number) \
        \n\tget_blob_for_date(string name, datetime date_time) \
        \n\tget_target_names()"

    def __str__(self):
        return "Target" + self._help
        
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl

@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(Target, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(Target, self).get_status()
        
    def get_current_blob(self, name):
        """
Get the current target data set.

@param name: a string containing the target name

@return a string containing the target data set

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        _data = b64decode(self._server.getCurrentBlob(str(name)))
        try:
            # check for error or warning tag
            parseString(_data, self._status_handler)
        except SAXParseException:
            pass # no tag found so as expected could not parse data
        return _data

    def get_blob_for_run(self, name, run_number):
        """
Get the target data set that was valid when the run represented by the run number
occurred.

@param name: a string containing the target name
@param run_number: a long containing the number of a run

@return a string containing the target data set

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        _data = b64decode(self._server.getBlobForRun(str(name), run_number))
        try:
            # check for error or warning tag
            parseString(_data, self._status_handler)
        except SAXParseException:
            pass # no tag found and could not parse data
        return _data

    def get_blob_for_date(self, name, date_time):
        """
Get the target data set that was valid at the given date time.

@param name: a string containing the target name
@param date_time:  a datetime in UTC

@return a string containing the target data set
            
@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        time = _get_string_from_date(date_time)
        _data = b64decode(self._server.getBlobForDate(str(name), time))
        try:
            # check for error or warning tag
            parseString(_data, self._status_handler)
        except SAXParseException:
            pass # no tag found and could not parse data
        return _data
    
    def get_target_names(self):
        """
Return a list of allowed target names.        

@return a list of strings representing the allowed target names

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        _targets = self._server.getTargetNames()
        try:
            # check for error or warning tag
            parseString(str(_targets), self._status_handler)
        except SAXParseException:
            pass # no tag found and could not parse data
        return _targets

