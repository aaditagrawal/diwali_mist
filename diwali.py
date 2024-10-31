import time
import os
import shutil
import random
import math

# ANSI escape codes for colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    # Add background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    # Add styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def center_text(text, color=Colors.WHITE):
    terminal_width = shutil.get_terminal_size().columns
    terminal_height = shutil.get_terminal_size().lines
    lines = text.split('\n')
    centered_lines = []
    for line in lines:
        padding = " " * ((terminal_width - len(line)) // 2)
        centered_lines.append(padding + line)
    vertical_padding = "\n" * ((terminal_height - len(lines)) // 2)
    return vertical_padding + color + '\n'.join(centered_lines) + Colors.RESET

def rainbow_text(text):
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    styles = [Colors.BOLD, Colors.UNDERLINE, Colors.BLINK]
    result = ""
    for i, char in enumerate(text):
        style = random.choice(styles) if random.random() < 0.3 else ""
        result += style + colors[i % len(colors)] + char
    return result + Colors.RESET

def create_diya_art():
    return ""

# Enhanced frames with decorative elements
frames = [
    "✨ M ✨",
    "✨ MI ✨",
    "✨ MIS ✨",
    "✨ MIST ✨",
    "🎆 MIST w 🎆",
    "🎆 MIST wi 🎆",
    "🎆 MIST wis 🎆",
    "🎆 MIST wish 🎆",
    "🌟 MIST wishe 🌟",
    "🌟 MIST wishes 🌟",
    "🌟 MIST wishes y 🌟",
    "🎇 MIST wishes yo 🎇",
    "🎇 MIST wishes you 🎇",
    "🎇 MIST wishes you a 🎇",
    "✨ MIST wishes you a h ✨",
    "✨ MIST wishes you a ha ✨",
    "✨ MIST wishes you a hap ✨",
    "🪔 MIST wishes you a happ 🪔",
    "🪔 MIST wishes you a happy 🪔",
    "🪔 MIST wishes you a happy Di 🪔",
    "🎆 MIST wishes you a happy Diw 🎆",
    "🎆 MIST wishes you a happy Diwa 🎆",
    "🎆 MIST wishes you a happy Diwal 🎆",
    f"🪔 MIST wishes you a happy Diwali! 🪔\n{create_diya_art()}"
]

def create_firecracker(width, height):
    firecracker = [[" " for _ in range(width)] for _ in range(height)]
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    symbols = ["*", ".", "💥", "✨", "🎇", "⚡"]

    # Create random explosions all over the screen
    for _ in range(width * 2):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        color = random.choice(colors)
        symbol = random.choice(symbols)
        firecracker[y][x] = color + symbol + Colors.RESET

    return "\n".join("".join(row) for row in firecracker)

# Main animation
for frame in frames:
    clear_screen()
    print(center_text(frame, random.choice([Colors.RED, Colors.YELLOW, Colors.GREEN]) + Colors.BOLD))
    time.sleep(0.15)

# Enhanced firecracker finale
width = shutil.get_terminal_size().columns
height = 15
for _ in range(50):
    clear_screen()
    print(create_firecracker(width, height))
    print(center_text(rainbow_text(frames[-1])))
    time.sleep(0.1)

final_message = f"""
{Colors.YELLOW}✨ Enjoy the festival of lights! ✨
{Colors.RED}May your Diwali be as bright as ever!
{Colors.GREEN}🪔  Peace, Prosperity and Happiness  🪔{Colors.RESET}
"""
print(center_text(final_message))
