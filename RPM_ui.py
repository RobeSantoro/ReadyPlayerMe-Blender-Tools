import bpy


# Create a new scene property group
class RPM_Globals(bpy.types.PropertyGroup):
    avatar_id: bpy.props.StringProperty(
        name="Avatar ID",
        description="The ID of the avatar you want to use",
        default="63ac69548d4fc7b44d50de62")

    quality: bpy.props.EnumProperty(
        name="Quality",
        description="The quality of the avatar you want to use",
        items=[
            ("not_set", "-", "Not set"),
            ("low", "Low", "Low quality"),
            ("medium", "Medium", "Medium quality"),
            ("high", "High", "High quality")
        ],
        default="not_set"
    )


# Create a new panel in the scene context of the properties editor
class RPM_PT_main(bpy.types.Panel):

    bl_label = "Ready Player Me"
    bl_idname = "RPM_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ready Player Me"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Get your avatar ID:")
        layout.operator("wm.url_open", text="RPM Website", icon="WORLD").url = "https://readyplayer.me"

        col = layout.column(align=True)
        col.use_property_decorate = False
        col.use_property_split = True
        col.prop(context.scene.RPM, "avatar_id")
        col.separator()
        col.prop(context.scene.RPM, "quality")

        layout.separator()
        layout.operator("rpm.make_request", text="Download Avatar", icon="IMPORT")
