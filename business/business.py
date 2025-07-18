# Business logic layer for managing facility records in memory.

facilities = []

def add_record(record):
    """
    Adds a new FacilityRecord to the in-memory list.
    """
    facilities.append(record)

def edit_record(index, updated_record):
    """
    Updates a FacilityRecord at the given index with new data.
    """
    if 0 <= index < len(facilities):
        facilities[index] = updated_record

def delete_record(index):
    """
    Deletes a FacilityRecord from the in-memory list based on index.
    """
    if 0 <= index < len(facilities):
        del facilities[index]

def get_all_records():
    """
    Retrieves the full list of records.
    """
    return facilities

def get_record(index):
    """
    Retrieves a specific record by its index.
    """
    if 0 <= index < len(facilities):
        return facilities[index]
    return None

def clear_records():
    """
    Clears all records from the in-memory list.
    """
    facilities.clear()

def sort_records_by_column(column_name):
    """
    Sorts the facilities list in place by a specific column name.
    Supported: 'facility_name', 'city', 'province', 'emissions'.
    """
    if column_name == "facility_name":
        facilities.sort(key=lambda r: r.facility_name.lower())
    elif column_name == "city":
        facilities.sort(key=lambda r: r.city.lower())
    elif column_name == "province":
        facilities.sort(key=lambda r: r.province.lower())
    elif column_name == "emissions":
        try:
            facilities.sort(key=lambda r: float(r.emissions) if r.emissions.replace('.', '', 1).isdigit() else float('inf'))
        except ValueError:
            print("Error: Emissions column contains invalid data.")
    else:
        print(f"Invalid column name for sorting: {column_name}")

def get_top_emitters(n=5):
    """
    Returns the top N facilities with the highest emissions.
    """
    try:
        sorted_list = sorted(
            facilities,
            key=lambda r: float(r.emissions) if r.emissions.replace('.', '', 1).isdigit() else 0,
            reverse=True
        )
        return sorted_list[:n]
    except Exception as e:
        print(f"Error calculating top emitters: {e}")
        return []