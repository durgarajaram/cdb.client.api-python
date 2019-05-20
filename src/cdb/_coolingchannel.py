"CoolingChannel module."

from xml.sax import parseString
from xml.sax.handler import ContentHandler

from cdb._base import _CdbBase
from cdb._base import _get_date_from_string
from cdb._base import _get_string_from_date
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError


__all__ = ["CoolingChannel"]


class CoolingChannel(_CdbBase):
    
    """
The CoolingChannel class is used to retrieve data about cooling channel
settings.

All available cooling channel data can be retrieved using
get_all_coolingchannels. A number of methods are available to retrieve subsets
of the data, get_coolingchannel_for_run and get_coolingchannel_for_date.

In addition there is the concept of tagged data. Tagged parameters can be
retrieved using get_coolingchannel_for_tag.

    """

    def __init__(self, url="",
                 wsdl_dir="/cdb/coolingChannel?wsdl"):
        """
Construct a CoolingChannel.

@param url: the url of the server in the form 'http://host.domain:port'
@param wsdl_dir: the path to the wsdl on the server

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(CoolingChannel, self).__init__(url, wsdl_dir)
        self._coolingchannel_handler = _CoolingChannelHandler()
        self._coolingchannel_absorber_handler = _CoolingChannelAbsorberHandler()
        self._help = self._base_help + "\n\tget_all_coolingchannels() \
        \n\tget_coolingchannel_for_run(int run_number) \
        \n\tget_coolingchannel_for_date(datetime timestamp) \
        \n\tget_coolingchannel_for_tag(str tag)\
        \n\tlist_tags()"

    def __str__(self):
        return "CoolingChannel" + self._help
 
    def set_url(self, url):
        """
Set the client to use the given CDB server.

@param url: the URL of the CDB wsdl

@exception CdbTemporaryError: Unable to contact CDB server
@exception CdbPermanentError: Invalid URL

        """
        super(CoolingChannel, self).set_url(url)

    def get_status(self):
        """
Get the status of the service.

@return a string containing the status of the service

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

        """
        return super(CoolingChannel, self).get_status()

    def get_all_coolingchannels(self):
        """
Get all cooling channel data.

@return a list of dictionaries with the following keys/values:<pre>
    key - valid_from_time, value -  a datetime in UTC
    key - valid_until_time, value -  a datetime in UTC, None if still valid
    key - magnets, value - a list of dictionaries containing magnet data
    magnets dictionary:    
        key - name, value - a string representing the magnet name
        key - mode, value - a string representing the magnet mode
        key - polarity, value - a string representing the magnet polarity
        key - coils, value - a list of dictionaries containing coil data
        coils dictionary:
            key - name, value - a string representing the magnet name
            key - calibration, value - a float
            key - ilim, value - a float
            key - iset, value - a float
            key - rate, value - a float
            key - stability, value - a float
            key - vlim, value - a float</pre>

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getAllCoolingchannels()
        return self._parse_cooling_channel_xml(str(xml))

    def get_coolingchannel_for_run(self, run_number):
        """
Get the cooling channel data for a given run.

@param run_number: an int representing the run number

@return a list of dictionaries containing magnet data with the following keys/values:<pre>
    key - name, value - a string representing the magnet name
    key - mode, value - a string representing the magnet mode
    key - polarity, value - a string representing the magnet polarity
    key - coils, value - a list of dictionaries containing coil data
    coils dictionary:
        key - name, value - a string representing the magnet name
        key - calibration, value - a float
        key - ilim, value - a float
        key - iset, value - a float
        key - rate, value - a float
        key - stability, value - a float
        key - vlim, value - a float</pre>

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getCoolingchannelForRun(run_number)
        #return self._get_magnets(xml)
        return self._get_coolingchannel(xml)

    def get_coolingchannel_for_date(self, timestamp):
        """
Get the cooling channel data for the given timestamp.

@param timestamp: a datetime in UTC

