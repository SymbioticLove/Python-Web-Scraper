import os
import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time
import random
import re

# Define the url_entry variable globally so it can be accessed by add_bookmark() function.
url_entry = None

# Set headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

def clean_address(address):
    # Remove abnormal characters from the address
    cleaned_address = re.sub(r'[^a-zA-Z0-9 ,.\n\r]', '', address)
    # Replace consecutive spaces with a single space
    cleaned_address = re.sub(r'\s+', ' ', cleaned_address)
    # Remove leading/trailing spaces and newlines
    cleaned_address = cleaned_address.strip()
    return cleaned_address

def initialize_bookmarks_file():
    try:
        with open('../bookmarks/bookmarks.txt', 'w') as f:
            # Write an empty string to initialize the file
            f.write("")

    except Exception as e:
        # Display error message if an exception occurs during file operations
        messagebox.showerror("File Operation Error", f"Error occurred during file operations: {e}")

def copy_bookmarks_to_scraped():
    try:
        # Read the content of "bookmarks.txt"
        with open('../bookmarks/bookmarks.txt', 'r') as f:
            bookmarks_content = f.read()

        # Append the content to "scraped.txt" instead of overwriting
        with open('../bookmarks/scraped/scraped.txt', 'a') as f:
            # Move the file pointer to the end of the file to append data
            f.seek(0, os.SEEK_END)
            if f.tell() != 0:  # If the file is not empty, add a separator before appending data
                f.write('\n')
            f.write(bookmarks_content)

        # Create a new, empty "bookmarks.txt" file
        with open('../bookmarks/bookmarks.txt', 'w') as f:
            f.write("")

    except Exception as e:
        # Display error message if an exception occurs during file operations
        messagebox.showerror("File Operation Error", f"Error occurred during file operations: {e}")

def scrape_data():
    scraped_data = []
    try:
        with open('../bookmarks/bookmarks.txt', 'r') as f:
            urls = f.readlines()

        for url in urls:
            url = url.strip()
            if not url.startswith('http'):
                url = 'http://' + url  # Add 'http://' if the URL doesn't have it.

            print("Fetching URL:", url)
            response = requests.get(url, headers=headers)  # Use the headers in the request

            if response.status_code != 200:
                raise Exception(f"Failed to fetch URL {url}. Status code: {response.status_code}")

            print("Parsing HTML content...")
            soup = BeautifulSoup(response.content, 'html.parser')
            print("Parsing complete.")

            # Extract first names and last names as pairs
            names = []
            seen_names = set()
            fname_elements = soup.select('.first-name')
            lname_elements = soup.select('.last-name')

            # Extract and clean the address from elements with class 'inline-block'
            address_elements = soup.select('.inline-block')
            address = ' '.join([addr.text.strip() for addr in address_elements])
            cleaned_address = clean_address(address)

            # Extract the business name if it exists, otherwise log "N/A"
            business_name_element = soup.select_one('.contact-logo')
            if business_name_element:
                business_name = business_name_element.get('title')
            else:
                business_name = "N/A"

            # Extract the text from elements with class 'profile-hero__segment'
            listing_address_element = soup.select_one('.profile-hero__segment')
            listing_address = listing_address_element.text.strip() if listing_address_element else ""

            for fname_el, lname_el in zip(fname_elements, lname_elements):
                first_name = fname_el.text.strip()
                last_name = lname_el.text.strip()
                full_name = f"{first_name} {last_name}"

                # Check if the name has already been logged and is not the invalid entry
                if full_name not in seen_names and full_name != "Please enter your first name. Please enter your last name.":
                    names.append(full_name)
                    seen_names.add(full_name)

            # Extract phone number from the href value of the element with class 'number'
            phone_number = ''
            phone_element = soup.select_one('.number')
            if phone_element:
                phone_number = phone_element.get('href')
                # Remove the space between the area code and the beginning of the phone number
                phone_number = phone_number.replace(" ", "")
                # Truncate 'tel:' from the phone number
                if phone_number.startswith('tel:'):
                    phone_number = phone_number[4:]

            # Extract and concatenate the address from elements with class 'inline-block'
            address_elements = soup.select('.inline-block')
            address = ' '.join([addr.text.strip() for addr in address_elements])

            scraped_data.append({
                'Names': names,
                'Address': cleaned_address,  # Use the cleaned address
                'PhoneNumber': phone_number,
                'BusinessName': business_name,
                'ListingAddress': listing_address,  # Add the listing address
                'DateStamp': datetime.now().strftime('%m-%d-%Y, %H:%M')
            })

            # Add a randomized delay between 1 and 4 seconds
            delay = random.uniform(1, 4)
            time.sleep(delay)

        # Load existing data from JSON file (if exists)
        output_file = '../data/scrape.json'
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        # Combine existing data and new scraped data
        combined_data = existing_data + scraped_data

        # Save combined data to JSON file (open in "write" mode, not "append" mode)
        with open(output_file, 'w') as f:
            json.dump(combined_data, f, indent=4)

        # Copy bookmarks to scraped.txt and delete bookmarks.txt
        copy_bookmarks_to_scraped()

        # Display back-end success message
        messagebox.showinfo("Scrape", "Data has been scraped and added to JSON file.")

    except Exception as e:
        # Display error message if an exception occurs during data scraping
        messagebox.showerror("Scrape Error", f"Error occurred while scraping data: {e}")

def reports():
    # Placeholder function for the "Reports" button
    messagebox.showinfo("Reports", "This feature is currently under development.")
        
def add_bookmark():
    global url_entry
    url = url_entry.get()
    try:
        # Read existing bookmarks from the file
        with open('../bookmarks/bookmarks.txt', 'r') as f:
            existing_bookmarks = f.readlines()

        # Check if the bookmark already exists
        if url + '\n' in existing_bookmarks:
            messagebox.showinfo("Bookmark Add", "Bookmark already added.")
        else:
            # Check if the bookmark URL is already scraped
            with open('../bookmarks/scraped/scraped.txt', 'r') as f:
                scraped_urls = f.readlines()

            if url + '\n' in scraped_urls:
                messagebox.showerror("Bookmark Add Error", "Page already scraped.")
            else:
                # Write the new bookmark to the file
                with open('../bookmarks/bookmarks.txt', 'a') as f:
                    f.write(url + '\n')
                url_entry.delete(0, tk.END)

                # Display front-end success message
                messagebox.showinfo("Bookmark Added", "Bookmark has been successfully added.")

    except Exception as e:
        # Display error message if an exception occurs during bookmark addition
        messagebox.showerror("Bookmark Add Error", f"Error occurred while adding the bookmark: {e}")

def main():
    global url_entry
    root = tk.Tk()
    root.title("Scrape and Reports")

    # Set the window size and make it non-resizable
    window_width = 300
    window_height = 300
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    # Initialize bookmarks.txt if it doesn't exist
    if not os.path.exists('../bookmarks/bookmarks.txt'):
        initialize_bookmarks_file()

    url_entry = tk.Entry(root, width=40)  # Increase the width of the entry box
    url_entry.pack(pady=10)

    add_button = tk.Button(root, text="Add Bookmark", command=add_bookmark)
    add_button.pack(pady=5)

    scrape_button = tk.Button(root, text="Scrape", command=scrape_data)
    scrape_button.pack(pady=20)

    reports_button = tk.Button(root, text="Reports", command=reports)
    reports_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
