"Mimic calls to suds.client."
# pylint: disable-msg=C0103
# pylint: disable-msg=W0613
# pylint: disable-msg=R0903
# pylint: disable-msg=R0904

from re import search
from urllib2 import URLError
from httplib import InvalidURL

from . import _xml

class Client():
    "Mimic suds.client Client class."

    def __init__(self, url):
        if search('URLError$', url):
            raise URLError("")
        elif search('TransportError$', url):
            raise TransportError()
        elif search('ValueError$', url):
            raise ValueError()
        elif search('InvalidURL$', url):
            raise InvalidURL()
        else:
            self.service = _Service(url)
            self.factory = _Factory(url)
            
class _Factory():
    "Mimic a suds factory."
    def __init__(self, status):
        pass
            
    def create(self, obj):
        "Mimic a suds create."
        pass
            
            
class _Service():
    "Mimic a suds service."

    def __init__(self, status):
        if search('error$', status):
            self.status = 2
        elif search('warn$', status):
            self.status = 1
        elif search('ok$', status):
            self.status = 0
        elif search('URLErr$', status):
            self.status = 3
        elif search('TransportErr$', status):
            self.status = 4
        elif search('cabling$', status):
            self.status = 'cabling'
        elif search('calibration$', status):
            self.status = 'calibration'
        elif search('beamline$', status):
            self.status = 'beamline'
        elif search('coolingchannel$', status):
            self.status = 'coolingchannel'
        elif search('baseError1$', status):
            self.status = 'baseError1'
        elif search('baseError2$', status):
            self.status = 'baseError2'
        else:
            self.status = 0           

    def getStatus(self):
        """Mimic soap call getStatus. Return a status dependent on how the class
        was initialised."""
        if self.status == 0:
            return _xml.STATUS_OK
        elif self.status == 1:
            return _xml.STATUS_WARN
        elif self.status == 2:
            return _xml.STATUS_ERROR
        elif self.status == 'baseError1':
            raise TransportError()
        elif self.status == 'baseError2':
            return _xml.STATUS_DUFF
                
    def getName(self):
        """Mimic soap call getName."""
        if self.status == 0:
            return _xml.SERVER_NAME
        elif self.status == 3:
            raise URLError("")
        elif self.status == 4:
            raise TransportError()
        return self.getStatus()
        
    def listDevices(self):
        "Mimic soap call listDevices."
        if self.status == 'cabling':
            return _xml.CAB_DEVICES
        elif self.status == 'calibration':
            return _xml.CAL_DEVICES
        return self.getStatus()
    
# ALARMHANDLER
    def getTaggedALH(self, tag):
        "Mimic soap call getTaggedALH."
        if self.status == 0:
            return _xml.ALH_TAGGED_ALH
        return self.getStatus()

    def getUsedALH(self, timestamp):
        "Mimic soap call getUsedALH."
        if self.status == 0:
            return _xml.ALH_USED_ALH
        return self.getStatus()

    def getUsedTags(self, start_time, stop_time):
        "Mimic soap call getUsedTags."
        if self.status == 0:
            return _xml.ALH_USED_TAGS
        return self.getStatus()

    def listTags(self):
        "Mimic soap call listTags."
        if self.status == 'beamline':
            return _xml.BL_LIST_TAGS
        elif self.status == 'coolingchannel':
            return _xml.CC_LIST_TAGS
        elif self.status == 0:
            return _xml.ALH_LIST_TAGS
        return self.getStatus()
    
    def setTaggedALH(self, tag, alarms):
        "Mimic soap call setTaggedALH."
        return self.getStatus()
    
    def setTagInUse(self, tag, creation_time):
        "Mimic soap call setTagInUse."
        return self.getStatus()

# BATCHITERATION
    def getDataRecord(self, iteration):
        if self.status == 0:
            if(iteration ==1 ):
             return _xml.BI_DATARECORD
            else:
             return _xml.BI_NOSUCHRECORD
        return self.getStatus()

    def getRecoDataCards(self, iteration):
        if self.status == 0:
            if(iteration ==1 ):
             return _xml.BI_RECORECORD
            else:
             return _xml.BI_NOSUCHRECORD
        return self.getStatus()

    def getMCDataCards(self, iteration):
        if self.status == 0:
            if(iteration ==1 ):
             return _xml.BI_MCRECORD
            else:
             return _xml.BI_NOSUCHRECORD
        return self.getStatus()

    def getComment(self, iteration):
        if self.status == 0:
            if(iteration ==1 ):
             return _xml.BI_COMMENT
            else:
             return _xml.BI_NOSUCHRECORD
        return self.getStatus()

    def setDataCards(self, comment, reco, mc):
        if( self.status == 0):
            return _xml.BI_INSERT_SUCCESS

        return self.getStatus()
