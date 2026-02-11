# Allows aiAgent to view and list directory contents and metadata

import os


def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    if valid_target_dir is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isdir(target_dir):
        pass
    else:
        return f'Error: "{directory}" is not a directory'

    try:
        for current_obj in os.listdir(target_dir):
            return f"{current_obj}: {os.path.getsize(current_obj)} {os.path.isdir}"
    except Exception as e:
        return f"Error occured: {e}"
