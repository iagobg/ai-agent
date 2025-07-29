import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory,directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(full_path)
        if not abs_target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'
        items = os.listdir(abs_target_dir)
        results = []
        for item in items:
            item_path = os.path.join(abs_target_dir, item)
            results.append(f'{str(item)}: file_size={os.path.getsize(item_path)}, is_dir={not os.path.isfile(item_path)}')

        return '\n'.join(results)
    except Exception as e:
        return f'Error: {str(e)}'
    