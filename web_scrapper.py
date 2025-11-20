# The sample script uses yellow pages as their primary reference url where the contact information is collected from small scale business in Camarillo, CA location. 
# YOu can use any url for webscrapping

#Sample_website (Lawfirms): #https://www.yellowpages.com/search?search_terms=Small+Business+Attorneys&geo_location_terms=Camarillo%2C+CA"
#website of small business development center: "https://www.yellowpages.com/search?search_terms=Small+Business+Development+Center&geo_location_terms=Camarillo%2C+CA"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Setup
driver = webdriver.Chrome()
url = 'GIVE ANY EXAMPLE URL OF LIST OF DATA FROM YELLOW PAGES/YELP FOR INSTANCE'.
driver.get(url)
time.sleep(3)

businesses = []

# Find all business listings
listings = driver.find_elements(By.CLASS_NAME, "result")[:15]

for listing in listings:
    business = {}
    
    # Company name
    try:
        business['company_name'] = listing.find_element(By.CLASS_NAME, "business-name").text.strip()
    except:
        business['company_name'] = ""
    
    # Phone number
    try:
        business['phone'] = listing.find_element(By.CLASS_NAME, "phone").text.strip()
    except:
        business['phone'] = ""
    
    # Address
    try:
        business['address'] = listing.find_element(By.CLASS_NAME, "street-address").text.strip()
        locality = listing.find_element(By.CLASS_NAME, "locality").text.strip()
        business['address'] = f"{business['address']}, {locality}"
    except:
        business['address'] = ""
    
    # Website URL
    try:
        website_link = listing.find_element(By.CSS_SELECTOR, "a.track-visit-website")
        business['website'] = website_link.get_attribute('href')
    except:
        business['website'] = ""
    
    businesses.append(business)
    print(f"Scraped: {business['company_name']}")

driver.quit()

# Print results
print("\n" + "="*80)
for i, biz in enumerate(businesses, 1):
    print(f"\n{i}. {biz['company_name']}")
    print(f"   Phone: {biz['phone']}")
    print(f"   Address: {biz['address']}")
    print(f"   Website: {biz['website']}")

# Save to CSV
with open('output_new.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['company_name', 'phone', 'address', 'website'])
    writer.writeheader()
    writer.writerows(businesses)

print("\n" + "="*80)
print(f"\nData saved to output.csv ({len(businesses)} companies)")
