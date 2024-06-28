# imported all the modules and packages 

import tkinter as tk
from tkinter import ttk, filedialog
import requests# request module
import threading # threading 
 
def download_file(url, save_path):# function to download the file 
    try:
        # initializing all the required requests
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar['maximum'] = total_size 
        with open(save_path, 'wb') as file:# to open the file
            for data in response.iter_content(block_size):
                file.write(data) #write data
                progress_bar['value'] += len(data)
        status_label.config(text="Download complete!")
    except Exception as e: #exception for no error
        status_label.config(text=f"Error: {e}")

def browse_save_path():# browse the path of the file
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
    save_path_entry.delete(0, tk.END)# delete and the insert the file
    save_path_entry.insert(0, save_path)#save path 
# a function to start the download
def start_download():# start download 
    url = url_entry.get()# to get basically the http request
    save_path = save_path_entry.get()
    if url and save_path:
        threading.Thread(target=download_file, args=(url, save_path)).start()
    else:
        status_label.config(text="Please enter URL and save path.")

# Create the main window
root = tk.Tk()#tinkter
root.title("Downloader")#title

# Create URL input field
url_label = tk.Label(root, text="URL:")# initializing the lenght, column, size
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

# Create Save Path input field
save_path_label = tk.Label(root, text="Save Path:")
save_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
save_path_entry = tk.Entry(root, width=50)
save_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
browse_button = tk.Button(root, text="Browse", command=browse_save_path)
browse_button.grid(row=1, column=2, padx=5, pady=5)

# Create Start Download button
start_button = tk.Button(root, text="Start Download", command=start_download)
start_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="we")

# Create progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Create status label
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Run the main event loop
root.mainloop()
