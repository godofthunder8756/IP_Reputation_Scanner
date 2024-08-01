import subprocess
import csv
import re

###########################################################
#                                                         #
#        Author: Aidan Ahern                              #
#                                                         #
###########################################################

# Input and output file paths
input_file = 'input_ips.txt'
output_csv = 'output/unfiltered/spiderfoot_results.csv'

# Define the list of modules to run
modules = [
    "sfp_abusech", "sfp_alienvault", "sfp_blocklistde", "sfp_cinsscore",
    "sfp_cleantalk", "sfp_comodo", "sfp_cybercrimetracker", "sfp_emergingthreats",
    "sfp_fortinet", "sfp_fraudguard", "sfp_greensnow", "sfp_hackertarget",
    "sfp_isc", "sfp_maltiverse", "sfp_opendns", "sfp_quad9", "sfp_spamcop",
    "sfp_spamhaus", "sfp_stevenblack_hosts", "sfp_surbl", "sfp_talosintel",
    "sfp_threatcrowd", "sfp_threatfox", "sfp_vxvault"
]

# Convert the list of modules to a comma-separated string
modules_str = ",".join(modules)

# Function to check if an IP is considered malicious
def is_malicious(spiderfoot_output):
    malicious_keywords = ["malicious", "blacklisted", "spammer", "threat"]
    for line in spiderfoot_output.splitlines():
        if any(keyword in line.lower() for keyword in malicious_keywords):
            return True
    return False

# Read IP addresses from input file
with open(input_file, 'r') as file:
    ip_addresses = [line.strip() for line in file.readlines()]

# Calculate the total number of IP addresses
total_ips = len(ip_addresses)

# Prepare CSV output
csv_columns = ["IP Address", "Is Malicious"]

with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_columns)

    for index, ip in enumerate(ip_addresses):
        print(f"Running scan for IP: {ip}")
        command = ["spiderfoot", "-s", ip, "-m", modules_str, "-q"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            is_malicious_flag = is_malicious(result.stdout)
            writer.writerow([ip, "Yes" if is_malicious_flag else "No"])
            print(f"Scan completed for IP: {ip} - Malicious: {'Yes' if is_malicious_flag else 'No'}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing Spiderfoot for IP {ip}: {e}")

        # Calculate remaining IPs and percentage completed
        remaining_ips = total_ips - (index + 1)
        percentage_completed = ((index + 1) / total_ips) * 100
        print(f"Remaining: {remaining_ips}, Completed: {percentage_completed:.2f}%")

print(f"Results saved to {output_csv}")
