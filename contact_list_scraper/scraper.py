import requests
import csv
import re
from bs4 import BeautifulSoup

# Load the CSV file with government office names
with open('government_offices.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    government_offices = [row[0] for row in csv_reader]

# Search Google for each government office name and extract associated website URLs
email_list = []
for office in government_offices:
    query = office + " government office"
    google_url = "https://www.google.com/search?q=" + query
    response = requests.get(google_url)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.select('a[href*="://"]')
    for link in search_results:
        url = link['href']
        if "google" not in url:
            try:
                website_response = requests.get(url)
                website_soup = BeautifulSoup(website_response.text, "html.parser")
                # Extract valid email addresses from website pages using regex
                email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                email_matches = re.findall(email_regex, website_soup.text)
                # Append the email addresses to the list
                email_list.extend([(office, email) for email in email_matches])
            except:
                pass

# Save the email addresses to a new CSV file
with open('government_office_emails.csv', mode='w', newline='') as email_file:
    email_writer = csv.writer(email_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    email_writer.writerow(['Government Office', 'Email Address'])
    for item in email_list:
        email_writer.writerow(item)
