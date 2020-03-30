#----------------------------------------------------------------------------
# menu.py
# Version: 1.0.2
# Last Updated: Mar. 29, 2020
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Global Imports ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#----------------------------------------------------------------------------

import nuke
import platform
import nukescripts

# Define where .nuke directory is on each OS's network.

Win_Dir = "C:\Users\yupushao\.nuke"
MacOS_Dir = "/Users/yupushao/.nuke"
Linux_Dir = "/home/yupushao/.nuke"

# Set global directory

if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOS_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None




#----------------------------------------------------------------------------
# Knob Defaults :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#----------------------------------------------------------------------------

nuke.knobDefault("Tracker4.shutteroffset", "centered")
nuke.knobDefault("Tracker4.label", "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()["reference_frame"].setValue(nuke.frame()), nodeClass="Tracker4")

nuke.addOnUserCreate(lambda:nuke.thisNode()["first_frame"].setValue(nuke.frame()), nodeClass="FrameHold")




#----------------------------------------------------------------------------
# Custom Menus ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#----------------------------------------------------------------------------

frankMenu = nuke.menu("Nuke").addMenu("FrankMenu")
frankMenu.addCommand("Autocrop", "nukescripts.autocrop()")


frankGizmosMenu = nuke.menu("Nodes").addMenu("FrankGizmos", icon = "frankGizmos.png")
frankGizmosMenu.addCommand("Autocrop", "nukescripts.autocrop()")

frankGizmosMenu.addCommand("bm_CameraShake", "nuke.createNode('bm_CameraShake')")


#----------------------------------------------------------------------------
toolbar = nuke.menu("Nodes")
toolbar.addCommand("FrankTool/GradeTool", "nuke.createNode('GradeTool')")



#----------------------------------------------------------------------------
# Keyboard Shortcuts ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#----------------------------------------------------------------------------

nuke.menu("Nodes").addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon = "Tracker.png", shortcutContext = 2)









