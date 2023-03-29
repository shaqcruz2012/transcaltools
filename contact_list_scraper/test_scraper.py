# contact_list_scraper/test_scraper.py
import unittest
import os.path


from scraper import *
class TestGovernmentOfficeScraper(unittest.TestCase):

    def test_output_file_exists(self):
        """Test that the output file is created"""
        scrape_emails('test_government_offices.csv')
        self.assertTrue(os.path.isfile('government_office_emails.csv'))

if __name__ == '__main__':
    unittest.main()
