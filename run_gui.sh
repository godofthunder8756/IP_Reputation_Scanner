#!/bin/bash

###########################################################
#                                                         #
#        Author: Aidan Ahern                              #
#                                                         #
###########################################################

# Check if tkinter is installed
if ! dpkg -s python3-tk &> /dev/null; then
    echo "tkinter is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3-tk
    echo "tkinter installed successfully."
else
    echo "tkinter is already installed."
fi

# Run the GUI script
python3 gui.py
