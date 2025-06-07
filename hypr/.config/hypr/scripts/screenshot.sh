#!/bin/bash

# Requirements: grim, slurp, wl-clipboard, notify-send, jq, hyprctl, swappy

save_dir="$HOME/Pictures/Screenshots"
mkdir -p "$save_dir"

filename="$(date +"%Y-%m-%d_%H-%M-%S").png"
filepath="$save_dir/$filename"

mode="$1"

case "$mode" in
    monitor)
        monitor=$(hyprctl -j activeworkspace | jq -r '.monitor')
        grim -o "$monitor" "$filepath"
        ;;
    window)
        window_json=$(hyprctl activewindow -j)
        if [[ "$window_json" == "null" || -z "$window_json" ]]; then
            notify-send "Screenshot failed" "No active window detected"
            exit 1
        fi

        # Extract window geometry
        x=$(echo "$window_json" | jq -r '.at[0]')
        y=$(echo "$window_json" | jq -r '.at[1]')
        w=$(echo "$window_json" | jq -r '.size[0]')
        h=$(echo "$window_json" | jq -r '.size[1]')

        echo "Capturing window at ${x},${y} ${w}x${h}"

        if [[ -z "$x" || -z "$y" || -z "$w" || -z "$h" ]]; then
            notify-send "Screenshot failed" "Could not get window geometry"
            exit 1
        fi

        grim -g "${x},${y} ${w}x${h}" "$filepath"
        ;;
    area)
        region=$(slurp)
        if [[ -z "$region" ]]; then
            # notify-send "Screenshot cancelled" "No area selected"
            exit 1
        fi
        grim -g "$region" "$filepath"
        ;;
    *)
        echo "Usage: $0 [monitor|window|area]"
        exit 1
        ;;
esac

# Confirm file was created
if [[ ! -f "$filepath" ]]; then
    notify-send "Screenshot failed" "File was not created"
    exit 1
fi

# Copy to clipboard
wl-copy < "$filepath"

# Notify with "View" action (that will open the screenshot in swappy)
notify-send "Screenshot saved" "$filepath" \
    -i "$filepath" \
    -a "Grimblast" \
    --action="scriptAction:-swappy -f $filepath=View" \
    -t 7000 \
    -u normal

# Exit the script
exit 0
