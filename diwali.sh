#!/bin/bash

# ANSI escape codes for color and styling
RED='\033[91m'
YELLOW='\033[93m'
GREEN='\033[92m'
MAGENTA='\033[95m'
CYAN='\033[96m'
BOLD='\033[1m'
RESET='\033[0m'

# Function to clear the screen
clear_screen() {
  clear
}

# Function to render a centered Diwali greeting frame
show_frame() {
  local color1="$1"
  local color2="$2"
  local color3="$3"
  local color4="$4"

  echo -e "
$color1$BOLD                             🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔
$color2                        ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
$color3                                                MIST WISHES YOU A
$color4                                     🌟 HAPPY AND PROSPEROUS DIWALI! 🌟
$color2                        ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
$color1$BOLD                             🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔🪔$RESET

$color4$BOLD
                                   ✨ May this Diwali bring you joy, health, and wealth! ✨
                                
$color3
                          🌼 May the glow of lamps brighten your life with endless happiness! 🌼

$color2
                🪔  Let the celebration of Diwali illuminate your path toward success and positivity!  🪔

$RESET
"
}

# Animation loop with color cycling
for i in {1..10}; do
  clear_screen
  case $((i % 5)) in
    0) show_frame "$RED" "$YELLOW" "$GREEN" "$MAGENTA" ;;
    1) show_frame "$CYAN" "$MAGENTA" "$YELLOW" "$RED" ;;
    2) show_frame "$MAGENTA" "$GREEN" "$CYAN" "$YELLOW" ;;
    3) show_frame "$YELLOW" "$RED" "$MAGENTA" "$CYAN" ;;
    4) show_frame "$GREEN" "$CYAN" "$RED" "$MAGENTA" ;;
  esac
  sleep 0.3
done

# Final static frame to keep on screen
show_frame "$YELLOW" "$RED" "$GREEN" "$CYAN"
