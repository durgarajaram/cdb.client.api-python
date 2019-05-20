"CoolingChannelSuperMouse module."

from xml.sax import parseString

from cdb._coolingchannel import CoolingChannel
from cdb._exceptions import CdbPermanentError
from datetime import datetime

__all__ = ["CoolingChannelSuperMouse"]

class CoolingChannelSuperMouse(CoolingChannel):
    
    """
The CoolingChannelSuperMouse class is used to set and retrieve cooling channel
settings.

Cooling channel data is stored using the set_coolingchannel method. All
available data can be retrieved using get_all_coolingchannels. A number of
methods are available to retrieve subsets of the data,
get_coolingchannel_for_run and get_coolingchannel_for_date.

In addition there is the concept of tagged data. It is possible to tag a set of
parameters using set_coolingchannel_tag. Tagged parameters can then be retrieved
using get_coolingchannel_for_tag. The use of set_coolingchannel_tag with an
existing tag name will replace the existing parameters, although the original
parameters will still be stored in the database.

    """
    
    def __init__(self, url=""):
        """
Construct a CoolingChannelSuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """

        super(CoolingChannelSuperMouse, self).__init__(url,
            "/cdb/coolingChannelSuperMouse?wsdl")

    def __str__(self):
        _help_super = "\n\tset_coolingchannel(list(dict) data) \
        \n\tset_coolingchannel_tag(str tag, list(dict) data)"
        return "CoolingChannelSuperMouse" + self._help + _help_super


    def set_coolingchannel(self, data, run = 0, tag = None, timestamp = None):
        """
Add the parameters associated with a cooling channel.

@param run is a run number the Cooling Channel data is set for
@param tag is a tag name (required) of the template (tag) the data comes from
@param data a list of dictionaries with the following keys/values:<pre>
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

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        try:
            xml = "<coolingchannel"
            if timestamp is not None:
                test = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
                xml =   (xml + " validfromtime='" + timestamp +"'")
            if run is not None:
                xml = xml + (" run='" + str(run) +"'")
            if tag is not None:
                xml = xml + (" tag='" + str(tag) +"'")
            xml = xml+">"
            for magnet in data:
                if (str(magnet['polarity']) != "-1" 
                    and str(magnet['polarity']) != "0" 
                    and str(magnet['polarity']) != "1" 
                    and str(magnet['polarity']) != "+1"):
                    raise CdbPermanentError("Polarity for " + magnet['name'] 
                                            + " is " + str(magnet['polarity']) 
                                            + ", it must be -1, 0 or +1")
                xml = xml + "<magnet name='" + str(magnet['name']) + "' "
                xml = xml + "mode='" + str(magnet['mode']) + "' "
                xml = xml + "polarity='" + str(magnet['polarity']) + "'>"
                
                coils = magnet['coils']
                for coil in coils:
                    xml = xml + "<coil name='" + str(coil['name']) + "' "
                    xml = (xml + "calibration='" 
                              + str(coil['calibration']) + "' ")
                    xml = xml + "ilim='" + str(coil['ilim']) + "' "
                    xml = xml + "iset='" + str(coil['iset']) + "' "
                    xml = xml + "rate='" + str(coil['rate']) + "' "
                    xml = (xml + "stability='" + str(coil['stability']) 
                              + "' ")
                    xml = xml + "vlim='" + str(coil['vlim']) + "'/>"
                
                xml = xml + "</magnet>"
            xml = xml + "</coolingchannel>"
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        except ValueError, ve:
            raise CdbPermanentError("Incorrect timestamp format " + str(ve))

        return_xml = str(self._server.setCoolingchannel(str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

    def set_absorber(self, run, tag, absorbers):
        """
        Set absorber data.
@param run is a run number the Cooling Channel Absorber data is set for
@param tag is a tag name (required) of the template (absorber tag) the data comes from
@param data a list of dictionaries with the following keys/values:<pre>
        key - comment,  value - user comment string
        key - name, value - absorber name
        key - material, value - absorber material
        key - pressure, value - absorber pressure (string)
        key - shape, value - absorber shape
        key - temperature - absorber temperature (string)
        </pre>
