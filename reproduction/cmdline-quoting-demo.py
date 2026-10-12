"""Show WHY Click 8.2.1 failed and 8.4.1 works (runs on any OS).

On Windows, subprocess.call(list) joins the list into one command-line string
with subprocess.list2cmdline(). An argument that contains a space is wrapped
in double quotes as a whole. Explorer does not understand the quoted form
"/select,<path>", so it falls back to opening the Documents folder.
"""
import subprocess

path = r"C:\Users\Public\click demo"

before = ["explorer", f"/select,{path}"]   # Click 8.2.1 (combined argument)
after = ["explorer", "/select,", path]     # Click 8.4.1 (separate arguments)

print("Click 8.2.1 command line:", subprocess.list2cmdline(before))
print("Click 8.4.1 command line:", subprocess.list2cmdline(after))
