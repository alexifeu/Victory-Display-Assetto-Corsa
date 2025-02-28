import sys
import ac
import acsys
import os
import platform

if platform.architecture()[0] == "64bit":
    libdir = 'third_party/lib64'
else:
    libdir = 'third_party/lib'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), libdir))
os.environ['PATH'] = os.environ['PATH'] + ";."

from third_party.sim_info import info

win_image = 0
app_window = 0
show_win_image = False

def acMain(ac_version):
    global win_image, app_window

    app_window = ac.newApp("Victory Display")
    ac.setSize(app_window, 1392, 206)
    ac.setBackgroundOpacity(app_window, 0)
    ac.drawBorder(app_window, 0)
    ac.setTitle(app_window, "")
    ac.setIconPosition(app_window, 0, -10000)

    win_image = ac.newTexture(os.path.join(os.path.dirname(__file__), "images", "win.png"))

    ac.addRenderCallback(app_window, render_image)

    return "YOU WIN App Loaded"

def render_image(deltaT):
    global win_image, app_window, show_win_image

    if show_win_image and win_image:
        image_width, image_height = 1392, 206
        ac.glColor4f(1.0, 1.0, 1.0, 1.0)
        ac.glQuadTextured(0, 0, image_width, image_height, win_image)

def acUpdate(deltaT):
    global show_win_image

    current_laps = ac.getCarState(0, acsys.CS.LapCount)
    total_laps = info.graphics.numberOfLaps
    session_type = info.graphics.session

    if session_type == 2:
        position = ac.getCarRealTimeLeaderboardPosition(0)
    else:
        position = ac.getCarLeaderboardPosition(0)

    if position != '-':
        if current_laps >= total_laps and str(position) == "0":
            show_win_image = True
        else:
            show_win_image = False
    else:
        show_win_image = False

def acShutdown():
    pass