# BEAMLINE
    def getAllBeamlines(self):
        "Mimic soap call getAllBeamlines."
        if self.status == 0:
            return _xml.BL_RUNS
        return self.getStatus()

    def getBeamlinesForDates(self, start_time, stop_time):
        "Mimic soap call getBeamlinesForDates."
        if self.status == 0:
            return _xml.BL_DATES
        return self.getStatus()

    def getBeamlinesForPulses(self, start_pulse, stop_pulse):
        "Mimic soap call getBeamlinesForPulses."
        if self.status == 0:
            return _xml.BL_PULSES
        return self.getStatus()

    def getBeamlineForRun(self, run_number):
        "Mimic soap call getBeamlineForRun."
        if self.status == 0:
            return _xml.BL_RUN
        return self.getStatus()
    
    def getBeamlineForTag(self, run_number):
        "Mimic soap call getBeamlineForTag."
        if self.status == 0:
            return _xml.BL_TAG
        return self.getStatus()
    
    def setStartRun(self, xml):
        "Mimic soap call setStartRun."
        return self.getStatus()
    
    def setEndRun(self, xml):
        "Mimic soap call setEndRun."
        return self.getStatus()
    
    def setBeamline(self, xml):
        "Mimic soap call setBeamline."
        return self.getStatus()
      
    def setBeamlineTag(self, xml):
        "Mimic soap call setBeamlineTag."
        return self.getStatus()
      
# CABLING
    def getCurrentCabling(self, device):
        "Mimic soap call getCurrentCabling."
        if self.status == 0:
            if device == "Controls":
                return _xml.CAB_CURRENT_CABLING_CONTROLS
            else:
                return _xml.CAB_CURRENT_CABLING_TRACKER
        return self.getStatus()
    
    def getCablingForDate(self, device, timestamp):
        "Mimic soap call getCablingForDate."
        if self.status == 0:
            return _xml.CAB_CURRENT_CABLING_CONTROLS
        return self.getStatus()

    def getCablingForRun(self, device, run):
        "Mimic soap call getCablingForRun."
        if self.status == 0:
            return _xml.CAB_CURRENT_CABLING_CONTROLS
        return self.getStatus()

    def setDetector(self, device, calibration_type, valid_from_time, data=""):
        "Mimic soap call setDetector."
        return self.getStatus()
    
    def getDetectorCablingForDate(self, device, timestamp):
        "Mimic soap call getDetectorCablingForDate."
        if self.status == 0:
            if device == "Ckov A":
                return _xml.CAB_B64
            else:
                return
        if device == "Ckov A":
            return self.get_b64_status()
        else:
            return self.getStatus()
            
    def getDetectorCablingForRun(self, device, run_number):
        "Mimic soap call getDetectorCablingForRun."
        if self.status == 0:
            if device == "Ckov A":
                return _xml.CAB_B64
            else:
                return
        if device == "Ckov A":
            return self.get_b64_status()
        else:
            return self.getStatus()
            
    def getCurrentDetectorCabling(self, device):
        "Mimic soap call getCurrentDetectorCabling."
        if self.status == 0:
            if device == "Ckov A":
                return _xml.CAB_B64
            else:
                return
        if device == "Ckov A":
            return self.get_b64_status()
        else:
            return self.getStatus()      
    
    def getCablingIds(self, start_time, stop_time):
        "Mimic soap call getCablingIds."
        if self.status == 0:
            return _xml.CAB_IDS
        return self.getStatus()
    
    def getDetectorCablingForId(self, id_):
        "Mimic soap call getDetectorCablingForId."
        if self.status == 0:
            return _xml.CAB_B64
        return self.get_b64_status()   
     
# CALIBRATION
    def getCurrentCalibration(self, device):
        "Mimic soap call getCurrentCalibration."
        if self.status == 0:
            return _xml.CAL_CALIBRATION_TRACKER
        return self.getStatus()
    
    def getCalibrationForDate(self, device, timestamp):
        "Mimic soap call getCalibrationForDate."
        if self.status == 0:
            return _xml.CAL_CALIBRATION_TRACKER
        return self.getStatus()

    def getCalibrationForRun(self, device, crate):
        "Mimic soap call getCalibrationForRun."
        if self.status == 0:
            return _xml.CAL_CALIBRATION_TRACKER
        return self.getStatus()
        
    def setTracker(self, device, data):
        "Mimic soap call setTracker."
        return self.getStatus()
    
    def getCurrentDetectorCalibration(self, device, type_):
        "Mimic soap call getCurrentDetectorCalibration."
        if self.status == 0:
            return _xml.CAL_B64
        return self.get_b64_status()
    
    def getDetectorCalibrationForDate(self, device, type_, timestamp):
        "Mimic soap call getDetectorCalibrationForDate."
        if self.status == 0:
            return _xml.CAL_B64
        return self.get_b64_status()

    def getDetectorCalibrationForRun(self, device, type_, crate):
        "Mimic soap call getDetectorCalibrationForRun."
        if self.status == 0:
            return _xml.CAL_B64
        return self.get_b64_status()
    
    def getDetectorCalibrationForId(self, id_):
        "Mimic soap call getDetectorCalibrationForId."
        if self.status == 0:
            return _xml.CAL_B64
        return self.get_b64_status()   
        
    def getCalibrationIds(self, start_time, stop_time):
        "Mimic soap call getCalibrationIds."
        if self.status == 0:
            return _xml.CAL_IDS
        return self.getStatus()
        
