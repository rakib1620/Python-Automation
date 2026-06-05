# ==============================================================================
# Script Name: 02_write_file.py
# Purpose: Demonstrates secure file creation, writing, and encoding in Python.
# Author: Rakib Hossain
# ==============================================================================

# 1. Opening a file in "w" (Write) mode with UTF-8 encoding.
# Note: "w" mode will overwrite the file if it already exists.
with open("myfile.txt", "w", encoding="utf-8") as file:
    
    # Writing multiple lines of text into the file.
    # The '\n' at the end ensures each string starts on a fresh line.
    file.write("Sample message for test\n")
    file.write("This is Rakib Hossain\n")
    file.write("Happy Programming\n")

# 2. Opening the same file in "r" (Read) mode to verify the written content.
with open("myfile.txt", "r", encoding="utf-8") as file:
    
    # Reading the entire file content and printing it to the console/terminal.
    print(file.read())