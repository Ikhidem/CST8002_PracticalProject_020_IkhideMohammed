"""
Presentation layer to interact with the user.
"""

""" To run Main use terminal command: python -m presentation.main"""

from model.record import FacilityRecord
import business.business as business
import persistence.persistence as persistence

print("Mohammed Ikhide\n")

def display_menu():
    print("\nMenu:")
    print("1. Load records from CSV")
    print("2. Save records to new CSV (UUID)")
    print("3. Display all records")
    print("4. Display one record")
    print("5. Add a new record")
    print("6. Edit a record")
    print("7. Delete a record")
    print("8. Sort records by column")
    print("9. Exit")

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
        records = persistence.load_records_from_csv(
            "C:/Users/Ikhid/Desktop/CST8002/Practical Project Repo/CST8002_PracticalProject_020_IkhideMohammed/Nitrogen oxide emissions by facility.csv"
        )
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
        print("Record added. Program by Mohammed Ikhide")

    elif choice == "6":
        idx = int(input("Enter index to edit: "))
        updated = prompt_record_input()
        business.edit_record(idx, updated)
        print("Record updated. Program by Mohammed Ikhide")

    elif choice == "7":
        idx = int(input("Enter index to delete: "))
        business.delete_record(idx)
        print("Record deleted. Program by Mohammed Ikhide")

    elif choice == "8":
        print("Choose column to sort by:")
        print("1. Facility name")
        print("2. City")
        print("3. Province")
        print("4. Emissions")
        sort_choice = input("Enter choice: ")

        column_map = {
            "1": "facility_name",
            "2": "city",
            "3": "province",
            "4": "emissions"
        }

        column_name = column_map.get(sort_choice)
        if column_name:
            business.sort_records_by_column(column_name)
            print(f"Records sorted by {column_name}. Program by Mohammed Ikhide")
        else:
            print("Invalid sort choice.")

    elif choice == "9":
        break

    else:
        print("Invalid choice.")
