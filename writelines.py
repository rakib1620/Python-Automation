# ==============================================================================
# Script Name: 05_writelines_file.py
# Purpose: Demonstrates how to write raw, messy server data using writelines().
# Author: Rakib Hossain
# ==============================================================================

# A simulation of raw, unformatted server logs and user data (Messy Data)
# Note: There are no newline characters (\n), so the data will be written in a single line.
messy_server_data = [
    "USER_ID:101,NAME:Rakib,STATUS:Active,IP:192.168.1.5;",
    "USER_ID:102,NAME:Arif,STATUS:Pending,IP:192.168.1.12;",
    "USER_ID:103,NAME:Sultana,STATUS:Active,IP:192.168.1.25;",
    "SERVER_STATUS:OK,CPU_LOAD:45%,RAM_USAGE:62%;"
]

# 1. Opening the file in "w" (Write) mode to dump the raw list.
with open("raw_logs.txt", "w", encoding="utf-8") as file:
    # writelines() pushes the entire list into the file at once.
    file.writelines(messy_server_data)

# 2. Opening the file in "r" (Read) mode to verify the output in the terminal.
with open("raw_logs.txt", "r", encoding="utf-8") as file:
    print("--- Raw File Content From Disk ---")
    print(file.read())