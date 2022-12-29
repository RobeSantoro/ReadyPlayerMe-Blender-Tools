import bpy


def update_quality_settings(self, context):

    if self.quality == "not_set":
        self.meshLod = 0
        self.textureSizeLimit = "1024"
        self.textureAtlas = "none"
        self.morphTargets = "all"

        print()
        print('--------------------------------------------')
        print("Quality set to not-set")
        print(f'meshLod: {self.meshLod}')
        print(f'textureSizeLimit: {self.textureSizeLimit}')
        print(f'textureAtlas: {self.textureAtlas}')
        print(f'morphTargets: {self.morphTargets}')
        print('--------------------------------------------')

    elif self.quality == "low":
        self.meshLod = 2
        self.textureSizeLimit = "256"
        self.textureAtlas = "256"
        self.morphTargets = "none"

        print()
        print('--------------------------------------------')
        print("Quality set to low")
        print(f'meshLod: {self.meshLod}')
        print(f'textureSizeLimit: {self.textureSizeLimit}')
        print(f'textureAtlas: {self.textureAtlas}')
        print(f'morphTargets: {self.morphTargets}')
        print('--------------------------------------------')

    elif self.quality == "medium":
        self.meshLod = 1
        self.textureSizeLimit = "512"
        self.textureAtlas = "512"
        self.morphTargets = "none"

        print()
        print('--------------------------------------------')
        print("Quality set to medium")
        print(f'meshLod: {self.meshLod}')
        print(f'textureSizeLimit: {self.textureSizeLimit}')
        print(f'textureAtlas: {self.textureAtlas}')
        print(f'morphTargets: {self.morphTargets}')
        print('--------------------------------------------')

    elif self.quality == "high":
        self.meshLod = 0
        self.textureSizeLimit = "1024"
        self.textureAtlas = "1024"
        self.morphTargets = "none"

        print()
        print('--------------------------------------------')
        print("Quality set to high")
        print(f'meshLod: {self.meshLod}')
        print(f'textureSizeLimit: {self.textureSizeLimit}')
        print(f'textureAtlas: {self.textureAtlas}')
        print(f'morphTargets: {self.morphTargets}')
        print('--------------------------------------------')

    return None


def update_morph_settings(self, context):
    if self.morphTargets != "custom":
        self.custom_morph_targets_enable_ARKit = False
        self.custom_morph_targets_enable_Oculus_Visemes = False


def update_texture_to_none(self, context):

    if self.none:
        self.baseColor = False
        self.normal = False
        self.metallicRoughness = False
        self.emissive = False
        self.occlusion = False

    return None


def update_texture_to_any(self, context):

    if self.baseColor or self.normal or self.metallicRoughness or self.emissive or self.occlusion:
        self.none = False

    return None


class RPM_MorphTarget(bpy.types.PropertyGroup):
    """Collection of Morph Targets"""
    value: bpy.props.BoolProperty(name="Value")


