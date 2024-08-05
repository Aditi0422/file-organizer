import os
import shutil

def organize_files_by_type(directory):
    # Get the list of all files and directories
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get file extension
        file_extension = file.split('.')[-1]

        # Create a directory for the file type if it doesn't exist
        target_dir = os.path.join(directory, file_extension)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move the file to the target directory
        shutil.move(os.path.join(directory, file), os.path.join(target_dir, file))

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files_by_type(directory)
    print("Files have been organized by type.")
