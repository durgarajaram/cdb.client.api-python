"Constants for use with tests."
import datetime
import StringIO

VERSION = '1.1.6'

CLASS_LIST = ['AlarmHandler', 'Beamline', 'Cabling', 'Calibration', 'CdbError',
'CdbPermanentError', 'CdbTemporaryError','DataQuality', 'Geometry', 'MCSerialNumber','PIDCtrl', 'StateMachine',
'Target', 'self']

STATUS_OK = 'feeling good'
_BASE_STR = """\n\tset_url(string url)         
\tget_name()         
\tget_server_host_name()         
\tget_status()         
\tget_version()\n"""

ALH_STR = ("""AlarmHandler""" + 
_BASE_STR + 
"""\tget_tagged_alh(string tag)         
\tget_used_alh(datetime timestamp)         
\tget_used_tags(datetime start_time, datetime stop_time)         
\tlist_tags()""")

ALH_SM_STR = ("""AlarmHandlerSuperMouse""" + 
_BASE_STR + 
"""\tget_tagged_alh(string tag)         
\tget_used_alh(datetime timestamp)         
\tget_used_tags(datetime start_time, datetime stop_time)         
\tlist_tags()
\tset_tagged_alh(string tag, [{string name, string hihi, string hi,         
\t\tstring lo, string lolo}] alarms)         
\tset_tag_in_use(string tag, datetime creation_time)""")

ALH_TAGGED_ALH = ({'alarms': {'A1': {'lolo': 0.0, 'lo': 5.0, 'hi': 15.0, 'hihi':
20.0}, 'A2': {'lolo': 101.0, 'lo': 102.0, 'hi': 104.0, 'hihi': 105.0}}, 'tag':
'tagged_alh', 'creationtime': datetime.datetime(2011, 2, 9, 8, 56, 18, 616000)})

ALH_USED_ALH = ({'alarms': {'A1': {'lolo': 0.0, 'lo': 5.0, 'hi': 15.0, 'hihi':
20.0}, 'A2': {'lolo': 101.0, 'lo': 102.0, 'hi': 104.0, 'hihi': 105.0}}, 'tag':
'used_alh', 'creationtime': datetime.datetime(2011, 2, 9, 8, 56, 18, 616000)})

ALH_USED_TAGS = ({datetime.datetime(2011, 2, 9, 8, 56, 18, 644000): 'Harry',
datetime.datetime(2011, 2, 9, 8, 56, 18, 588000): 'Harry',
datetime.datetime(2011, 2, 9, 8, 56, 18, 568000): 'Harry',
datetime.datetime(2011, 2, 9, 8, 56, 18, 610000): 'Harry',
datetime.datetime(2011, 2, 9, 8, 56, 18, 522000): 'Fred',
datetime.datetime(2011, 2, 9, 8, 56, 18, 502000): 'Harry',
datetime.datetime(2011, 2, 9, 8, 56, 18, 544000): 'Harry',
datetime.datetime(2011, 2, 9, 8, 56, 18, 477000): 'Harry'})

ALH_LIST_TAGS = ['tag1', 'tag2']

ALH_SET_TAGGED_ALH = ([{'name': 'A1', 'lolo': 0.0, 'lo': 5.0, 'hi': 15.0,
'hihi': 20.0}, {'name': 'A2', 'lolo': 101.0, 'lo': 102.0, 'hi': 104.0, 'hihi':
105.0}])

BI_STR = ("""BatchIteration""" +
_BASE_STR +
"""\tget_datarecord(int iteration_number) \
        \n\tget_reco_datacards(int iteration_number)\
        \n\tget_mc_datacards(int iteration_number) \
        \n\tget_comment(int iteration_number)""")


BI_DATARECORD ={'comment': u'changed comment', 'reco': u' reco data ', 'mc': u' mac data'}
BI_RECORECORD ={'reco': u' reco data '}
BI_MCRECORD ={'mc': u' mc data '}
BI_COMMENT ={'comment': u'changed comment'}

BISM_STR=("""BatchIterationSuperMouse""" +
_BASE_STR +
 """\tget_datarecord(int iteration_number) \
        \n\tget_reco_datacards(int iteration_number)\
        \n\tget_mc_datacards(int iteration_number) \
        \n\tget_comment(int iteration_number) \
        \n\tset_datacards(int iteration_number, string comment, string reco_datacards, string mc_datacards)""")
# not quite right for now (above)
BISM_SET_DATACARDS_OK="SetDataCards - INSERT - Success !"

BL_STR = ("""Beamline""" + 
_BASE_STR + 
"""\tget_all_beamlines()         
\tget_all_beamlines_xml()         
\tget_beamline_for_run(int run_number)         
\tget_beamline_for_run_xml(int run_number)         
\tget_beamlines_for_dates(datetime start_time, datetime stop_time)         
\tget_beamlines_for_dates_xml(datetime start_time, datetime stop_time)         
\tget_beamlines_for_pulses(int start_pulse, int end_pulse)         
\tget_beamlines_for_pulses_xml(int start_pulse, int end_pulse)        
\tget_beamline_for_tag(str tag)        
\tlist_tags()""")

BL_SM_STR = ("""BeamlineSuperMouse""" + 
_BASE_STR + 
"""\tget_all_beamlines()         
\tget_all_beamlines_xml()         
\tget_beamline_for_run(int run_number)         
\tget_beamline_for_run_xml(int run_number)         
\tget_beamlines_for_dates(datetime start_time, datetime stop_time)         
\tget_beamlines_for_dates_xml(datetime start_time, datetime stop_time)         
\tget_beamlines_for_pulses(int start_pulse, int end_pulse)         
\tget_beamlines_for_pulses_xml(int start_pulse, int end_pulse)        
\tget_beamline_for_tag(str tag)        
\tlist_tags()
\tset_start_run(dict run_data)         
\tset_end_run(dict run_data, dict scalar_data)         
\tset_beamline(dict run_data, list(dict) magnets         
\tset_beamline_tag(str tag, dict data, list(dict) magnets""")

