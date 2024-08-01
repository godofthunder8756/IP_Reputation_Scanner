 IP_Reputation_Scanner
Automation of Spiderfoot's external scanning of IPs for reputation verification. 


###########################################################
#                                                         #
#        Author: Aidan Ahern                              #
#                                                         #
###########################################################

How To Use:

1. Populate the file 'input_ips.txt' with the list of IP address
    you would like to verify.

2. Execute the program by opening a terminal in this directory
    and either running 'sudo bash ./run.sh' or 'sudo bash ./run_gui.sh'

3. The GUI mode has two options to either run a full scan and filter
    the results or filter an exisiting "spiderfoot_results.csv" (for
    testing purposes). The GUI mode will not show scan progress until
    it has completed the scan.

    The normal CLI mode will show the progress of the scan in real-time.

4. Look in 'outputs/filtered/' to see the final list of all malicious IPs
    presented in .csv and .txt.


Notes:

-Running the GUI mode will attempt to install tkinter if not already installed.
-For longer lists of IPs it is reccomened to use the CLI mode.
-The scans uses 23 different Spiderfoot modules for strong scan confidence.
