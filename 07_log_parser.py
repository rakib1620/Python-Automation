# ==============================================================================
# Script Name: 07_log_parser.py
# Purpose: DevOps Mini Project - Lightweight Automated Log Analyzer.
#          Scans system log files, extracts critical errors, and counts incidents.
# Author: Md Rakib Hossain
# ==============================================================================

from pathlib import Path

# 1. Define target log file and output report path using pathlib
mylog = Path("app.log")
final_report = Path("report.txt")

print("--- Starting Automated Log Analysis Workflow ---")

# 2. Safety Check: Verify if the source log file exists before operations
if not mylog.exists():
    print("Abort: Target log file was not found in the current directory!")
else:
    # Initialize error counter variable
    error_count = 0
    print("Critical report scanning initiated...\n")
    
    # 3. Open the log file safely using context manager in read mode
    with open(mylog, "r") as file:
        # Loop line-by-line to optimize memory and CPU performance
        for line in file:
            # Match target keyword to isolate incidents
            if "ERROR" in line:
                error_count += 1  # Increment counter for every match
                print(f"[{error_count}] Detected -> {line.strip()}")

    print("\n--- Analysis Complete ---")

    # 4. Final summary reporting logic based on total incidents found
    if error_count > 0:
        print(f"Alert: Total of {error_count} error incidents identified.")
    else:
        print("Success: Zero errors found. Server health status is optimal.")