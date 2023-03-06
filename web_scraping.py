import requests
import json
import os
import unicodedata
from bs4 import BeautifulSoup

url = 'https://www.bigbearcoolcabins.com/big-bear-cabin-rentals/moonridge-cali-bear-cabin/'

# Remove the trailing slash if present
url = url.rstrip('/')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the content within the HTML paragraph tags
paragraphs = soup.select('#node-vr-listing-full-group-vr-property-desc p, #node-vr-listing-full-group-vr-property-desc ul li')
content = ''.join([paragraph.get_text() + ' ' for paragraph in paragraphs])


# Remove special Unicode characters
content = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore').decode()

# Extract the file name from the URL
file_name = os.path.basename(url)

# Create a dictionary with the data
data = {'content': content}

# Save the data to a .json file
with open(file_name + '.json', 'w') as outfile:
  json.dump(data, outfile, separators=(',', ':'), indent=2)
