# ==============================================================================
# Script Name: 08_file_renamer.py
# Purpose: DevOps Mini Project - Automation script to batch rename files in a folder.
# Author: Md Rakib Hossain
# ==============================================================================

import os
from pathlib import Path

def main():
    # 1. Define the target directory containing the files to rename
    target_folder = Path("test")
    
    # 2. Safety Check: Verify if the directory exists and is actually a folder
    if not target_folder.exists() or not target_folder.is_dir():
        print(f"❌ Abort: The directory '{target_folder}' was not found!")
        return

    print(f"--- Starting File Renaming Workflow in '{target_folder}' ---\n")
    
    # 3. Loop through the directory contents sorted alphabetically
    for count, file_path in enumerate(sorted(target_folder.iterdir())):
        
        # Process only files (skip sub-directories if any)
        if file_path.is_file():
            
            # Generate the new filename (e.g., Hostel 0.jpg, Hostel 1.jpg)
            new_name = f"Hostel {count}{file_path.suffix}"
            
            # Construct the full destination path
            new_file_path = target_folder / new_name
            
            try:
                # Execute the rename operation using pathlib
                file_path.rename(new_file_path)
                print(f"✅ Renamed: {file_path.name} -> {new_name}")
            except Exception as e:
                print(f"❌ Error renaming {file_path.name}: {e}")

    print("\n--- Workflow Completed Successfully ---")

if __name__ == '__main__':
    main()