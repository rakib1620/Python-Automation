# ==============================================================================
# Script Name: 04_exclusive_file.py
# Purpose: Demonstrates safe file creation using exclusive "x" mode with try-except.
# Author: Rakib Hossain
# ==============================================================================

try:
    # 1. Attempting to open a file in "x" (Exclusive) mode with UTF-8 encoding.
    # Note: "x" mode strictly requires that the file does NOT already exist.
    with open("file.txt", "x", encoding="utf-8") as file:
        
        # Writing data only if the file is freshly created.
        file.write("Created using exclusive mode.\n")

except FileExistsError:
    # 2. Handling the specific error if "file.txt" already exists.
    # This prevents the script from crashing with a red error screen.
    print("file.txt already exists, exclusive creation aborted.")