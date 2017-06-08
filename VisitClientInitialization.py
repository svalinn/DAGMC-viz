import subprocess

# Visit needs to be added to PATH for this to work.
subprocess.call(["visit", "-cli", "-nowin", "-s", "make_images.py"])