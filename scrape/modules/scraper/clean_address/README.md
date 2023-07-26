# Clean Address Module Documentation

This module utilizes the Python `re` (regular expressions) library to manipulate and clean string data. Specifically, it focuses on cleaning addresses.

## Dependencies

- re: The `re` module in Python provides regular expression matching operations.

## Functions

### clean_address(address)

This function cleans an address by removing abnormal characters, reducing consecutive spaces, and trimming leading/trailing spaces. 

#### Parameters:

- address (str): The address to be cleaned.

#### Returns:

- cleaned_address (str): The cleaned address.

The function uses regular expressions to perform the following operations:
1. Remove abnormal characters from the address, leaving only alphanumeric characters, spaces, commas, periods, newlines, and carriage returns.
2. Replace consecutive spaces with a single space.
3. Remove leading/trailing spaces and newlines.
