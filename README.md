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



  
