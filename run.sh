#!/bin/bash

###########################################################
#                                                         #
#        Author: Aidan Ahern                              #
#                                                         #
###########################################################


# Path to Python interpreter (adjust if necessary)
PYTHON_EXEC=python

# Run the first Python script
echo "Running the Spiderfoot scan script..."
$PYTHON_EXEC spiderfoot_scan.py

# Check if the first script executed successfully
if [ $? -eq 0 ]; then
    echo "Spiderfoot scan completed successfully. Now running the filter script..."
    # Run the second Python script
    $PYTHON_EXEC filter_malicious_ips.py

    if [ $? -eq 0 ]; then
        echo "Filtering malicious IPs completed successfully."
    else
        echo "Error: Filtering malicious IPs failed."
    fi
else
    echo "Error: Spiderfoot scan failed."
fi
