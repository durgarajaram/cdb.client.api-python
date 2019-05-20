"XML used to mimic soap responses."

from base64 import b64encode

STATUS_OK = "<ok>feeling good</ok>"
STATUS_WARN = "<warning>a bit poorly</warning>"
STATUS_ERROR = "<error>dead</error>"
STATUS_DUFF = "<duff>beer</duff>"
SERVER_NAME = "<serverName>Mock SUDS</serverName>"

G_STATUS_OK = b64encode("<ok>feeling good</ok>")
G_STATUS_WARN = b64encode("<warning>a bit poorly</warning>")
G_STATUS_ERROR = b64encode("<error>dead</error>")

ALH_TAGGED_ALH = """<alarmhandler creationtime='2011-02-09 08:56:18.616'
tag='tagged_alh'><alarm><name>A1</name><hihi>20.0</hihi><hi>15.0</hi>
<lo>5.0</lo><lolo>0.0</lolo></alarm><alarm><name>A2</name><hihi>105.0</hihi>
<hi>104.0</hi><lo>102.0</lo><lolo>101.0</lolo></alarm></alarmhandler>"""

ALH_USED_ALH = """<alarmhandler creationtime='2011-02-09 08:56:18.616'
tag='used_alh'><alarm><name>A1</name><hihi>20.0</hihi><hi>15.0</hi><lo>5.0</lo>
<lolo>0.0</lolo></alarm><alarm><name>A2</name><hihi>105.0</hihi><hi>104.0</hi>
<lo>102.0</lo><lolo>101.0</lolo></alarm></alarmhandler>"""

ALH_USED_TAGS = """<tags><tag starttime='2011-02-09 08:56:18.477' name='Harry'/>
<tag starttime='2011-02-09 08:56:18.502' name='Harry'/>
<tag starttime='2011-02-09 08:56:18.522' name='Fred'/>
<tag starttime='2011-02-09 08:56:18.544' name='Harry'/>
<tag starttime='2011-02-09 08:56:18.568' name='Harry'/>
<tag starttime='2011-02-09 08:56:18.588' name='Harry'/>
<tag starttime='2011-02-09 08:56:18.61' name='Harry'/>
<tag starttime='2011-02-09 08:56:18.644' name='Harry'/></tags>"""

ALH_LIST_TAGS = """<tags><tag name='tag1'/><tag name='tag2'/></tags>"""


BI_DATARECORD = """<batchiteration><recodatacards> reco data </recodatacards><mcdatacards> mac data</mcdatacards>
<comment>changed comment</comment><creationtime>2014-03-07 18:00:26.271</creationtime></batchiteration>
"""
BI_RECORECORD = """<batchiteration><recodatacards> reco data </recodatacards></batchiteration>"""
BI_MCRECORD = """<batchiteration><mcdatacards> mc data </mcdatacards></batchiteration>"""
BI_COMMENT = """<batchiteration><comment>changed comment</comment></batchiteration>"""

BI_NOSUCHRECORD = """<error>SELECT * returned no rows for batchiteration number = 2</error>"""
BI_INSERT_SUCCESS = """<ok>SetDataCards - INSERT - Success !</ok> """
BI_INSERT_FAILURE = """<error>Duplicate Record !</error>"""

BL_DATES = """<runs><run runNumber='1' startTime='2001-01-22 15:01:40.339916'
endTime='2001-01-22 15:01:45.339916' startNotes='nd' optics='od'
protonAbsorberThickness='55' startPulse='1110' endPulse='1120' step='12.3'
status='false' runType='cosmic' daqTrigger='TOF1' daqGateWidth='110.0'
daqVersion='DATES' beamStop='false' diffuserThickness='30'
endNotes='en1'><ldcHost name='host1'/><ldcHost name='host2'/>
<magnet name='q11' setCurrent='19.4' polarity='1'/><magnet
name='q12' setCurrent='19.7' polarity='-1'/><scalar name='s1'
value='11'/><scalar name='s2' value='22'/></run><run runNumber='2'
startTime='2002-02-22 15:01:40.339916' endTime='2002-02-22 15:01:45.339916'
startNotes='null' optics='null' protonAbsorberThickness='55' startPulse='2110'
endPulse='2120' step='22.3' status='true' runType='test' daqTrigger='TOF2'
daqGateWidth='210.0' daqVersion='no' beamStop='true' diffuserThickness='31'
endNotes='en2'><ldcHost name='host1'/><ldcHost name='host2'/>
<magnet name='q21' setCurrent='29.4' polarity='1'/><magnet
name='q22' setCurrent='29.7' polarity='-1'/><scalar name='s3'
value='33'/><scalar name='s4' value='44'/></run></runs>
"""

