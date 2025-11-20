# WebScrapping_PinnacleMinds

A Python-based web scraping script that extracts business information from Yellow Pages and stores it in Pinecone vector database for efficient retrieval and analysis.

## Project Structure

This project demonstrates a complete data pipeline:
1. **Web Scraping**: Automated extraction of business listings from Yellow Pages(for instance)
2. **Data Processing**: Cleaning and structuring scraped data and saving it to output.csv file.
3. **Vector Storage**: Connecting to Pinecone database and adding the data from output file. 
4. **Data Export**: Retrieving and exporting data from the vector database by python script.

## Features

- Automated web scraping using Selenium
- Extracts key business information (name, phone, address, website)
- Stores data in CSV format
- Uploads to Pinecone vector database with metadata
- Exports data from Pinecone for analysis


## Installation

1. Clone the repository:
```python
git clone https://github.com/akhilakambhatla/WebScrapping_PinnacleMinds.git
cd WebScrapping_PinnacleMinds
```

2. Create a virtual Environment.
```python
python -m venv venv
```
   
4. Install Dependencies.
```bash
pip install -r requirements.txt
```

## Usage

1. Running WebScrapping Python Selinium Script. 
```python
python webscrapper.py
```
It takes the url as input (with search term and location) and extracts the contact information and export it to output.csv file. <br>
Input: User Given URL: <br>
Output: company name, website, address and phone number are extracted and saved it in .csv file.  <br>

2. PineCone Database

```python
python pinecone.py
```
this scripts takes output.csv file and add the extracted data into pinecone database. <br>
NOTE: Before running this script, you need to create your own API key from pinecone.io for accessing your own Database.<br> 
Input: output.csv<br>
Output: importing to Pinecone DB. You can verify it in your portal after login at pinecone.io (.home/database/indexes)<br>

3. Exporting from Pinecone DB

```python
python export_data.py
```
This script exports the data from your pinecone database to pinecone_export.csv file.
this script is for verification purposes. <br>
Input: your own Pinecone API Key. <br>
Output: pinecone_export.csv file. <br>


## References Taken from: 

- Yellow Pages for providing publicly accessible business data<br>
- Pinecone for vector database infrastructure<br>
- Selenium community for dynamic webscrapping. <br>




  
