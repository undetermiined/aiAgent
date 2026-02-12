# Allows aiAgent to view and list file contents and metadata.

import os


def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_path = (
        os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    )

    if valid_target_path is False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_dir):
        pass
    else:
        return f'Error: "{directory}" is not a directory'
