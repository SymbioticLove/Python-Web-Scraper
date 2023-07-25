from tkinter import messagebox
import os

def copy_bookmarks_to_scraped():
    """
    Copies the contents of the 'bookmarks.txt' file to the 'scraped.txt' file, then clears 'bookmarks.txt'.

    This function uses a 'try/except' block to handle any file operation errors, and if an error is encountered,
    it uses a tkinter messagebox to display the error to the user.

    Parameters:
        None

    Returns:
        None
    """
    try:
        # Read the content of "bookmarks.txt"
        with open('./bookmarks/bookmarks.txt', 'r') as f:
            bookmarks_content = f.read()

        # Append the content to "scraped.txt" instead of overwriting
        with open('./bookmarks/scraped/scraped.txt', 'a') as f:
            # Move the file pointer to the end of the file to append data
            f.seek(0, os.SEEK_END)
            if f.tell() != 0:  # If the file is not empty, add a separator before appending data
                f.write('\n')
            f.write(bookmarks_content)

        # Create a new, empty "bookmarks.txt" file
        with open('./bookmarks/bookmarks.txt', 'w') as f:
            f.write("")

    except Exception as e:
        # Display error message if an exception occurs during file operations
        messagebox.showerror("File Operation Error", f"Error occurred during file operations: {e}")