"""
business.py - Business Logic Layer for Facility Emissions Record Management

This module manages the in-memory list of facility records and provides 
functions for creating, updating, deleting, and retrieving records. 
All modifications to the data structure happen here to enforce separation 
of concerns.

Author: Mohammed Ikhide
"""

# In-memory list to store FacilityRecord objects
facilities = []

def add_record(record):
    """
    Adds a new FacilityRecord to the in-memory list.

    Args:
        record (FacilityRecord): The record object to be added.
    """
    facilities.append(record)

def edit_record(index, updated_record):
    """
    Replaces a record at a specific index with an updated record.

    Args:
        index (int): The index of the record to update.
        updated_record (FacilityRecord): The updated record object.
    """
    if 0 <= index < len(facilities):
        facilities[index] = updated_record

def delete_record(index):
    """
    Removes a record from the in-memory list by index.

    Args:
        index (int): The index of the record to delete.
    """
    if 0 <= index < len(facilities):
        del facilities[index]

def get_all_records():
    """
    Retrieves all records currently stored in memory.

    Returns:
        list: A list of FacilityRecord objects.
    """
    return facilities

def get_record(index):
    """
    Retrieves a specific record by index.

    Args:
        index (int): The index of the desired record.

    Returns:
        FacilityRecord or None: The requested record if found; otherwise, None.
    """
    if 0 <= index < len(facilities):
        return facilities[index]
    return None

def clear_records():
    """
    Clears all records from the in-memory list.
    """
    facilities.clear()
