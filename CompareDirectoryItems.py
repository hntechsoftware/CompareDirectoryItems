import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def get_size(path):
    """Returns the total size of a file or directory."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def choose_directory():
    """Prompts user to choose a directory and displays item sizes in a bar chart."""
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    items = os.listdir(folder)
    sizes = {item: get_size(os.path.join(folder, item)) for item in items}
    
    if not sizes:
        return
    
    # Plot data
    plt.figure(figsize=(10, 6))
    plt.bar(sizes.keys(), sizes.values(), color='skyblue')
    plt.xlabel("Items")
    plt.ylabel("Size (bytes)")
    plt.title(f"Size of Items in {folder}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Initialize Tkinter window
root = tk.Tk()
root.withdraw()  # Hide root window

choose_directory()

