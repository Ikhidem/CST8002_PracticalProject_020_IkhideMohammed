"""
main.py - Presentation Layer for the Facility Emissions Record Management System

This module serves as the user interface, allowing interaction with the application
through a command-line menu system. It enables users to load, view, add, update,
delete, and save facility records. This file communicates with the Business and
Persistence layers to delegate functionality.

Author: Mohammed Ikhide
"""

from record import FacilityRecord  # Data model import
import business                    # Business logic module
import persistence                 # File I/O module

# Display developer identification
print("Mohammed Ikhide - Program by ACSIS 040871093\n")

def display_menu():
    """
    Displays the main menu with available user options.
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
    Prompts the user for all required record fields and returns a populated FacilityRecord object.
    
    Returns:
        FacilityRecord: A new record instance with user input values.
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

# Main interaction loop
while True:
    display_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        # Load records from the CSV file and populate the in-memory list
        business.clear_records()
        records = persistence.load_records_from_csv("Nitrogen oxide emissions by facility.csv")
        for rec in records:
            business.add_record(rec)
        print(f"{len(records)} records loaded.")

    elif choice == "2":
        # Save current in-memory records to a new CSV file with a UUID-based filename
        saved_path = persistence.save_records_to_csv(business.get_all_records())
        print(f"Records saved to {saved_path}")

    elif choice == "3":
        # Display all records, with name printed every 10 records
        for i, record in enumerate(business.get_all_records()):
            print(f"{i}: {record}")
            if (i + 1) % 10 == 0:
                print("Program by Mohammed Ikhide")

    elif choice == "4":
        # Display a single record by index
        idx = int(input("Enter record index: "))
        rec = business.get_record(idx)
        print(rec if rec else "Record not found.")

    elif choice == "5":
        # Add a new record to the in-memory list
        record = prompt_record_input()
        business.add_record(record)
        print("Record added.")

    elif choice == "6":
        # Edit an existing record by index
        idx = int(input("Enter index to edit: "))
        updated = prompt_record_input()
        business.edit_record(idx, updated)
        print("Record updated.")

    elif choice == "7":
        # Delete a record from memory by index
        idx = int(input("Enter index to delete: "))
        business.delete_record(idx)
        print("Record deleted.")

    elif choice == "8":
        # Exit the program
        break

    else:
        # Handle invalid input
        print("Invalid choice.")
