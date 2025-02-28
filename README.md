# Assetto Corsa "You Win" App (Basic Lap Completion)

This is a basic Assetto Corsa Python app that displays a "You Win" image after the player completes one lap.

## How it Works

The app uses the Assetto Corsa Python API to:

1.  **Track Lap Completion:** It monitors the player's lap count using `ac.getCarState(0, acsys.CS.LapCount)`.
2.  **Display Image:** Once the lap count reaches 1 or more, it displays a "You Win" image (`win.png`) on the screen.

## Installation

1.  **Copy Folder:** Copy the entire `appName` folder into your Assetto Corsa `apps/python/` directory. The folder structure should look like this:

    ```
    assettocorsa/
    └── apps/
        └── python/
            └── appName/
                ├── appName.py
                ├── images/
                │   └── win.png
                └── third_party/
                    ├── sim_info.py
                    ├── lib/
                    │   └── _ctypes.pyd
                    └── lib64/
                        └── _ctypes.pyd
    ```

2.  **Run Assetto Corsa:** Launch Assetto Corsa and activate the "appName" app from the app sidebar.

## Customization

This is a very basic implementation. Here are some potential improvements:

* **Win Condition (First Place):** The app currently shows the image after any lap completion. If you want to show it only when the player finishes in first place, you'll need to use `ac.getCarLeaderboardPosition(0)` and `ac.isRaceCompleted()` to check the player's final position at the end of the race.
* **Race Length:** The app currently triggers after one lap. To make it work for races with a specific number of laps, you'll need to retrieve the total number of laps for the current race session and modify the lap completion check accordingly.
* **Image Positioning/Scaling:** The image's position and scaling can be adjusted within the `render_image` function.
* **Error Handling:** Add error handling for cases where the image file is not found or other unexpected issues occur.

## Contributions

Feel free to fork this repository and submit pull requests with improvements! If you know how to implement the win condition or race length features, your contributions would be greatly appreciated.
