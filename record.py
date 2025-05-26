class FacilityRecord:
    def __init__(self, np_id, facility_name, company_name, address, city, province,
                 postal_code, latitude, longitude, emissions, units,
                 facility_details, facility_info, report_year):
        self.uuid = uuid.uuid4()  # API usage
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
                f"Emissions: {self.emissions} {self.units} | Record ID: {self.uuid}")
