"BeamlineSuperMouse module."

from xml.sax import parseString

from cdb._base import _get_string_from_date
from cdb._beamline import Beamline
from cdb._exceptions import CdbPermanentError

__all__ = ["BeamlineSuperMouse"]

class BeamlineSuperMouse(Beamline):
    
    """
The BeamlineSuperMouse class is used to set and retrieve  beam line settings.

Beam line data is stored on a per run basis. Prior to a run commencing the
set_start_run and set_beamline methods should be called to record the initial
parameters. At the end of the set_end_run should be called to record the final
parameters. All available data can be retrieved using get_all_beamlines. A
number of methods are available to retrieve subsets of the data,
get_beamline_for_run, get_beamlines_for_dates and get_beamlines_for_pulses.

In addition there is the concept of tagged data. It is possible to tag a set of
parameters using set_beamline_tag. Tagged parameters can then be retrieved using
get_beamline_for_tag. The use of set_beamline_tag with an existing tag name will
replace the existing parameters, although the original parameters will still be
stored in the database.

    """
    
    def __init__(self, url=""):
        """
Construct a BeamlineSuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """

        super(BeamlineSuperMouse, self).__init__(url,
                                                 "/cdb/beamlineSuperMouse?wsdl")

    def __str__(self):
        _help_super = "\n\tset_start_run(dict run_data) \
        \n\tset_end_run(dict run_data, dict scalar_data) \
        \n\tset_beamline(dict run_data, list(dict) magnets \
        \n\tset_beamline_tag(str tag, dict data, list(dict) magnets"
        return "BeamlineSuperMouse" + self._help + _help_super

    def set_start_run(self, run_data):
        """
Add the initial parameters associated with a run.

@param run_data a dictionary containing the run data set with the following keys/values:<pre>
    key - run_number, value - an int representing the run number
    key - start_time, value - a datetime that should represent the time the run started
    key - start_notes, value - a string
    key - optics, value - a string representing the beamline optics
    key - start_pulse, value - an int representing the total number of pulses at the start of run
    key - step, value - a float representing the MICE phase
    key - run_type, value - a sting
    key - daq_trigger, value - a string
    key - daq_gate_width, value - a float representing the gate width in ms
    key - daq_version, value - a string
    key - gdc_host_name, value - a string
    key - ldc_host_names, value - a list of strings
    key - target_delay, value - a float representing the target delay
    key - target_depth, value - a float representing the target depth
    key - target_drive_voltage, value - a float representing the target drive voltage</pre>

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        try:
            run_xml = ("<startRun runNumber='" + str(run_data['run_number'])
                       + "' startTime='"
                       + _get_string_from_date(run_data['start_time'])
                       + "' startNotes='" + str(run_data['start_notes'])
                       + "' optics='" + str(run_data['optics'])
                       + "' startPulse='" + str(run_data['start_pulse'])
                       + "' step='" + str(run_data['step'])
                       + "' runType='" + str(run_data['run_type'])
                       + "' daqTrigger='" + str(run_data['daq_trigger'])
                       + "' daqGateWidth='" + str(run_data['daq_gate_width'])
                       + "' daqVersion='" + str(run_data['daq_version'])
                       + "' gdcHostName='" + str(run_data['gdc_host_name'])
                       + "' ")
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        try:    
            run_xml = (run_xml + "targetDelay='" 
                       + str(run_data['target_delay']) + "' ")
        except KeyError, exception:
            pass  
        try:    
            run_xml = (run_xml + "targetDepth='" 
                       + str(run_data['target_depth']) + "' ")
        except KeyError, exception:
            pass
        try:    
            run_xml = (run_xml + "targetDriveVoltage='" 
                       + str(run_data['target_drive_voltage']) + "' ")
        except KeyError, exception:
            pass
        try:
            run_xml = (run_xml + "overwrite='" 
                       + str(int(run_data['overwrite'])) + "' >")
        except KeyError, exception:
            run_xml = (run_xml + "overwrite='" + str(False) + "' >")
        try:
            for host in run_data['ldc_host_names']:
                run_xml = (run_xml + "<ldcHost name='" 
                       + str(host) + "' />")
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        
        run_xml = (run_xml + "</startRun>")
        xml = str(self._server.setStartRun(str(run_xml)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_start_runXML(self, run_xml):
       xml = str(self._server.setStartRun(str(run_xml)))
       parseString(xml, self._status_handler)
       return self._status_handler.get_message()

    def set_end_run(self, run_data, scalar_data, isis_beam): 
        """
Add the parameters associated with the end of a run.

@param run_data a dictionary containing the run data set with the following keys/values:<pre>
    key - run_number, value - an int representing the run number
    key - end_time, value - a datetime that should represent the time the run ended
    key - end_notes, value - a string
    key - end_pulse, value - an int representing the total number of pulses at the end of run
    key - status, value - a boolean, true indicates data are analysable</pre>
  
@param scalar_data a dictionary containing the scalar data set with the following keys/values:<pre>
    key - a string representing the name of the scalar, value - an int representing the sum of the scalar</pre>