# CONTROL
    def getControls(self):
        "Mimic soap call getControls."
        if self.status == 0:
            return _xml.C_CONTROLS
        return self.getStatus()

    def getControlsForCrate(self, crate):
        "Mimic soap call getControlsForCrate."
        if self.status == 0:
            return _xml.C_CONTROLS_FOR_CRATE
        return self.getStatus()
    
    def getControlsForChannel(self, crate, slot, channel):
        "Mimic soap call getControlsForChannel."
        if self.status == 0:
            return _xml.C_CONTROLS_FOR_CRATE
        return self.getStatus()

    def getPreviousSettings(self, timestamp):
        "Mimic soap call getPreviousSettings."
        if self.status == 0:
            return _xml.C_CONTROLS_FOR_PREVIOUS
        return self.getStatus()
    
    def addControl(self, crate, module, channel, name):
        "Mimic soap call addControl."
        return self.getStatus()
    
    def updateControl(self, crate, module, channel, name):
        "Mimic soap call updateControl."
        return self.getStatus()
       
    def setParameter(self, crate, module, channel, parameter_name,
                      parameter_value):
        # pylint: disable-msg=R0913
        "Mimic soap call setParameter."
        return self.getStatus()
    
    def updateParameter(self, crate, module, channel, parameter_name,
                      parameter_value):
        # pylint: disable-msg=R0913
        "Mimic soap call updateParameter."
        return self.getStatus()

# COOLING CHANNEL
    def getAllCoolingchannels(self):
        "Mimic soap call getAllCoolingchannels."
        if self.status == 0:
            return _xml.CC_ALL
        return self.getStatus()
    
    def getCoolingchannelForDate(self, date):
        "Mimic soap call getCoolingchannelForDate."
        if self.status == 0:
            return _xml.CC_DATE
        return self.getStatus()
    
    def getCoolingchannelForRun(self, run):
        "Mimic soap call getCoolingchannelForRun."
        if self.status == 0:
            return _xml.CC_RUN
        return self.getStatus()
        
    def getCoolingchannelForTag(self, tag):
        "Mimic soap call getCoolingchannelForTag."
        if self.status == 0:
            if tag == 1:
                return _xml.CC_ERROR_1
            elif tag == 2:
                return _xml.CC_ERROR_2
            else:
                return _xml.CC_TAG
        return self.getStatus()

    def getCoolingchannelAbsorberForTag(self, tag):
        if self.status == 0:
            return _xml.CC_ABS_TAG
        return self.getStatus()

    def getCoolingchannelAbsorberForRun(self, run):
        if self.status == 0:
            return _xml.CC_ABS  # run number 5624 is fixed in the XML
        return self.getStatus()

    def listAbsorberTags(self):
        if self.status == 0:
            return _xml.CC_LIST_ABS_TAGS
        return self.getStatus()

    def setCoolingchannel(self, xml):
        "Mimic soap call setCoolingchannel."
        return self.getStatus()

    def setCoolingchannelTag(self, xml):
        "Mimic soap call setCoolingchannelTag."
        return self.getStatus()

    def setCoolingchannelAbsorber(self, xml):
        "Mimic soap call setCoolingchannelAbsorber."
        return self.getStatus()

    def setCoolingchannelAbsorberTag(self, xml):
        "Mimic soap call setCoolingchannelAbsorberTag."
        return self.getStatus()
