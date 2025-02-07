import os
from datetime import datetime, timezone
import pandas as pd
import json

def save_file(data, filename, file_extension):
    base_dir = "output"  # Main output directory

    # Mapping extensions to subfolders
    folder_mapping = {
        "md": "markdown",
        "csv": "csv",
        "xlsx": "excel"
    }

    # Validate the file extension
    if file_extension not in folder_mapping:
        raise ValueError("Unsupported file extension. Supported extensions: md, csv, xlsx")

    # Define the subfolder path
    subfolder = folder_mapping[file_extension]
    folder_path = os.path.join(base_dir, subfolder)

    # Ensure the subfolder exists
    os.makedirs(folder_path, exist_ok=True)

    # Define full file path
    file_name = ""
    if file_extension == 'md':
        current_time = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")[:-3]
        file_name = f"{current_time}{filename}.{file_extension}"
    else:
        file_name = f"{file_name}.{file_extension}"
    file_path = os.path.join(folder_path, file_name)

    # Handle different file types correctly
    if file_extension == "csv":
        if isinstance(data, list):
            data = "\n".join([",".join(map(str, row)) for row in data])  # Convert list to CSV format
        elif isinstance(data, dict):
            data = json.dumps(data)  # Convert dict to JSON string format

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    elif file_extension == "md":
        if isinstance(data, dict) or isinstance(data, list):
            data = json.dumps(data, indent=4)  # Convert to readable JSON format

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(data))  # Ensure data is a string

    elif file_extension == "xlsx":
        if isinstance(data, list):
            df = pd.DataFrame(data)  # Convert list to DataFrame
        elif isinstance(data, dict):
            df = pd.DataFrame([data])  # Convert single dictionary to DataFrame
        else:
            raise ValueError("Unsupported data format for Excel. Use a list of lists or dictionary.")

        df.to_excel(file_path, index=False, engine="openpyxl")

    return file_name
