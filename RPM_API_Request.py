import os
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
        url_params_string = ''

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

        textureChannels = []
        textureChannels_string = ''
        # ?textureChannels=baseColor,normal,metallicRoughness,emissive,occlusion,none (default)

        # ?quality
        if quality != "not_set":
            url_params_list.append(f"quality={quality}")

        # ?meshLod
        if meshLod != 0 or len(url_params_list) > 0:
            url_params_list.append(f"meshLod={meshLod}")

        # ?textureSizeLimit
        if textureSizeLimit != '1024' or len(url_params_list) > 0:
            url_params_list.append(f"textureSizeLimit={textureSizeLimit}")

        # ?textureAtlas
        if textureAtlas != "none" or len(url_params_list) > 0:
            url_params_list.append(f"textureAtlas={textureAtlas}")

        # ?morphTargets
        if morphTargets != "all":
            if morphTargets == "custom":
                morphTargets = context.scene.RPM.custom_morph_targets_textarea
                if context.scene.RPM.custom_morph_targets_enable_ARKit:
                    morphTargets += ",ARKit"
                if context.scene.RPM.custom_morph_targets_enable_Oculus_Visemes:
                    morphTargets += ",Oculus Visemes"
                url_params_list.append(f"morphTargets={morphTargets}")
            else:
                url_params_list.append(f"morphTargets={morphTargets}")

        # ?textureChannels
        if context.scene.RPM.baseColor:
            textureChannels.append("baseColor")
        if context.scene.RPM.normal:
            textureChannels.append("normal")
        if context.scene.RPM.metallicRoughness:
            textureChannels.append("metallicRoughness")
        if context.scene.RPM.emissive:
            textureChannels.append("emissive")
        if context.scene.RPM.occlusion:
            textureChannels.append("occlusion")
        if context.scene.RPM.none:
            textureChannels = []
            textureChannels.append("none")
        if len(textureChannels) > 0:
            textureChannels_string = "textureChannels=" + ",".join(textureChannels)

        # ?pose
        if context.scene.RPM.pose == "T":
            url_params_list.append("pose=T")

        # ?useDracoMeshCompression
        if context.scene.RPM.useDracoMeshCompression:
            url_params_list.append("useDracoMeshCompression=true")

        url_params_string = "&".join(url_params_list) + f"{'&' if len(textureChannels_string) > 0 else '' }" + textureChannels_string

        url = url_id + f"{'?' if len(url_params_string) > 0 else ''}{url_params_string}"

        print('--------------------------------------------')
        print()
        print(f'Making request to Ready Player Me API')
        print()
        print(f'{url}')
        print()
        print(f'quality: {quality}')
        print(f'meshLod: {meshLod}')
        print(f'textureSizeLimit: {textureSizeLimit}')
        print(f'textureAtlas: {textureAtlas}')
        print(f'morphTargets: {morphTargets}')
        print()
        print(f'textureChannels: {textureChannels if len(textureChannels) > 0 else "All"}')
        print()

        response = requests.get(url)

        if response.status_code == 200:
            self.report({"INFO"}, "Avatar downloaded successfully")

            # Check if the blend file has been saved
            if bpy.data.filepath == "":
                self.report({"ERROR"}, "Please save the blend file before downloading the avatar")
                return {"FINISHED"}

            # Get the path of the blend file
            blend_path = bpy.path.abspath("//")

            print(f'blend_path: {blend_path}')

            # Save the file
            with open(f"{blend_path}avatar.glb", "wb") as f:
                f.write(response.content)

            # Import the file as glTF
            bpy.ops.import_scene.gltf(filepath=f"{blend_path}avatar.glb")

            # Delete the file after importing
            os.remove(f"{blend_path}avatar.glb")

            # Rename the armature by adding the params if any
            rename_armature(context, url_params_list)

        elif response.status_code == 404:
            self.report({"ERROR"}, "The requested avatar is not available")

        else:
            self.report({"ERROR"}, "Avatar could not be downloaded")

        return {"FINISHED"}