BL_PULSES = """<runs><run runNumber='1' startTime='2001-01-22 15:01:40.339916'
endTime='2001-01-22 15:01:45.339916' startNotes='note1' optics='optic1'
protonAbsorberThickness='55' startPulse='1110' endPulse='1120' step='12.3'
status='false' runType='cosmic' daqTrigger='TOF1'
daqGateWidth='110.0' daqVersion='PULSES' beamStop='true'
diffuserThickness='32' endNotes='en1'><ldcHost name='host1'/><ldcHost name='host2'/>
<magnet name='q11' setCurrent='19.4'
polarity='1'/><magnet name='q12' setCurrent='19.7'
polarity='-1'/></run><run runNumber='2' startTime='2002-02-22
15:01:40.339916' endTime='2002-02-22 15:01:45.339916' startNotes='null' optics='null'
protonAbsorberThickness='55' startPulse='2110' endPulse='2120' step='22.3'
status='true' runType='test' daqTrigger='TOF2'
daqGateWidth='210.0' daqVersion='no' beamStop='false'
diffuserThickness='33' endNotes='en2'><ldcHost name='host1'/><ldcHost name='host2'/>
<magnet name='q21' setCurrent='29.4'
polarity='1'/><magnet name='q22' setCurrent='29.7'
polarity='-1'/></run></runs>
"""

BL_RUNS = """<runs><run runNumber='5' startTime='2001-01-22 15:01:40.339916'
endTime='2001-01-22 15:01:45.339916' startNotes='run 5' optics='optics5'
protonAbsorberThickness='55' startPulse='1110' endPulse='1120' step='12.3'
status='false' runType='cosmic' daqTrigger='TOF1'
daqGateWidth='110.0' daqVersion='RUNS' targetDepth='13.1' targetDelay='10.0'
targetDriveVoltage='14.2' beamStop='true' diffuserThickness='34' endNotes='en1'>
<ldcHost name='host1'/><ldcHost name='host2'/><magnet
name='q11' setCurrent='19.4' polarity='1'/><magnet name='q12'
setCurrent='19.7' polarity='-1'/></run><run runNumber='6'
startTime='2002-02-22 15:01:40.339916' endTime='2002-02-22 15:01:45.339916'
startNotes='run 6' optics='null' protonAbsorberThickness='55' startPulse='2110'
endPulse='2120' step='22.3' status='true'
runType='test' daqTrigger='TOF2'
daqGateWidth='210.0' daqVersion='no' beamStop='false'
diffuserThickness='35' endNotes='en2'><ldcHost name='host1'/><ldcHost name='host2'/>
<magnet name='q21' setCurrent='29.4'
polarity='1'/><magnet name='q22' setCurrent='29.7'
polarity='-1'/></run></runs>
"""

BL_RUN = """<runs><run runNumber='1' startTime='2001-01-22 15:01:40.339916'
endTime='2001-01-22 15:01:45.339916' startNotes='run1' optics='opt1'
protonAbsorberThickness='55' startPulse='1110' endPulse='1120' step='12.3'
status='false' runType='cosmic' daqTrigger='TOF1'
daqGateWidth='110.0' daqVersion='RUN' beamStop='true'
diffuserThickness='36' endNotes='en1'><ldcHost name='host1'/><ldcHost name='host2'/>
<isisBeam name='one' mean='2' sigma='3'/><isisBeam name='four' mean='5' sigma='6'/>
<magnet name='q11' setCurrent='19.4'
polarity='1'/><magnet name='q12' setCurrent='19.7'
polarity='-1'/></run></runs>
"""

BL_TAG = """<tags><tag name='1' protonAbsorberThickness='55' beamStop='true'
diffuserThickness='36'><magnet name='q11' setCurrent='19.4'
polarity='1'/><magnet name='q12' setCurrent='19.7' polarity='-1'/></tag></tags>
"""

BL_LIST_TAGS = """<tagNames><tag name='1'/><tag name='2'/></tagNames>"""

