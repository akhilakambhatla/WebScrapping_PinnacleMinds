# After exporting the .csv file, you need to create an API key from Pinecone.io
# AFter login with your credentials, your API is created and it is recommended not to share your API key publicly. 

from pinecone import Pinecone, ServerlessSpec
import csv
import time

# Initialize Pinecone 
pc = Pinecone(api_key="Need to have your own API key") 


# Create index with lowercase name
index_name = "business-data"

# create index if not present. 
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    time.sleep(10)  # waiting for index to be ready.

index = pc.Index(index_name)

# Read CSV and add to Pinecone DB
with open('output.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for i, row in enumerate(reader, 1):
     
        dummy_embedding = [0.1] * 384
        
        index.upsert(vectors=[{
            'id': f'biz-{i}',
            'values': dummy_embedding,
            'metadata': {
                'company_name': row['company_name'],
                'phone': row['phone'],
                'address': row['address'],
                'website': row['website']
            }
        }])
        print(f"Added: {row['company_name']}")

print(f"\n✓ Successfully imported to Pinecone!")