@param isis_beam a list of dictionaries containing the isis beam data with the following keys/values:<pre>
    key - name, value - a string representing the name of the data
    key - mean, value - a float representing the mean
    key - sigma, value - a float representing the sigma</pre>

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        try:
            run_xml = ("<endRun runNumber='" + str(run_data['run_number'])
                       + "' endTime='"
                       + _get_string_from_date(run_data['end_time'])
                       + "' endPulse='" + str(run_data['end_pulse'])
                       + "' status='" + str(int(run_data['status']))   
                       + "' endNotes='" + str(run_data['end_notes'])   
                       + "' ")
        except KeyError, exception: 
            raise CdbPermanentError("Missing value for " + str(exception))

        try:
            run_xml = (run_xml + "overwrite='" 
                           + str(int(run_data['overwrite'])) + "' >")
        except KeyError, exception:
            run_xml = (run_xml + "overwrite='" + str(False) 
                           + "' >")
          
        for key in scalar_data.keys():
            run_xml = run_xml + ("<scalar name='" + str(key) + "' value='" 
                                 + str(scalar_data[key]) + "' />")

        for beam in isis_beam:
            run_xml = run_xml + ("<isisBeam name='" + str(beam['name']) 
                                 + "' mean='" + str(beam['mean']) 
                                 + "' sigma='" + str(beam['sigma']) + "' />")   
        run_xml = run_xml + ("</endRun>")            
            
        xml = str(self._server.setEndRun(str(run_xml)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_end_runXML(self, run_xml):
        xml = str(self._server.setEndRun(str(run_xml)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_beamline(self, run_data, magnets):
        """
Add the initial parameters associated with a run.

@param run_data a dictionary containing the beam line data set with the following keys/values:<pre>
    key - run_number, value - an int representing the run number
    key - diffuser_thickness, value - an int representing the thickness of diffuser the in mm
    key - beam_stop, value - a string, allowed values 'Open' and 'Closed'
    key - proton_absorber_thickness, value - an int representing the thickness of the proton absorber in mm</pre>
@param magnets a list of dictionaries containing the magnet data with the following keys/values:<pre>
    key - name, value - a string
    key - current, value - a float
    key - polarity, value - an int, must be -1 or 1</pre>

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        try:
            if str(run_data['beam_stop']).upper() == 'OPEN':
                beam_stop = str(True)
            elif str(run_data['beam_stop']).upper() == 'CLOSED':
                beam_stop = str(False)
            else:
                raise CdbPermanentError(
                    "Value for beam_stop must be 'OPEN' or 'CLOSED' not "
                    + str(run_data['beam_stop']))

            run_xml = ("<beamline runNumber='" + str(run_data['run_number'])
                       + "' beamStop='" + beam_stop
                       + "' diffuserThickness='" 
                       + str(run_data['diffuser_thickness'])
                       + "' protonAbsorberThickness='" 
                       + str(run_data['proton_absorber_thickness'])
                       + "' ")                    
            try:
                run_xml = (run_xml + "overwrite='" 
                           + str(int(run_data['overwrite'])) + "' >")
            except KeyError, exception:
                run_xml = (run_xml + "overwrite='" + str(False) 
                           + "' >")                          
            if magnets != None:
                for magnet in magnets:
                    if (str(magnet['polarity']) != "-1" 
                        and str(magnet['polarity']) != "0" 
                        and str(magnet['polarity']) != "1" 
                        and str(magnet['polarity']) != "+1"):
                        raise CdbPermanentError("Polarity for " 
                                                + magnet['name'] + " is " 
                                                + str(magnet['polarity']) 
                                                + ", it must be -1, 0 or +1")
                    run_xml = (run_xml + "<magnet name='" + str(magnet['name'])
                               + "' setCurrent='" + str(magnet['current'])
                               + "' polarity='" + str(magnet['polarity'])
                               + "'/>")
            run_xml = run_xml + "</beamline>"
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        xml = str(self._server.setBeamline(str(run_xml)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_beamlineXML(self, run_xml):
        xml = str(self._server.setBeamline(str(run_xml)))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_beamline_tag(self, tag, data, magnets):
        """
Add a tagged set of beamline parameters.

@param tag a string containing the name of the tag 
@param data a dictionary containing the beam line data set with the following keys/values:<pre>
    key - diffuser_thickness, value - an int representing the thickness of diffuser the in mm
    key - beam_stop, value - a string, allowed values 'Open' and 'Closed'
    key - proton_absorber_thickness, value - an int representing the thickness of the proton absorber in mm</pre>
@param magnets a list of dictionaries containing the magnet data with the following keys/values:<pre>
    key - name, value - a string
    key - current, value - a float</pre>

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: Maybe due to to bad data being passed in or an
unexpected internal error

        """
        try:
            if str(data['beam_stop']).upper() == 'OPEN':
                beam_stop = str(True)
            elif str(data['beam_stop']).upper() == 'CLOSED':
                beam_stop = str(False)
            else:
                raise CdbPermanentError(
                    "Value for beam_stop must be 'OPEN' or 'CLOSED' not "
                    + str(data['beam_stop']))
                
            xml = ("<tag name='" + str(tag)
                       + "' beamStop='" + beam_stop
                       + "' diffuserThickness='" 
                       + str(data['diffuser_thickness'])
                       + "' protonAbsorberThickness='" 
                       + str(data['proton_absorber_thickness'])
                       + "' >")
            if magnets != None:
                for magnet in magnets:
                    xml = (xml + "<magnet name='" + str(magnet['name'])
                               + "' setCurrent='" + str(magnet['current'])
                               + "'/>")
            xml = xml + "</tag>"
        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))
        return_xml = str(self._server.setBeamlineTag(str(xml)))
        parseString(return_xml, self._status_handler)
        return self._status_handler.get_message()

