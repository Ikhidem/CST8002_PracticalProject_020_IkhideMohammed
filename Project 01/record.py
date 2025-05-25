# record.py

"""
    Record object representing a facility's emission data.
    Includes all attributes from the dataset as class variables.
    """
class FacilityRecord:
    
    def __init__(self, np_id, facility_name, company_name, address, city, province,
                 postal_code, latitude, longitude, emissions, units,
                 facility_details, facility_info, report_year):
        """
        Constructor method to initialize the FacilityRecord object
        with all the data fields provided by the CSV dataset.
        """
        self.np_id = np_id
        self.facility_name = facility_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.province = province
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude
        self.emissions = emissions
        self.units = units
        self.facility_details = facility_details
        self.facility_info = facility_info
        self.report_year = report_year

    def __str__(self):
        return (f"{self.facility_name} ({self.company_name}) - {self.city}, {self.province} | "
                f"Emissions: {self.emissions} {self.units}")
        
        """Similar to the tostring() method in Java, this method returns a string representation of the object."""