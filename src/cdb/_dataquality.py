"DataQuality module."

from xml.sax import parseString
from xml.sax import SAXParseException
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError

__all__ = ["DataQuality"]


class DataQuality(_CdbBase):

    """
The DataQuality class is used to retrieve MICE quality flags.

A couple of methods are provided for diagnostics. It is possible to retrieve a
list of ...


        """

    def __init__(self, url="",
                 wsdl_dir="/cdb/dataQuality?wsdl"):
        """
Construct an DataQuality object.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(DataQuality, self).__init__(url, wsdl_dir)
        self._dataq_handler = _DataQualityHandler()
        self._help = self._base_help + "\n\tget_beamline_flags(run_number)\
\n\tget_detector_flags(run_number)\
\n\tget_daq_flags(run_number)\
\n\tget_reconstruction_flags(run_number, maus_version, batch_iteration_number)"

    def __str__(self):
        return "DataQuality" + self._help
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl
xception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(DataQuality, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(DataQuality, self).get_status()

    def get_beamline_flags(self, run_number):
        xml = self._server.getBeamlineFlags(run_number)
        parseString(xml, self._dataq_handler)
        return  self._dataq_handler.getData()

    def get_detector_flags(self, run_number):
        xml = self._server.getDetectorFlags(run_number)
        parseString(xml, self._dataq_handler)
        return self._dataq_handler.getData()

    def get_daq_flags(self, run_number):
        xml = self._server.getDaqFlags(run_number)
        parseString(xml, self._dataq_handler)
        return self._dataq_handler.getData()

    def get_reconstruction_flags(self, run_number, maus_version, batch_iteration_number):
        """
        Get a reconstruction flags (up to 44  bits) for all detectors and a given run number, MAUS version and batch
        iteration number.
        @param run_number run number
        @param maus_version MAUS version
        @param batch_iteration_number Batch Iteration Number

        Returns a dictionary with detector names as keys and integers (0-15, 4 bits) as flag values.

        """

        masks = [('TOF0',0xf0000000000L), ('TOF1',0xf000000000L), ('CkovA',0xf00000000L), ('CkovB',0xf0000000L), ('Tracker0',0xf000000L),
                 ('Tracker1',0xf00000L), ('TOF2',0xf0000L), ('KL',0xf000L), ('EMR',0xf00L), ('RF1',0xf0L), ('RF2',0xfL)]
        det_dict={}
        maxFshift=10

        flags = self._server.getReconstructionFlags(run_number, maus_version, batch_iteration_number)
        print  flags
        try:
            # check for error or warning tag
            parseString(flags, self._status_handler)
        except SAXParseException:
            try:
               iflags = int(flags,16)
            except ValueError as ve:
               raise CdbPermanentError(str(ve))
            for n, k in enumerate(masks):
                det_dict[k[0]]=(masks[n][1]&iflags)>>(maxFshift-n)*4
                print 4*(maxFshift-n), k[0], hex(det_dict[k[0]])
        return det_dict

    def get_reconstruction_flags_for_detector(self, detector, run_number, maus_version, batch_iteration_number):
        """
        Get a reconstruction flag (4 bits) for a given detector, run number, MAUS version and batch
        iteration number.
        @param detector - a detector name.
        @param run_number run number
        @param maus_version MAUS version
        @param batch_iteration_number Batch Iteration Number
        Don't use this operation in a loop if you need flags for many detectors. Use a @ref get_reconstruction_flags(...)
        above and loop over a dictionary obtained.

        """

        det_dict = self.get_reconstruction_flags(run_number, maus_version, batch_iteration_number)

        try:
            f = det_dict[detector]
        except KeyError as k:
            raise CdbPermanentError('(client-side) ' + k.__class__.__name__+': '+ k.message + \
                                    '\nValid keys are: '+ str(sorted(det_dict.keys())))
        return f

class _DataQualityHandler(ContentHandler):

    " ContentHandler for QualityFlags data. "

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
        elif name == 'quality':
            self.data = {}

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
        elif name == 'quality':
            self._data['flags']=self._message

    def getData(self):
        return self._data
