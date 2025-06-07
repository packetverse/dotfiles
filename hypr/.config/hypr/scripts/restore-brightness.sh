#!/bin/bash

# Check if saved brightness file exists
if [ -f ~/.last_brightness ]; then
    value=$(cat ~/.last_brightness)
    if [[ "$value" =~ ^[0-9]+$ ]]; then
        ddcutil setvcp 10 "$value"
        echo "Brightness restored to $value"
    else
        echo "Error: saved brightness value is invalid."
    fi
else
    echo "No saved brightness found. Run save-brightness.sh first."
fi