CAB_CURRENT_CABLING_CONTROLS = """
<cabling type='CONTROL'>
<crate number='2'>
<module number='1'>
<channel number='4' name='a4'/>
<channel number='5' name='a5'/>
</module>
<module number='2'>
<channel number='6' name='b6'/> 
<channel number='7' name='b7'/> 
</module> 
</crate>
<crate number='3'>
<module number='33'>
<channel number='333' name='a333'/>
<channel number='3333' name='a3333'/>
</module> 
</crate>
</cabling> 
"""

CAB_CURRENT_CABLING_TRACKER = """
<cabling type='TRACKER'>
<vlsbComputerId number='1'> 
<vlsbGeoNumber number='2'> 
<vlsbChannel number='3' trackerNumber='4' station='5' plane='6' channel='7'/> 
<vlsbChannel number='8' trackerNumber='9' station='10' plane='11' channel='12'/> 
</vlsbGeoNumber> 
<vlsbGeoNumber number='13'> 
<vlsbChannel number='14' trackerNumber='15' station='16' plane='17' channel='18'/> 
<vlsbChannel number='19' trackerNumber='20' station='21' plane='22' channel='23'/> 
</vlsbGeoNumber> 
</vlsbComputerId>
<vlsbComputerId number='24'> 
<vlsbGeoNumber number='25'> 
<vlsbChannel number='26' trackerNumber='27' station='28' plane='29' channel='30'/> 
<vlsbChannel number='31' trackerNumber='32' station='33' plane='34' channel='35'/> 
</vlsbGeoNumber>
</vlsbComputerId>
</cabling> 
"""

CAB_DEVICES = """<cabling>
<deviceList>
<device name='CONTROL'/>
<device name='CKOV A'/>
<device name='CKOV B'/>
<device name='EMR'/>
<device name='KL'/>
<device name='SCALERS'/>
<device name='TOF0'/>
<device name='TOF1'/>
<device name='TOF2'/>
</deviceList>
</cabling> """


CAB_B64 = b64encode("CAB B64")

CAB_IDS = """<ids>
<id name='1' validFrom='2001-01-01 01:02:03' created='2001-01-01 01:02:04' 
device='mouse wheel' />
<id name='2' validFrom='2002-01-01 01:02:03' created='2002-01-01 01:02:04' 
device='mouse wheel'/>
</ids>"""

CAL_CALIBRATION_TRACKER = """
<calibration type='TRACKER'>
<board number='1'>
<bank number='2'> 
<channel number='3' adcPedestal='4' adcGain='5' tdcPedestal='6' tdcSlope='7'/> 
<channel number='8' adcPedestal='9' adcGain='10' tdcPedestal='11' tdcSlope='12'/> 
</bank> 
<bank number='13'> 
<channel number='14' adcPedestal='15' adcGain='16' tdcPedestal='17' tdcSlope='18'/> 
<channel number='19' adcPedestal='20' adcGain='21' tdcPedestal='22' tdcSlope='23'/> 
</bank> 
</board>
</calibration>
"""

CAL_DEVICES = """<calibration>
<deviceList>
<device name='CKOV A'/>
<device name='CKOV B'/>
<device name='EMR'/>
<device name='KL'/>
<device name='SCALERS'/>
<device name='TOF0'/>
<device name='TOF1'/>
<device name='TOF2'/>
</deviceList>
</calibration> """

CAL_B64 = b64encode("CAL B64")

CAL_IDS = """<ids>
<id name='1' validFrom='2001-01-01 01:02:03' created='2001-01-01 01:02:04' 
device='mouse wheel' type='random'/>
<id name='2' validFrom='2002-01-01 01:02:03' created='2002-01-01 01:02:04' 
device='mouse wheel' type='spanner'/>
</ids>"""

C_CONTROLS = """
<controls>
<crate name='1' rack='HV Rack 1'>
<channel name='0' module='0' remoteChannelName='n_1'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1700.0'/>
</channel>
<channel name='1' module='0' remoteChannelName='n_2'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1700.0'/>
</channel>
<channel name='2' module='0' remoteChannelName='n_3'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
</crate>
<crate name='2' rack='HV Rack 1'>
<channel name='3' module='1' remoteChannelName='n_4'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
<channel name='4' module='1' remoteChannelName='n_5'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
</crate>
</controls>
"""

