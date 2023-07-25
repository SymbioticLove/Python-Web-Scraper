# Main.py and Modules Documentation

The `main.py` script serves as the entry point for the web scraping and bookmark management application, utilizing the Tkinter library to create a graphical user interface (GUI). This script is packaged with multiple modules that are structured as follows:

```
.
+-- main.py
+-- main.md
+-- unpackaged_script
  +-- scrape.py
+-- modules
  +-- scraper
    +-- add_bookmark
|     +-- add_bookmark.py
      +-- add_bookmark.md
    +-- clean_address
      +-- clean_address.py
      +-- clean_address.md
    +-- copy_bookmarks_to_scraped
      +-- copy_bookmarks_to_scraped.py
      +-- copy_bookmarks_to_scraped.md
    +-- initialize_bookmarks
      +-- initialize_bookmarks.py
      +-- initialize_bookmarks.md
    +-- scrape_data
      +-- scrape_data.py
      +-- scrape_data.md
  +-- reports
    (report modules/.md's here)
+-- bookmarks
  +-- bookmarks.txt
  +-- bookmarks.md
  +-- scraped
    +-- scraped.txt
    +-- scraped.md
+-- data
  +-- scrape.json
  +-- scrape.md
```

## Modules

### `./modules/scraper/add_bookmark/add_bookmark.py`
This module has the `add_bookmark()` function that takes a URL entered by the user, verifies it against the existing bookmarks and scraped URLs, and adds it to the bookmarks if it is unique. The bookmarked URL is then cleared from the entry box in the GUI.

### `./modules/scraper/scrape_data/scrape_data.py`
This module contains the `scrape_data()` function. It scrapes data from the bookmarked URLs and saves the extracted information in a JSON file. If the JSON file already exists, the new data is appended to the existing data; if not, a new file is created. After scraping the data, it copies the scraped URLs from `bookmarks.txt` to `scraped.txt` and clears the bookmarks file.

### `./modules/scraper/initialize_bookmarks/initialize_bookmarks.py`
This module contains the `initialize_bookmarks_file()` function which creates the `bookmarks.txt` file if it doesn't exist. It is called at the beginning of the `main()` function.

## Functions Description

### Function: clean_address
This function cleans the address string input by removing abnormal characters and excessive white spaces.

### Function: copy_bookmarks_to_scraped
This function copies the bookmarked URLs to the `scraped.txt` file and then reinitializes the bookmarks file.

### Function: reports
This function is a placeholder for a "Reports" feature that is currently under development. When clicked, it displays a message indicating this status.

### Function: main
This is the main function of the script and serves as the entry point. It initializes the Tkinter GUI and sets up the layout and functionalities of the buttons.

## How to Use

1. Run `main.py` to start the application.
2. Enter a URL in the input box and click the "Add Bookmark" button to add it as a bookmark. The application will display a success message if the bookmark is added successfully, or an error message if the bookmark already exists or if the page has been scraped.
3. Click the "Scrape" button to start the scraping process for all bookmarked URLs. A success message will appear when the data has been successfully scraped and added to the JSON file.
4. The "Reports" button is currently under development and displays a message indicating this when clicked.
