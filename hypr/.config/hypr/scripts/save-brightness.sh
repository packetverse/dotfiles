#!/bin/bash

# Save current brightness value from monitor using ddcutil
ddcutil getvcp 10 | awk -F'=' '/Brightness/ {gsub(/,/, "", $2); print $2}' | awk '{print $1}' > ~/.last_brightness

echo "Brightness saved to ~/.last_brightness"
