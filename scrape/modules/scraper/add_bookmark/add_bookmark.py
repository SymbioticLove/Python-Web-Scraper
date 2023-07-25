import tkinter as tk
from tkinter import messagebox

def add_bookmark(url_entry):
    """
    Add a new bookmark to the bookmarks file.

    Parameters:
        url_entry (tkinter.Entry): A tkinter Entry widget where the user enters the URL to bookmark.

    Returns:
        None
    """
    url = url_entry.get()
    try:
        # Read existing bookmarks from the file
        with open('./bookmarks/bookmarks.txt', 'r') as f:
            existing_bookmarks = f.readlines()

        # Check if the bookmark already exists
        if url + '\n' in existing_bookmarks:
            messagebox.showinfo("Bookmark Add", "Bookmark already added.")
        else:
            # Check if the bookmark URL is already scraped
            with open('./bookmarks/scraped/scraped.txt', 'r') as f:
                scraped_urls = f.readlines()

            if url + '\n' in scraped_urls:
                messagebox.showerror("Bookmark Add Error", "Page already scraped.")
            else:
                # Write the new bookmark to the file
                with open('./bookmarks/bookmarks.txt', 'a') as f:
                    f.write(url + '\n')
                url_entry.delete(0, tk.END)

                # Display front-end success message
                messagebox.showinfo("Bookmark Added", "Bookmark has been successfully added.")

    except Exception as e:
        # Display error message if an exception occurs during bookmark addition
        messagebox.showerror("Bookmark Add Error", f"Error occurred while adding the bookmark: {e}")