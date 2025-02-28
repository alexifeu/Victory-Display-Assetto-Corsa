Assetto Corsa "You Win" App

A simple Assetto Corsa Python app that displays a "You Win" image when the player completes the required number of laps.

Features

✅ Lap Tracking: Detects the total number of laps set for the race and displays an image only when the player completes the required number of laps.
✅ On-Screen Notification: Displays a "You Win" image on-screen at the end of the race, specifically when the player's completed lap count matches the total laps of the race.
This app is ideal for races where a specific number of laps are set. It does not currently detect race position.

Installation

Copy the appName folder into Assetto Corsa/apps/python/.
Start Assetto Corsa and the app will automatically run.
How It Works

Uses ac.getCarState(0, acsys.CS.LapCount) to track the player's completed laps.
Uses shared memory via the sim_info.py to track the total number of laps.
Displays win.png in the app window when the player's completed laps match the total laps.
Future Improvements

🔹 Detect actual race completion & position.
🔹 Add customizable image display options.
Contributions

Feel free to improve this app—contributions are welcome!
