# In-memory list to store all FacilityRecord objects
facilities = []

def add_record(record):
    """
    Adds a new FacilityRecord to the in-memory list.
    
    Args:
        record (FacilityRecord): The record to be added.
    """
    facilities.append(record)

def edit_record(index, updated_record):
    """
    Updates a FacilityRecord at the given index with new data.
    
    Args:
        index (int): The index of the record to update.
        updated_record (FacilityRecord): The new record to replace the existing one.
    """
    if 0 <= index < len(facilities):
        facilities[index] = updated_record

def delete_record(index):
    """
    Deletes a FacilityRecord from the in-memory list based on index.
    
    Args:
        index (int): The index of the record to remove.
    """
    if 0 <= index < len(facilities):
        del facilities[index]

def get_all_records():
    """
    Retrieves the full list of records.
    
    Returns:
        list: All FacilityRecord objects in memory.
    """
    return facilities

def get_record(index):
    """
    Retrieves a specific record by its index.
    
    Args:
        index (int): The index of the record to fetch.
    
    Returns:
        FacilityRecord or None: The requested record if it exists, otherwise None.
    """
    if 0 <= index < len(facilities):
        return facilities[index]
    return None

def clear_records():
    """
    Clears all records from the in-memory list.
    Used to reset the state between operations or tests.
    """
    facilities.clear()
