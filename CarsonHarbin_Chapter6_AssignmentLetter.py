"""
Carson Harbin
Programming Exercise 6
This program prompts the user to input a phone number, SSN, and zip code, and then displays the validity of each.
"""


import re

def validate_phone(phone):
    #Validates a phone number format: (XXX) XXX-XXXX or XXX-XXX-XXXX
    pattern = r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"
    return bool(re.match(pattern, phone))


def validate_ssn(ssn):
    #Validates a Social Security number format: XXX-XX-XXXX
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))


def validate_zip(zip_code):
    #Validates a ZIP code format: XXXXX or XXXXX-XXXX
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))


def main():
    #Main function to get user input and validate entries
    phone = input("Enter a phone number [(XXX) XXX-XXXX or XXX-XXX-XXXX]: ")
    ssn = input("Enter a Social Security number [XXX-XX-XXXX]: ")
    zip_code = input("Enter a ZIP code [XXXXX or XXXXX-XXXX]: ")

    print(f"Phone number valid: {validate_phone(phone)}")
    print(f"Social Security number valid: {validate_ssn(ssn)}")
    print(f"ZIP code valid: {validate_zip(zip_code)}")

if __name__ == "__main__":
    main()
