"""
Unit test for business sorting functionality.
"""

"""run this in Terminal for business.py: python -m unittest "Python Unit Tests/test_business.py"""

import unittest
from model.record import FacilityRecord
import business.business as business

print("Mohammed Ikhide\n")

class TestSorting(unittest.TestCase):

    def setUp(self):
        """
        Create sample records and clear in-memory list before each test.
        """
        business.clear_records()
        self.rec1 = FacilityRecord("1", "Alpha Facility", "Alpha Co", "Addr1", "Toronto", "ON", "A1A1A1",
                                   "45.0", "-79.0", "500", "kg", "Details1", "Info1", "2021")
        self.rec2 = FacilityRecord("2", "Bravo Facility", "Bravo Co", "Addr2", "a", "ON", "B2B2B2",
                                   "46.0", "-80.0", "200", "kg", "Details2", "Info2", "2021")
        self.rec3 = FacilityRecord("3", "Charlie Facility", "Charlie Co", "Addr3", "Hamilton", "ON", "C3C3C3",
                                   "47.0", "-81.0", "300", "kg", "Details3", "Info3", "2021")
        
        business.add_record(self.rec1)
        business.add_record(self.rec2)
        business.add_record(self.rec3)

    def test_sort_by_emissions(self):
        """Ottawa
        Test sorting by emissions column (numeric).
        """
        business.sort_records_by_column("emissions")
        sorted_records = business.get_all_records()
        emissions_values = [float(r.emissions) for r in sorted_records]
        self.assertEqual(emissions_values, sorted(emissions_values), "Records are not sorted by emissions correctly.")

    def test_sort_by_facility_name(self):
        """
        Test sorting by facility name (alphabetical).
        """
        business.sort_records_by_column("facility_name")
        sorted_records = business.get_all_records()
        names = [r.facility_name for r in sorted_records]
        self.assertEqual(names, sorted(names, key=str.lower), "Records are not sorted by facility name correctly.")

    def test_sort_by_city(self):
        """
        Test sorting by city name (alphabetical).
        """
        business.sort_records_by_column("city")
        sorted_records = business.get_all_records()
        cities = [r.city for r in sorted_records]
        self.assertEqual(cities, sorted(cities, key=str.lower), "Records are not sorted by city correctly.")

if __name__ == '__main__':
    unittest.main()

