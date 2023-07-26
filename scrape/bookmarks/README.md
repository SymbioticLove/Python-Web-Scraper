# Bookmarks Directory

The bookmarks directory contains the `bookmarks.txt` file, which is where all the URLs input by the user through the `add_bookmark` function are stored. The file `scraped.txt` is also housed in this directory, under a subdirectory named `scraped`, it keeps a list of all URLs that have been scraped.

## Function: add_bookmark

The `add_bookmark` function accepts an input of type `tkinter.Entry`, which represents the URL to be bookmarked.

Here's what it does:

1. Extracts the URL entered by the user from the `url_entry` widget.
2. Reads existing bookmarks from the `bookmarks.txt` file.
3. Checks if the entered URL is already present in the `bookmarks.txt` file.
    - If it is, an info message is displayed to the user indicating that the bookmark already exists.
    - If it isn't, it then checks if the URL is present in the `scraped.txt` file.
        - If it is, an error message is displayed to the user indicating that the page has already been scraped.
        - If it isn't, the URL is added to the `bookmarks.txt` file and a success message is displayed.
    - If an exception occurs during the process of adding the bookmark, an error message is displayed to the user.

The function concludes by deleting the entered URL from the `url_entry` widget.

The purpose of this directory is to keep track of all URLs that the user intends to scrape, as well as those that have already been scraped. This organization helps prevent duplicate scraping and gives the user a clear view of which web pages are pending for scraping.
