import bpy
from math import radians as R  # to convert rotation to degrees

# ------------ Blender Info ------------ #
bl_info = {
    "name": "Weld Model Maker",
    "author": "Fyahh Dragon <dragon.fyahh@gmail.com>",
    "version": (0, 1, 2),
    "blender": (2, 91, 0),
    "category": "Mesh",
    "location": "3D Viewport",
    "description": "Generate a Weld model at intersect of 2 objects",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}


# Main Operator  - generates mesh (for now just a rotated Cube)
class MESH_OT_weld_model(bpy.types.Operator):
    """ generate weld model """  # tool-tip description
    bl_idname = "mesh.weld_model"  # identifier... goes after bpy.ops.
    bl_label = "Generate Weld"  # label that appears in menus and buttons.
    bl_options = {'REGISTER', 'UNDO'}  # to register and redo

    size: bpy.props.FloatProperty(  # property for redo
        name="Size",
        description="Size of Weld model",
        default=0.5,
        min=0.1,
        soft_max=3.0)

    location: bpy.props.FloatVectorProperty(  # property for redo
        name="Location",
        description="Location of Weld model",
        default=(0.0, 0.0, 1.0),
        soft_min=-5,
        soft_max=5,
        subtype='COORDINATES',
        size=3)

    rotation: bpy.props.FloatVectorProperty(  # property for redo
        name="Rotation",
        description="Rotation of Weld model",
        default=(R(0.0), R(45.0), R(0.0)),
        soft_min=R(-180),
        soft_max=R(180),
        subtype='EULER',
        unit='ROTATION',
        size=3)

    @classmethod  # poll to validate
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):  # Main execute staement
        bpy.ops.mesh.primitive_cube_add(  # adds a Cube
                size=self.size,           # with
                location=self.location,   # defalt
                rotation=self.rotation)   # settings

        return {'FINISHED'}  # for Blender


# 3DViewport Tool Panel -generate button. TO DO-> add Properties from Operator
class VIEW3D_PT_weld_generate(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Weld Maker"  # TAB label
    bl_label = "Generate Weld"  # section header label

    def draw(self, context):  # UI Draw function
        col = self.layout.column(align=True)
        col.operator('mesh.weld_model',
                     text='Make Weld',
                     icon='META_CUBE')  # Operator Button


# MENU Item function
def mesh_add_menu_draw(self, context):
    self.layout.operator('mesh.weld_model',
                         text='Make Weld',
                         icon='META_CUBE')


blender_classes = [           # list for register
    VIEW3D_PT_weld_generate,  # Panel
    MESH_OT_weld_model,       # Operator
]


def register():
    bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)  # register MENU
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)  # register from list


def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)  # unregister MENU
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)  # unregister from list
