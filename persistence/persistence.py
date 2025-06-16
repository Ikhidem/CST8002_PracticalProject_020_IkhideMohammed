"""
Persistence layer for reading and writing facility records from/to CSV
"""

import csv         # For reading and writing CSV files
import uuid        # For generating unique filenames
from model.record import FacilityRecord  # Import the data model (FacilityRecord)

def clean_text(text):
    """
    Helper function to sanitize text values by removing newline and carriage return characters,
    and trimming any leading or trailing whitespace.
    """
    if text:
        return text.replace('\n', ' ').replace('\r', '').strip()
    return text

def load_records_from_csv(file_path, max_records=100):
    """
    Loads up to `max_records` facility records from the specified CSV file.

    Args:
        file_path (str): The name of the CSV file to load.
        max_records (int): Maximum number of records to read (default is 100).

    Returns:
        list: A list of FacilityRecord objects loaded from the file.
    """
    records = []
    try:
        # Open the CSV file for reading using the correct encoding
        with open("Nitrogen oxide emissions by facility.csv", mode='r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file)  # Read file as dictionary rows
            for i, row in enumerate(reader):
                if i >= max_records:
                    break  # Stop if max_records limit is reached

                # Create a FacilityRecord from each row, cleaning each field
                record = FacilityRecord(
                    np_id=clean_text(row['NPRI ID']),
                    facility_name=clean_text(row['Facility name']),
                    company_name=clean_text(row['Company name']),
                    address=clean_text(row['Address']),
                    city=clean_text(row['City']),
                    province=clean_text(row['Province']),
                    postal_code=clean_text(row['PostalCode']),
                    latitude=clean_text(row['Latitude']),
                    longitude=clean_text(row['Longitude']),
                    emissions=clean_text(row['Emissions']),
                    units=clean_text(row['Units']),
                    facility_details=clean_text(row['Facility details']),
                    facility_info=clean_text(row['Facility information']),
                    report_year=clean_text(row['Report year'])
                )
                records.append(record)  # Add the record to the list
    except FileNotFoundError:
        print("Dataset file not found.")  # Handle missing file gracefully
    return records

def save_records_to_csv(records, output_dir="./"):
    """
    Saves the current list of FacilityRecord objects to a new CSV file.
    The file is named using a generated UUID to ensure uniqueness.

    Args:
        records (list): The list of FacilityRecord objects to save.
        output_dir (str): The directory to save the new file in (default is current directory).

    Returns:
        str: The path to the newly created CSV file.
    """
    filename = f"{uuid.uuid4()}.csv"      # Generate unique filename
    path = output_dir + filename          # Create full file path

    # Open the new file for writing
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header row with field names
        writer.writerow([
            "NPRI ID", "Facility name", "Company name", "Address", "City", "Province",
            "PostalCode", "Latitude", "Longitude", "Emissions", "Units",
            "Facility details", "Facility information", "Report year"
        ])

        # Write each FacilityRecord object as a row
        for rec in records:
            writer.writerow([
                rec.np_id, rec.facility_name, rec.company_name, rec.address,
                rec.city, rec.province, rec.postal_code, rec.latitude,
                rec.longitude, rec.emissions, rec.units,
                rec.facility_details, rec.facility_info, rec.report_year
            ])

    return path  # Return the path of the saved file
