import os


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def write_to_file(path, data):
    with open(path, 'w') as file:
        file.write(data)
