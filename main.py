"""
Presentation layer to interact with the user.
Handles menu display and user input, and delegates actions to the business and persistence layers.
"""

from model.record import FacilityRecord                 # Import data model
import business.business as business                    # Import business logic module
import persistence.persistence as persistence           # Import file I/O operations

# Display author information
print("Mohammed Ikhide - Program by ACSIS 040871093\n")

def display_menu():
    """
    Displays the command-line menu options for the user.
    """
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
    """
    Prompts the user to enter all fields for a new FacilityRecord.
    
    Returns:
        FacilityRecord: A record object with the entered field values.
    """
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

# Main interactive loop
while True:
    display_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        # Clear current in-memory data and load fresh data from CSV
        business.clear_records()
        records = persistence.load_records_from_csv(
            "C:/Users/Ikhid/Desktop/CST8002/Practical Project Repo/CST8002_PracticalProject_020_IkhideMohammed/Nitrogen oxide emissions by facility.csv"
        )
        for rec in records:
            business.add_record(rec)
        print(f"{len(records)} records loaded.")

    elif choice == "2":
        # Save current in-memory records to a new CSV file using a UUID name
        saved_path = persistence.save_records_to_csv(business.get_all_records())
        print(f"Records saved to {saved_path}")

    elif choice == "3":
        # Display all records in memory, include author stamp every 10 records
        for i, record in enumerate(business.get_all_records()):
            print(f"{i}: {record}")
            if (i + 1) % 10 == 0:
                print("Program by Mohammed Ikhide")

    elif choice == "4":
        # Display a specific record by index
        idx = int(input("Enter record index: "))
        rec = business.get_record(idx)
        print(rec if rec else "Record not found.")

    elif choice == "5":
        # Prompt user to enter a new record, then add to memory
        record = prompt_record_input()
        business.add_record(record)
        print("Record added. Program by Mohammed Ikhide")

    elif choice == "6":
        # Edit a record by index with new values entered by user
        idx = int(input("Enter index to edit: "))
        updated = prompt_record_input()
        business.edit_record(idx, updated)
        print("Record updated. Program by Mohammed Ikhide")

    elif choice == "7":
        # Delete a record by index
        idx = int(input("Enter index to delete: "))
        business.delete_record(idx)
        print("Record deleted. Program by Mohammed Ikhide")

    elif choice == "8":
        # Exit the program
        break

    else:
        # Handle invalid input
        print("Invalid choice.")
