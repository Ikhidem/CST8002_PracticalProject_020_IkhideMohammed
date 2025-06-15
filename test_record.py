"""
test_business.py - Unit Test for Business Logic Layer

This test module verifies the correctness of operations in the business logic layer,
specifically ensuring that records can be added to the in-memory data structure 
as expected.

Author: Mohammed Ikhide
"""

import unittest
from record import FacilityRecord       # Import data model
import business                         # Import business logic functions

class TestBusinessLayer(unittest.TestCase):
    """
    Unit test class for verifying business logic operations such as adding records.
    """

    def setUp(self):
        """
        Test setup method that runs before each test.
        It clears the in-memory record list to ensure a fresh state.
        """
        business.clear_records()

    def test_add_record(self):
        """
        Test whether a record can be successfully added to the in-memory data structure.
        Verifies both the size of the list and the content of the inserted record.
        """
        # Create a sample record
        record = FacilityRecord("123", "Test Facility", "Test Co", "123 St", "City", "Province",
                                "A1A1A1", "45.0", "-75.0", "100", "kg",
                                "details", "info", "2025")
        
        # Add the record to the business logic layer
        business.add_record(record)
        
        # Assert that one record was added
        self.assertEqual(len(business.get_all_records()), 1)

        # Assert that the record content is correct
        self.assertEqual(business.get_all_records()[0].facility_name, "Test Facility")

# Entry point to run the unit test
if __name__ == '__main__':
    unittest.main()
