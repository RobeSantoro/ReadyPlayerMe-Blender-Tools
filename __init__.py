# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from . RPM_Globals import RPM_MorphTarget
from . RPM_Globals import RPM_Globals

from . RPM_request import RPM_OT_Request
from . RPM_ui import RPM_PT_main

from . RPM_GetMorphs import RPM_OT_Get_Morphs

bl_info = {
    "name": "Ready Player Me Tools",
    "author": "Robe Santoro",
    "description": "",
    "blender": (3, 3, 0),
    "version": (0, 0, 1),
    "location": "View3D > UI > Ready Player Me",
    "warning": "",
    "category": "Ready Player Me"
}

classes = (
    RPM_MorphTarget,
    RPM_Globals,
    RPM_OT_Request,
    RPM_PT_main,
    RPM_OT_Get_Morphs
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.RPM = bpy.props.PointerProperty(type=RPM_Globals)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.RPM
