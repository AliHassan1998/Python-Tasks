# Way of Clearing the folder clutter using Python
import os


def clear_the_clutter(path, file_type):
    try:
        files = os.listdir(path)
        if not any(file.lower().endswith(file_type.lower()) for file in files):
            print(f"No file with this extension: '{file_type}' found in the directory.")
        else:
            i = 1
            for file in files:
                if file.endswith(file_type):
                    old_path = os.path.join(path, file)
                    new_file_name = f"{i}{file_type}"
                    new_path = os.path.join(path, new_file_name)
                    os.rename(old_path, new_path)
                    i += 1
            print("Successfully Renamed!")

    except FileNotFoundError:
        print(f"Directory not found: {path}")


file_path = input("Enter the file path: ")
file_extension = input("Enter the file extension: ")
clear_the_clutter(file_path, file_extension)