BL_DATES = {1L: {'status': False, 'beam_stop': 'Closed', 'run_type': 'cosmic',
'run_number': 1L, 'scalars': {'s1': 11, 's2': 22}, 'daq_trigger': 'TOF1',
'diffuser_thickness': 30, 'end_notes': 'en1', 'start_notes': 'nd', 'end_pulse':
1120L, 'proton_absorber_thickness': 55, 'daq_version': 'DATES', 'step': 12.3,
'daq_gate_width': 110.0, 'end_time': datetime.datetime(2001, 1, 22, 15, 1, 45,
339916), 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'],
'magnets': {'q11': {'polarity': 1, 'set_current':
19.4}, 'q12': {'polarity':-1, 'set_current': 19.7}}, 'start_pulse': 1110L,
'optics': 'od', 'start_time': datetime.datetime(2001, 1, 22, 15, 1, 40,
339916)}, 2L: {'status': True, 'beam_stop': 'Open', 'run_type': 'test',
'run_number': 2L, 'scalars': {'s3': 33, 's4': 44}, 'daq_trigger': 'TOF2',
'diffuser_thickness': 31, 'end_notes': 'en2', 'start_notes': None, 'end_pulse':
2120L, 'proton_absorber_thickness': 55, 'daq_version': 'no', 'step': 22.3,
'daq_gate_width': 210.0, 'end_time': datetime.datetime(2002, 2, 22, 15, 1, 45,
339916), 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'],
'magnets': {'q21': {'polarity': 1, 'set_current':
29.4}, 'q22': {'polarity':-1, 'set_current': 29.7}}, 'start_pulse': 2110L,
'optics': None, 'start_time': datetime.datetime(2002, 2, 22, 15, 1, 40,
339916)}}

BL_PULSES = {1L: {'status': False, 'beam_stop': 'Open', 'run_type': 'cosmic',
'run_number': 1L, 'scalars': {}, 'daq_trigger': 'TOF1', 'end_pulse': 1120L,
'start_notes': 'note1', 'proton_absorber_thickness': 55, 'start_pulse': 1110L,
'step': 12.3, 'daq_gate_width': 110.0, 'end_time': datetime.datetime(2001, 1,
22, 15, 1, 45, 339916), 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'], 'magnets': {'q11': {'polarity': 1,
'set_current': 19.4}, 'q12': {'polarity':-1, 'set_current': 19.7}},
'diffuser_thickness': 32, 'end_notes': 'en1', 'daq_version': 'PULSES', 'optics':
'optic1', 'start_time': datetime.datetime(2001, 1, 22, 15, 1, 40, 339916)}, 2L:
{'status': True, 'beam_stop': 'Closed', 'run_type': 'test', 'run_number': 2L,
'scalars': {}, 'daq_trigger': 'TOF2', 'end_pulse': 2120L, 'start_notes': None,
'proton_absorber_thickness': 55, 'start_pulse': 2110L, 'step': 22.3,
'daq_gate_width': 210.0, 'end_time': datetime.datetime(2002, 2, 22, 15, 1, 45,
339916), 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'],
'magnets': {'q21': {'polarity': 1, 'set_current':
29.4}, 'q22': {'polarity':-1, 'set_current': 29.7}}, 'diffuser_thickness': 33,
'end_notes': 'en2', 'daq_version': 'no', 'optics': None, 'start_time':
datetime.datetime(2002, 2, 22, 15, 1, 40, 339916)}}

BL_RUNS = {5L: {'status': False, 'beam_stop': 'Open', 'run_type': 'cosmic',
'run_number': 5L, 'scalars': {}, 'daq_trigger': 'TOF1', 'diffuser_thickness':
34, 'end_notes': 'en1', 'start_notes': 'run 5', 'end_pulse': 1120L,
'proton_absorber_thickness': 55, 'daq_version': 'RUNS', 'step': 12.3,
'daq_gate_width': 110.0, 'end_time': datetime.datetime(2001, 1, 22, 15, 1, 45,
339916), 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'],
'magnets': {'q11': {'polarity': 1, 'set_current':
19.4}, 'q12': {'polarity':-1, 'set_current': 19.7}}, 'start_pulse': 1110L,
'optics': 'optics5', 'start_time': datetime.datetime(2001, 1, 22, 15, 1, 40,
339916)}, 6L: {'status': True, 'beam_stop': 'Closed', 'run_type': 'test',
'run_number': 6L, 'scalars': {}, 'daq_trigger': 'TOF2', 'diffuser_thickness':
35, 'end_notes': 'en2', 'start_notes': 'run 6', 'end_pulse': 2120L,
'proton_absorber_thickness': 55, 'daq_version': 'no', 'step': 22.3,
'daq_gate_width': 210.0, 'end_time': datetime.datetime(2002, 2, 22, 15, 1, 45,
339916), 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'],
'magnets': {'q21': {'polarity': 1, 'set_current':
29.4}, 'q22': {'polarity':-1, 'set_current': 29.7}}, 'start_pulse': 2110L,
'optics': None, 'start_time': datetime.datetime(2002, 2, 22, 15, 1, 40,
339916)}}

BL_RUN = {1L: {'status': False, 'beam_stop': 'Open', 'run_type': 'cosmic',
'run_number': 1L, 'scalars': {}, 'daq_trigger': 'TOF1', 'diffuser_thickness':
36, 'end_notes': 'en1', 'start_notes': 'run1', 'end_pulse': 1120L,
'proton_absorber_thickness': 55, 'daq_version': 'RUN', 'step': 12.3,
'daq_gate_width': 110.0, 'end_time': datetime.datetime(2001, 1, 22, 15, 1, 45,
339916), 'gdc_host_name': '', 'isis_beam': {'four': {'mean': 5.0, 'sigma': 6.0},
'one': {'mean': 2.0, 'sigma': 3.0}}, 'ldc_host_names': ['host1', 'host2'],
'magnets': {'q11': {'polarity': 1, 'set_current':
19.4}, 'q12': {'polarity':-1, 'set_current': 19.7}}, 'start_pulse': 1110L,
'optics': 'opt1', 'start_time': datetime.datetime(2001, 1, 22, 15, 1, 40,
339916)}}

BL_TAG = {'1': {'beam_stop': 'Open', 'diffuser_thickness': 36, 'magnets':
{'q11': 19.4, 'q12': 19.7}, 'proton_absorber_thickness': 55}}

BL_TAGS = ['1', '2']

BL_START_RUN = {'run_number': 1L, 'run_type': 'cosmic', 'daq_trigger': 'TOF1',
'start_notes': 'run1', 'daq_version': 'RUN', 'step': 12.3, 'daq_gate_width':
110.0, 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'],
'start_pulse': 1110L, 'optics': 'opt1',
'start_time': datetime.datetime(2001, 1, 22, 15, 1, 40, 339916)}

BL_START_RUN_ERROR = {'run_number': 1L, 'run_type': 'cosmic', 'daq_trigger':
'TOF1', 'start_notes': 'run1', 'daq_version': 'RUN', 'step': 12.3,
'daq_gate_width': 110.0, 'gdc_host_name': '', 'isis_beam': {},
'ldc_host_names': ['host1', 'host2'], 'start_pulse': 1110L, 'optics': 'opt1'}

