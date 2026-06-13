# ---------------------------------------------------------
# METHOD 1: Traditional Way (Best for Large Files / Streaming)
# ---------------------------------------------------------
with open("file.txt", "r") as file:
    content = file.read()

# ---------------------------------------------------------
# METHOD 2: Modern Way (Best for Quick Automation / Short Files)
# ---------------------------------------------------------
from pathlib import Path
content = Path("file.txt").read_text()