@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error
        """
        try:

            xml="<absorbers run='" + str(run)+"' tag='" + str(tag) + "'>"
            for absorber in absorbers:
                xml = xml + "<absorber name='" + str(absorber['name']) + "' "
                xml = xml + "material='" + str(absorber['material']) + "' "
                xml = xml + "shape='" + str(absorber['shape']) + "' "
                xml = xml + "temperature='" + str(absorber['temperature']) + "' "
                xml = xml + "pressure='" + str(absorber['pressure']) + "' "
                xml = xml + "comment='" + str(absorber['comment']) + "'/> "
            xml = xml + "</absorbers>"

        except KeyError, exception:
               raise CdbPermanentError("Missing value for " + str(exception))

        return_xml = str(self._server.setCoolingchannelAbsorber(str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

    def set_absorber_tag(self, tag, absorbers):

        try:
            xml = ("<tag name='" + str(tag) + "'>")
            for absorber in absorbers:
                xml = xml + "<absorber name='" + str(absorber['name']) + "' "
                xml = xml + "material='" + str(absorber['material']) + "' "
                xml = xml + "shape='" + str(absorber['shape']) + "' "
                xml = xml + "temperature='" + str(absorber['temperature']) + "' "
                xml = xml + "pressure='" + str(absorber['pressure']) + "' "
                xml = xml + "comment='" + str(absorber['comment']) + "'/> "
            xml = xml + "</tag>"

        except KeyError, exception:
               raise CdbPermanentError("Missing value for " + str(exception))

        return_xml = str(self._server.setCoolingchannelAbsorberTag(str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

    def set_coolingchannel_tag(self, tag, data):
        """
Add a tagged set of cooling channel parameters.

@param tag a string containing the name of the tag 
@param data a list of dictionaries with the following keys/values:<pre>
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

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        try:
            xml = ("<tag name='" + str(tag) + "'>")
                      
            for magnet in data:
                if (str(magnet['polarity']) != "-1" 
                    and str(magnet['polarity']) != "0" 
                    and str(magnet['polarity']) != "1" 
                    and str(magnet['polarity']) != "+1"):
                    raise CdbPermanentError("Polarity for " + magnet['name'] 
                                            + " is " + str(magnet['polarity']) 
                                            + ", it must be -1, 0 or +1")
                xml = xml + "<magnet name='" + str(magnet['name']) + "' "
                xml = xml + "mode='" + str(magnet['mode']) + "' "
                xml = xml + "polarity='" + str(magnet['polarity']) + "'>"
                
                coils = magnet['coils']
                for coil in coils:
                    xml = xml + "<coil name='" + str(coil['name']) + "' "
                    xml = (xml + "calibration='" 
                              + str(coil['calibration']) + "' ")
                    xml = xml + "ilim='" + str(coil['ilim']) + "' "
                    xml = xml + "iset='" + str(coil['iset']) + "' "
                    xml = xml + "rate='" + str(coil['rate']) + "' "
                    xml = (xml + "stability='" + str(coil['stability']) 
                              + "' ")
                    xml = xml + "vlim='" + str(coil['vlim']) + "'/>"
                
                xml = xml + "</magnet>"
            xml = xml + "</tag>"
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        return_xml = str(self._server.setCoolingchannelTag(str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

    def set_coolingchannel_csv_tag(self, csv_file_handle):
        """
Add a tagged set of cooling channel parameters.

@param csv_file_handle a csv file handle, with the following data format:
<pre>
    tag,      <tag_value>
    name,     <name_value>
    mode,     <mode_value>
    polarity, <polarity_value>
    coils, name, vlim, ilim, rate, iset, stability, calibration
       , <coil_name>, <vlim>, <ilim>, <rate>, <iset>, <stability>, <calibration>
    ... one line per coil ...
</pre>
where values take meanings and types as specified in set_coolingchannel_tag(...)

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error
        """
        tag, data = self._coolingchannel_csv(csv_file_handle)
        return self.set_coolingchannel_tag(tag, data)

    def _coolingchannel_csv(self, csv_file_handle):
        """
Helper for set_coolingchannel_csv_tag
        """
        tag, data = None, {}
        line = csv_file_handle.readline()
        while line != '':
            line = line[0:-1]
            words = line.split(',')
            if words[0] == 'tag':
                tag = words[1]
            elif words[0] == 'coils':
                break
            elif words[0] in ['name', 'mode', 'polarity']:
                data[words[0]] = words[1]
            else:
                raise CdbPermanentError("Failed to parse key '"+str(words[0])+"'")
            line = csv_file_handle.readline()
        data['coils'] = []
        line = csv_file_handle.readline()
        while line != '':
            line = line[0:-1]
            data['coils'].append(self._get_csv_coil(words[1:], line))
            line = csv_file_handle.readline()
        if tag == None:
            raise CdbPermanentError("No tag defined in csv file")
        return tag, [data]

    def _get_csv_coil(self, header, coil_line):
        """
Load a coil from a csv file
        """
        coil_data = {}
        words = coil_line.split(',')[1:]
        types = {"name":str, "calibration":float, "ilim":float, "iset":float,
                 "rate":float, "stability":float, "vlim":float}
        try:
            for i, key in enumerate(header):
                coil_data[key] = types[key](words[i])
        except KeyError:
            raise CdbPermanentError("Failed to parse header item "+str(key))
        return coil_data

