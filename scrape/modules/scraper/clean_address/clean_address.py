import re

def clean_address(address):
    """
    Cleans an address by removing abnormal characters, reducing consecutive spaces, and trimming leading/trailing spaces.

    Parameters:
        address (str): The address to be cleaned.

    Returns:
        cleaned_address (str): The cleaned address.
    """
    # Remove abnormal characters from the address
    cleaned_address = re.sub(r'[^a-zA-Z0-9 ,.\n\r]', '', address)
    # Replace consecutive spaces with a single space
    cleaned_address = re.sub(r'\s+', ' ', cleaned_address)
    # Remove leading/trailing spaces and newlines
    cleaned_address = cleaned_address.strip()
    return cleaned_address