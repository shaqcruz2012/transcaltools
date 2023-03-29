# Government Office Email Scraper

This Python script searches for government office websites and extracts any valid email addresses found on those websites. The script reads a CSV file containing a list of government office names and uses Google search to find any associated websites. It then scrapes each website to extract any email addresses found on the website. The script saves the extracted email addresses to a new CSV file with the name "government_office_emails.csv" in the same directory.

## Requirements

This script requires the following Python libraries:

- requests
- csv
- re
- beautifulsoup4

You can install these libraries using pip:

`pip install requests csv re beautifulsoup4`


## Usage

1. Save the `government_office_scraper.py` file and `government_offices.csv` file in the same directory.
2. Open the terminal or command prompt and navigate to the directory where the files are saved.
3. Run the Python script by entering the command `python government_office_scraper.py`.
4. After the script finishes running, you should see a new file named `government_office_emails.csv` in the same directory.

Make sure that you have obtained the necessary permissions to scrape the websites and that your scraping practices are ethical and legal. Additionally, you may need to modify the code to handle any specific cases, such as different CSV file formats or website structures.

## Input File Format

The input file should be a CSV file containing a list of government office names in the first column. The column header should be "Government Office Name". Each row should contain the name of a single government office.

Example input file:

`
CA Government Office Name
CA Department of Agriculture
CA Department of Commerce
CA Department of Defense
...
`


## Output File Format

The output file is a CSV file named "government_office_emails.csv" that contains a list of email addresses extracted from government office websites. Each row in the output file contains the government office name and email address in the same row. The first row of the output file contains the column headers "Government Office" and "Email Address".

Example output file:
`
Government Office,Email Address
Department of Agriculture,info@usda.gov
Department of Agriculture,ocfo.info@usda.gov
Department of Commerce,webmaster@doc.gov
...
`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
