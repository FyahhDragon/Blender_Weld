# Blender_Weld
 An add-on for Blender to create models of weld joints

v.0.2.0 - Operator calls functions to create objects and then creates
          heirarchy of parented objects and configures array and curve modifiers
          and finally adds material to mesh.
        - removed Panel (for now).
        - mesh now generated with bmesh from vertex and face data.
        - function to return mesh data.
        - function to create, name and rename empties.
        - function to create bezier curve and set points & handles and attach hooks to empties.
        - function to generate mesh and attach array & curve modifiers.
        
        TO DO ->    add data to give choice of meshes
                    reinstate Panel with mesh options
                    enable scaling of mesh at generation
 
v.0.1.2 - added location and rotation properties for redo.
        - Updated comments.

v.0.1.1 - added size "property" to make "Redo Panel" activate.

v.0.1.0 - basic single file Blender Add-On.
        - Creates - Add Menu mesh item and Viewport Panel tab
        - with single button to generate Weld model
        - (at present just adds a scaled and rotated cube at location(0, 0, 1))
      