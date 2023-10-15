import os

# Return creation time of file
def get_creation_time(path):
    return os.stat(path).st_birthtime



# Return modification time of file
def get_modification_time(path):
    return os.path.getmtime(path)



# Return size of file
def get_size(path):
    return os.stat(path).st_size


