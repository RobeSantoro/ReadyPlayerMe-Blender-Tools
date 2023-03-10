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

from . RPM_GetMorphs import RPM_OT_Get_Morphs

from . RPM_Globals import RPM_MorphTarget
from . RPM_Globals import RPM_Globals

from . RPM_API_Request import RPM_OT_Request

from . RPM_ui import RPM_PT_MenuMain
from . RPM_ui import RPM_PT_MenuUrlParams
from . RPM_ui import RPM_PT_MenuQualitySettings
from . RPM_ui import RPM_PT_MenuDownload
from . RPM_ui import RPM_PT_MenuTextureSettings
from . RPM_ui import RPM_PT_MenuPoseSettings

bl_info = {
    "name": "Ready Player Me Tools",
    "author": "Robe Santoro",
    "description": "",
    "blender": (3, 3, 0),
    "version": (1, 0, 0),
    "location": "View3D > UI > Ready Player Me",
    "warning": "",
    "category": "Ready Player Me"
}

classes = (
    RPM_OT_Get_Morphs,
    RPM_MorphTarget,
    RPM_Globals,
    RPM_OT_Request,
    RPM_PT_MenuMain,
    RPM_PT_MenuUrlParams,
    RPM_PT_MenuQualitySettings,
    RPM_PT_MenuDownload,
    RPM_PT_MenuTextureSettings,
    RPM_PT_MenuPoseSettings
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.RPM = bpy.props.PointerProperty(type=RPM_Globals)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.RPM
