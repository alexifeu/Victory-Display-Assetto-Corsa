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

def acMain(ac_version):
    global win_image, app_window

    # Create the app window with a specific name and size
    app_window = ac.newApp("Race Status")  # The name here can be anything.
    ac.setSize(app_window, 1392, 206)  # Size of the app window
    ac.setBackgroundOpacity(app_window, 0)  # Make the background transparent
    ac.drawBorder(app_window, 0)  # Remove the window border
    ac.setTitle(app_window, "")  # Remove the title for a cleaner look

    # Move the window's icon off-screen to hide it
    ac.setIconPosition(app_window, 0, -10000)  # Moves the icon out of view

    # Load the "YOU WIN" image texture
    win_image = ac.newTexture(os.path.join(os.path.dirname(__file__), "images", "win.png"))

    # Set the render callback to display the image when conditions are met
    ac.addRenderCallback(app_window, render_image)

    return "YOU WIN App Loaded"  # App description when it's initialized

def render_image(deltaT):
    global win_image, app_window, show_win_image

    if show_win_image and win_image:
        image_width, image_height = 1392, 206

        # Draw the "YOU WIN" image in the window
        ac.glColor4f(1.0, 1.0, 1.0, 1.0)  # Set the image color (white)
        ac.glQuadTextured(0, 0, image_width, image_height, win_image)  # Display the image at the window’s top-left corner

def acUpdate(deltaT):
    global show_win_image

    current_laps = ac.getCarState(0, acsys.CS.LapCount)
    total_laps = info.graphics.numberOfLaps

    session_type = info.graphics.session

    # Check if we are in a race session (session_type == 2)
    if session_type == 2:
        position = ac.getCarRealTimeLeaderboardPosition(0)  # Real-time position
    else:
        position = ac.getCarLeaderboardPosition(0)  # Regular leaderboard position

    # Check if the player has completed the race and is in the first position
    if position != '-':
        if current_laps >= total_laps and str(position) == "0":
            show_win_image = True  # Show the win image
        else:
            show_win_image = False  # Hide the win image if conditions aren't met
    else:
        show_win_image = False  # Hide the image if position is unavailable

def acShutdown():
    # Clean up if necessary when the app is closed
    pass
