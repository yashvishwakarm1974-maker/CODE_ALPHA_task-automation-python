import os
import shutil

# Source folder path
source_folder = input("Enter the source folder path: ")

# Destination folder path
destination_folder = input("Enter the destination folder path: ")

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Destination folder created.")

# Counter for moved files
count = 0

# Loop through all files
for file in os.listdir(source_folder):

    # Check if file ends with .jpg
    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

        count += 1

print("--------------------------------")
print(f"Total JPG files moved: {count}")
print("Task Completed Successfully!")