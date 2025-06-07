#!/bin/bash

WALLPAPER_DIR="$HOME/Pictures/Wallpapers"
WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.png" \) | shuf -n 1)
TRANSITION_TYPES=("simple" "fade" "left" "right" "top" "bottom" "wipe" "wave" "grow" "center" "outer")
RANDOM_TRANSITION=${TRANSITION_TYPES[$RANDOM % ${#TRANSITION_TYPES[@]}]}
RANDOM_DURATION=$(awk 'BEGIN{srand(); print 1+rand()}')
FPS=75
RANDOM_STEP=$((RANDOM % 31 + 90))

# Put wallpaper in a file for external programs to read
echo "$WALLPAPER" > "$HOME/.cache/current_wallpaper"

WALLPAPER_EXTENSION="${WALLPAPER##*.}"
cp "$WALLPAPER" "$HOME/.cache/current_wallpaper.$EXTENSION"

swww img "$WALLPAPER" \
    --transition-type "$RANDOM_TRANSITION" \
    --transition-fps "$FPS" \
    --transition-duration "$RANDOM_DURATION" \
