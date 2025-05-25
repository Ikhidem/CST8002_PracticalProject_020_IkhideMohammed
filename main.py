import csv
from record import FacilityRecord

print("Mohammed Ikhide\n")  # Display name permanently

facilities = []  # Array-like data structure

def clean_text(text):  # Method to clean text fields
    if text:
        return text.replace('\n', ' ').replace('\r', '').strip()
    return text

try:
    with open("Nitrogen oxide emissions by facility.csv", mode='r', encoding='ISO-8859-1') as file:  # File-IO
        reader = csv.DictReader(file)  # Read CSV as dictionaries
        for i, row in enumerate(reader):  # Loop with counter
            if i >= 5:
                break
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
            facilities.append(record)

except FileNotFoundError:
    print("Dataset file not found. Please ensure it is in the same folder.")

# Display records using loop structure
for facility in facilities:
    print(facility)