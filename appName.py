import sys
import ac
import acsys
import os
import platform

# Add third_party to sys.path
if platform.architecture()[0] == "64bit":
    libdir = 'third_party/lib64'
else:
    libdir = 'third_party/lib'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), libdir))
os.environ['PATH'] = os.environ['PATH'] + ";."

from third_party.sim_info import info

# Global variables
win_image = 0
app_window = 0
show_win_image = False
laps_completed = 0

def acMain(ac_version):
    global win_image, app_window

    app_window = ac.newApp("appName")
    ac.setSize(app_window, 1392, 206) #Set window size to image size
    ac.setBackgroundOpacity(app_window, 0) #Set background to transparent.

    ac.log("Hello, Assetto Corsa application world!")
    ac.console("Hello, Assetto Corsa console!")

    win_image = ac.newTexture(os.path.join(os.path.dirname(__file__), "images", "win.png"))

    ac.addRenderCallback(app_window, render_image)

    return "appName"

def render_image(deltaT):
    global win_image, app_window, show_win_image

    if show_win_image and win_image:
        image_width, image_height = 1392, 206

        ac.glColor4f(1.0, 1.0, 1.0, 1.0) #Set color to white
        ac.glQuadTextured(0, 0, image_width, image_height, win_image) #Draw image at 0,0

def acUpdate(deltaT):
    global show_win_image, laps_completed

    current_laps = ac.getCarState(0, acsys.CS.LapCount)

    if current_laps > laps_completed:
        laps_completed = current_laps
        if laps_completed >= info.graphics.numberOfLaps:
            show_win_image = True
        else:
            show_win_image = False
    elif current_laps < laps_completed:
        laps_completed = current_laps
        show_win_image = False

def acShutdown():
    return