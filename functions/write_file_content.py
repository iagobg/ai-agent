import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        full_file_path = os.path.join(working_directory,file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_file_path)
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        parent_dir = os.path.dirname(abs_file_path)

        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir,exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files in the specified directory with, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write files from, relative to the working directory. If not provided, write files in the working directory itself.",
                
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content being written.",
                
            ),
        },
    ),
)