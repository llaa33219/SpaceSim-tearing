import os

# Function to remove time-related differences
def remove_time_related_differences(file1_data, file2_data, excluded_functions):
    modified_data = bytearray(file1_data)
    
    # Iterate over the excluded functions and remove differences
    for func in excluded_functions:
        func_encoded = func.encode()
        func_start = 0
        
        while func_start != -1:
            func_start1 = file1_data.find(func_encoded, func_start)
            func_start2 = file2_data.find(func_encoded, func_start)
            if func_start1 != -1 and func_start2 != -1:
                func_end1 = func_start1 + len(func_encoded)
                func_end2 = func_start2 + len(func_encoded)
                if file1_data[func_start1:func_end1] != file2_data[func_start2:func_end2]:
                    # If there is a difference, replace the section with the version from file2
                    modified_data[func_start1:func_end1] = file2_data[func_start2:func_end2]
                func_start = func_end1
            else:
                func_start = -1
    
    return modified_data

# Paths to the files
file1_path = r"D:\SpaceSim Contest Edition\SpaceSim.exe"  # 첫 번째 파일 경로
file2_path = r"C:\Program Files (x86)\SpaceSim\SpaceSim.exe"  # 두 번째 파일 경로

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))
destination_file_path = os.path.join(current_directory, "Modified_SpaceSim.exe")

# List of time-related functions to be addressed
excluded_functions = [
    "GetSystemTime",
    "GetLocalTime",
    "GetSystemTimeAsFileTime",
    "strftime",
    "localtime",
    "gmtime",
    "_localtime64_s",
    "_gmtime64_s",
    "_time64",
    "_mktime64"
]

# Read the data from both files
with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
    file1_data = file1.read()
    file2_data = file2.read()

# Remove time-related differences
modified_data = remove_time_related_differences(file1_data, file2_data, excluded_functions)

# Write the modified data to a new file
with open(destination_file_path, 'wb') as modified_file:
    modified_file.write(modified_data)

print(f"Time-related differences have been removed. The modified file is saved as {destination_file_path}")
