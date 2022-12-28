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

        col = layout.column(align=True)
        col.scale_y = 1.2
        col.alignment = "EXPAND"
        col.label(text="Get your avatar:")
        col.operator("wm.url_open", text="https://readyplayer.me", icon="WORLD").url = "https://readyplayer.me"

        col.separator()

        col1 = layout.column(align=True)
        col1.use_property_decorate = False
        col1.use_property_split = False
        col1.scale_y = 1.2

        col1.prop(context.scene.RPM, "avatar_id")

        col2 = layout.column(align=True)
        col2.use_property_split = False

        col2.prop(context.scene.RPM, "quality", text="Quality")
        col2.scale_y = 1.3

        box = layout.box()

        box.use_property_split = True
        box.use_property_decorate = False
        box.scale_y = 1.2

        box.prop(context.scene.RPM, "meshLod")
        box.prop(context.scene.RPM, "textureSizeLimit", text="Texture Limit")

        col3 = layout.column(align=True)
        col3.scale_y = 1.3

        col3.separator()
        col3.separator()

        col3.prop(context.scene.RPM, "avatar_name")
        col3.operator("rpm.make_request", text="Download Avatar", icon="IMPORT")
