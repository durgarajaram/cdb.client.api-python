"GeometrySuperMouse module."

from base64 import b64encode
from xml.sax import parseString

from cdb._base import _get_string_from_date
from cdb._geometry import Geometry

__all__ = ["GeometrySuperMouse"]


class GeometrySuperMouse(Geometry):
    """
The GeometrySuperMouse class is used to store and retrieve GDML data sets.

A GDML data set can be stored using set_gdml, where the user defines the time
the data was valid from and provides a brief description of the change. The data
set will be assigned an id and creation time. Use get_ids to retrieve a list of
ids.

Setting another GDML data set with a later valid_from_time implies that the
earlier data set is no longer valid after the later valid_from_time. It is
possible to "update" an existing GDML data set by setting a new one with the
same valid_from_time as an existing one. The old data set is kept and the GDML
data sets can be distinguished by their creation_times.

    """

    def __init__(self, url=""):
        """
Construct a GeometrySuperMouse.

@param url: the url of the server in the form 'http://host.domain:port'

@exception CdbPermanentError: Unable to contact CDB server or invalid URL

        """
        super(GeometrySuperMouse, self).__init__(url,
                                                 "/cdb/geometrySuperMouse?wsdl")

    def __str__(self):
        _help_super = (
            "\n\tset_gdml(string gdml, datetime valid_from_time, string notes, \
        \n\t\tstring technical_drawing_name)")
        return "GeometrySuperMouse" + self._help + _help_super

    def set_gdml(self, gdml, valid_from_time, notes="",
                 technical_drawing_name=""):
        """
Set the GDML data set.

The GDML is converted to a byte array thus enabling the user to pass in the
data in a zipped format if so required.

@param gdml: a string containing a GDML data set
@param valid_from_time: a datetime that should represent the time from which
this data set is considered to be valid.
@param notes: a string containing a description of the change
@param technical_drawing_name: a string containing the name of the technical drawing

@return a string containing a status message

@exception CdbTemporaryError: The problem maybe transient and retrying the
request MAY succeed
@exception CdbPermanentError: An unexpected internal error

     """
        valid_from_time = _get_string_from_date(valid_from_time)
        xml = str(self._server.setGDML(b64encode(gdml), valid_from_time, notes,
                                       technical_drawing_name))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_corrections_xml(self, corr_xml):
        """
        Set corrections for a given geometry ID.
        :param corrections: XML containing corrections by module.
        :return: string containing a status message

        @exception CdbTemporaryError: The problem maybe transient and retrying the
        request MAY succeed
        @exception CdbPermanentError: An unexpected internal error

        """

        xml = str(self._server.setCorrections(corr_xml))
        parseString(xml, self._status_handler)
        return self._status_handler.get_message()

    def set_corrections(self, modules, geometry_id, comment='', run_start=0):
        """
        Set corrections for a given geometry ID.
        :param corrections: list of dictionaries (one per module) containing corrections by module.
        :param geometryID: geometry ID
        :param run_start: (optional) initial run the corrections are valid for.
        :param run_end:   (optional  final run the corrections are valid for.
        :return: string containing a status message

        @exception CdbTemporaryError: The problem maybe transient and retrying the
        request MAY succeed
        @exception CdbPermanentError: An unexpected internal error

        """
        try:
            xml = "<GeometryID  value='" + str(geometry_id) + "' comment='" + str(comment) + "' runmin='" + str(run_start) +"'>"
            for module in modules:
                xml = xml + "<ModuleName name='" + str(module['name']) + "' "
                xml = xml + "dx='" + str(module['dx']) + "' "
                xml = xml + "dx_err='" + str(module['dx_err']) + "' "
                xml = xml + "dy='" + str(module['dy']) + "' "
                xml = xml + "dy_err='" + str(module['dy_err']) + "' "
                xml = xml + "dz='" + str(module['dz']) + "' "
                xml = xml + "dz_err='" + str(module['dz_err']) + "' "
                xml = xml + "dx_rot='" + str(module['dx_rot']) + "' "
                xml = xml + "dx_rot_err='" + str(module['dx_rot_err']) + "' "
                xml = xml + "dy_rot='" + str(module['dy_rot']) + "' "
                xml = xml + "dy_rot_err='" + str(module['dy_rot_err']) + "' "
                xml = xml + "dz_rot='" + str(module['dz_rot']) + "' "
                xml = xml + "dz_rot_err='" + str(module['dz_rot_err']) + "' />"
            xml = xml + "</GeometryID>"

        except KeyError, exception:
            raise CdbPermanentError("Missing value for " + str(exception))

        ret = self.set_corrections_xml(xml)

        return ret