# GEOMETRY
    def get_b64_status(self):
        """Mimic soap call getStatus. Return a status dependent on how the class
        was initialised."""
        if self.status == 0:
            return _xml.G_STATUS_OK
        elif self.status == 1:
            return _xml.G_STATUS_WARN
        elif self.status == 2:
            return _xml.G_STATUS_ERROR

    def getCurrentGDML(self):
        "Mimic soap call getCurrentGDML."
        if self.status == 0:
            return _xml.G_GDML_CURRENT
        return self.get_b64_status()

    def getGDMLForId(self, id_):
        "Mimic soap call getGDMLForId."
        if self.status == 0:
            return _xml.G_GDML_FOR_ID
        return self.get_b64_status()

    def getGDMLForRun(self, run):
        "Mimic soap call getGDMLForRun."
        if self.status == 0:
            return _xml.G_GDML_FOR_RUN
        return self.get_b64_status()

    def getIds(self, start_time, stop_time):
        "Mimic soap call getIds."
        if self.status == 0:
            return _xml.G_IDS
        return self.getStatus()
    
    def setGDML(self, gdml, valid_from_time, notes="",
                technical_drawing_name=""):
        "Mimic soap call setGDML."
        return self.getStatus()

    def getGeometryCorrectionsForRun(self, run):
        if run == 0:
            return _xml.G_CORR_BAD
        if self.status == 0:
            return _xml.G_CORR
        return self.getStatus()

    def getGeometryCorrectionsForGeometryId(self, id):
        if id == 0:
            return _xml.G_CORR_BAD
        if self.status == 0:
            return _xml.G_CORR
        return self.getStatus()


    def setCorrections(self, modules, gid, run1, run2):
        if self.status == 0:
            return "<ok>Geometry Corrections stored</ok>"
        return self.getStatus()

# MC SERIAL NUMBER

    def getDataCards(self, serial):
        if self.status == 0:
            return _xml.MC_SERIAL
        return self.getStatus()

    def getSWVersion(self, serial):
        if self.status == 0:
            return _xml.MC_SW_VER
        return self.getStatus()

    #def getComment(self, serial):  conflict with B.I.N getComment()
    #    if self.status == 0:
    #        return _xml.MC_COMMENT
    #    return self.getStatus()

# QUALITY FLAGS
    def getReconstructionFlags(self,run_number, maus_version, batch_iteration_number):
        if self.status == 0:
            if run_number == 0 :
                return _xml.DQ_FLAGS01
            else:
               return _xml.DQ_FLAGS0
        return self.getStatus()

    def setReconstructionFlags(self, run_number, maus_version, batch_iteration_number, flags):
        return self.getStatus()

# STATEMACHINE
    def getAllowedTransitions(self):
        "Mimic soap call getAllowedTransitions."
        if self.status == 0:
            return _xml.SM_ALLOWED_TRANS
        return self.getStatus()
    
    def getCurrentState(self, system):
        "Mimic soap call getCurrentState."
        if self.status == 0:
            return _xml.SM_CURRENT
        return self.getStatus()
    
    def getCurrentStateMachine(self):
        "Mimic soap call getCurrentStateMachine."
        if self.status == 0:
            return _xml.SM_CURRENT_SM
        return self.getStatus()
    
    def getStateMachineForDate(self, timestamp):
        "Mimic soap call getStateMachineForDate."
        if self.status == 0:
            return _xml.SM_FOR_DATE
        return self.getStatus()

    def getStateMachineForRun(self, run):
        "Mimic soap call getStateMachineForRun."
        if self.status == 0:
            return _xml.SM_FOR_RUN
        return self.getStatus()
    
    def getPVData(self, system, state):
        "Mimic soap call getPVData."
        if self.status == 0:
            return _xml.SM_PV_DATA
        return self.getStatus()
    
    def setState(self, system, state):
        "Mimic soap call setState."
        return self.getStatus()
    
    def setPVData(self, system, state, pvData):
        "Mimic soap call setPVData."
        return self.getStatus()
     
# TARGET
    def get_target_status(self):
        """Mimic soap call getStatus. Return a status dependent on how the class
        was initialised."""
        if self.status == 0:
            return _xml.G_STATUS_OK
        elif self.status == 1:
            return _xml.G_STATUS_WARN
        elif self.status == 2:
            return _xml.G_STATUS_ERROR
        
    def getBlobForDate(self, name, timestamp):
        "Mimic soap call getBlobForDate."
        if self.status == 0:
            return _xml.T_BLOB_FOR_DATE
        return self.get_target_status()
    
    def getBlobForRun(self, name, run):
        "Mimic soap call getBlobForRun."
        if self.status == 0:
            return _xml.T_BLOB_FOR_RUN
        return self.get_target_status()
    
    def getCurrentBlob(self, name):
        "Mimic soap call getCurrentBlob."
        if self.status == 0:
            return _xml.T_BLOB_CURRENT
        return self.get_target_status()
    
    def addBlob(self, name, blob):
        "Mimic soap call addBlob."
        return self.getStatus()
    
    def getTargetNames(self):
        "Mimic soap call getTargetNames."
        if self.status == 0:
            return _xml.T_TARGET_NAMES
        return self.get_target_status()

class TransportError(Exception):
    "Mimic suds TransportError class."

    def __init__(self):
        super(TransportError, self).__init__()

