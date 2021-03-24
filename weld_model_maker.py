import bpy

bl_info = {
    "name": "Mesh: Weld Generator",
    "author": "Fyahh Dragon <dragon.fyahh@gmail.com>",
    "version": (0, 1),
    "blender": (2, 91, 0),
    "category": "Mesh",
    "location": "3D Viewport",
    "description": "Generate a Weld model at intersect of 2 objects",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}


class MESH_OT_create_Weld(bpy.types.Operator):
    """ generate weld model """  # tool-tip description
    bl_idname = "mesh.weld_model"  # identifier... goes after bpy.ops.
    bl_label = "Generate Weld"  # label that appears in menus and buttons.
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(
                size=0.5,
                location=(0, 0, 2),
                rotation=(0, 45, 0))

        return {'FINISHED'}


class VIEW3D_PT_weld_generate(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Weld Maker"
    bl_label = "Generate Weld"

    def draw(self, context):
        col = self.layout.column(align=True)
        col.operator('mesh.weld_model',
                     text='Make Weld',
                     icon='META_CUBE')


def mesh_add_menu_draw(self, context):
    self.layout.operator('mesh.weld_model',
                         text='Make Weld',
                         icon='META_CUBE')


blender_classes = [
    VIEW3D_PT_weld_generate,
    MESH_OT_create_Weld,
]


def register():
    bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)


def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
