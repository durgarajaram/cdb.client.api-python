"""@package cdb
The cdb module provides the client interface to the Configuration Database
server.
<h3>Pointing to a Server</h3>
The client makes use of a cdb server via a web service. The address of
the cdb server can be set in the class constructor:<pre>
from cdb import CoolingChannel
COOLING_CHANNEL = CoolingChannel('http://cdb.mice.rl.ac.uk')</pre>
If a URL is not passed in as part of the constructor then it is determined from
the from the environment variable CDB_SERVER. If that is not set then the
property cdb.server is obtained from the configuration file /opt/mice/etc/cdb-
client/cdb.props. If this is not found then the default http://cdb.mice.rl.ac.uk
is used.

<h3>Classes</h3>
All of the classes come in pairs. A class that provides read
only methods and a 'SuperMouse' class that extends the read only class to
provide additional write methods. N.B. the default server, cdb.mice.rl.ac.uk, is
publicly accessible and only exposes the read methods.

The AlarmHandler class is used to retrieve Alarm Handlers (ALH).

The AlarmHandlerSuperMouse class is used to store and retrieve Alarm Handlers
(ALH).

The Beamline class is used to retrieve data about beam line settings.

The BeamlineSuperMouse class is used to set and retrieve data about beam line
settings.

The Cabling class is used to retrieve cabling data.

The CablingSuperMouse class is used to set and retrieve cabling data.

The Calibration class is used to retrieve calibration data.

The CalibrationSuperMouse class is used to set and retrieve calibration data.

The CoolingChannel class is used to retrieve cooling channel data.

The CoolingChannelMouse class is used to set and retrieve cooling channel data.

The PIDCtrl class is used to retrieve parameter values.

The PIDCtrlSuperMouse class is used to set and retrieve parameter
values.

The Geometry class is used to retrieve a GDML data set.

The GeometrySuperMouse class is used to set and retrieve GDML data sets.

The StateMachine class is used to retrieve state machine data.

The StateMachineSuperMouse class is used to set and retrieve state machine
settings.

The Target class is used to retrieve a target data.

The TargetSuperMouse class is used to set and retrieve target data."""

from cdb._exceptions import CdbError
from cdb._exceptions import CdbPermanentError
from cdb._exceptions import CdbTemporaryError
from cdb._alarmhandler import AlarmHandler
from cdb._alarmhandler_supermouse import AlarmHandlerSuperMouse
from cdb._batchiteration import BatchIteration
from cdb._batchiteration_supermouse import BatchIterationSuperMouse
from cdb._beamline import Beamline
from cdb._beamline_supermouse import BeamlineSuperMouse
from cdb._cabling import Cabling
from cdb._cabling_supermouse import CablingSuperMouse
from cdb._calibration import Calibration
from cdb._calibration_supermouse import CalibrationSuperMouse
from cdb._coolingchannel import CoolingChannel
from cdb._coolingchannel_supermouse import CoolingChannelSuperMouse
from cdb._pid_ctrl import PIDCtrl
from cdb._pid_ctrl_supermouse import PIDCtrlSuperMouse
from cdb._dataquality import DataQuality
from cdb._dataquality_supermouse import DataQualitySuperMouse
from cdb._geometry import Geometry
from cdb._geometry_supermouse import GeometrySuperMouse
from cdb._mcserialnumber import MCSerialNumber
from cdb._mcserialnumber_supermouse import MCSerialNumberSuperMouse
from cdb._statemachine import StateMachine
from cdb._statemachine_supermouse import StateMachineSuperMouse
from cdb._target import Target
from cdb._target_supermouse import TargetSuperMouse

__all__ = ["CdbError", "CdbPermanentError", "CdbTemporaryError", "AlarmHandler",
"AlarmHandlerSuperMouse", "BatchIteration","BatchIterationSuperMouse","Beamline", "BeamlineSuperMouse", "Cabling",
"CablingSuperMouse", "Calibration", "CalibrationSuperMouse","CoolingChannel",
"CoolingChannelSuperMouse", "PIDCtrl", "PIDCtrlSuperMouse", "DataQuality", "DataQualitySuperMouse", "Geometry",
"GeometrySuperMouse","MCSerialNumber" ,"MCSerialNumberSuperMouse","StateMachine", "StateMachineSuperMouse", "Target",
"TargetSuperMouse"]

__version__ = '1.1.9'

