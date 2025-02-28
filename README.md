# **Assetto Corsa "You Win" App**  

A simple **Assetto Corsa Python app** that displays a **"You Win"** image when the player completes a lap.  

## **Features**  
✅ **Lap Tracking** Detects how many laps a race has and only shows image when laps are completed.  
✅ **On-Screen Notification** – Shows a **"You Win"** image after completing **one lap**.  

This app works perfectly for **Initial D-style Touge races**, which are typically **one-lap duels**. It **doesn't check for first place**, but as long as you're racing **one opponent**, it works just fine. 😆  

## **Installation**  
1. Copy the `appName` folder into `Assetto Corsa/apps/python/`.  
2. Start Assetto Corsa and enable the app from the in-game sidebar.  

## **How It Works**  
- Uses `ac.getCarState(0, acsys.CS.LapCount)` to track laps.  
- Displays `win.png` in the app window after at least **one lap**.  

## **Future Improvements**  
🔹 Detect **actual race completion & position**.  
🔹 Add **custom lap support** instead of triggering after just one lap.  

## **Contributions**  
Feel free to improve this—but please let me know!
