# import bpy
# import os

# # Set the path to your blend files and the number of files to link
# path = "/home/ritaank/Documents/dev/motion_synthesis/soma-experiments/soma_experiment_1/support_files/render_out_temp/immersion_tiny/png_files/soma_standard/soma_subject2_Amelia_001/"
# num_files = 3642

# # Set the frame rate for your animation
# bpy.context.scene.render.fps = 25

# blend_files = [f for f in os.listdir(path) if f.endswith("0.blend")]

# # Sort the blend files in numerical order
# blend_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# #print(blend_files[0])
# #print(blend_files[10:20])

# for file_name in blend_files:
#     # Check if the blend file is a directory or a single blend file
#     if os.path.isdir(os.path.join(path, file_name)):
#         # Append objects from all the blend files in the directory
#         object_dir = os.path.join(path, file_name, "Object")
#         for object_file in os.listdir(object_dir):
#             if object_file.endswith(".blend"):
#                 directory = os.path.join(path, file_name, "Object", object_file)
#                 bpy.ops.wm.append(filepath=directory, directory=directory, filename="")
#     elif file_name.endswith(".blend"):
#         # Append objects from a single blend file
# #        directory = os.path.join(path, file_name)
#         blend_file_path = os.path.join(path, file_name)

#         # Get the directory containing the blend file
#         blend_file_dir = os.path.dirname(blend_file_path)
# #        print(blend_file_dir)
#         bpy.ops.wm.append(filepath=blend_file_path, directory=blend_file_dir, filename="")

# # Loop through each file and link the objects to the scene
# #for i in range(0, num_files+1):
# #    file_name = "{:05d}.blend".format(i*10)
# #    print(file_name)
# #    bpy.ops.wm.append(filepath=path + file_name + "/Object/", directory=path + file_name + "/", filename="")

# #    # Set the start and end frames for each object
# #    bpy.context.scene.frame_start = (i-1) * bpy.context.scene.render.fps
# #    bpy.context.scene.frame_end = i * bpy.context.scene.render.fps - 1
# #    
# #    /home/ritaank/Documents/dev/motion_synthesis/soma-experiments/soma_experiment_1/support_files/render_out_temp/immersion_tiny/png_files/soma_standard/soma_subject2_Amelia_001/00000.blend

# import bpy
# import os

# # Set the root path to the blend files
# root_path = "/home/ritaank/Documents/dev/motion_synthesis/soma-experiments/soma_experiment_1/support_files/render_out_temp/immersion_tiny/png_files/soma_standard/soma_subject2_Amelia_001/"

# # Set the name of the output blend file
# output_file_name = "soma_subject2_Amelia_001.blend"

# # Create a new blend file
# bpy.ops.wm.read_homefile(use_empty=True)

# # Set the frame rate to 20fps
# bpy.context.scene.render.fps = 20

# # Loop through the blend files and append the objects to the new file
# for i in range(0, 101):
#     file_name = "{:05d}.blend".format(i*10)
#     file_path = os.path.join(root_path, file_name)

#     print(file_path)
#     assert os.path.exists(file_path), "path does not exist"
#     print(file_name)

#     # raise AssertionError

#     blendfile = file_name
#     section = "\\Object\\"
#     object = "Body"
#     object2 = "Object"

#     filepath = blendfile + section + object
#     directory = blendfile + section
#     filename = object

#     bpy.ops.wm.append(filepath=filepath, directory=directory, filename=filename)

#     raise KeyError
    
#     # if os.path.exists(file_path):
#     #     bpy.ops.wm.append(filepath=file_path + "/Object/", directory=root_path, filename=file_path + "meep")
#     #     raise KeyError
#     # else:
#     #     print(f"File not found: {file_path}")

# # Save the new blend file
# bpy.ops.wm.save_as_mainfile(filepath=os.path.join(root_path, output_file_name))

import bpy
import os

# Set the root path to the blend files
root_path = "/home/ritaank/Documents/dev/motion_synthesis/soma-experiments/soma_experiment_1/support_files/render_out_temp/immersion_tiny/png_files/soma_standard/soma_subject2_Amelia_001/"

# Set the name of the output blend file
output_file_name = "soma_subject2_Amelia_001.blend"

# Create a new blend file
bpy.ops.wm.read_homefile(use_empty=True)

# Set the frame rate to 20fps
bpy.context.scene.render.fps = 20

total_frames = 3642

# Loop through the blend files and append the objects to the new file
for i in range(0, total_frames):
    file_name = "{:05d}.blend".format(i*10)
    file_path = os.path.join(root_path, file_name)

    if os.path.exists(file_path):
        # Append the object from the blend file
        section = "Object"

        object_name = "Body"
        filepath = file_path + "\\Object\\" + object_name
        directory = file_path + "\\Object\\"
        filename = object_name
        bpy.ops.wm.append(filepath=filepath, directory=directory, filename=filename)

        object_name2 = "Object"
        filepath = file_path + "\\Object\\" + object_name2
        directory = file_path + "\\Object\\"
        filename = object_name2
        bpy.ops.wm.append(filepath=filepath, directory=directory, filename=filename)

    else:
        print(f"File not found: {file_path}")

output_file_path = os.path.join(os.path.dirname(root_path), output_file_name)
print("saving the file to: " +  output_file_path)
bpy.ops.wm.save_as_mainfile(filepath=output_file_path)