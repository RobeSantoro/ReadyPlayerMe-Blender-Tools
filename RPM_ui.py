import bpy
from .RPM_Globals import RPM_Globals


class ReadyPlayerMePanel():
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ready Player Me"


class RPM_PT_MenuMain(bpy.types.Panel, ReadyPlayerMePanel):

    bl_label = "Ready Player Me"

    def draw(self, context):

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        col.scale_y = 1.2
        col.alignment = "EXPAND"
        col.label(text="Get your avatar:")
        col.operator("wm.url_open", text="https://readyplayer.me", icon="WORLD").url = "https://readyplayer.me"


class RPM_PT_MenuUrlParams(bpy.types.Panel, ReadyPlayerMePanel):

    bl_label = "API Request"

    def draw(self, context):

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col0 = layout.column(align=True)
        col0.prop(context.scene.RPM, "avatar_id_type", text="ID type")

        col1 = layout.column(align=True)
        col1.use_property_decorate = False
        col1.use_property_split = False
        col1.scale_y = 1.2

        if context.scene.RPM.avatar_id_type == "url":
            col1.prop(context.scene.RPM, "avatar_id", text="ID")
        elif context.scene.RPM.avatar_id_type == "shortcode":
            col1.prop(context.scene.RPM, "avatar_shortcode", text="CODE")

        col2 = layout.column(align=True)
        col2.use_property_split = False
        col2.use_property_decorate = True

        col2.prop(context.scene.RPM, "quality", text="Quality", expand=False)
        col2.scale_y = 1.3


class RPM_PT_MenuQualitySettings(bpy.types.Panel, ReadyPlayerMePanel):

    bl_label = "Quality Settings"
    bl_parent_id = "RPM_PT_MenuUrlParams"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context is not None

    def draw(self, context):

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()

        box.use_property_split = True
        box.use_property_decorate = False
        box.scale_y = 1

        box.prop(context.scene.RPM, "meshLod", text="LOD")
        box.prop(context.scene.RPM, "textureSizeLimit", text="Tex Limit")
        box.prop(context.scene.RPM, "textureAtlas", text="Atlas")

        row0 = box.row(align=True)
        row0.prop(context.scene.RPM, "morphTargets", text="Morph Targets")
        row0.operator("rpm.get_morphs", text="", icon="IMPORT")

        if context.scene.RPM.morphTargets == "custom":

            box.operator("wm.url_open", text="Check Supported Morphs",
                         icon="WORLD").url = "https://docs.readyplayer.me/ready-player-me/avatars/avatar-creator/customization-and-configuration#list-of-supported-facial-animation-blend-shapes"

            # box.label(text="Custom Targets List:")
            row1 = box.row(align=True)
            row1.prop(context.scene.RPM, "custom_morph_targets_textarea", text="")
            row1.scale_y = 1.3

            row2 = box.row(align=True, heading="Add Targets:")
            row2.alignment = "EXPAND"
            row2.use_property_split = True

            row2.prop(context.scene.RPM, "custom_morph_targets_enable_ARKit", text="ARKit")
            row2.prop(context.scene.RPM, "custom_morph_targets_enable_Oculus_Visemes", text="Oculus Visemes")

        if context.scene.RPM.morphTargets != "all":
            if context.scene.RPM.morphTargets != "none":
                if context.scene.RPM.morphTargets != "custom":
                    box.prop(context.scene.RPM, "custom_morph_targets", text="Morphs to apply")


class RPM_PT_MenuTextureSettings(bpy.types.Panel, ReadyPlayerMePanel):

    bl_label = "Texture Settings"
    bl_parent_id = "RPM_PT_MenuUrlParams"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context is not None

    def draw(self, context):

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()

        box.use_property_split = True
        box.use_property_decorate = False
        box.scale_y = 1

        box.prop(context.scene.RPM, "baseColor", text="Base Color")
        box.prop(context.scene.RPM, "normal", text="Normal")
        box.prop(context.scene.RPM, "metallicRoughness", text="Metallic/Roughness")
        box.prop(context.scene.RPM, "emissive", text="Emissive")
        box.prop(context.scene.RPM, "occlusion", text="Occlusion")
        box.prop(context.scene.RPM, "none", text="None")


class RPM_PT_MenuDownload(bpy.types.Panel, ReadyPlayerMePanel):

    bl_label = "Download Avatar"

    def draw(self, context):

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col3 = layout.column(align=True)
        col3.scale_y = 1.3

        col3.prop(context.scene.RPM, "avatar_name")
        col3.operator("rpm.make_request", text="Download Avatar", icon="IMPORT")
