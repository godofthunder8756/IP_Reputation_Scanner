import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading
import os

###########################################################
#                                                         #
#        Author: Aidan Ahern                              #
#                                                         #
###########################################################

# Function to run a command and capture output in real-time
def run_command(command, text_widget):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    for line in iter(process.stdout.readline, ''):
        text_widget.insert(tk.END, line.strip() + "\n")
        text_widget.see(tk.END)
    process.stdout.close()
    return_code = process.wait()
    return return_code

# Function to run the first script
def run_first_script(output_text):
    output_text.insert(tk.END, "Running Spiderfoot scan script...\n")
    ret_code = run_command(['python3', 'spiderfoot_scan.py'], output_text)
    if ret_code == 0:
        output_text.insert(tk.END, "Spiderfoot scan completed successfully.\n")

# Function to run the second script
def run_second_script(output_text):
    output_text.insert(tk.END, "Running filter malicious IPs script...\n")
    ret_code = run_command(['python3', 'filter_malicious_ips.py'], output_text)
    if ret_code == 0:
        output_text.insert(tk.END, "Filtering malicious IPs completed successfully.\n")
        messagebox.showinfo("Success", "Filtering completed.")

# Function to check and run filter script if CSV exists
def check_and_run_filter(output_text):
    if os.path.exists('output/unfiltered/spiderfoot_results.csv'):
        run_second_script(output_text)
    else:
        messagebox.showwarning("File Not Found", "Spiderfoot results CSV not found.")

# Function to start the scripts
def run_scripts():
    thread = threading.Thread(target=run_first_script, args=(output_text,))
    thread.start()

# GUI setup
root = tk.Tk()
root.title("IP Reputation Verification GUI")

# Create a frame
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Add a button to run the scripts
run_button = tk.Button(frame, text="Run Spiderfoot Scan", command=run_scripts, padx=20, pady=10)
run_button.pack(pady=20)

# Add a button to filter malicious IPs if CSV exists
filter_button = tk.Button(frame, text="Filter Malicious IPs", command=lambda: check_and_run_filter(output_text), padx=20, pady=10)
filter_button.pack(pady=10)

# Create a text widget to display output
output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=15, width=60)
output_text.pack(padx=5, pady=5)

# Create a scroll bar for the text widget
scroll_bar = tk.Scrollbar(frame, command=output_text.yview)
output_text.config(yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

# Bind the close window event to the quit function
root.protocol("WM_DELETE_WINDOW", root.quit)

# Run the Tkinter event loop
root.mainloop()
