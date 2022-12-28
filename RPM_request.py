import bpy
import requests


def rename_armature():
    # Get the armature
    armature = bpy.data.objects["Armature"]

    # Get the quality
    quality = bpy.context.scene.RPM.quality

    if quality != "not_set":
        # Rename the armature
        armature.name += f"_{quality}"


class RPM_OT_Request(bpy.types.Operator):

    bl_idname = "rpm.make_request"
    bl_label = "Download Avatar"
    bl_description = "Make Request to RPM API to get avatar .glb file"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        avatar_id = context.scene.RPM.avatar_id

        if avatar_id == "":
            self.report({"ERROR"}, "No avatar ID provided")
            return {"CANCELLED"}

        url_to_request = f"https://api.readyplayer.me/v1/avatars/{avatar_id}.glb"

        quality = context.scene.RPM.quality
        # ?quality=low (meshLod=2, textureSizeLimit=256, textureAtlas=256, morphTargets=none)
        # ?quality=medium (meshLod=1, textureSizeLimit=512, textureAtlas=512, morphTargets=none)
        # ?quality=high (meshLod=0, textureSizeLimit=1024, textureAtlas=1024, morphTargets=none)
        print(quality)

        if quality != "not_set":
            url_to_request += f"?quality={quality}"

        response = requests.get(url_to_request)

        if response.status_code == 200:
            self.report({"INFO"}, "Avatar downloaded successfully")

            # Save the file
            with open("avatar.glb", "wb") as f:
                f.write(response.content)

            # Import the file as glTF
            bpy.ops.import_scene.gltf(filepath="avatar.glb")

            # Rename the armature by adding the quality to the name
            rename_armature()

        else:
            self.report({"ERROR"}, "Avatar could not be downloaded")

        return {"FINISHED"}
