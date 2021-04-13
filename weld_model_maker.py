import bpy
from math import radians as R  # to convert rotation to degrees
import bmesh
# from bpy_extras.object_utils import AddObjectHelper


# ------------ Blender Info ------------ #
bl_info = {
    "name": "Weld Mesh Maker",
    "author": "Fyahh Dragon <dragon.fyahh@gmail.com>",
    "version": (0, 2, 0),
    "blender": (2, 91, 0),
    "category": "Mesh",
    "location": "3D Viewport",
    "description": "Generate an adjustable Weld model.",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

#################################################
#           MESH DATA function                  #
#      contains data for "Weld Segment"         #
#              and "Weld Path"                  #
#################################################
# width, height, depth


def weld_data():
    """
    This function returns vertex and face arrays.
    no actual mesh data creation is done here.
    """

    verts = [
        (0.004, 0.001429, -0.0),
        (0.003893, 0.001429, -0.0),
        (0.0036, 0.001429, -0.0),
        (0.0032, 0.001429, -0.0),
        (0.0028, 0.001429, -0.0),
        (0.002507, 0.001429, -0.0),
        (0.0024, 0.001429, -0.0),
        (0.003923, 0.002125, 1e-06),
        (0.003818, 0.002107, 6.3e-05),
        (0.003531, 0.002056, 9.3e-05),
        (0.003139, 0.001986, 8.7e-05),
        (0.002746, 0.001916, 5.9e-05),
        (0.002459, 0.001865, 2.9e-05),
        (0.002354, 0.001429, -0.0),
        (0.003696, 0.002795, -2e-06),
        (0.003596, 0.002759, 0.000192),
        (0.003326, 0.002659, 0.000297),
        (0.002956, 0.002522, 0.000286),
        (0.002587, 0.002385, 0.000198),
        (0.002316, 0.002285, 9.4e-05),
        (0.002217, 0.001429, -0.0),
        (0.003326, 0.003413, -1.2e-05),
        (0.003237, 0.00336, 0.000321),
        (0.002993, 0.003214, 0.00051),
        (0.002661, 0.003016, 0.000503),
        (0.002328, 0.002817, 0.000361),
        (0.002085, 0.002672, 0.000179),
        (0.001996, 0.001429, -1e-06),
        (0.002828, 0.003954, -0.0),
        (0.002753, 0.003886, 0.000403),
        (0.002546, 0.003701, 0.000661),
        (0.002263, 0.003449, 0.000687),
        (0.00198, 0.003196, 0.00052),
        (0.001773, 0.003011, 0.000269),
        (0.001697, 0.001429, -0.0),
        (0.002222, 0.004398, 0.0),
        (0.002163, 0.004319, 0.000426),
        (0.002, 0.004101, 0.000724),
        (0.001778, 0.003804, 0.000742),
        (0.001556, 0.003507, 0.000643),
        (0.001393, 0.00329, 0.000346),
        (0.001333, 0.001429, 0.0),
        (0.001531, 0.004728, 0.0),
        (0.00149, 0.00464, 0.000426),
        (0.001378, 0.004398, 0.00073),
        (0.001225, 0.004068, 0.000784),
        (0.001072, 0.003738, 0.000717),
        (0.000959, 0.003497, 0.000401),
        (0.000918, 0.001429, 1e-06),
        (0.00078, 0.004931, 0.0),
        (0.000759, 0.004838, 0.000426),
        (0.000702, 0.004581, 0.00073),
        (0.000624, 0.004231, 0.000784),
        (0.000546, 0.003881, 0.00073),
        (0.000489, 0.003624, 0.000425),
        (0.000468, 0.001429, 2e-06),
        (0.0, 0.005, 0.0),
        (0.0, 0.004904, 0.000426),
        (0.0, 0.004643, 0.00073),
        (0.0, 0.004286, 0.000784),
        (0.0, 0.003929, 0.00073),
        (0.0, 0.003667, 0.000426),
        (0.0, 0.001429, 2e-06),
        (-0.00078, 0.004931, 0.0),
        (-0.000759, 0.004838, 0.000426),
        (-0.000702, 0.004581, 0.00073),
        (-0.000624, 0.004231, 0.000784),
        (-0.000546, 0.003881, 0.00073),
        (-0.000489, 0.003624, 0.000425),
        (-0.000468, 0.001429, 2e-06),
        (-0.001531, 0.004728, 0.0),
        (-0.00149, 0.00464, 0.000426),
        (-0.001378, 0.004398, 0.00073),
        (-0.001225, 0.004068, 0.000784),
        (-0.001072, 0.003738, 0.000717),
        (-0.000959, 0.003497, 0.000401),
        (-0.000918, 0.001429, 1e-06),
        (-0.002222, 0.004398, 0.0),
        (-0.002163, 0.004319, 0.000426),
        (-0.002, 0.004101, 0.000724),
        (-0.001778, 0.003804, 0.000742),
        (-0.001556, 0.003507, 0.000643),
        (-0.001393, 0.00329, 0.000346),
        (-0.001333, 0.001429, 0.0),
        (-0.002828, 0.003954, -0.0),
        (-0.002753, 0.003886, 0.000403),
        (-0.002546, 0.003701, 0.000661),
        (-0.002263, 0.003449, 0.000687),
        (-0.00198, 0.003196, 0.00052),
        (-0.001773, 0.003011, 0.000269),
        (-0.001697, 0.001429, -0.0),
        (-0.003326, 0.003413, -1.2e-05),
        (-0.003237, 0.00336, 0.000321),
        (-0.002993, 0.003214, 0.00051),
        (-0.002661, 0.003016, 0.000503),
        (-0.002328, 0.002817, 0.000361),
        (-0.002085, 0.002672, 0.000179),
        (-0.001996, 0.001429, -1e-06),
        (-0.003696, 0.002795, -2e-06),
        (-0.003596, 0.002759, 0.000192),
        (-0.003326, 0.002659, 0.000297),
        (-0.002956, 0.002522, 0.000286),
        (-0.002587, 0.002385, 0.000198),
        (-0.002316, 0.002285, 9.4e-05),
        (-0.002217, 0.001429, -0.0),
        (-0.003923, 0.002125, 1e-06),
        (-0.003818, 0.002107, 6.3e-05),
        (-0.003531, 0.002056, 9.3e-05),
        (-0.003139, 0.001986, 8.7e-05),
        (-0.002746, 0.001916, 5.9e-05),
        (-0.002459, 0.001865, 2.9e-05),
        (-0.002354, 0.001429, -0.0),
        (-0.004, 0.001429, -0.0),
        (-0.003893, 0.001429, -0.0),
        (-0.0036, 0.001429, -0.0),
        (-0.0032, 0.001429, -0.0),
        (-0.0028, 0.001429, -0.0),
        (-0.002507, 0.001429, -0.0),
        (-0.0024, 0.001429, -0.0),
        (0.004, 0.0, -0.0),
        (0.003893, 0.0, -0.0),
        (0.0036, 0.0, -0.0),
        (0.0032, 0.0, -0.0),
        (0.0028, 0.0, -0.0),
        (0.002507, 0.0, -0.0),
        (0.0024, -0.0, -0.0),
        (0.002354, -0.0, -0.0),
        (0.002217, -0.0, -0.0),
        (0.001996, -0.0, -1e-06),
        (0.001697, -0.0, -0.0),
        (0.001333, -0.0, 0.0),
        (0.000918, -0.0, 1e-06),
        (0.000468, -0.0, 2e-06),
        (0.0, -0.0, 2e-06),
        (-0.000468, -0.0, 2e-06),
        (-0.000918, -0.0, 1e-06),
        (-0.001333, -0.0, 0.0),
        (-0.001697, -0.0, -0.0),
        (-0.001996, -0.0, -1e-06),
        (-0.002217, -0.0, -0.0),
        (-0.002354, -0.0, -0.0),
        (-0.004, 0.0, -0.0),
        (-0.003893, 0.0, -0.0),
        (-0.0036, 0.0, -0.0),
        (-0.0032, 0.0, -0.0),
        (-0.0028, 0.0, -0.0),
        (-0.002507, 0.0, -0.0),
        (-0.0024, -0.0, -0.0),
        (0.004, 0.001429, -0.000205),
        (0.003923, 0.002125, -0.000203),
        (0.003696, 0.002795, -0.000206),
        (0.003326, 0.003413, -0.000216),
        (0.002828, 0.003954, -0.000205),
        (0.002222, 0.004398, -0.000204),
        (0.001531, 0.004728, -0.000204),
        (0.00078, 0.004931, -0.000204),
        (0.0, 0.005, -0.000204),
        (-0.00078, 0.004931, -0.000204),
        (-0.001531, 0.004728, -0.000204),
        (-0.002222, 0.004398, -0.000204),
        (-0.002828, 0.003954, -0.000205),
        (-0.003326, 0.003413, -0.000216),
        (-0.003696, 0.002795, -0.000206),
        (-0.003923, 0.002125, -0.000203),
        (-0.004, 0.001429, -0.000205),
        (0.004, 0.0, -0.000205),
        (0.003893, 0.0, -0.000205),
        (0.0036, 0.0, -0.000205),
        (0.0032, 0.0, -0.000205),
        (0.0028, 0.0, -0.000205),
        (0.002507, 0.0, -0.000205),
        (0.0024, -0.0, -0.000205),
        (0.002354, -0.0, -0.000205),
        (0.002217, -0.0, -0.000205),
        (0.001996, -0.0, -0.000205),
        (0.001697, -0.0, -0.000205),
        (0.001333, -0.0, -0.000204),
        (0.000918, -0.0, -0.000203),
        (0.000468, -0.0, -0.000202),
        (0.0, -0.0, -0.000202),
        (-0.000468, -0.0, -0.000202),
        (-0.000918, -0.0, -0.000203),
        (-0.001333, -0.0, -0.000204),
        (-0.001697, -0.0, -0.000205),
        (-0.001996, -0.0, -0.000205),
        (-0.002217, -0.0, -0.000205),
        (-0.002354, -0.0, -0.000205),
        (-0.004, 0.0, -0.000205),
        (-0.003893, 0.0, -0.000205),
        (-0.0036, 0.0, -0.000205),
        (-0.0032, 0.0, -0.000205),
        (-0.0028, 0.0, -0.000205),
        (-0.002507, 0.0, -0.000205),
        (-0.0024, -0.0, -0.000205)
    ]

    faces = [
        (0, 7, 8, 1),
        (1, 8, 9, 2),
        (2, 9, 10, 3),
        (3, 10, 11, 4),
        (4, 11, 12, 5),
        (5, 12, 13, 6),
        (7, 14, 15, 8),
        (8, 15, 16, 9),
        (9, 16, 17, 10),
        (10, 17, 18, 11),
        (11, 18, 19, 12),
        (12, 19, 20, 13),
        (14, 21, 22, 15),
        (15, 22, 23, 16),
        (16, 23, 24, 17),
        (17, 24, 25, 18),
        (18, 25, 26, 19),
        (19, 26, 27, 20),
        (21, 28, 29, 22),
        (22, 29, 30, 23),
        (23, 30, 31, 24),
        (24, 31, 32, 25),
        (25, 32, 33, 26),
        (26, 33, 34, 27),
        (28, 35, 36, 29),
        (29, 36, 37, 30),
        (30, 37, 38, 31),
        (31, 38, 39, 32),
        (32, 39, 40, 33),
        (33, 40, 41, 34),
        (35, 42, 43, 36),
        (36, 43, 44, 37),
        (37, 44, 45, 38),
        (38, 45, 46, 39),
        (39, 46, 47, 40),
        (40, 47, 48, 41),
        (42, 49, 50, 43),
        (43, 50, 51, 44),
        (44, 51, 52, 45),
        (45, 52, 53, 46),
        (46, 53, 54, 47),
        (47, 54, 55, 48),
        (49, 56, 57, 50),
        (50, 57, 58, 51),
        (51, 58, 59, 52),
        (52, 59, 60, 53),
        (53, 60, 61, 54),
        (54, 61, 62, 55),
        (56, 63, 64, 57),
        (57, 64, 65, 58),
        (58, 65, 66, 59),
        (59, 66, 67, 60),
        (60, 67, 68, 61),
        (61, 68, 69, 62),
        (63, 70, 71, 64),
        (64, 71, 72, 65),
        (65, 72, 73, 66),
        (66, 73, 74, 67),
        (67, 74, 75, 68),
        (68, 75, 76, 69),
        (70, 77, 78, 71),
        (71, 78, 79, 72),
        (72, 79, 80, 73),
        (73, 80, 81, 74),
        (74, 81, 82, 75),
        (75, 82, 83, 76),
        (77, 84, 85, 78),
        (78, 85, 86, 79),
        (79, 86, 87, 80),
        (80, 87, 88, 81),
        (81, 88, 89, 82),
        (82, 89, 90, 83),
        (84, 91, 92, 85),
        (85, 92, 93, 86),
        (86, 93, 94, 87),
        (87, 94, 95, 88),
        (88, 95, 96, 89),
        (89, 96, 97, 90),
        (91, 98, 99, 92),
        (92, 99, 100, 93),
        (93, 100, 101, 94),
        (94, 101, 102, 95),
        (95, 102, 103, 96),
        (96, 103, 104, 97),
        (98, 105, 106, 99),
        (99, 106, 107, 100),
        (100, 107, 108, 101),
        (101, 108, 109, 102),
        (102, 109, 110, 103),
        (103, 110, 111, 104),
        (105, 112, 113, 106),
        (106, 113, 114, 107),
        (107, 114, 115, 108),
        (108, 115, 116, 109),
        (109, 116, 117, 110),
        (110, 117, 118, 111),
        (113, 112, 141, 142),
        (27, 34, 129, 128),
        (90, 97, 138, 137),
        (117, 116, 145, 146),
        (1, 2, 121, 120),
        (97, 104, 139, 138),
        (34, 41, 130, 129),
        (5, 6, 125, 124),
        (41, 48, 131, 130),
        (104, 111, 140, 139),
        (115, 114, 143, 144),
        (111, 118, 147, 140),
        (48, 55, 132, 131),
        (114, 113, 142, 143),
        (3, 4, 123, 122),
        (55, 62, 133, 132),
        (118, 117, 146, 147),
        (2, 3, 122, 121),
        (62, 69, 134, 133),
        (116, 115, 144, 145),
        (0, 1, 120, 119),
        (69, 76, 135, 134),
        (6, 13, 126, 125),
        (4, 5, 124, 123),
        (13, 20, 127, 126),
        (76, 83, 136, 135),
        (83, 90, 137, 136),
        (20, 27, 128, 127),
        (128, 129, 175, 174),
        (125, 126, 172, 171),
        (70, 63, 157, 158),
        (130, 131, 177, 176),
        (127, 128, 174, 173),
        (132, 133, 179, 178),
        (77, 70, 158, 159),
        (28, 21, 151, 152),
        (129, 130, 176, 175),
        (134, 135, 181, 180),
        (35, 28, 152, 153),
        (131, 132, 178, 177),
        (136, 137, 183, 182),
        (133, 134, 180, 179),
        (84, 77, 159, 160),
        (138, 139, 185, 184),
        (135, 136, 182, 181),
        (0, 119, 165, 148),
        (144, 143, 189, 190),
        (91, 84, 160, 161),
        (42, 35, 153, 154),
        (137, 138, 184, 183),
        (140, 147, 193, 186),
        (119, 120, 166, 165),
        (49, 42, 154, 155),
        (139, 140, 186, 185),
        (122, 123, 169, 168),
        (142, 141, 187, 188),
        (141, 112, 164, 187),
        (98, 91, 161, 162),
        (7, 0, 148, 149),
        (145, 144, 190, 191),
        (120, 121, 167, 166),
        (123, 124, 170, 169),
        (105, 98, 162, 163),
        (56, 49, 155, 156),
        (143, 142, 188, 189),
        (146, 145, 191, 192),
        (121, 122, 168, 167),
        (63, 56, 156, 157),
        (14, 7, 149, 150),
        (124, 125, 171, 170),
        (126, 127, 173, 172),
        (112, 105, 163, 164),
        (21, 14, 150, 151),
        (147, 146, 192, 193)
    ]

    curvePoints = [
        (0.0, 0.0, 0.0),
        (-0.05, 0.05, 0.0),
        (0.0, 0.1, 0.0),
        (0.05, 0.05, 0.0),
        (0.02, 0.0, 0.0),
    ]

    return verts, faces, curvePoints

#################################################
#                                               #
#               CURVE function                  #
#  adds Curve and positions bezier points and   #
#  handles (TO DO-> add hook modifiers)         #
#################################################


def make_weld_path(objname, curvename, pointData):
    if curvename in bpy.data.curves.keys():
        bpy.data.curves[curvename].name = curvename+' (Older)'

    curve = bpy.data.curves.new(name=curvename, type="CURVE")
    curve.dimensions = "3D"
    

    objectdata = bpy.data.objects.new(objname, curve)
    objectdata.location = (0.0, 0.0, 0.0)  # object origin
    bpy.context.collection.objects.link(objectdata)

    bezLine = curve.splines.new("BEZIER")
    bezLine.radius_interpolation = "EASE"
    bezLine.use_endpoint_u = True
    bezLine.use_smooth = True
    bezLine.bezier_points.add(len(pointData)-1)
    for num in range(len(pointData)):
        bezLine.bezier_points[num].co = pointData[num]
        thisPoint = bezLine.bezier_points[num]
        if num == 0:
            thisPoint.handle_left.x = pointData[num][0] + 0.005
            thisPoint.handle_left.y = pointData[num][1]
            thisPoint.handle_right.x = pointData[num][0] - 0.025
            thisPoint.handle_right.y = pointData[num][1]            
        elif num == 1:
            thisPoint.handle_left.x = pointData[num][0]
            thisPoint.handle_left.y = pointData[num][1] - 0.025
            thisPoint.handle_right.x = pointData[num][0]
            thisPoint.handle_right.y = pointData[num][1] + 0.025
        elif num == 2:
            thisPoint.handle_left.x = pointData[num][0] - 0.025
            thisPoint.handle_left.y = pointData[num][1]
            thisPoint.handle_right.x = pointData[num][0] + 0.025
            thisPoint.handle_right.y = pointData[num][1]
        elif num == 3:
            thisPoint.handle_left.x = pointData[num][0]
            thisPoint.handle_left.y = pointData[num][1] + 0.025
            thisPoint.handle_right.x = pointData[num][0]
            thisPoint.handle_right.y = pointData[num][1] - 0.025
        elif num == 4:
            thisPoint.handle_left.x = pointData[num][0] + 0.025
            thisPoint.handle_left.y = pointData[num][1]
            thisPoint.handle_right.x = pointData[num][0] - 0.005
            thisPoint.handle_right.y = pointData[num][1]
        thisPoint.handle_left_type = 'FREE'
        thisPoint.handle_right_type = 'FREE'

    objectdata.select_set(True)
    bpy.context.view_layer.objects.active = objectdata
    bpy.ops.object.editmode_toggle()
    objData = bpy.data.objects
    for num in range(len(pointData)):
        bpy.ops.object.modifier_add(type='HOOK')
        bpy.data.curves['weld_path'].splines[0].bezier_points[num].select_control_point = True
        bpy.data.curves['weld_path'].splines[0].bezier_points[num].select_left_handle = True
        bpy.data.curves['weld_path'].splines[0].bezier_points[num].select_right_handle = True
        if num == 0:
            objectdata.modifiers["Hook"].object = objData["Hook_0"+str(num)+" - BASE"]
            bpy.ops.object.hook_assign(modifier='Hook')
        elif num == 4:
            objectdata.modifiers["Hook.00"+str(num)].object = objData["Hook_0"+str(num)+" - END"]
            bpy.ops.object.hook_assign(modifier="Hook.00"+str(num))
        else:
            objectdata.modifiers["Hook.00"+str(num)].object = objData["Hook_0"+str(num)]
            bpy.ops.object.hook_assign(modifier="Hook.00"+str(num))
        bpy.ops.curve.select_all(action='DESELECT')

    objectdata.select_set(True)
    bpy.context.view_layer.objects.active = objectdata
    bpy.ops.object.editmode_toggle()
#    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

#################################################
#                                               #
#               EMPTIES function                #
#  adds, scales, positions and renames Empties  #
#################################################


def make_empties(pointData):
    for num in range(len(pointData)):
        objData = bpy.data.objects
        if num == 0:
            bpy.ops.object.empty_add(type="SINGLE_ARROW",
                                     radius=0.004,
                                     align="WORLD",
                                     location=pointData[num])
            # check that prior named object not present before naming
            if "Array_Offset_Anchor" in objData.keys():
                objData["Array_Offset_Anchor"].name = "Array_Offset_Anchor (Older)"
            objData["Empty"].name = "Array_Offset_Anchor"
            objData["Array_Offset_Anchor"].scale = (1.0, 1.0, 1.0)

            bpy.ops.object.empty_add(type="CUBE",
                                     radius=0.05,
                                     align="WORLD",
                                     location=(0, 0, 0))
            if "Weld Holder" in objData.keys():
                objData["Weld Holder"].name = "Weld Holder (Older)"
            objData["Empty"].name = "Weld Holder"
            objData["Weld Holder"].scale = (0.1, 0.1, 0.1)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

            bpy.ops.object.empty_add(type="CUBE",
                                     radius=0.005,
                                     align="WORLD",
                                     location=pointData[num])
            if "Hook_0"+str(num)+" - BASE" in objData.keys():
                objData["Hook_0"+str(num)+" - BASE"].name = "Hook_0"+str(num)+" - BASE (Older)"
            objData["Empty"].name = "Hook_0"+str(num)+" - BASE"
            objData["Hook_0"+str(num)+" - BASE"].scale = (2.0, 0.5, 0.5)

        elif num == 4:
            bpy.ops.object.empty_add(type="SPHERE",
                                     radius=0.005,
                                     align="WORLD",
                                     location=pointData[num])
            if "Hook_0"+str(num)+" - END" in objData.keys():
                objData["Hook_0"+str(num)+" - END"].name = "Hook_0"+str(num)+" - END (Older)"
            objData["Empty"].name = "Hook_0"+str(num)+" - END"
            objData["Hook_0"+str(num)+" - END"].scale = (2.0, 1.0, 1.0)

        else:
            bpy.ops.object.empty_add(type="SPHERE",
                                     radius=0.005,
                                     align="WORLD",
                                     location=pointData[num])
            if "Hook_0"+str(num) in objData.keys():
                objData["Hook_0"+str(num)].name = "Hook_0"+str(num)+" (Older)"
            objData["Empty"].name = "Hook_0"+str(num)
            if num/2 == int(num/2):
                objData["Hook_0"+str(num)].scale = (4.0, 1.0, 1.0)
            else:
                objData["Hook_0"+str(num)].scale = (1.0, 4.0, 1.0)


#################################################
#                                               #
#             WELD SEGMENT CREATOR              #
#       creates base mesh & adds modifiers      #
#################################################

def make_segment(verts_loc, faces):

    mesh = bpy.data.meshes.new("Weld Segment")

    bm = bmesh.new()

    for v_co in verts_loc:
        bm.verts.new(v_co)

    bm.verts.ensure_lookup_table()
    for f_idx in faces:
        bm.faces.new([bm.verts[i] for i in f_idx])

    bm.to_mesh(mesh)
    mesh.update()

    # add the mesh as an object into the scene then adds modifiers
    context = bpy.context
    from bpy_extras import object_utils
    object_utils.object_data_add(context, mesh)
    bpy.ops.object.shade_smooth()
    bpy.ops.object.modifier_add(type="ARRAY")
    bpy.ops.object.modifier_add(type="CURVE")


#################################################
#                                               #
#                   MAIN OPERATOR               #
#         generates weld configuration          #
#################################################

"""
    # generic transform props - temporarily?? removed from Operator
    align_items = (
        ("WORLD", "World", "Align the new object to the world"),
        ("VIEW", "View", "Align the new object to the view"),
        ("CURSOR", "3D Cursor", "Use the 3D cursor orientation for new object")
    )
    align: EnumProperty(
        name="Align",
        items=align_items,
        default="WORLD",
        update=AddObjectHelper.align_update_callback,
    )
    location: FloatVectorProperty(
        name="Location",
        subtype="TRANSLATION",
    )
    rotation: FloatVectorProperty(
        name="Rotation",
        subtype="EULER",
    )
"""


class AddWeld(bpy.types.Operator):
    """Add a Weld configuration"""
    bl_idname = "mesh.weld_mesh_add"
    bl_label = "Add Weld"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # store mesh and curve data in ref objects
        verts_loc, faces, cpoints = weld_data()            # weld data func
        objData = bpy.data.objects
        meshData = bpy.data.meshes

        # generate named empties
        make_empties(cpoints)                              # empties func

        # generate curve
        if "Weld Path" not in objData.keys():  # check that prior named object not present before naming
            make_weld_path("Weld Path", "weld_path", cpoints)  # curve func
        else:  # if named object already exists rename it
            objData["Weld Path"].name = "Weld Path (Older)"
            make_weld_path("Weld Path", "weld_path", cpoints)
        

        # generate weld segment(with modifiers)
        if "Weld Segment" not in meshData.keys():  # check that prior named object not present before naming
            make_segment(verts_loc, faces)                 # weld segment func
        else:  # if named object already exists rename it (both "mesh" and "object")
            objData["Weld Segment"].name = "Weld Segment (Older)"
            meshData["Weld Segment"].name = "Weld Segment (Older)"
            make_segment(verts_loc, faces)

        # store modifiers, curve and anchor objects in ref objects
        arrayMod = objData["Weld Segment"].modifiers["Array"]
        curveMod = objData["Weld Segment"].modifiers["Curve"]
        curvePath = objData["Weld Path"]
        curvePath.rotation_euler = (R(-60.0), R(0.0), R(0.0))
        curveOffset = objData["Array_Offset_Anchor"]

        # configure Array and Curve modifiers
        arrayMod.fit_type = "FIT_CURVE"
        arrayMod.curve = curvePath
        arrayMod.use_relative_offset = True
        arrayMod.relative_offset_displace[0] = 0
        arrayMod.relative_offset_displace[1] = 0.4
        arrayMod.relative_offset_displace[2] = 0
        arrayMod.use_object_offset = True
        arrayMod.offset_object = curveOffset
        curveMod.object = curvePath
        curveMod.deform_axis = "POS_Y"
        # parenting
        wh = objData['Weld Holder']
        h0 = objData['Hook_00 - BASE']
        h1 = objData['Hook_01']
        h2 = objData['Hook_02']
        h3 = objData['Hook_03']
        h4 = objData['Hook_04 - END']
        wp = objData['Weld Path']
        aoa = objData['Array_Offset_Anchor']
        ws = objData['Weld Segment']
        h0.parent = wh
        h1.parent = wh
        h2.parent = wh
        h3.parent = wh
        h4.parent = wh
        wp.parent = wh
        aoa.parent = wp
        ws.parent = wp
        
        # create (if not already made) & assign "Weld Metal" material 
        bpy.ops.object.material_slot_add()  # add material slot to active object
        if "Weld Metal" not in bpy.data.materials.keys():
            bpy.ops.material.new()  # create new material
            bpy.data.materials[-1].name= "Weld Metal"  # rename last created [-1] material
            # set material values
            bpy.data.materials["Weld Metal"].node_tree.nodes["Principled BSDF"].inputs[4].default_value = 0.9
            bpy.data.materials["Weld Metal"].node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.3
            bpy.data.materials["Weld Metal"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.1, 0.1, 0.1, 1)
            # assign material to object's material slot
            bpy.data.objects["Weld Segment"].material_slots[0].material = bpy.data.materials["Weld Metal"]
        else:
             bpy.data.objects["Weld Segment"].material_slots[0].material = bpy.data.materials["Weld Metal"]

        return {"FINISHED"}


#################################################
#                                               #
#               PANEL function                  #
#                maybe...???                    #
#################################################


#################################################
#                                               #
#               MENU BUTTON function            #
#                                               #
#################################################

def menu_func(self, context):
    self.layout.operator(AddWeld.bl_idname, icon="HAND")


#################################################
#                                               #
#               REGISTRATION                    #
#                                               #
#################################################

def register():
    bpy.utils.register_class(AddWeld)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(AddWeld)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