BL_START_RUN_ERROR_LDC = {'run_number': 1L, 'run_type': 'cosmic',
'daq_trigger': 'TOF1',
'start_notes': 'run1', 'daq_version': 'RUN', 'step': 12.3, 'daq_gate_width':
110.0, 'gdc_host_name': '', 'isis_beam': {}, 'start_pulse': 1110L,
'optics': 'opt1',
'start_time': datetime.datetime(2001, 1, 22, 15, 1, 40, 339916)}

BL_END_RUN = {'run_number': 1L, 'status': False, 'end_notes': 'en1',
'end_pulse': 1120L, 'end_time': datetime.datetime(2001, 1, 22, 15, 1, 45,
339916), 'scl_sum_00': 0, 'scl_name_00': '0', 'scl_sum_01': 1, 'scl_name_01':
'1', 'scl_sum_02': 2, 'scl_name_02': '2', 'scl_sum_03': 3, 'scl_name_03': '3',
'scl_sum_04': 4, 'scl_name_04': '4', 'scl_sum_05': 5, 'scl_name_05': '5',
'scl_sum_06': 6, 'scl_name_06': '6', 'scl_sum_07': 7, 'scl_name_07': '7',
'scl_sum_08': 8, 'scl_name_08': '8', 'scl_sum_09': 9, 'scl_name_09': '9',
'scl_sum_10': 10, 'scl_name_10': '10', 'scl_sum_11': 11, 'scl_name_11': '11'}

BL_END_RUN_SCALAR = {'SumPartTrig': 1L, 'SumReqTrig': 2L, 'SumGVa1': 3L,
'SumToF0': 4L, 'SumToF1': 5L, 'SumLMC12': 6L, 'SumLMC34': 7L, 'SumLMC1234': 8L}

BL_END_RUN_ISIS_BEAM = [{'name': 'val1', 'mean': 1L, 'sigma': 2L}, {'name':
'val1', 'mean': 3.0, 'sigma': 4.0}]

BL_END_RUN_ERROR = {'run_number': 1L, 'status': False, 'end_notes': 'en1',
'end_pulse': 1120L}

BL_BEAMLINE_1 = {'run_number': 1L, 'beam_stop': 'Open',
'diffuser_thickness': 36, 'proton_absorber_thickness': 55}

BL_BEAMLINE_2 = {'run_number': 1L, 'beam_stop': 'closed',
'diffuser_thickness': 36, 'proton_absorber_thickness': 55}

BL_BEAMLINE_MAGNETS = [{'name': 'q11', 'polarity': 1, 'current': 19.4},
{'name': 'q12', 'polarity':-1, 'current': 19.7}]

BL_BEAMLINE_MAGNETS_ERROR = [{'name': 'q11', 'polarity': 1, 'current': 19.4},
{'name': 'q12', 'polarity':-2, 'current': 19.7}]

BL_BEAMLINE_ERROR_1 = {'run_number': 1L, 'beam_stop': 'Open',
'diffuser_thickness': 36}

BL_BEAMLINE_ERROR_2 = {'run_number': 1L, 'beam_stop': 'pen',
'diffuser_thickness': 36}

CAB_STR = ("""Cabling""" + 
_BASE_STR + 
"""\tget_cabling_for_date(string device, datetime timestamp)         
\tget_cabling_for_id(int id)         
\tget_cabling_for_run(string device, int run_number)         
\tget_current_cabling(string device)         
\tget_ids(datetime start_time, datetime stop_time)         
\tlist_devices()""")

CAB_SM_STR = ("""CablingSuperMouse""" + 
_BASE_STR + 
"""\tget_cabling_for_date(string device, datetime timestamp)         
\tget_cabling_for_id(int id)         
\tget_cabling_for_run(string device, int run_number)         
\tget_current_cabling(string device)         
\tget_ids(datetime start_time, datetime stop_time)         
\tlist_devices()
\tadd_control(int crate, int module, int channel, string name)         
\tupdate_control(int crate, int module, int channel, string name)         
\tset_tracker(string device, dict data)         
\tset_detector(string device, datetime valid_from_time, string data)""")

CAB_CABLING_CONTROLS = ([{'crate': 2, 'channel': 4, 'module': 1, 'name': 'a4'},
{'crate': 2, 'channel': 5, 'module': 1, 'name': 'a5'}, {'crate': 2, 'channel':
6, 'module': 2, 'name': 'b6'}, {'crate': 2, 'channel': 7, 'module': 2, 'name':
'b7'}, {'crate': 3, 'channel': 333, 'module': 33, 'name': 'a333'}, {'crate': 3,
'channel': 3333, 'module': 33, 'name': 'a3333'}])

CAB_CABLING_TRACKER = ([{'vlsb_geo_number': 2, 'vlsb_computer_id': 1, 'plane':
6, 'tracker_no': 4, 'station': 5, 'vlsb_channel': 3, 'channel': 7},
{'vlsb_geo_number': 2, 'vlsb_computer_id': 1, 'plane': 11, 'tracker_no': 9,
'station': 10, 'vlsb_channel': 8, 'channel': 12}, {'vlsb_geo_number': 13,
'vlsb_computer_id': 1, 'plane': 17, 'tracker_no': 15, 'station': 16,
'vlsb_channel': 14, 'channel': 18}, {'vlsb_geo_number': 13, 'vlsb_computer_id':
1, 'plane': 22, 'tracker_no': 20, 'station': 21, 'vlsb_channel': 19, 'channel':
23}, {'vlsb_geo_number': 25, 'vlsb_computer_id': 24, 'plane': 29, 'tracker_no':
27, 'station': 28, 'vlsb_channel': 26, 'channel': 30}, {'vlsb_geo_number': 25,
'vlsb_computer_id': 24, 'plane': 34, 'tracker_no': 32, 'station': 33,
'vlsb_channel': 31, 'channel': 35}])

CAB_DEVICES = ['CONTROL', 'CKOV A', 'CKOV B', 'EMR', 'KL', 'SCALERS', 'TOF0',
'TOF1', 'TOF2']

