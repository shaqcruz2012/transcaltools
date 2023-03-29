#contact_list_scraper/scraper.py
import requests
import csv
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import logging
import time
import random

def scrape_emails(csv_file_path):
    # Load the CSV file with government office names
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        government_offices = [row[0] for row in csv_reader]
    
    # Set up logging
    logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    logging.info("Starting email scraping")
    
    # Search Google for each government office name and extract associated website URLs
    email_list = []
    for office in tqdm(government_offices):
        query = office + " government office"
        google_url = "https://www.google.com/search?q=" + query
        
        # Wait for a random period of time before making the request to avoid getting blocked
        time.sleep(random.randint(1, 5))
        
        response = requests.get(google_url)
        
        # Check if the response is successful and contains the search term to avoid getting blocked
        if response.status_code == 200 and query.lower() in response.text.lower():
            soup = BeautifulSoup(response.text, "html.parser")
            search_results = soup.select('a[href*="://"]')
            
            # Wait for a random period of time before making the request to avoid getting blocked
            time.sleep(random.randint(1, 5))
            
            for link in search_results:
                url = link['href']
                if "google" not in url:
                    try:
                        website_response = requests.get(url)
                        
                        # Check if the response is successful and contains the search term to avoid getting blocked
                        if website_response.status_code == 200 and query.lower() in website_response.text.lower():
                            website_soup = BeautifulSoup(website_response.text, "html.parser")
                            
                            # Extract valid email addresses from website pages using regex
                            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            email_matches = re.findall(email_regex, website_soup.text)
                            
                            # Append the email addresses to the list
                            email_list.extend([(office, email) for email in email_matches])
                            
                            # Log the email addresses found
                            for email in email_matches:
                                logging.info(f"Found email address {email} for {office}")
                        
                        else:
                            logging.warning(f"Failed to retrieve website for {office}")
                    
                    except Exception as e:
                        logging.error(f"An error occurred while retrieving website for {office}: {e}")
                        
        else:
            logging.warning(f"Failed to retrieve Google search results for {office}")
    
    # Save the email addresses to a new CSV file
    with open('government_office_emails.csv', mode='w', newline='') as email_file:
        email_writer = csv.writer(email_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        email_writer.writerow(['Government Office', 'Email Address'])
        for item in email_list:
            email_writer.writerow(item)
    
    logging.info("Email scraping complete")
