import os

def validate_file(filepath):
    if os.path.exists(filepath):
        return True
    else:
        return False
