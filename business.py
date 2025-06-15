facilities = []

def add_record(record):
    facilities.append(record)

def edit_record(index, updated_record):
    if 0 <= index < len(facilities):
        facilities[index] = updated_record

def delete_record(index):
    if 0 <= index < len(facilities):
        del facilities[index]

def get_all_records():
    return facilities

def get_record(index):
    if 0 <= index < len(facilities):
        return facilities[index]
    return None

def clear_records():
    facilities.clear()