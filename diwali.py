# diwali_animation.py

import time
import os
import shutil

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    return "\n".join(line.center(terminal_width) for line in text.split("\n"))

# ASCII Art frames for animation
frames = [
    "M",
    "MI",
    "MIS",
    "MIST",
    "MIST w",
    "MIST wi",
    "MIST wis",
    "MIST wish",
    "MIST wishe",
    "MIST wishes",
    "MIST wishes y",
    "MIST wishes yo",
    "MIST wishes you",
    "MIST wishes you a",
    "MIST wishes you a h",
    "MIST wishes you a ha",
    "MIST wishes you a hap",
    "MIST wishes you a happ",
    "MIST wishes you a happy",
    "MIST wishes you a happy d",
    "MIST wishes you a happy di",
    "MIST wishes you a happy diw",
    "MIST wishes you a happy diwa",
    "MIST wishes you a happy diwal",
    "MIST wishes you a happy diwali"
]

# Firecracker animation frames
firecracker_frames = [
    "|",
    "*",
    "*|",
    "*|*",
    "-*-",
    "--*--",
    "-*|*-",
    "*-|-*",
    "**|**",
    "*\\|/*",
    "*/|\\*",
    "..*..",".*|*.","*.|.*",
    ".*♦*.","*♦|♦*","♦*|*♦",
    "*.✷.*","*✷|✷*","✷*|*✷",
    ".  ✷  .",
    " . ✷ . ",
    "  .✷.  ",
    "   .   ",
    "       "
]

# Animate text
for frame in frames:
    clear_screen()
    print(center_text(frame))
    time.sleep(0.1)

# Animate firecracker
for frame in firecracker_frames:
    clear_screen()
    print(center_text(frames[-1]))
    print(center_text(frame))
    time.sleep(0.08)

print(center_text("\nEnjoy the festival of lights!"))
