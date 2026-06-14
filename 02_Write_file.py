# ==============================================================================
# Script Name: 02_Write_file.py
# Purpose: Demonstrates traditional vs modern ways of writing/appending files.
# Author: Rakib Hossain
# ==============================================================================

# ------------------------------------------------------------------------------
# METHOD 1: Traditional Way (Best for Large Files / Streaming / Context Control)
# ------------------------------------------------------------------------------

# 1. Create a new file in "w" (write) mode and insert initial structural text
with open("myfile.txt", "w", encoding="utf-8") as file:
    file.write("Sample message for test\n")
    file.write("This is Rakib Hossain\n")
    file.write("Happy Programming\n")

# 2. Open in "a" (append) mode to add new data at the bottom without overwriting
with open("myfile.txt", "a", encoding="utf-8") as file:
    file.write("--- Update Sections (Method 1) ---\n")
    file.write("This is an appended log entry using traditional way.\n")


# ------------------------------------------------------------------------------
# METHOD 2: Modern Way (Best for Quick Automation / Short Files)
# ------------------------------------------------------------------------------

from pathlib import Path

# 1. Define the structural tracking file path object
file_path = Path("myfile.txt")

# 2. Write in "w" mode (By default, write_text overwrites the existing file)
# Note: Re-initializing the file state to isolate and test Method 2 behaviors
initial_content = "Sample message for test\nThis is Rakib Hossain\nHappy Programming\n"
file_path.write_text(initial_content, encoding="utf-8")

# 3. Utilize the 'mode="a"' parameter to explicitly safely append updates at the bottom
updated_content = "--- Update Sections (Method 2) ---\nThis is an appended log entry using pathlib.\n"
file_path.write_text(updated_content, encoding="utf-8", mode="a")


# ------------------------------------------------------------------------------
# Verification: Reading the final content to console
# ------------------------------------------------------------------------------
print("--- Final Output From File ---")
print(file_path.read_text(encoding="utf-8"))