import importlib.util

def extension_path():
    return importlib.util.find_spec('icu').origin
