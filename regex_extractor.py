#!/usr/bin/env python3

import re
"""
A. create a regex function and the regex rules
1. stores predefined regex patterns
2 search for matching patterns
3. returns the extracted data
B. Create the main function
1. takes a string as input
2. calls the regex function
3. prints the extracted data
"""
def extract_data(text):
    """Extracts various types of data using regex patterns:
    - Email addresses
    - URLs
    - Phone numbers
    - Credit card numbers
    - Time(12hrs and 24hrs)    
    """
    regex_rules = {
        "emails": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        "URLs": r'https?://[a-zA-Z0-9./_-]+',
        "phone numbers": r'\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}',
        "credit card numbers": r'\d{4}[-]?\d{4}[-]?\d{4}[-]?\d{4}',
        "Time": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM|am|pm))?\b'
    }

    extracted_data = {}

    for data_type, regex_rule in regex_rules.items():
        extracted_data[data_type] = re.findall(regex_rule, text)

    return extracted_data

def main():
    """MAin function to test regex extraction"""

    test_string = """
    Emails: user@example.com, firstname.lastname@company.co.uk
    URLs: https://www.example.comLinks to an external site., https://subdomain.example.org/pageLinks to an external site.
    Phones: (123) 456-7890, 987-654-3210, 555.123.4567
    Cards: 1234 5678 9012 3456, 4321-5678-9012-3456
    Time: 14:30, 2:30 PM, 09:15, 7:45 AM
    """
    extracted_results = extract_data(test_string)

    print("\nExtracted Data:")
    for data_type, values in extracted_results.items():
      print(f"{data_type}: {', '.join(values)}")

if __name__ == "__main__":
    main()

test_srting2 = """
    Emails:j.ishimwe4@alustudent.com, jonathanlivish@gmail.com
    URLs: https://www.youtube.com/watch?v=JG1livF44_E, https://watchseries.pe/home
    Phones: 078-123-4567, 078.123.4567
    Cards: 1234-5678-9012-3456
    Time: 14:30, 2:30 PM, 09:15, 7:45 AM
    """
another_extracted_result = extract_data(test_srting2)
print("\nExtracted Data for Test String 2:")
for data_type, values in another_extracted_result.items():
    print(f"{data_type}: {', '.join(values)}")
    