C_CONTROLS_FOR_CRATE = """
<controls>
<crate name='3' rack='HV Rack 1'>
<channel name='0' module='0' remoteChannelName='n_1'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1700.0'/>
</channel>
<channel name='1' module='0' remoteChannelName='n_2'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1700.0'/>
</channel>
<channel name='2' module='0' remoteChannelName='n_3'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
</crate>
</controls>"""

C_CONTROLS_FOR_PREVIOUS = """
<controls>
<crate name='4' rack='HV Rack 1'>
<channel name='0' module='0' remoteChannelName='n_1'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1700.0'/>
</channel>
<channel name='1' module='0' remoteChannelName='n_2'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1700.0'/>
</channel>
<channel name='2' module='0' remoteChannelName='n_3'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
</crate>
<crate name='5' rack='HV Rack 1'>
<channel name='3' module='1' remoteChannelName='n_4'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
<channel name='4' module='1' remoteChannelName='n_5'>
<parameter name='ILim' value='600.0'/>
<parameter name='On/Off' value='0'/>
<parameter name='RmpDn' value='100'/>
<parameter name='RmpUp' value='100'/>
<parameter name='Trip' value='10'/>
<parameter name='VSet' value='1750.0'/>
</channel>
</crate>
</controls>
"""
CC_ALL = """<coolingchannels><coolingchannel validfromtime='2013-05-15
10:48:10.067' validuntiltime='2013-05-15 10:48:45.081'><magnets><magnet
name='mag1' mode='flip' polarity='1'><coil name='coil1' calibration='1.1'
ilim='1.2' iset='1.3' rate='1.4' stability='1.5' vlim='1.6'/><coil name='coil2'
calibration='2.1' ilim='2.2' iset='2.3' rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 10:48:45.081' validuntiltime='2013-05-15
10:55:58.297'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 10:55:58.297' validuntiltime='2013-05-15
11:22:49.437'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 11:22:49.437' validuntiltime='2013-05-15
11:28:24.534'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 11:28:24.534' validuntiltime='2013-05-15
11:29:21.06'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 11:29:21.06' validuntiltime='2013-05-15
11:29:37.562'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 11:29:37.562' validuntiltime='2013-05-15
11:29:40.308'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 11:29:40.308' validuntiltime='2013-05-15
11:30:48.357'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 11:30:48.357' validuntiltime='2013-05-15
13:24:35.36'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:24:35.36' validuntiltime='2013-05-15
13:30:45.109'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:30:45.109' validuntiltime='2013-05-15
13:32:54.877'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:32:54.877' validuntiltime='2013-05-15
13:37:12.955'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:37:12.955' validuntiltime='2013-05-15
13:38:53.366'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:38:53.366' validuntiltime='2013-05-15
13:41:28.768'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:41:28.768' validuntiltime='2013-05-15
13:42:25.385'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:42:25.385' validuntiltime='2013-05-15
13:43:49.577'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:43:49.577' validuntiltime='2013-05-15
13:45:16.219'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:45:16.219' validuntiltime='2013-05-15
13:50:28.224'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:50:28.224' validuntiltime='2013-05-15
13:51:05.172'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 13:51:05.172' validuntiltime='2013-05-15
14:01:03.467'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:01:03.467' validuntiltime='2013-05-15
14:06:05.559'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:06:05.559' validuntiltime='2013-05-15
14:08:29.663'><magnets><magnet name='mag1' mode='flip' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:08:29.663' validuntiltime='2013-05-15
14:08:58.021'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:08:58.021' validuntiltime='2013-05-15
14:10:52.699'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:10:52.699' validuntiltime='2013-05-15
14:44:09.954'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:44:09.954' validuntiltime='2013-05-15
14:46:12.89'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:46:12.89' validuntiltime='2013-05-15
14:47:05.431'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:47:05.431' validuntiltime='2013-05-15
14:47:57.136'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:47:57.136' validuntiltime='2013-05-15
14:48:58.941'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:48:58.941' validuntiltime='2013-05-15
14:50:34.154'><magnets><magnet name='mag1' mode='flip1' polarity='1'><coil
name='coil1' calibration='1.1' ilim='1.2' iset='1.3' rate='1.4' stability='1.5'
vlim='1.6'/><coil name='coil2' calibration='2.1' ilim='2.2' iset='2.3'
rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 14:50:34.154' validuntiltime='2013-05-15
15:04:49.116'><magnets><magnet name='mag2' mode='flip2' polarity='-1'><coil
name='coil3' calibration='3.1' ilim='3.2' iset='3.3' rate='3.4' stability='3.5'
vlim='3.6'/><coil name='coil4' calibration='4.1' ilim='4.2' iset='4.3'
rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 15:04:49.116' validuntiltime='2013-05-15
15:15:26.325'><magnets><magnet name='mag2' mode='flip2' polarity='-1'><coil
name='coil3' calibration='3.1' ilim='3.2' iset='3.3' rate='3.4' stability='3.5'
vlim='3.6'/><coil name='coil4' calibration='4.1' ilim='4.2' iset='4.3'
rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel><coolingchannel
validfromtime='2013-05-15 15:15:26.325' validuntiltime='null'><magnets><magnet
name='mag1' mode='flip1' polarity='1'><coil name='coil1' calibration='1.1'
ilim='1.2' iset='1.3' rate='1.4' stability='1.5' vlim='1.6'/><coil name='coil2'
calibration='2.1' ilim='2.2' iset='2.3' rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel></coolingchannels>"""

