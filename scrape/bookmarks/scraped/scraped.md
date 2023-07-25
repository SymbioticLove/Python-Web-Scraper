# Scraped Directory

The scraped directory, nested inside the bookmarks directory, houses the `scraped.txt` file. All URLs that have been successfully scraped are copied from the `bookmarks.txt` file to the `scraped.txt` file via the `copy_bookmarks_to_scraped` function. 

## Function: copy_bookmarks_to_scraped

The `copy_bookmarks_to_scraped` function doesn't require any input parameters. It executes the following operations:

1. Reads the content of the `bookmarks.txt` file.
2. Appends this content to the `scraped.txt` file.
3. Clears the content of the `bookmarks.txt` file by writing an empty string to it.

If an error occurs during any of these operations, it's captured and displayed to the user through a tkinter messagebox. The function doesn't return any output.

The purpose of the scraped directory is to maintain a record of all URLs that have been scraped. This way, the script can avoid scraping the same URL multiple times, resulting in efficient use of resources.