class RPM_Globals(bpy.types.PropertyGroup):

    avatar_name: bpy.props.StringProperty(
        name="avatar_name",
        description="The name of the avatar for the object name",
        default="Robe")

    avatar_id_type: bpy.props.EnumProperty(
        name="avatar_id_type",
        description="""\
The type of the avatar ID you want to use: \n\n \
shortcode:  The avatar shortcode (default) \n\n \
url:        The avatar ID in the URL \n\n \
""",
        items=[
            ("shortcode", "Shortcode", "The avatar shortcode"),
            ("url", "URL", "The avatar ID in the URL")
        ],
        default="url"
    )

    avatar_shortcode: bpy.props.StringProperty(
        name="avatar_shortcode",
        description="The shortcode of the avatar you want to use",
        default="QKCJNP")

    avatar_id: bpy.props.StringProperty(
        name="avatar_id",
        description="The ID of the avatar you want to use",
        default="63ac69548d4fc7b44d50de62")

    quality: bpy.props.EnumProperty(
        name="quality",
        description="""\
The quality of the avatar you want to use: \n\n \
not_set: The avatar will be downloaded without any optimization preset. (default)  \n\n \
low:     meshLod=2, textureSizeLimit=256, textureAtlas=256, morphTargets=none \n\n \
medium:  meshLod=1, textureSizeLimit=512, textureAtlas=512, morphTargets=none) \n\n \
high:    meshLod=0, textureSizeLimit=1024, textureAtlas=1024, morphTargets=none)\n\n\
All other values overwrite quality.
So e.g.
You can use quality=low and overwrite the LOD with 0 to get the high-res avatar. See Examples.\n\n\
""",
        items=[
            ("not_set", "-", "Not set"),
            ("low", "Low", "Low quality"),
            ("medium", "Medium", "Medium quality"),
            ("high", "High", "High quality")
        ],
        default="not_set",
        update=update_quality_settings
    )

    meshLod: bpy.props.IntProperty(
        name="meshLod",
        description=""" \
The level of detail of the mesh \n\n \
0 - No triangle count reduction is applied (default). \n\n \
1 - Retain 50% of the original triangle count. \n\n \
2 - Retain 25% of the original triangle count. \n\n \
""",
        default=0,
        min=0,
        max=2
    )

    textureSizeLimit: bpy.props.EnumProperty(
        name="textureSizeLimit",
        description=""" \
The maximum size of the textures \n\n \
256 - 256x256 \n\n \
512 - 512x512 \n\n \
1024 - 1024x1024 (default) \n\n \
""",
        items=[
            ("256", "256", "Limit textures to 256x256"),
            ("512", "512", "Limit textures to 512x512"),
            ("1024", "1024", "Limit textures to 1024x1024")
        ],
        default="1024"
    )

    textureAtlas: bpy.props.EnumProperty(
        name="textureAtlas",
        description=""" \
The size of the texture atlas \n\n \
none - Do not create a texture atlas (default) \n\n \
256 - Create a texture atlas of 256x256px \n\n \
512 - Create a texture atlas of 512x512px \n\n \
1024 - Create a texture atlas of 1024x1024px \n\n \
""",
        items=[
            ("none", "none", "Do not create a texture atlas"),
            ("256", "256", "Create a texture atlas of 256x256px"),
            ("512", "512", "Create a texture atlas of 512x512px"),
            ("1024", "1024", "Create a texture atlas of 1024x1024px"),
        ],
        default="none"
    )

    morphTargets: bpy.props.EnumProperty(
        name="morphTargets",
        description=""" \
The morph targets to include: \n\n \
none - Do not include any morph targets \n\n \
all - Include all morph targets (default) \n\n \
default - Include Default targets \n\n \
ARKit - Blend shapes compatible with Apple ARKit (52) \n\n \
Oculus Visemes - Visemes compatible with Oculus LipSync SDK (15) \n\n \
Custom - Include custom morph targets from RPM_MorphTarget Collection\n\n \
""",
        items=[
            ("none", "None", "Do not include any morph targets"),
            ("all", "All", "Include all morph targets"),
            ("Default", "Standard", "Include Standard targets"),
            ("ARKit", "ARKit", "Blend shapes compatible with Apple ARKit (52)"),
            ("Oculus Visemes", "Oculus Visemes", "Visemes compatible with Oculus LipSync SDK (15)"),
            ("custom", "Custom", "Include custom morph targets from from RPM_MorphTarget Collection"),
        ],
        default="all",
        update=update_morph_settings
    )

    custom_morph_targets: bpy.props.CollectionProperty(
        type=RPM_MorphTarget,
        name="custom_morph_targets",
        description="Custom Morph Targets"
    )

    custom_morph_targets_textarea: bpy.props.StringProperty(

        name="custom_morph_targets_textarea",
        description="""\
Custom Morph Targets Text Area\n\n\
Enter the morph targets you want to include separated by a comma.\n\n\
""",
        default="mouthOpen,mouthSmile,eyesClosed,eyesLookUp,eyesLookDown"
    )

    custom_morph_targets_enable_ARKit: bpy.props.BoolProperty(
        name="custom_morph_targets_enable_ARKit",
        description="Enable ARKit Morph Targets",
        default=False
    )

    custom_morph_targets_enable_Oculus_Visemes: bpy.props.BoolProperty(
        name="custom_morph_targets_enable_Oculus_Visemes",
        description="Enable Oculus Visemes Morph Targets",
        default=False
    )

    baseColor: bpy.props.BoolProperty(
        name="baseColor",
        description="Include Base Color Texture",
        default=False,
        update=update_texture_to_any
    )

    normal: bpy.props.BoolProperty(
        name="normal",
        description="Include Normal Texture",
        default=False,
        update=update_texture_to_any
    )

    metallicRoughness: bpy.props.BoolProperty(
        name="metallicRoughness",
        description="Include Metallic Roughness Texture",
        default=False,
        update=update_texture_to_any
    )

    emissive: bpy.props.BoolProperty(
        name="emissive",
        description="Include Emissive Texture",
        default=False,
        update=update_texture_to_any
    )

    occlusion: bpy.props.BoolProperty(
        name="occlusion",
        description="Include Occlusion Texture",
        default=False,
        update=update_texture_to_any
    )

    none: bpy.props.BoolProperty(
        name="none",
        description="Do not include any textures",
        default=False,
        update=update_texture_to_none
    )

    pose: bpy.props.EnumProperty(
        name="pose",
        description="""\
The pose to use for the avatar \n\n\
a-pose - Use the A-Pose (default)\n\n\
t-pose - Use the T-Pose  \n\n\
""",
        items=[
            ("a-pose", "A-Pose", "Use the A-Pose"),
            ("t-pose", "T-Pose", "Use the T-Pose")
        ],
        default="a-pose"
    )
