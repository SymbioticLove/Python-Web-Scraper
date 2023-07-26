# Scrape Data Module Documentation

The Scrape Data module provides the main functionality for scraping data from URLs in the 'bookmarks.txt' file.

## Dependencies

- BeautifulSoup: Library for web scraping purposes to pull the data out of HTML and XML files.
- requests: Library for making HTTP requests in Python.
- json: Library for working with JSON data.
- datetime: Module to work with dates.
- time: This module provides various time-related functions.
- tkinter: Python's standard GUI package.
- random: This module implements pseudo-random number generators for various distributions.
- modules.scraper.copy_bookmarks_to_scraped: Module for copying bookmarks to scraped.
- modules.scraper.clean_address: Module for cleaning addresses.

## Functions

### scrape_data()

This function scrapes data from URLs specified in the 'bookmarks.txt' file and saves it to a JSON file.

The scraped data includes names, addresses, phone numbers, business names, and other relevant details from each URL. 

The function also cleans and processes the data as necessary, handles any exceptions encountered during the scraping process, and uses a tkinter messagebox to display any error messages.

#### Parameters:

None

#### Returns:

None

This function follows these main steps:

1. Reads the 'bookmarks.txt' file to get the URLs to scrape.
2. Sends a request to each URL and parses the HTML content.
3. Extracts the relevant data from the HTML content.
4. Cleans and processes the data as necessary.
