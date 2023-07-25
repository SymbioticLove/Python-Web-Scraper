from bs4 import BeautifulSoup
import requests
import os
import json
from datetime import datetime
import time
from tkinter import messagebox
import random
from modules.scraper.copy_bookmarks_to_scraped.copy_bookmarks_to_scraped import copy_bookmarks_to_scraped
from modules.scraper.clean_address.clean_address import clean_address

# Set headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

def scrape_data():
    """
    Scrapes data from URLs provided in the 'bookmarks.txt' file and saves it to a JSON file. It extracts the names,
    addresses, phone numbers, and other relevant details from the URLs and then writes this data to a JSON file named 'scrape.json'.
    The function also cleans and processes the data, and handles exceptions during the process.

    Parameters:
        None

    Returns:
        None
    """
    scraped_data = []
    try:
        with open('./bookmarks/bookmarks.txt', 'r') as f:
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

            # Add a randomized delay between 1 and 3 seconds
            delay = random.uniform(1, 3)
            time.sleep(delay)

        # Load existing data from JSON file (if exists)
        output_file = './data/scrape.json'
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