import os
from config import CHARACTER_LIMIT

def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abs_full = os.path.abspath(full_path)
        if not abs_full.startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        lines = []
        file = open(full_path)
        for line in file:
            lines.append(line)
        combined = "\n".join(lines)
        if len(combined) > CHARACTER_LIMIT:
            combined = combined[:CHARACTER_LIMIT] + f'[...File "{file_path}" truncated at 10000 characters]'
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e} happened!"

    