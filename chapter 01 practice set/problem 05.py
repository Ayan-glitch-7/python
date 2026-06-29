import os

# select the directory whose contents you want to list
directory_path = '/windows'

# use the os moduke to list the directory contents
contents = os.listdir(directory_path)

# print the contents of the directory
for item in contents :
    print(item)