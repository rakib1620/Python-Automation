# ==============================================================================
# Script Name: 03_append_file.py
# Purpose: Demonstrates how to append new lines to a file without overwriting.
# Author: Rakib Hossain
# ==============================================================================

# 1. Opening a file in "a" (Append) mode with UTF-8 encoding.
# Note: "a" mode preserves old text and adds new content to the end of the file.
with open("myfile.txt", "a", encoding="utf-8") as file:
    
    # Writing a new line into the file.
    # The '\n' ensures that any future text will start on a fresh line.
    file.write("Appended line1.\n")

# 2. Opening the same file in "r" (Read) mode to verify the entire content.
with open("myfile.txt", "r", encoding="utf-8") as file:
    
    # Reading the entire file content (old + new) and printing it to the terminal.
    print(file.read())