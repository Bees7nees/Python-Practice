import psutil # type: ignore
import time
import os

try:
    print("psutil is installed")
except ImportError:
    print("psutil is not installed")

# Configuration
game_name = "Baldur.exe"  # Replace with your game's process name
time_limit = 20  # Time limit in seconds (e.g., 30 minutes)

def monitor_game():
    """
    Monitors the specified game process and shuts it down if it exceeds the time limit.

    This function continuously checks for the specified game's process. If the game is running,
    it starts a timer. If the game runs longer than the specified time limit, the function
    terminates the game process.

    The function checks for the game process at regular intervals (every 10 seconds).

    Returns:
    None
    """
    start_time = None
    print(f"Monitoring {game_name}...")

    while True:
        # Get a list of all running processes with their names and PIDs
        running_processes = [proc.info for proc in psutil.process_iter(['name', 'pid'])]

        # Look for the game process by its name
        game_process = next((proc for proc in running_processes if proc['name'] == game_name), None)

        if game_process:
            if start_time is None:
                # Start the timer when the game is detected
                start_time = time.time()
                print(f"{game_name} started at {time.ctime(start_time)}")

            # Calculate elapsed time since the game started
            elapsed_time = time.time() - start_time
            print(f"{game_name} has been running for {int(elapsed_time)} seconds.")

            # Check if the game has exceeded the time limit
            if elapsed_time > time_limit:
                print(f"Time limit reached! Shutting down {game_name}...")
                os.system(f"taskkill /IM {game_name} /F")
                break
        else:
            # Reset start_time if the game is not running
            start_time = None

        # Wait for 10 seconds before checking again
        time.sleep(10)

if __name__ == "__main__":
    monitor_game()