CC_DATE = """<coolingchannels><coolingchannel validfromtime='2013-05-15
14:50:34.154' validuntiltime='null'><magnets><magnet name='mag2' mode='flip2'
polarity='-1'><coil name='coil3' calibration='3.1' ilim='3.2' iset='3.3'
rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4' calibration='4.1'
ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel></coolingchannels>"""

CC_ERROR_1 = """<coolingchannels></coolingchannels>"""

CC_ERROR_2 = """<coolingchannels><coolingchannel validfromtime='2013-05-15
14:50:34.154' validuntiltime='null'></coolingchannel></coolingchannels>"""

CC_LIST_TAGS = """<tagNames><tag name='10'/><tag name='20'/></tagNames>"""

CC_RUN = """<coolingchannels><coolingchannel validfromtime='2013-05-15
15:19:08.269' validuntiltime='null'><magnets><magnet name='mag1' mode='flip1'
polarity='1'><coil name='coil1' calibration='1.1' ilim='1.2' iset='1.3'
rate='1.4' stability='1.5' vlim='1.6'/><coil name='coil2' calibration='2.1'
ilim='2.2' iset='2.3' rate='2.4' stability='2.5' vlim='2.6'/></magnet><magnet
name='mag2' mode='flip2' polarity='-1'><coil name='coil3' calibration='3.1'
ilim='3.2' iset='3.3' rate='3.4' stability='3.5' vlim='3.6'/><coil name='coil4'
calibration='4.1' ilim='4.2' iset='4.3' rate='4.4' stability='4.5'
vlim='4.6'/></magnet></magnets></coolingchannel></coolingchannels>"""

CC_TAG = """<coolingchannels><coolingchannel validfromtime='2013-05-15
15:15:26.344' validuntiltime='null'><magnets><magnet name='mag1' mode='flip1'
polarity='1'><coil name='coil1' calibration='1.1' ilim='1.2' iset='1.3'
rate='1.4' stability='1.5' vlim='1.6'/><coil name='coil2' calibration='2.1'
ilim='2.2' iset='2.3' rate='2.4' stability='2.5'
vlim='2.6'/></magnet></magnets></coolingchannel></coolingchannels>"""

CC_ABS_TAG=""" <tag name='navi_tag' validfromtime='2016-05-26 17:00:18.721' validuntiltime='null'>
<absorber name='test_abs_03' material='Ne' shape='cube' temperature='24.0' pressure='116.0' comment='vivere '/>
<absorber name='test_abs_02' material='He' shape='cube' temperature='22.0' pressure='118.0' comment='necesse est '/>
<absorber name='test_abs_01' material='vac' shape='cube' temperature='20.0' pressure='120.0' comment='navigare'/>
</tag>"""

CC_ABS=""" <absorbers run='5624'>
<absorber name='test_abs_03' material='Ne' shape='cube' temperature='24.0' pressure='116.0' comment='vivere '/>
<absorber name='test_abs_02' material='He' shape='cube' temperature='22.0' pressure='118.0' comment='necesse est '/>
<absorber name='test_abs_01' material='vac' shape='cube' temperature='20.0' pressure='120.0' comment='navigare'/>
</absorbers>"""


CC_LIST_ABS_TAGS="""<tagNames><tag name='navi_tag' /><tag name='navi_tag2' /></tagNames>"""