CAB_SET_TRACKER = ([{'vlsb_geo_number': 2, 'vlsb_computer_id': 1, 'plane':
6, 'tracker_no': 4, 'station': 5, 'vlsb_channel': 3, 'channel': 7},
{'vlsb_geo_number': 2, 'vlsb_computer_id': 1, 'plane': 11, 'tracker_no': 9,
'station': 10, 'vlsb_channel': 8, 'channel': 12}, {'vlsb_geo_number': 13,
'vlsb_computer_id': 1, 'plane': 17, 'tracker_no': 15, 'station': 16,
'vlsb_channel': 14, 'channel': 18}, {'vlsb_geo_number': 13, 'vlsb_computer_id':
1, 'plane': 22, 'tracker_no': 20, 'station': 21, 'vlsb_channel': 19, 'channel':
23}, {'vlsb_geo_number': 25, 'vlsb_computer_id': 24, 'plane': 29, 'tracker_no':
27, 'station': 28, 'vlsb_channel': 26, 'channel': 30}, {'vlsb_geo_number': 25,
'vlsb_computer_id': 24, 'plane': 34, 'tracker_no': 32, 'station': 33,
'vlsb_channel': 31, 'channel': 35}])

CAB_SET_TRACKER_ERROR = ([{'vlsb_geo_number': 2, 'vlsb_computer_id': 1, 'plane':
6, 'tracker_no': 4, 'station': 5, 'vlsb_channel': 3, 'channel': 7},
{'vlsb_geo_number': 2, 'vlsb_computer_id': 1, 'plane': 11, 'tracker_no': 9,
'station': 10, 'vlsb_channel': 8, 'channel': 12}, {'vlsb_geo_number': 13,
'vlsb_computer_id': 1, 'plane': 17, 'tracker_no': 15, 'station': 16,
'vlsb_channel': 14, 'channel': 18}, {'vlsb_geo_number': 13, 'vlsb_computer_id':
1, 'plane': 22, 'tracker_no': 20, 'station': 21, 'vlsb_channel': 19, 'channel':
23}, {'vlsb_geo_number': 25, 'vlsb_computer_id': 24, 'plane': 29, 'tracker_no':
27, 'station': 28, 'vlsb_channel': 26, 'channel': 30}, {'vlsb_geo_number': 25,
'vlsb_computer_id': 24, 'plane': 34, 'tracker_no': 32, 'station': 33,
'vlsb_channel': 31}])

CAB_B64 = "CAB B64"

CAB_IDS = {'1': {'device': 'mouse wheel', 'valid_from': datetime.datetime(2001,
1, 1, 1, 2, 3), 'id': '1', 'created': datetime.datetime(2001, 1, 1, 1, 2, 4)},
'2': {'device': 'mouse wheel', 'valid_from': datetime.datetime(2002, 1, 1, 1, 2,
3), 'id': '2', 'created': datetime.datetime(2002, 1, 1, 1, 2, 4)}}


CAL_STR = ("""Calibration""" + 
_BASE_STR + 
"""\tget_calibration_for_date(string device, datetime timestamp,         
\t\tstring calibration_type)         
\tget_calibration_for_id(int id)         
\tget_calibration_for_run(string device, int run_number,         
\t\tstring calibration_type)         
\tget_current_calibration(string device, string calibration_type)         
\tget_ids(datetime start_time, datetime stop_time)         
\tlist_devices()""")

CAL_SM_STR = ("""CalibrationSuperMouse""" + 
_BASE_STR + 
"""\tget_calibration_for_date(string device, datetime timestamp,         
\t\tstring calibration_type)         
\tget_calibration_for_id(int id)         
\tget_calibration_for_run(string device, int run_number,         
\t\tstring calibration_type)         
\tget_current_calibration(string device, string calibration_type)         
\tget_ids(datetime start_time, datetime stop_time)         
\tlist_devices()
\tset_tracker(string device, dict data)         
\tset_detector(string device, string calibration_type,         
\t\tdatetime valid_from_time, string data)""")

CAL_CALIBRATION_TRACKER = ([{'channel': 3, 'adc_gain': 5, 'tdc_slope': 7,
'board': 2, 'tdc_pedestal': 6, 'bank': 1, 'adc_pedestal': 4} , {'channel': 8,
'adc_gain': 10, 'tdc_slope': 12, 'board': 2, 'tdc_pedestal': 11, 'bank': 1,
'adc_pedestal': 9}, {'channel': 14, 'adc_gain': 16, 'tdc_slope': 18, 'board':
13, 'tdc_pedestal': 17, 'bank': 1, 'adc_pedestal': 15}, {'channel': 19,
'adc_gain': 21, 'tdc_slope': 23, 'board': 13, 'tdc_pedestal': 22, 'bank': 1,
'adc_pedestal': 20}])

CAL_DEVICES = ['CKOV A', 'CKOV B', 'EMR', 'KL', 'SCALERS', 'TOF0', 'TOF1',
'TOF2']

CAL_SET_TRACKER = ([{'channel': 3, 'adc_gain': 5, 'tdc_slope': 7,
'board': 2, 'tdc_pedestal': 6, 'bank': 1, 'adc_pedestal': 4} , {'channel': 8,
'adc_gain': 10, 'tdc_slope': 12, 'board': 2, 'tdc_pedestal': 11, 'bank': 1,
'adc_pedestal': 9}, {'channel': 14, 'adc_gain': 16, 'tdc_slope': 18, 'board':
13, 'tdc_pedestal': 17, 'bank': 1, 'adc_pedestal': 15}, {'channel': 19,
'adc_gain': 21, 'tdc_slope': 23, 'board': 13, 'tdc_pedestal': 22, 'bank': 1,
'adc_pedestal': 20}])

CAL_SET_TRACKER_ERROR = ([{'channel': 3, 'adc_gain': 5, 'tdc_slope': 7,
'board': 2, 'tdc_pedestal': 6, 'bank': 1, 'adc_pedestal': 4} , {'channel': 8,
'adc_gain': 10, 'tdc_slope': 12, 'board': 2, 'tdc_pedestal': 11, 'bank': 1,
'adc_pedestal': 9}, {'channel': 14, 'adc_gain': 16, 'tdc_slope': 18, 'board':
13, 'tdc_pedestal': 17, 'bank': 1, 'adc_pedestal': 15}, {'channel': 19,
'adc_gain': 21, 'tdc_slope': 23, 'board': 13, 'tdc_pedestal': 22, 'bank': 1}])

CAL_B64 = "CAL B64"

CAL_IDS = {'1': {'device': 'mouse wheel', 'calibration_type': 'random',
'valid_from': datetime.datetime(2001, 1, 1, 1, 2, 3), 'id': '1', 'created':
datetime.datetime(2001, 1, 1, 1, 2, 4)}, '2': {'device': 'mouse wheel',
'calibration_type': 'spanner', 'valid_from': datetime.datetime(2002, 1, 1, 1, 2,
3), 'id': '2', 'created': datetime.datetime(2002, 1, 1, 1, 2, 4)}}

