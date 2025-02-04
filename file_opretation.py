import os
import time

def create_file(data, title, file_extension):
    timestamp = int(time.time())
    base_dir = "./output/"
    
    # Define supported extensions and folders
    extensions = {"csv": "csv", "md": "markdown", "xlsx": "excel"}
    
    if file_extension not in extensions:
        raise ValueError("Unsupported file extension")
    
    folder = extensions[file_extension]
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)  # Ensure folder exists
    
    if file_extension == "csv" or file_extension == "xlsx":
        file_path = os.path.join(folder_path, title)
        with open(file_path, "w") as file:
            file.write(data)
        return title
    elif file_extension == "md":
        filename = f"{timestamp}_{title}.{file_extension}"
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "w") as file:
            file.write(data)
        return file_name
