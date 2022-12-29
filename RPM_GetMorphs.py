import bpy


class RPM_OT_Get_Morphs(bpy.types.Operator):
    bl_idname = "rpm.get_morphs"
    bl_label = "RPM_Get_Morphs"
    bl_description = "Get morphs from lists"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def get_morph_targets(self, context):

        viseme_list = ['viseme_sil', 'viseme_PP', 'viseme_FF', 'viseme_TH', 'viseme_DD', 'viseme_kk', 'viseme_CH',
                       'viseme_SS', 'viseme_nn', 'viseme_RR', 'viseme_aa', 'viseme_E', 'viseme_I', 'viseme_O', 'viseme_U']

        ARKit_list = ['eyeBlinkLeft', 'eyeLookDownLeft', 'eyeLookInLeft', 'eyeLookOutLeft', 'eyeLookUpLeft', 'eyeSquintLeft', 'eyeWideLeft', 'eyeBlinkRight', 'eyeLookDownRight', 'eyeLookInRight', 'eyeLookOutRight', 'eyeLookUpRight', 'eyeSquintRight', 'eyeWideRight', 'jawForward', 'jawLeft', 'jawRight', 'jawOpen', 'mouthClose', 'mouthFunnel', 'mouthPucker', 'mouthLeft', 'mouthRight', 'mouthSmileLeft', 'mouthSmileRight', 'mouthFrownLeft', 'mouthFrownRight',
                      'mouthDimpleLeft', 'mouthDimpleRight', 'mouthStretchLeft', 'mouthStretchRight', 'mouthRollLower', 'mouthRollUpper', 'mouthShrugLower', 'mouthShrugUpper', 'mouthPressLeft', 'mouthPressRight', 'mouthLowerDownLeft', 'mouthLowerDownRight', 'mouthUpperUpLeft', 'mouthUpperUpRight', 'browDownLeft', 'browDownRight', 'browInnerUp', 'browOuterUpLeft', 'browOuterUpRight', 'cheekPuff', 'cheekSquintLeft', 'cheekSquintRight', 'noseSneerLeft', 'noseSneerRight', 'tongueOut']

        additional_blendshape_list = ['mouthOpen', 'mouthSmile', 'eyesClosed', 'eyesLookUp', 'eyesLookDown']

        morph_list = viseme_list + ARKit_list + additional_blendshape_list

        if context.scene.RPM.morphTargets == 'all':
            context.scene.RPM.customMorphTargets.clear()
            for morph_target in morph_list:
                item = context.scene.RPM.customMorphTargets.add()
                item.name = morph_target
                item.value = True
                print(item.name)

        elif context.scene.RPM.morphTargets == 'ARKit':
            context.scene.RPM.customMorphTargets.clear()
            for morph_target in morph_list:
                if morph_target in ARKit_list:
                    item = context.scene.RPM.customMorphTargets.add()
                    item.name = morph_target
                    item.value = True
                    print(item.name)

        elif context.scene.RPM.morphTargets == 'Oculus Visemes':
            context.scene.RPM.customMorphTargets.clear()
            for morph_target in morph_list:
                if morph_target in viseme_list:
                    item = context.scene.RPM.customMorphTargets.add()
                    item.name = morph_target
                    item.value = True
                    print(item.name)

        elif context.scene.RPM.morphTargets == 'none':
            context.scene.RPM.customMorphTargets.clear()

        elif context.scene.RPM.morphTargets == 'custom':
            context.scene.RPM.customMorphTargets.clear()

        return None

    def execute(self, context):
        self.get_morph_targets(context=context)
        return {'FINISHED'}
