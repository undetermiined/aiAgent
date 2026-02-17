# Allows aiAgent to utilize Python files

import os

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_path = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )

        if valid_target_path is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith('py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
