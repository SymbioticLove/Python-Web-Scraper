import tkinter as tk
from tkinter import messagebox
import os
import sys
from modules.scraper.add_bookmark.add_bookmark import add_bookmark
from modules.scraper.scrape_data.scrape_data import scrape_data
from modules.scraper.initialize_bookmarks.initialize_bookmarks import initialize_bookmarks_file

# Add the path to the "modules" directory to sys.path
sys.path.append('./modules')

url_entry = None

def reports():
    # Placeholder function for the "Reports" button
    messagebox.showinfo("Reports", "This feature is currently under development.")

def main():
    """
    This script provides a user interface for a web scraper and bookmark manager.

    Functions:
        reports: Placeholder function for a future "Reports" feature. Currently, it displays a message indicating that the feature is under development.

        main: The main function for the script. It initializes the Tkinter GUI and sets up the layout and functions of the buttons.

    Notes:
        url_entry: A global variable used for the URL entry field in the Tkinter GUI.
    """
    root = tk.Tk()
    root.title("Scrape and Reports")

    # Set the window size
    window_width = 300
    window_height = 300
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    # Initialize bookmarks.txt if it doesn't exist
    if not os.path.exists('./bookmarks/bookmarks.txt'):
        initialize_bookmarks_file()

    url_entry = tk.Entry(root, width=40)
    url_entry.pack(pady=10)

    add_button = tk.Button(root, text="Add Bookmark", command=lambda: add_bookmark(url_entry))
    add_button.pack(pady=5)

    scrape_button = tk.Button(root, text="Scrape", command=scrape_data)
    scrape_button.pack(pady=20)

    reports_button = tk.Button(root, text="Reports", command=reports)
    reports_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
