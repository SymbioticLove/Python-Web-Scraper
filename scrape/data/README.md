## Data Directory and JSON Structure

The data resulting from the `scrape_data` function is stored in the `data` directory. This data is saved as a JSON file (`scrape.json`), which is a universal data structure that's easy to read and write for both humans and machines.

Each entry in the `scrape.json` file represents a single scraped webpage and is stored as a JSON object, an example of which is shown below:

```json
{
    "Names": [
        "Rachael Thompson",
        "Perry Gabuzzi, CCIM"
    ],
    "Address": "2525 E Camelback Rd, Suite 210 Phoenix, AZ 85016",
    "PhoneNumber": "(602)513-5122",
    "BusinessName": "Kidder Mathews",
    "ListingAddress": "Osborn Medical Plaza",
    "DateStamp": "07-25-2023, 14:44"
}
```

### Here's what each field represents:

- **Names**: This is an array that holds the names scraped from the webpage. Each name is a string.
- **Address**: This is a string that holds the physical address of the business or individual.
- **PhoneNumber**: This is a string that holds the contact phone number.
- **BusinessName**: This is a string that holds the name of the business.
- **ListingAddress**: This is a string that holds the listing address or location scraped from the webpage.
- **DateStamp**: This is a string that represents the date and time when the webpage was scraped. The date format is "MM-DD-YYYY", and the time format is in 24-hour format.

The `data` directory serves to consolidate all scraped data into a single location. This makes it easy to manage and access the data, whether it's for viewing, backup, or further analysis.
