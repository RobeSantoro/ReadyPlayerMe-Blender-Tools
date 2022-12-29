import bpy


def update_quality_settings(self, context):

    if self.quality == "not-set":
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


class RPM_MorphTarget(bpy.types.PropertyGroup):
    """Collection of Morph Targets"""
    value: bpy.props.BoolProperty(name="Value")


class RPM_Globals(bpy.types.PropertyGroup):

    avatar_name: bpy.props.StringProperty(
        name="Avatar Name",
        description="The name of the avatar for the object name",
        default="Robe")

    avatar_id_type: bpy.props.EnumProperty(
        name="Avatar ID Type",
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
        name="Avatar Shortcode",
        description="The shortcode of the avatar you want to use",
        default="QKCJNP")

    avatar_id: bpy.props.StringProperty(
        name="Avatar ID",
        description="The ID of the avatar you want to use",
        default="63ac69548d4fc7b44d50de62")

    quality: bpy.props.EnumProperty(
        name="Quality",
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
        name="Mesh LOD",
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
        name="Texture Size Limit",
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
        name="Texture Atlas",
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
        name="Morph Targets",
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
            ("all", "All (default)", "Include all morph targets"),
            ("Default", "Standard", "Include Standard targets"),
            ("ARKit", "ARKit", "Blend shapes compatible with Apple ARKit (52)"),
            ("Oculus Visemes", "Oculus Visemes", "Visemes compatible with Oculus LipSync SDK (15)"),
            ("custom", "Custom", "Include custom morph targets from from RPM_MorphTarget Collection"),
        ],
        default="all"
    )

    customMorphTargets: bpy.props.CollectionProperty(
        type=RPM_MorphTarget,
        name="Custom Morph Targets",
        description="Custom Morph Targets"
    )

    customMorphTargetsTextArea: bpy.props.StringProperty(

        name="Custom Morph Targets Text Area",
        description="""\
Custom Morph Targets Text Area\n\
Enter the morph targets you want to include separated by a comma.\n\
""",
        default="mouthOpen,mouthSmile,eyesClosed,eyesLookUp,eyesLookDown"
    )
