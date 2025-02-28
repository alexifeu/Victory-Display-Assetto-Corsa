Assetto Corsa "You Win" App
A simple Assetto Corsa Python app that displays a "You Win" image when the player completes a lap.

Features
✅ Lap Tracking – Detects and updates the lap count in real time.
✅ On-Screen Notification – Displays a "You Win" image when at least one lap is completed.
This app works perfectly for **Initial D-style Touge races**, which are usually **one-lap duels**. 
It doesn’t check for **first place**, but as long as you're racing **one opponent** and **one lap**, it does the job. xD

Installation
Copy the appName folder into Assetto Corsa/apps/python/.
Start Assetto Corsa and enable the app from the in-game sidebar.
How It Works
Uses ac.getCarState(0, acsys.CS.LapCount) to track laps.
Displays win.png in the app window after at least one lap.

Future Improvements
🔹 Detect actual race completion & position.
🔹 Add custom race lap support instead of triggering after one lap.

Contributions
Feel free to improve this, but please let me know!!
