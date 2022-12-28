import bpy
from .RPM_Globals import RPM_Globals


class RPM_PT_main(bpy.types.Panel):

    bl_label = "Ready Player Me"
    bl_idname = "RPM_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ready Player Me"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Get your avatar ID:")
        layout.operator("wm.url_open", text="Ready Player Me Website", icon="WORLD").url = "https://readyplayer.me"

        layout.separator()

        col = layout.column(align=True)
        col.use_property_decorate = False
        col.use_property_split = True
        col.prop(context.scene.RPM, "avatar_id")

        col.separator()
        col.separator()

        col.prop(context.scene.RPM, "quality")
        col.prop(context.scene.RPM, "meshLod")

        layout.separator()
        layout.separator()

        layout.prop(context.scene.RPM, "avatar_name")
        layout.operator("rpm.make_request", text="Download Avatar", icon="IMPORT")
