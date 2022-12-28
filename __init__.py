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
from . import auto_load
from . RPM_ui import RPM_Globals

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


auto_load.init()


def register():
    auto_load.register()
    bpy.types.Scene.RPM = bpy.props.PointerProperty(type=RPM_Globals)


def unregister():
    del bpy.types.Scene.RPM
    auto_load.unregister()
