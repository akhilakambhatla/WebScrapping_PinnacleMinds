# THis code is useful  to export the data from pinecone to .csv file for verification purposes. 
# pinecone database doesnt allow the users to export directly from their website. Hence this script is needed. 
#You need to paste your own API key below. 

from pinecone import Pinecone
import pandas as pd

# Initialize Pinecone
pc = Pinecone(api_key='YOU NEED TO HAVE YOUR OWN API KEY.')
index = pc.Index('business-data')

# Fetch data (you'll need to query in batches)
results = index.query(
    vector=[0]*384,  # dummy vector, adjust dimensions
    top_k=10000,
    include_metadata=True
)

# Convert to DataFrame
data = []
for match in results['matches']:
    row = {
        'id': match['id'],
        'score': match['score'],
        **match['metadata']  # This includes all your metadata fields
    }
    data.append(row)

df = pd.DataFrame(data)
df.to_csv('pinecone_export.csv', index=False)
