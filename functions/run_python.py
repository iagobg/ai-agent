import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    try:
        full_file_path = os.path.join(working_directory,file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_file_path)
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        command = ['python', abs_file_path] + args

        completed_process = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = []

        if completed_process.stdout:
            output.append(f'STDOUT: {completed_process.stdout}')
        if completed_process.stderr:
            output.append(f'STDERR: {completed_process.stderr}')
        if completed_process.returncode != 0:
            output.append(f'Process existed with code {completed_process.returncode}')

        if output:
            return "\n".join(output)
        else:
            return f'No output produced'

    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Process timed out after 30 seconds"

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute python code located in the specified directory with optional arguments, constrained to the working directory. Don't ask for arguments if none are provided, but pass them to the function if they are.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to execute files from, relative to the working directory. If not provided, execute files in the working directory itself.",
                
            ),
            "arguments": types.Schema(
                type=types.Type.STRING,
                description="The arguments for the given code. If none are provided, simply don't pass any",
                
            ),
        },
    ),
)