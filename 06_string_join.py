# ==============================================================================
# Script Name: 06_string_join_file.py
# Purpose: Demonstrates joining a list of strings with newlines and writing via write().
# Author: Rakib Hossain
# ==============================================================================

lines = ["Line A", "Line B", "Line C"]

# Joining the list elements with a newline character and adding a final trailing newline
text = "\n".join(lines) + "\n"

# 1. Opening the file in "w" (Write) mode to save the formatted string
with open("file2.txt", "w", encoding="utf-8") as file:
    file.write(text)

# 2. Opening the file in "r" (Read) mode to verify the output
with open("file2.txt", "r", encoding="utf-8") as file:
    print(file.read())