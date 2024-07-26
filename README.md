# Alarm Clock

This project is a simple Python-based alarm clock application. It allows the user to set an alarm for a specified time duration and plays a song when the alarm goes off. The user can stop the alarm by pressing the 'q' or 'Q' key.

## Features
- Set an alarm for a specific duration (hours, minutes, seconds)
- Plays a specified MP3 file when the alarm goes off
- Stop the alarm by pressing the 'q' or 'Q' key

## Requirements
- Python 3.x
- Pygame
- Msvcrt (only available on Windows)

## Installation

1. Ensure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).
2. Install the required Pygame library using pip:
    ```bash
    pip install pygame
    ```
3. Place your MP3 file at the specified path in the code. The default path is `"C:/Users/AMAN/Documents/STUDY/song.mp3"`. You can change this path to the location of your MP3 file.

## Usage

1. Clone the repository or download the code.
2. Run the script:
    ```bash
    python alarm_clock.py
    ```
3. Follow the on-screen prompts to set the alarm time:
    - Enter the number of hours
    - Enter the number of minutes
    - Enter the number of seconds
4. The alarm will play the specified song when the time is up.
5. Press the 'q' or 'Q' key to stop the alarm.

## Code Explanation

### Functions

- `set_alarm()`: This function prompts the user to enter the alarm duration, calculates the alarm time, and continuously checks the current time. When the current time matches or exceeds the alarm time, it plays the alarm sound and waits for the user to press 'q' or 'Q' to stop the alarm.

- `play_song()`: This function plays the alarm song using the Pygame mixer.

- `stop_song()`: This function stops the alarm song and quits the Pygame mixer.

## Notes

- This script uses the `msvcrt` library, which is only available on Windows. If you are using a different operating system, you will need to find an alternative way to detect key presses.
- Ensure the path to your MP3 file is correct to avoid any file not found errors.

## Output

Check out the LinkedIn post showcasing the output of this code [here](https://www.linkedin.com/posts/aman-mogal_internpe-python-coding-activity-7078415538175057920-scCi?utm_source=share&utm_medium=member_desktop).


