# alu_regex-data-extraction-IshimweJ-Ona
HTML, REGEX practice
# Regex-Based Data Extraction Tool

## **Project Overview**
This project is a **Regular Expressions (Regex)** based tool written in Python that extracts structured data from unstructured text. It efficiently searches for and extracts:
- Email addresses
- URLs (web links)
- Phone numbers (various formats)
- Credit card numbers
- Time formats (both 12-hour and 24-hour)

Regex enables precise matching, making this script ideal for handling large text inputs and automating data extraction.

-----------

## **Features**
 Extracts multiple types of structured data using regex  
 Handles different formats for phone numbers, URLs, and time representations  
 Outputs extracted data in a clean and structured format  
 Fully optimized Python implementation  

-----------

## **regex**
a. extracting email addresses
- [a-zA-Z0-9_.+-]+ : Matches the username part (letters, numbers, _, ., +, -).
- @ → Matches the @ symbol.
- [a-zA-Z0-9-]+\. :Matches the domain (letters/numbers, followed by .).
- [a-zA-Z0-9-.]+ :Matches the extension (e.g., .com, .co.uk).

b. Extracting URLs
- https?:// :Matches http:// or https://
- [a-zA-Z0-9./_-]+ : Matches domain names and file paths

c. extracting phone numbers
- \(?\d{3}\)? : Matches an optional area code (123).
- [-.]? : Matches optional separators - or ..
- \d{3}[-.]?\d{4} : Matches the remaining number format.

d. Extracting credit card number
- \d{4}[- ]? : Matches 4-digit groups separated by - or a space.
- Repeated 4 times to match full card numbers.

e. Extracting time
 - \b → Ensures the match starts at a word boundary, preventing partial matches within words.
- (?:[01]?\d|2[0-3]) → Matches the hour:
- [01]?\d → Allows single-digit (7, 9) and two-digit (01, 10, 12) hours.
- 2[0-3] → Covers 24-hour format (20, 23).
- : → Matches the colon separator.
- [0-5]\d → Matches the minutes (00-59).
- (?:\s?(?:AM|PM))? → Handles optional AM/PM notation:
- (?:AM|PM) → Captures cases like "2:30 PM".
- \s? → Allows an optional space before AM/PM.

-----------

##**Run program**
When we execute the script using:
python regex_extractor.py
The program will:
- Search the sample text for emails, URLs, phone numbers, credit card numbers, and time formats.
- Extract matched values and store them in a dictionary.
- Print the extracted results to the screen.

