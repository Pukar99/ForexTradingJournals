#this code is used for creative dummies empty .md file by modifying the requirement

import os

def create_md_files(num_files, base_filename, directory="output"):
    """Creates multiple empty MD files with numbered filenames.

    Args:
        num_files (int): The number of files to create.
        base_filename (str): The base filename for the files.
        directory (str, optional): The directory to create the files in. Defaults to "output".
    """

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, num_files + 1):
        filename = f"{base_filename}{i}Trade1.md"  # Ensure "Trade1" is part of the filename
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as f:
            pass  # Create an empty file

# Create 30 files with the specified filename pattern
create_md_files(30, "Dem")
