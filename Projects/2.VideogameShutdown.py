"""
Monitors the specified game process and shuts it down if it exceeds the time limit.

This function continuously checks for the specified game's process. If the game is running,
it starts a timer. If the game runs longer than the specified time limit, the function
terminates the game process.

The function checks for the game process at regular intervals (every 10 seconds).

Returns:
None
"""

import psutil  # type: ignore
import time
import os
from plyer import notification # type: ignore

try:
    print("psutil is installed")
except ImportError:
    print("psutil is not installed")

# Configuration: Add the names of your games and their respective time limits (in seconds)
games = {
    "Baldur.exe": 80 ,
    "swkotor2.exe": 80
}

active_games = {}
notification_sent = {}

def send_notification(game_name, remaining_time):
    """
    Sends a notification to the user to remind them of the time remaining
    to save their progress in the specified game.

    Args:
        game_name (str): The name of the game.
        remaining_time (int): The remaining time (in seconds) to save progress.
    """
    notification.notify(
        # Set the title of the notification
        title="Game Time Alert",
        # Set the message of the notification
        message=f"You have {remaining_time//1} second(s) left to save your progress in {game_name}.",
        # Set the timeout for how long the notification will stay on the screen
        timeout=10  # Notification stays for 10 seconds
    )

def monitor_games():
    print("Monitoring games...")

    while True:
        # Iterate over the games dictionary
        for game_name, time_limit in games.items():
            # Search for the game process
            game_process = next(
                (proc for proc in psutil.process_iter(['name', 'pid']) if proc.info['name'] == game_name), 
                None
            )

            # If the game process is found
            if game_process:
                # If this is the first time we've seen this game, start a timer
                if game_name not in active_games:
                    active_games[game_name] = time.time()
                    notification_sent[game_name] = False  # Reset notification flag
                    print(f"{game_name} started at {time.ctime(active_games[game_name])}")
                    print(f"Time limit for {game_name} is {time_limit} seconds.")

                # Calculate the elapsed time and remaining time
                elapsed_time = time.time() - active_games[game_name]
                remaining_time = time_limit - elapsed_time
                print(f"{game_name} has been running for {int(elapsed_time)} seconds.")
                print(f"Remaining time for {game_name} is {int(remaining_time)} seconds.")

                # Check if remaining time is exactly 60 seconds and notification hasn't been sent yet
                if remaining_time <= 60 and not notification_sent.get(game_name, False):
                    print(f"Sending notification for {game_name}...")
                    send_notification(game_name, remaining_time)
                    notification_sent[game_name] = True
                    print(f"Notification sent for {game_name}.")

                # If the elapsed time exceeds the time limit, shut down the game
                if elapsed_time > time_limit:
                    print(f"Time limit reached for {game_name}! Shutting it down...")
                    os.system(f"taskkill /IM {game_name} /F")
                    active_games.pop(game_name, None)
                    notification_sent.pop(game_name, None)
                    print(f"{game_name} shut down.")
            else:
                # If the game process is no longer running, remove it from the dictionaries
                if game_name in active_games:
                    print(f"{game_name} is no longer running.")
                    active_games.pop(game_name, None)
                    notification_sent.pop(game_name, None)

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    monitor_games()
