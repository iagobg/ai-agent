import os
from config import CHARACTER_LIMIT

def get_file_content(working_directory, file_path):
    try:
        full_file_path = os.path.join(working_directory,file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_file_path)
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: {file_path}'
        
        with open(abs_file_path) as f:
            file_content = f.read(CHARACTER_LIMIT)
        suffix = ''
        if len(file_content) >= CHARACTER_LIMIT:
            suffix = '[...File "{abs_file_path}" truncated at {CHARACTER_LIMIT} characters]'
        return file_content+suffix
    except Exception as e:
        return f'Error: {e}'
