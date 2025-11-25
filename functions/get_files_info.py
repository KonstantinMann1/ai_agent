import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, directory)
        abs_full = os.path.abspath(full_path)
        if not abs_full.startswith(abs_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        lines = []
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e} happened!"

