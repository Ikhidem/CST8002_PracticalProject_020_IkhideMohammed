"""
Persistence layer for reading and writing facility records from/to CSV
"""
import csv
import uuid
from record import FacilityRecord

def clean_text(text):
    if text:
        return text.replace('\n', ' ').replace('\r', '').strip()
    return text

def load_records_from_csv(file_path, max_records=100):
    records = []
    try:
        with open("Nitrogen oxide emissions by facility.csv", mode='r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                if i >= max_records:
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
                records.append(record)
    except FileNotFoundError:
        print("Dataset file not found.")
    return records

def save_records_to_csv(records, output_dir="./"):
    filename = f"{uuid.uuid4()}.csv"
    path = output_dir + filename
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["NPRI ID", "Facility name", "Company name", "Address", "City", "Province",
                         "PostalCode", "Latitude", "Longitude", "Emissions", "Units",
                         "Facility details", "Facility information", "Report year"])
        for rec in records:
            writer.writerow([rec.np_id, rec.facility_name, rec.company_name, rec.address,
                             rec.city, rec.province, rec.postal_code, rec.latitude,
                             rec.longitude, rec.emissions, rec.units,
                             rec.facility_details, rec.facility_info, rec.report_year])
    return path
