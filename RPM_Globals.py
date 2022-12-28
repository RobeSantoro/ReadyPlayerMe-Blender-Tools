import bpy


class RPM_Globals(bpy.types.PropertyGroup):
    avatar_name: bpy.props.StringProperty(
        name="Avatar Name",
        description="The name of the avatar you want to use",
        default="Robe")

    avatar_id: bpy.props.StringProperty(
        name="Avatar ID",
        description="The ID of the avatar you want to use",
        default="63ac69548d4fc7b44d50de62")

    quality: bpy.props.EnumProperty(
        name="Quality",
        description="""\
The quality of the avatar you want to use: \n\n \
not_set: The avatar will be downloaded without any optimization. (default)  \n\n \
low:     meshLod=2, textureSizeLimit=256, textureAtlas=256, morphTargets=none \n\n \
medium:  meshLod=1, textureSizeLimit=512, textureAtlas=512, morphTargets=none) \n\n \
high:    meshLod=0, textureSizeLimit=1024, textureAtlas=1024, morphTargets=none)\n\n \
""",
        items=[
            ("not_set", "-", "Not set"),
            ("low", "Low", "Low quality"),
            ("medium", "Medium", "Medium quality"),
            ("high", "High", "High quality")
        ],
        default="not_set"
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
            ("256", "256", "256x256"),
            ("512", "512", "512x512"),
            ("1024", "1024", "1024x1024")
        ],
        default="1024"
    )
