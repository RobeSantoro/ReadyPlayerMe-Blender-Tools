import bpy
import requests


def rename_armature(context, url_params_list):

    if len(url_params_list) > 1:

        print()
        print(url_params_list)
        print()

        postfix = []

        if 'quality=low' in url_params_list:
            postfix.append('Low')
        elif 'quality=medium' in url_params_list:
            postfix.append('Med')
        elif 'quality=high' in url_params_list:
            postfix.append('Hi')

        if 'meshLod=0' in url_params_list:
            postfix.append('LOD0')
        elif 'meshLod=1' in url_params_list:
            postfix.append('LOD1')
        elif 'meshLod=2' in url_params_list:
            postfix.append('LOD2')

        if 'textureSizeLimit=256' in url_params_list:
            postfix.append('limit256')
        elif 'textureSizeLimit=512' in url_params_list:
            postfix.append('limit512')
        elif 'textureSizeLimit=1024' in url_params_list:
            postfix.append('limit1024')

        if 'textureAtlas=256' in url_params_list:
            postfix.append('atlas256')
        elif 'textureAtlas=512' in url_params_list:
            postfix.append('atlas512')
        elif 'textureAtlas=1024' in url_params_list:
            postfix.append('atlas1024')

        context.object.name = context.scene.RPM.avatar_name + '_' + '_'.join(postfix)

    elif len(url_params_list) <= 1:
        context.object.name = context.scene.RPM.avatar_name


class RPM_OT_Request(bpy.types.Operator):

    bl_idname = "rpm.make_request"
    bl_label = "Download Avatar"
    bl_description = "Make Request to RPM API to get avatar .glb file"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        if context.scene.RPM.avatar_id_type == 'shortcode':
            avatar_id = context.scene.RPM.avatar_shortcode
        else:
            avatar_id = context.scene.RPM.avatar_id

        url_id = f"https://api.readyplayer.me/v1/avatars/{avatar_id}.glb"

        url_params_list = []

        quality = context.scene.RPM.quality
        # ?quality=low (meshLod=2, textureSizeLimit=256, textureAtlas=256, morphTargets=none)
        # ?quality=medium (meshLod=1, textureSizeLimit=512, textureAtlas=512, morphTargets=none)
        # ?quality=high (meshLod=0, textureSizeLimit=1024, textureAtlas=1024, morphTargets=none)

        meshLod = context.scene.RPM.meshLod
        # ?meshLod=0 (highest quality) (default)
        # ?meshLod=1 (medium quality)
        # ?meshLod=2 (lowest quality)

        textureSizeLimit = context.scene.RPM.textureSizeLimit
        # ?textureSizeLimit=256
        # ?textureSizeLimit=512
        # ?textureSizeLimit=1024 (default)

        textureAtlas = context.scene.RPM.textureAtlas
        # ?textureAtlas=none (default)
        # ?textureAtlas=256
        # ?textureAtlas=512
        # ?textureAtlas=1024

        morphTargets = context.scene.RPM.morphTargets
        # ?morphTargets=none
        # ?morphTargets=default
        # ?morphTargets=ARKit
        # ?morphTargets=Oculus Visemes
        # + or any morph targets, separated with comma
        # The default value is "Default,ARKit,Oculus Visemes"

        if quality != "not_set":
            url_params_list.append(f"quality={quality}")

        if meshLod != 0 or len(url_params_list) > 0:
            url_params_list.append(f"meshLod={meshLod}")

        if textureSizeLimit != '1024' or len(url_params_list) > 0:
            url_params_list.append(f"textureSizeLimit={textureSizeLimit}")

        if textureAtlas != "none" or len(url_params_list) > 0:
            url_params_list.append(f"textureAtlas={textureAtlas}")

        if morphTargets != "all":
            url_params_list.append(f"morphTargets={morphTargets}")

        url_params_string = "&".join(url_params_list)

        url = url_id + "?" + url_params_string

        print('--------------------------------------------')
        print()
        print(f'Making request to Ready Player Me API')
        print()
        print(url_params_string if len(url_params_string) != 0 else "No params")
        print()
        print(f'{url}')
        print()
        print(f'quality: {quality}')
        print(f'meshLod: {meshLod}')
        print(f'textureSizeLimit: {textureSizeLimit}')
        print(f'textureAtlas: {textureAtlas}')
        print(f'morphTargets: {morphTargets}')
        print()

        response = requests.get(url)

        if response.status_code == 200:
            self.report({"INFO"}, "Avatar downloaded successfully")

            # Save the file
            with open("avatar.glb", "wb") as f:
                f.write(response.content)

            # Import the file as glTF
            bpy.ops.import_scene.gltf(filepath="avatar.glb")

            # Rename the armature by adding the params if any
            rename_armature(context, url_params_list)

        elif response.status_code == 404:
            self.report({"ERROR"}, "The requested avatar is not available")

        else:
            self.report({"ERROR"}, "Avatar could not be downloaded")

        return {"FINISHED"}
