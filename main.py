main.py

"""
Presentation layer to interact with the user
"""
from record import FacilityRecord
import business
import persistence

print("Mohammed Ikhide - Program by ACSIS 040871093\n")

def display_menu():
    print("\nMenu:")
    print("1. Load records from CSV")
    print("2. Save records to new CSV (UUID)")
    print("3. Display all records")
    print("4. Display one record")
    print("5. Add a new record")
    print("6. Edit a record")
    print("7. Delete a record")
    print("8. Exit")

def prompt_record_input():
    return FacilityRecord(
        input("NPRI ID: "),
        input("Facility name: "),
        input("Company name: "),
        input("Address: "),
        input("City: "),
        input("Province: "),
        input("PostalCode: "),
        input("Latitude: "),
        input("Longitude: "),
        input("Emissions: "),
        input("Units: "),
        input("Facility details: "),
        input("Facility information: "),
        input("Report year: ")
    )

while True:
    display_menu()
    choice = input("Enter choice: ")
    if choice == "1":
        business.clear_records()
        records = persistence.load_records_from_csv("Nitrogen oxide emissions by facility.csv")
        for rec in records:
            business.add_record(rec)
        print(f"{len(records)} records loaded.")
    elif choice == "2":
        saved_path = persistence.save_records_to_csv(business.get_all_records())
        print(f"Records saved to {saved_path}")
    elif choice == "3":
        for i, record in enumerate(business.get_all_records()):
            print(f"{i}: {record}")
            if (i + 1) % 10 == 0:
                print("Program by Mohammed Ikhide")
    elif choice == "4":
        idx = int(input("Enter record index: "))
        rec = business.get_record(idx)
        print(rec if rec else "Record not found.")
    elif choice == "5":
        record = prompt_record_input()
        business.add_record(record)
        print("Record added.")
    elif choice == "6":
        idx = int(input("Enter index to edit: "))
        updated = prompt_record_input()
        business.edit_record(idx, updated)
        print("Record updated.")
    elif choice == "7":
        idx = int(input("Enter index to delete: "))
        business.delete_record(idx)
        print("Record deleted.")
    elif choice == "8":
        break
    else:
        print("Invalid choice.")