@return a list of dictionaries containing magnet data with the following keys/values:<pre>
    key - name, value - a string representing the magnet name
    key - mode, value - a string representing the magnet mode
    key - polarity, value - a string representing the magnet polarity
    key - coils, value - a list of dictionaries containing coil data
    coils dictionary:
        key - name, value - a string representing the magnet name
        key - calibration, value - a float
        key - ilim, value - a float
        key - iset, value - a float
        key - rate, value - a float
        key - stability, value - a float
        key - vlim, value - a float</pre>

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        timestamp = _get_string_from_date(timestamp)
        xml = self._server.getCoolingchannelForDate(timestamp)
        return self._get_coolingchannel(xml)

    def get_absorber_for_run(self, run):
        """
Get the cooling channel data for the given run.
@param run: run number

@return a dictionary keyed by run number of a list  of dictionaries containing absorber data with the following keys/values:<pre>
    key - run number, value - list of dictionaries
      list of dictionaries, each having :
      key - name, value - a string representing the absorber name
      key - material, value - a string representing the absorber material
      key - shape, value - a string representing the absorber shape
      key - comment, value - a comment string

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error
        """
        xml = self._server.getCoolingchannelAbsorberForRun(run)
        self._coolingchannel_absorber_handler.reset()
        parseString(xml, self._coolingchannel_absorber_handler)
        return self._coolingchannel_absorber_handler.get_data()

    def get_absorber_for_tag(self, tag):
        xml = self._server.getCoolingchannelAbsorberForTag(tag)
        self._coolingchannel_absorber_handler.reset()
        parseString(xml, self._coolingchannel_absorber_handler)
        return self._coolingchannel_absorber_handler.get_data()

    def get_coolingchannel_for_tag(self, tag):
        """
Get the cooling channel data for the given tag.

@param tag: a string containing the tag name

@return a list of dictionaries containing magnet data with the following keys/values:<pre>
    key - name, value - a string representing the magnet name
    key - mode, value - a string representing the magnet mode
    key - polarity, value - a string representing the magnet polarity
    key - coils, value - a list of dictionaries containing coil data
    coils dictionary:
        key - name, value - a string representing the magnet name
        key - calibration, value - a float
        key - ilim, value - a float
        key - iset, value - a float
        key - rate, value - a float
        key - stability, value - a float
        key - vlim, value - a float</pre>

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = self._server.getCoolingchannelForTag(tag)
        return self._get_magnets(xml)
    
    def list_tags(self):
        """
Return a list of known tags.

