import os
import json
import shutil

def create_dir(dir):
    """Create the dir if the dir does not exists
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def delete_dir(path):
    """rm a dir
    """
    shutil.rmtree(path)


def open_file(file):
    """Open a file and read the content
    """
    if not file:
        return ''
    content = ''
    with open(file, 'r') as file:
        content = file.read()
    return content


def save_file(dir, file_name, content):
    """Write the content in a file
    """
    path = os.path.join(dir, file_name)
    with open(path, 'w') as f:
        f.write(content)
    return path


def open_json(file):
    """Read a json file and returns its content has a dict
    """
    with open(file) as f:
        data = json.load(f)
        return data
    return None


def save_json(dir, file_name, content, sort=False):
    """Save a a given dict to the specified location
    """
    with open(os.path.join(dir, file_name), 'w') as f:
        json.dump(content, f, indent=4, sort_keys=sort)