G_GDML_CURRENT = b64encode("GDML_CURRENT")

G_GDML_FOR_ID = b64encode("GDML_FOR_ID")

G_GDML_FOR_RUN = b64encode("GDML_FOR_RUN")

G_IDS = """<ids><id name='9' validFrom='2010-10-15 12:32:59.80'
created='2011-01-21 15:48:01.099' notes='fred' technicalDrawingName='v1.1'/><id
name='13' validFrom='2010-10-15 12:32:59.80' created='2011-01-21 15:48:52.615'
notes='tom' technicalDrawingName='v1.2'/><id name='17' validFrom='2010-10-15
12:32:59.80' created='2011-01-21 15:49:08.027' notes='dick'
technicalDrawingName='v1.3'/><id name='21' validFrom='2010-10-15 12:32:59.80'
created='2011-01-21 15:57:31.68' notes='harry' technicalDrawingName='v1.4'/><id
name='25' validFrom='2010-10-15 12:32:59.80' created='2011-01-21 16:06:45.675'
notes='sam' technicalDrawingName='v1.5'/></ids>"""

G_CORR_BAD="""<dummy/>"""
G_CORR="""<GeometryID value= '12' >
<ModuleName name= 'TOF0' dx='12.1' dx_err='0.01' dy='22.2' dy_err='0.02' dz='32.299' dz_err='0.03' dx_rot='0.11' dx_rot_err='0.011' dy_rot='0.12' dy_rot_err='0.021' dz_rot='0.13' dz_rot_err='0.031'/>
<ModuleName name= 'TRACKER0' dx='12.4' dx_err='0.001' dy='22.5' dy_err='0.002' dz='32.60' dz_err='0.003' dx_rot='0.14' dx_rot_err='0.0011' dy_rot='0.149' dy_rot_err='0.0021' dz_rot='0.14' dz_rot_err='0.0030'/>
</GeometryID>"""

DQ_FLAGS0='A1FF0'
DQ_FLAGS01 = 'A1FF0X' # not hex

MC_SERIAL="""<mcserialnumber><sw_version>MAUS_MC_dummy</sw_version><creationtime>2014-08-11 16:00:15.333</creationtime>
<comment> a comment</comment><datacards>test cards 1</datacards></mcserialnumber>"""

MC_SW_VER = """<mcserialnumber><sw_version>MAUS_MC_dummy</sw_version></mcserialnumber>"""
MC_COMMENT = """<mcserialnumber><comment> a comment</comment></mcserialnumber>"""

SM_CURRENT = "<state>ON</state>"

SM_ALLOWED_TRANS = """<stateMachine>
<system name='sys1' state='on1'/>
<system name='sys2' state='off2'/>
<system name='sys3' state='powered3'/>
</stateMachine>"""

SM_CURRENT_SM = """<stateMachine>
<system name='sys4' state='on4'/>
<system name='sys5' state='off5'/>
<system name='sys6' state='powered6'/>
</stateMachine>"""

SM_FOR_DATE = """<stateMachine>
<system name='sys7' state='on7'/>
<system name='sys8' state='off8'/>
<system name='sys9' state='powered9'/>
</stateMachine>"""

SM_FOR_RUN = """<stateMachine>
<system name='sys10' state='on10'/>
<system name='sys11' state='off11'/>
<system name='sys12' state='powered12'/>
</stateMachine>"""

SM_PV_DATA = """<pvdata>
<pv name='pv10' hihi='10' hi='9' lo='8' lolo='7' units='mm' transition='9.9999' mode='scan' autosms='true' frequency='9.8'/>
<pv name='pv11' hihi='20' hi='19' lo='18' lolo='17' units='cm' transition='19.9999' mode='scan2' autosms='false' deadband='4.2'/>
<pv name='pv12' hihi='30' hi='29' lo='28' lolo='27' units='m' transition='29.9999' mode='scan3' autosms='true' frequency='333.3' deadband='222.2'/>
</pvdata>"""

T_BLOB_CURRENT = b64encode("BLOB_CURRENT")

T_BLOB_FOR_DATE = b64encode("BLOB_FOR_DATE")

T_BLOB_FOR_RUN = b64encode("BLOB_FOR_RUN")

T_TARGET_NAMES = ['ISIS', 'R78', 'SHEFFIELD']