C_STR = ("""PIDCtrl""" + 
_BASE_STR + 
"""\tget_pid_ctrls()         
\tget_pid_ctrls_for_channel(int crate, int slot, int channel)         
\tget_pid_ctrls_for_crate(int crate)         
\tget_previous_settings(datetime timestamp)""")

C_SM_STR = ("""PIDCtrlSuperMouse""" + 
_BASE_STR + 
"""\tget_pid_ctrls()         
\tget_pid_ctrls_for_channel(int crate, int slot, int channel)         
\tget_pid_ctrls_for_crate(int crate)         
\tget_previous_settings(datetime timestamp)
\tset_parameter(int crate, int module, int channel,         
\t\tstring parameter_name, string parameter_value)         
\tupdate_parameter(int crate, int module, int channel,        
\t\tstring parameter_name, string parameter_value)""")

C_CONTROLS = ([{'Chn': 0, 'Name': 'n_1', 'RmpUp': '100', 'Crt': 1, 'ILim':
'600.0', 'VSet': '1700.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10', 'RmpDn':
'100'}, {'Chn': 1, 'Name': 'n_2', 'RmpUp': '100', 'Crt': 1, 'ILim':
'600.0', 'VSet': '1700.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10', 'RmpDn':
'100'}, {'Chn': 2, 'Name': 'n_3', 'RmpUp': '100', 'Crt': 1, 'ILim':
'600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10', 'RmpDn':
'100'}, {'Chn': 3, 'Name': 'n_4', 'RmpUp': '100', 'Crt': 2, 'ILim':
'600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 1, 'Trip': '10', 'RmpDn':
'100'}, {'Chn': 4, 'Name': 'n_5', 'RmpUp': '100', 'Crt': 2, 'ILim':
'600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 1, 'Trip': '10', 'RmpDn':
'100'}])

C_CONTROLS_FOR_CRATE = ([{'Chn': 0, 'Name': 'n_1', 'RmpUp': '100', 'Crt':
3, 'ILim': '600.0', 'VSet': '1700.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10',
'RmpDn': '100'}, {'Chn': 1, 'Name': 'n_2', 'RmpUp': '100', 'Crt': 3,
'ILim': '600.0', 'VSet': '1700.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10',
'RmpDn': '100'}, {'Chn': 2, 'Name': 'n_3', 'RmpUp': '100', 'Crt': 3,
'ILim': '600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10',
'RmpDn': '100'}])

C_CONTROLS_FOR_PREVIOUS = ([{'Chn': 0, 'Name': 'n_1', 'RmpUp': '100', 'Crt':
4, 'ILim': '600.0', 'VSet': '1700.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10',
'RmpDn': '100'}, {'Chn': 1, 'Name': 'n_2', 'RmpUp': '100', 'Crt': 4,
'ILim': '600.0', 'VSet': '1700.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10',
'RmpDn': '100'}, {'Chn': 2, 'Name': 'n_3', 'RmpUp': '100', 'Crt': 4,
'ILim': '600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 0, 'Trip': '10',
'RmpDn': '100'}, {'Chn': 3, 'Name': 'n_4', 'RmpUp': '100', 'Crt': 5,
'ILim': '600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 1, 'Trip': '10',
'RmpDn': '100'}, {'Chn': 4, 'Name': 'n_5', 'RmpUp': '100', 'Crt': 5,
'ILim': '600.0', 'VSet': '1750.0', 'On/Off': '0', 'Slt': 1, 'Trip': '10',
'RmpDn': '100'}])


CC_STR = ("""CoolingChannel""" + 
_BASE_STR + 
"""\tget_all_coolingchannels()         
\tget_coolingchannel_for_run(int run_number)         
\tget_coolingchannel_for_date(datetime timestamp)         
\tget_coolingchannel_for_tag(str tag)        
\tlist_tags()""")

CC_SM_STR = ("""CoolingChannelSuperMouse""" + 
_BASE_STR + 
"""\tget_all_coolingchannels()         
\tget_coolingchannel_for_run(int run_number)         
\tget_coolingchannel_for_date(datetime timestamp)         
\tget_coolingchannel_for_tag(str tag)        
\tlist_tags()
\tset_coolingchannel(list(dict) data)         
\tset_coolingchannel_tag(str tag, list(dict) data)""")
# old style xml, with no run attribute generates 'run':'null' dict element. Add this (jm 12.07.2016)
CC_1 = [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3,
'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6,
'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5,
'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'}]

