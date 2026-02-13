# Allows aiAgent to view and list file contents and metadata.

import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_path = (
        os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    )

    if valid_target_path is False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" is not a directory'

    try:
        with open(target_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (
                    f'\n\n...File: "{file_path}" truncated at {MAX_CHARS} characters...'
                )
            return file_content
    except Exception as e:
        return f"Error: {e}"