@return a list of strings containing the names of the tags

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = str(self._server.listTags())
        return self._parse_cooling_channel_xml(str(xml))
        
    def list_absorber_tags(self):
        """
Return a list of known absorber tags.

@return a list of strings containing the names of the tags

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        xml = str(self._server.listAbsorberTags())
        return self._parse_cooling_channel_xml(str(xml))

    def _get_magnets(self, xml):
        """ Get the list of magnets from the xml"""
        try:
            result = self._parse_cooling_channel_xml(str(xml))[0]['magnets']
        except IndexError:
            return []
        except KeyError:
            return []
        return result

    def _get_coolingchannel(self, xml):
        # get the first cc from a list
        try:
            result = self._parse_cooling_channel_xml(str(xml))[0]
        except IndexError:
            return []
        except KeyError:
            return []
        return result

    def _parse_cooling_channel_xml(self, xml):
        """ Parser for coolingchannel data. """
        parseString(xml, self._coolingchannel_handler)
        return self._coolingchannel_handler.get_data()

class _CoolingChannelAbsorberHandler(ContentHandler):
    """ Parse cooling channel absorber data
    """
    def __init__(self):
        ContentHandler.__init__(self)
        #self._absorbers={}
        #self._tag={}
        #self._absorber={}
        #self._message=""
        self.reset()

    def reset(self):
        self._absorbers={}
        self._tag={}
        self._absorber={}
        self._intag = False
        self._message=""


    def get_data(self):
        #from operator import itemgetter
        #return sorted(self._absorbers, key=itemgetter('run'))
        return self._absorbers

    def startElement(self, name, attrs):  # pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            self._message = ""
        elif name == 'warning':
            self._message = ""
        elif name == 'absorbers':
            self._intag = False
            self._run = _get_int(str(attrs.get('run', '')))
            self._utag = str(attrs.get('tag', '')) # tag attribute passed in with absorbers
            #self._absorbers[self._run]=[{'tag' : self._tag}]
            self._absorbers[(self._run,self._utag)]=[]
        elif name == 'tag':
            self._intag = True
            self._tag = str(attrs.get('name', ''))
            self._absorbers[self._tag]=[]
        elif name == 'absorber':
            self._add_absorber(attrs)

    def characters(self, message):
        """ Method required for ContentHandler. """
        self._message = self._message + message

    def endElement(self, name):  # pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            raise CdbPermanentError(self._message)
        elif name == 'warning':
            raise CdbTemporaryError(self._message)
        elif name == 'absorbers':
            pass
        elif name == 'absorber':
            if not self._intag:
               if(hasattr(self, '_run')):
                   self._absorbers[(self._run,self._utag)].append(self._absorber)
            else:
               if(hasattr(self,'_tag')):
                self._absorbers[self._tag].append(self._absorber)
    def _add_absorber(self, attrs):
        self._absorber={}
        #self._absorber['run'] = _get_int(str(attrs.get('run', '')))
        self._absorber['name'] = str(attrs.get('name', ''))
        self._absorber['material'] = str(attrs.get('material', ''))
        self._absorber['shape'] = str(attrs.get('shape', ''))
        self._absorber['temperature'] = str(attrs.get('temperature', ''))
        self._absorber['pressure'] = str(attrs.get('pressure', ''))
        self._absorber['comment'] = str(attrs.get('comment', ''))


class _CoolingChannelHandler(ContentHandler):
# pylint: disable-msg=R0902

    " ContentHandler for coolingchannel data. "

    def __init__ (self):
        ContentHandler.__init__(self)
        self._coolingchannels = []
        self._coolingchannel = {}
        self._magnets = []
        self._magnet = {}
        self._coils = []
        self._message = ""
        self._tag_names = []
        self.cc_xml = False
        self.tag_names_xml = False

    def get_data(self):
        """
        Get a dictionary containing the parsed XML.

        @return the dictionary containing the parsed XML

        """
        if self.cc_xml:
            return self._coolingchannels
        else:
            return self._tag_names
        
    def startElement(self, name, attrs):  # pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            self._message = ""
        elif name == 'warning':
            self._message = ""
        elif name == 'coolingchannels':
            self._set_ccs()
            self.cc_xml = True
            self.tag_names_xml = False
        elif name == 'coolingchannel':
            self._add_cc(attrs)
        elif name == 'magnets':
            self._set_magnets()
        elif name == 'magnet':
            self._add_magnet(attrs)
        elif name == 'coil':
            self._add_coil(attrs)
        elif name == 'tagNames':
            self._tag_names = []
            self.cc_xml = False
            self.tag_names_xml = True
        elif name == 'tag':
            self._add_tag(attrs)
        return

    def characters(self, message):
        """ Method required for ContentHandler. """
        self._message = self._message + message

    def endElement(self, name):  # pylint: disable-msg=C0103
        """ Method required for ContentHandler. """
        if name == 'error':
            raise CdbPermanentError(self._message)
        elif name == 'warning':
            raise CdbTemporaryError(self._message)
        elif name == 'magnet':
            self._magnet['coils'] = self._coils
            self._magnets.append(self._magnet)
        elif name == 'magnets':
            self._coolingchannel['magnets'] = self._magnets
        elif name == 'coolingchannel':
            self._coolingchannels.append(self._coolingchannel)
            
    def _add_tag(self, attrs):
        """ Populate a list with data from the XML. """
        self._tag_names.append(str(attrs.get('name', '')))
        
    def _set_ccs(self):
        """ Initialise a cooling channel list. """
        self._coolingchannels = []

    def _add_cc(self, attrs):
        """ Populate a cooling channel dictionary with data from the XML. """
        self._coolingchannel = {}
        self._coolingchannel['valid_from_time'] = (
            _get_date_from_string(attrs.get('validfromtime', '')))
        # to allow both old (timestamp based) and new (run based) data, we make both validuntiltime and run optional.(JM)
        self._coolingchannel['valid_until_time'] = (
            _get_date_from_string(attrs.get('validuntiltime', 'null')))
        self._coolingchannel['run'] = str(attrs.get('run', 'null'))
        self._coolingchannel['tag'] = str(attrs.get('tag', 'null'))
                
    def _set_magnets(self):
        """ Initialise a magnets list. """
        self._magnets = []
              
    def _add_magnet(self, attrs):
        """ Populate a magnet dictionary with data from the XML. """
        self._magnet = {}
        self._coils = []
        self._magnet['name'] = str(attrs.get('name', ''))
        self._magnet['mode'] = str(attrs.get('mode', ''))
        self._magnet['polarity'] = _get_int(str(attrs.get('polarity', '')))
        
    def _add_coil(self, attrs):
        """ Populate a coil dictionary with data from the XML. """
        coil = {}
        coil['name'] = str(attrs.get('name', ''))
        coil['calibration'] = _get_float(attrs.get('calibration', ''))
        coil['ilim'] = _get_float(attrs.get('ilim', ''))
        coil['iset'] = _get_float(attrs.get('iset', ''))
        coil['rate'] = _get_float(attrs.get('rate', ''))
        coil['stability'] = _get_float(attrs.get('stability', ''))
        coil['vlim'] = _get_float(attrs.get('vlim', ''))
        self._coils.append(coil)


def _get_float(string):
    """ Convert string to float """
    try:
        float_attr = float(string)
    except ValueError:
        return None
    return float_attr
    
def _get_int(string):
    """ Convert string to int """
    try:
        int_attr = int(string)
    except ValueError:
        return None
    return int_attr