CC_2 = [{'polarity': -1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3,
'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6,
'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5,
'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}]

CC_ALL = [{'valid_from_time': datetime.datetime(2013, 5, 15, 10, 48, 10, 67000),
'valid_until_time': datetime.datetime(2013, 5, 15, 10, 48, 45, 81000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 10, 48, 45, 81000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 10, 55, 58, 297000), 'run': 'null',
'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 10, 55, 58, 297000), 'valid_until_time': datetime.datetime(2013, 5, 15,
11, 22, 49, 437000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 11, 22, 49, 437000),
'valid_until_time': datetime.datetime(2013, 5, 15, 11, 28, 24, 534000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 11, 28, 24, 534000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 11, 29, 21, 60000), 'run': 'null',
'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 11, 29, 21, 60000), 'valid_until_time': datetime.datetime(2013, 5, 15,
11, 29, 37, 562000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 11, 29, 37, 562000),
'valid_until_time': datetime.datetime(2013, 5, 15, 11, 29, 40, 308000),
 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 11, 29, 40, 308000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 11, 30, 48, 357000), 'run': 'null',
'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 11, 30, 48, 357000), 'valid_until_time': datetime.datetime(2013, 5, 15,
13, 24, 35, 360000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 13, 24, 35, 360000),
'valid_until_time': datetime.datetime(2013, 5, 15, 13, 30, 45, 109000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 13, 30, 45, 109000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 13, 32, 54, 877000), 'run': 'null',
'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 13, 32, 54, 877000), 'valid_until_time': datetime.datetime(2013, 5, 15,
13, 37, 12, 955000), 'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 13, 37, 12, 955000),
'valid_until_time': datetime.datetime(2013, 5, 15, 13, 38, 53, 366000),'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 13, 38, 53, 366000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 13, 41, 28, 768000),'run': 'null', 'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 13, 41, 28, 768000), 'valid_until_time': datetime.datetime(2013, 5, 15,
13, 42, 25, 385000),'run': 'null', 'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 13, 42, 25, 385000),
'valid_until_time': datetime.datetime(2013, 5, 15, 13, 43, 49, 577000),'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 13, 43, 49, 577000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 13, 45, 16, 219000), 'run': 'null','magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 13, 45, 16, 219000), 'valid_until_time': datetime.datetime(2013, 5, 15,
13, 50, 28, 224000),'run': 'null', 'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 13, 50, 28, 224000),
'valid_until_time': datetime.datetime(2013, 5, 15, 13, 51, 5, 172000),'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 13, 51, 5, 172000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 14, 1, 3, 467000),'run': 'null', 'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 14, 1, 3, 467000), 'valid_until_time': datetime.datetime(2013, 5, 15, 14,
6, 5, 559000),'run': 'null', 'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]},
{'valid_from_time': datetime.datetime(2013, 5, 15, 14, 6, 5, 559000),
'valid_until_time': datetime.datetime(2013, 5, 15, 14, 8, 29, 663000),'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 14, 8, 29, 663000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 14, 8, 58, 21000),'run': 'null', 'magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip1'}, {'polarity': -1, 'coils': [{'vlim': 3.6,
'name': 'coil3', 'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5,
'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1,
'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}], 'name': 'mag2', 'mode':
'flip2'}]}, {'valid_from_time': datetime.datetime(2013, 5, 15, 14, 8, 58,
21000), 'valid_until_time': datetime.datetime(2013, 5, 15, 14, 10, 52, 699000),'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'}, {'polarity': -1, 'coils':
[{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2,
'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4', 'iset': 4.3,
'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}], 'name':
'mag2', 'mode': 'flip2'}]}, {'valid_from_time': datetime.datetime(2013, 5, 15,
14, 10, 52, 699000), 'valid_until_time': datetime.datetime(2013, 5, 15, 14, 44,
9, 954000),'run': 'null', 'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1',
'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4},
{'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2,
'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'}, {'polarity':
-1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3, 'calibration': 3.1,
'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4',
'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}],
'name': 'mag2', 'mode': 'flip2'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 14, 44, 9, 954000), 'valid_until_time': datetime.datetime(2013, 5, 15,
14, 46, 12, 890000), 'run': 'null','magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'},
{'polarity': -1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3,
'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6,
'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5,
'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 14, 46, 12, 890000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 14, 47, 5, 431000), 'run': 'null','magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip1'}, {'polarity': -1, 'coils': [{'vlim': 3.6,
'name': 'coil3', 'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5,
'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1,
'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}], 'name': 'mag2', 'mode':
'flip2'}]}, {'valid_from_time': datetime.datetime(2013, 5, 15, 14, 47, 5,
431000), 'valid_until_time': datetime.datetime(2013, 5, 15, 14, 47, 57, 136000),'run': 'null',
'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'}, {'polarity': -1, 'coils':
[{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2,
'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4', 'iset': 4.3,
'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}], 'name':
'mag2', 'mode': 'flip2'}]}, {'valid_from_time': datetime.datetime(2013, 5, 15,
14, 47, 57, 136000), 'valid_until_time': datetime.datetime(2013, 5, 15, 14, 48,
58, 941000),'run': 'null', 'magnets': [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name':
'coil1', 'iset': 1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate':
1.4}, {'vlim': 2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim':
2.2, 'stability': 2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'},
{'polarity': -1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3,
'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6,
'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5,
'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 14, 48, 58, 941000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 14, 50, 34, 154000), 'run': 'null','magnets': [{'polarity': 1,
'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip1'}, {'polarity': -1, 'coils': [{'vlim': 3.6,
'name': 'coil3', 'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5,
'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1,
'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}], 'name': 'mag2', 'mode':
'flip2'}]}, {'valid_from_time': datetime.datetime(2013, 5, 15, 14, 50, 34,
154000), 'valid_until_time': datetime.datetime(2013, 5, 15, 15, 4, 49, 116000),'run': 'null',
'magnets': [{'polarity': -1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset':
3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim':
4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability':
4.5, 'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}]}, {'valid_from_time':
datetime.datetime(2013, 5, 15, 15, 4, 49, 116000), 'valid_until_time':
datetime.datetime(2013, 5, 15, 15, 15, 26, 325000),'run': 'null', 'magnets': [{'polarity': -1,
'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3, 'calibration': 3.1,
'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4',
'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}],
'name': 'mag2', 'mode': 'flip2'}]}, {'valid_from_time': datetime.datetime(2013,
5, 15, 15, 15, 26, 325000), 'valid_until_time': None, 'run': 'null','magnets': [{'polarity':
1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3, 'calibration': 1.1,
'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6, 'name': 'coil2',
'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5, 'rate': 2.4}],
'name': 'mag1', 'mode': 'flip1'}]}]

CC_DATE = [{'polarity': -1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset':
3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim':
4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability':
4.5, 'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}]

CC_CSV = StringIO.StringIO("""tag,0_to_240FlipP2,,,,,,
name,SS1,,,,,,
mode,Flip,,,,,,
polarity,-1,,,,,,
coils,name,vlim,ilim,rate,iset,stability,calibration
,SS1-M1,6.0,300.0,23.66,270.3,0.0,1.0
,SS1-M2,6.0,300.0,25.00,285.6,0.0,1.0
,SS1-T1,5.0,60.0,3.93,-44.9,0.0,1.0
,SS1-C,15.0,300.0,24.82,283.6,0.0,1.0
,SS1-T2,5.0,60.0,2.59,-29.6,0.0,1.0""")

CC_CSV_ERROR_1 = StringIO.StringIO("""name,SS1,,,,,,
mode,Flip,,,,,,
polarity,-1,,,,,,
coils,name,vlim,ilim,rate,iset,stability,calibration
,SS1-M1,6.0,300.0,23.66,270.3,0.0,1.0
,SS1-M2,6.0,300.0,25.00,285.6,0.0,1.0
,SS1-T1,5.0,60.0,3.93,-44.9,0.0,1.0
,SS1-C,15.0,300.0,24.82,283.6,0.0,1.0
,SS1-T2,5.0,60.0,2.59,-29.6,0.0,1.0""")

CC_CSV_ERROR_2 = StringIO.StringIO("""tag,0_to_240FlipP2,,,,,,
name,SS1,,,,,,
polarity,-1,,,,,,
coils,name,vlim,ilim,rate,iset,stability,not_valid
,SS1-M1,6.0,300.0,23.66,270.3,0.0,1.0
,SS1-M2,6.0,300.0,25.00,285.6,0.0,1.0
,SS1-T1,5.0,60.0,3.93,-44.9,0.0,1.0
,SS1-C,15.0,300.0,24.82,283.6,0.0,1.0
,SS1-T2,5.0,60.0,2.59,-29.6,0.0,1.0""")

CC_CSV_ERROR_3 = StringIO.StringIO("""name,SS1,,,,,,
mode,Flip,,,,,,
polarity,-1,,,,,,
coils,name,vlim,ilim,rate,iset,stability,not_valid
,SS1-M1,6.0,300.0,23.66,270.3,0.0,1.0
,SS1-M2,6.0,300.0,25.00,285.6,0.0,1.0
,SS1-T1,5.0,60.0,3.93,-44.9,0.0,1.0
,SS1-C,15.0,300.0,24.82,283.6,0.0,1.0
,SS1-T2,5.0,60.0,2.59,-29.6,0.0,1.0""")

CC_ERROR_1 = [{'polarity': -2, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset':
3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim':
4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability':
4.5, 'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}] 

CC_ERROR_2 = [{'polarity': -2, 'coils': [{'vlim': 'abcd', 'name': 'coil3',
'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4},
{'vlim': 4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2,
'stability': 4.5, 'rate': 4.4}], 'name': 'mag2', 'mode': 'flip2'}]

CC_ERROR_3 = [{'polarity': -1, 'coils': [{'vlim': 3.6, 'name': 'coil3', 'iset':
3.3, 'calibration': 3.1, 'ilim': 3.2, 'stability': 3.5, 'rate': 3.4}, {'vlim':
4.6, 'name': 'coil4', 'iset': 4.3, 'calibration': 4.1, 'ilim': 4.2, 'stability':
4.5, 'rate': 4.4}], 'name': 'mag2'}]

CC_RUN = [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset': 1.3,
'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim': 2.6,
'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability': 2.5,
'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'}, {'polarity': -1, 'coils':
[{'vlim': 3.6, 'name': 'coil3', 'iset': 3.3, 'calibration': 3.1, 'ilim': 3.2,
'stability': 3.5, 'rate': 3.4}, {'vlim': 4.6, 'name': 'coil4', 'iset': 4.3,
'calibration': 4.1, 'ilim': 4.2, 'stability': 4.5, 'rate': 4.4}], 'name':
'mag2', 'mode': 'flip2'}]

CC_TAG_1 = []

CC_TAG_3 = [{'polarity': 1, 'coils': [{'vlim': 1.6, 'name': 'coil1', 'iset':
1.3, 'calibration': 1.1, 'ilim': 1.2, 'stability': 1.5, 'rate': 1.4}, {'vlim':
2.6, 'name': 'coil2', 'iset': 2.3, 'calibration': 2.1, 'ilim': 2.2, 'stability':
2.5, 'rate': 2.4}], 'name': 'mag1', 'mode': 'flip1'}]

CC_TAGS = ['10', '20']

CC_LIST_ABS_TAGS=['navi_tag','navi_tag2']

CC_ABS_TAG={'navi_tag': [{'comment': 'vivere ', 'name': 'test_abs_03', 'material': 'Ne', 'pressure': '116.0', 'shape': 'cube', 'temperature': '24.0'},
{'comment': 'necesse est ', 'name': 'test_abs_02', 'material': 'He', 'pressure': '118.0', 'shape': 'cube', 'temperature': '22.0'},
{'comment': 'navigare', 'name': 'test_abs_01', 'material': 'vac', 'pressure': '120.0', 'shape': 'cube', 'temperature': '20.0'}]}

CC_ABS=[{'comment': 'vivere ', 'name': 'test_abs_03', 'material': 'Ne', 'pressure': '116.0', 'shape': 'cube', 'temperature': '24.0'},
{'comment': 'necesse est ', 'name': 'test_abs_02', 'material': 'He', 'pressure': '118.0', 'shape': 'cube', 'temperature': '22.0'},
{'comment': 'navigare', 'name': 'test_abs_01', 'material': 'vac', 'pressure': '120.0', 'shape': 'cube', 'temperature': '20.0'}]

EXCEPT_STR = "Bang!"

G_STR = ("""Geometry""" + 
_BASE_STR + 
"""\tget_current_gdml()         
\tget_gdml_for_id(string id)         
\tget_gdml_for_run(string run_number)         
\tget_ids(datetime start_time, datetime stop_time)""")

G_SM_STR = ("""GeometrySuperMouse""" + 
_BASE_STR + 
"""\tget_current_gdml()         
\tget_gdml_for_id(string id)         
\tget_gdml_for_run(string run_number)         
\tget_ids(datetime start_time, datetime stop_time)
\tset_gdml(string gdml, datetime valid_from_time, string notes,         
\t\tstring technical_drawing_name)""")

G_GDML_CURRENT = "GDML_CURRENT"
G_GDML_FOR_ID = "GDML_FOR_ID"
G_GDML_FOR_RUN = "GDML_FOR_RUN"

G_IDS = ({9: {'notes': 'fred', 'validFrom': datetime.datetime(2010, 10, 15, 12,
32, 59, 800000,), 'created': datetime.datetime(2011, 1, 21, 15, 48, 1, 99000),
'technical_drawing_name': 'v1.1'}, 25: {'notes': 'sam', 'validFrom':
datetime.datetime(2010, 10, 15, 12, 32, 59, 800000), 'created':
datetime.datetime(2011, 1, 21, 16, 6, 45, 675000), 'technical_drawing_name':
'v1.5'}, 21: {'notes': 'harry', 'validFrom': datetime.datetime(2010, 10, 15, 12,
32, 59, 800000), 'created': datetime.datetime(2011, 1, 21, 15, 57, 31, 680000),
'technical_drawing_name': 'v1.4'}, 13: {'notes': 'tom', 'validFrom':
datetime.datetime(2010, 10, 15, 12, 32, 59, 800000), 'created':
datetime.datetime(2011, 1, 21, 15, 48, 52, 615000), 'technical_drawing_name':
'v1.2'}, 17: {'notes': 'dick', 'validFrom': datetime.datetime(2010, 10, 15, 12,
32, 59, 800000), 'created': datetime.datetime(2011, 1, 21, 15, 49, 8, 27000),
'technical_drawing_name': 'v1.3'}})

G_CORR=[{'name':'TOF0','dx':12.1,'dx_err':0.01, 'dy':22.20,'dy_err':0.02, 'dz':32.30, 'dz_err':0.029,
         'dx_rot':0.11,'dx_rot_err':0.011,'dy_rot':0.12,'dy_rot_err':0.021,'dz_rot':0.13,'dz_rot_err':0.031},
        {'name':'TRACKER0', 'dx':12.4, 'dx_err':0.001, 'dy':22.5, 'dy_err':0.002, 'dz':32.60 ,'dz_err':0.0030,
         'dx_rot':0.140,'dx_rot_err':0.00110, 'dy_rot':0.150, 'dy_rot_err':0.0021,'dz_rot':0.140,'dz_rot_err':0.0031}]

DQ_STR = ("""DataQuality""" +
_BASE_STR +
"""\tget_beamline_flags(run_number)
\tget_detector_flags(run_number)
\tget_daq_flags(run_number)
\tget_reconstruction_flags(run_number, maus_version, batch_iteration_number)""")

DQ_SM_STR= ("""DataQualitySuperMouse""" +
_BASE_STR +
"""\tget_beamline_flags(run_number)
\tget_detector_flags(run_number)
\tget_daq_flags(run_number)
\tget_reconstruction_flags(run_number, maus_version, batch_iteration_number)
\tset_reconstruction_flags(string flags)""")

DQ_MASKS_DICT = dict([('TOF0',0xf0000000000L), ('TOF1',0xf000000000L), ('CkovA',0xf00000000L), ('CkovB',0xf0000000L), ('Tracker0',0xf000000L),
                 ('Tracker1',0xf00000L), ('TOF2',0xf0000L), ('KL',0xf000L), ('EMR',0xf00L), ('RF1',0xf0L), ('RF2',0xfL)])
DQ_DICT = {'CkovB': 0L, 'RF2': 0L, 'RF1': 15L, 'CkovA': 0L, 'Tracker0': 0L, 'Tracker1': 0L, 'TOF1': 0L, 'TOF0': 0L, 'TOF2': 10L, 'KL': 1L, 'EMR': 15L}


MC_STR=("""MCSerialNumber""" +
_BASE_STR +
"""\tget_datacards(int serial_number)
\tget_comment(int serial_number)
\tget_sw_version(int serial_number)""")

MC_SERIAL = {'comment': u' a comment', 'softw': u'MAUS_MC_dummy', 'data': u'test cards 1'}
MC_COMMENT = {'comment': u' a comment'}
MC_SW_VER = u'MAUS_MC_dummy'

SM_STR = ("""StateMachine""" + 
_BASE_STR + 
"""\tget_allowed_transitions()         
\tget_current_state(string system)         
\tget_current_state_machine()         
\tget_state_machine_for_date(datetime timestamp)         
\tget_state_machine_for_run(int run_number)         
\tget_pv_data(string system, string state)""")

SM_SM_STR = ("""StateMachineSuperMouse""" + 
_BASE_STR + 
"""\tget_allowed_transitions()         
\tget_current_state(string system)         
\tget_current_state_machine()         
\tget_state_machine_for_date(datetime timestamp)         
\tget_state_machine_for_run(int run_number)         
\tget_pv_data(string system, string state)
\tset_state(string system, string state)         
\tset_pv_data(string system, string state, list pv_data)""")

SM_ALLOWED_TRANS = ({'sys1': 'on1', 'sys2': 'off2', 'sys3': 'powered3'})
SM_CURRENT = "ON"
SM_CURRENT_SM = ({'sys5': 'off5', 'sys4': 'on4', 'sys6': 'powered6'})
SM_FOR_DATE = ({'sys7': 'on7', 'sys8': 'off8', 'sys9': 'powered9'})
SM_FOR_RUN = ({'sys10': 'on10', 'sys11': 'off11', 'sys12': 'powered12'})
SM_PV_DATA = ([{'name': 'pv10', 'lo': 8.0, 'transition': 9.9999, 'lolo': 7.0,
'auto_sms': True, 'hi': 9.0, 'frequency': 9.8, 'mode': 'scan', 'units': 'mm',
'hihi': 10.0}, {'name': 'pv11', 'lo': 18.0, 'transition': 19.9999, 'lolo': 17.0,
'auto_sms': True, 'hi': 19.0, 'mode': 'scan2', 'units': 'cm', 'hihi': 20.0,
'deadband': 4.2}, {'name': 'pv12', 'lo': 28.0, 'transition': 29.9999, 'lolo':
27.0, 'auto_sms': True, 'hi': 29.0, 'frequency': 333.3, 'mode': 'scan3',
'units': 'm', 'hihi': 30.0, 'deadband': 222.2}])
SM_PV_DATA_ERROR_1 = ([{'name': 'pv10', 'auto_sms': False, 'lo': 8.0,
'transition': 9.9999, 'lolo': 7.0, 'hi': 9.0, 'mode': 'scan', 'units': 'mm',
'hihi': 10.0}])
SM_PV_DATA_ERROR_2 = ([{'name': 'pv10', 'auto_sms': False, 'lo': 8.0,
 'transition': 9.9999, 'lolo': 7.0, 'hi': 9.0, 'mode': 'scan', 'units': 'mm'}])


T_STR = ("""Target""" + 
_BASE_STR + 
"""\tget_current_blob(string name)         
\tget_blob_for_run(string name, string run_number)         
\tget_blob_for_date(string name, datetime date_time)         
\tget_target_names()""")

T_SM_STR = ("""TargetSuperMouse""" + 
_BASE_STR + 
"""\tget_current_blob(string name)         
\tget_blob_for_run(string name, string run_number)         
\tget_blob_for_date(string name, datetime date_time)         
\tget_target_names()
\tadd_blob(string name, string data)""")

T_BLOB_CURRENT = "BLOB_CURRENT"
T_BLOB_FOR_DATE = "BLOB_FOR_DATE"
T_BLOB_FOR_RUN = "BLOB_FOR_RUN"
T_TARGET_NAMES = ['ISIS', 'R78', 'SHEFFIELD']

T_IDS = ({9: {'notes': 'fred', 'validFrom': datetime.datetime(2010, 10, 15, 12,
32, 59, 800000,), 'created': datetime.datetime(2011, 1, 21, 15, 48, 1, 99000),
'technical_drawing_name': 'v1.1'}, 25: {'notes': 'sam', 'validFrom':
datetime.datetime(2010, 10, 15, 12, 32, 59, 800000), 'created':
datetime.datetime(2011, 1, 21, 16, 6, 45, 675000), 'technical_drawing_name':
'v1.5'}, 21: {'notes': 'harry', 'validFrom': datetime.datetime(2010, 10, 15, 12,
32, 59, 800000), 'created': datetime.datetime(2011, 1, 21, 15, 57, 31, 680000),
'technical_drawing_name': 'v1.4'}, 13: {'notes': 'tom', 'validFrom':
datetime.datetime(2010, 10, 15, 12, 32, 59, 800000), 'created':
datetime.datetime(2011, 1, 21, 15, 48, 52, 615000), 'technical_drawing_name':
'v1.2'}, 17: {'notes': 'dick', 'validFrom': datetime.datetime(2010, 10, 15, 12,
32, 59, 800000), 'created': datetime.datetime(2011, 1, 21, 15, 49, 8, 27000),
'technical_drawing_name': 'v1.3'}})
