import csv

###########################################################
#                                                         #
#        Author: Aidan Ahern                              #
#                                                         #
###########################################################

# Input and output file paths
input_csv = 'output/unfiltered/spiderfoot_results.csv'
output_txt = 'output/filtered/malicious_ips.txt'
output_csv = 'output/filtered/malicious_ips.csv'

# Column names in the input CSV
ip_column = "IP Address"
malicious_column = "Is Malicious"

# Read and filter malicious IPs
malicious_ips = []

with open(input_csv, mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row[malicious_column].strip().lower() == 'yes':
            malicious_ips.append(row[ip_column])

# Write malicious IPs to output CSV
with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([ip_column])
    for ip in malicious_ips:
        writer.writerow([ip])

# Write malicious IPs to output TXT
with open(output_txt, mode='w') as txt_file:
    for ip in malicious_ips:
        txt_file.write(f"{ip}\n")

print(f"Malicious IPs have been exported to {output_txt} and {output_csv}")
