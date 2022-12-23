import os

root = os.path.join('.', 'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
    print()
import os
cwd = os.getcwd()
for dir_path, dir_names, file_names in os.walk(cwd):
    for f in file_names:
        print(f)
