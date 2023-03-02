## Read this url and find the 10 most frequent words. 
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import requests
from collections import Counter
import re

# Retrieve the text from the URL
response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
text = response.text

# Clean up the text
text = re.sub(r'\n+', ' ', text)  
text = re.sub(r'\r', '', text)   
text = re.sub(r'\s+', ' ', text)  

# Find the 10 most frequent words
words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)
top_words = word_counts.most_common(10)

print(top_words)

## Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats
import requests
import statistics
from collections import Counter

cats_api = 'https://api.thecatapi.com/v1/breeds'

# Retrieve data from the API
response = requests.get(cats_api)
breeds = response.json()

# Extract weight and lifespan data
weights = []
lifespans = []
for breed in breeds:
    weight_metric = breed['weight']['metric']
    weight = float(weight_metric.split()[0])
    weights.append(weight)
    
    lifespan = breed['life_span']
    if lifespan.isdigit():
        lifespans.append(int(lifespan))
        
# Calculate summary statistics for weight and lifespan
weight_min = min(weights)
weight_max = max(weights)
weight_mean = statistics.mean(weights)
weight_median = statistics.median(weights)
weight_stddev = statistics.stdev(weights)

lifespan_min = min(lifespans)
lifespan_max = max(lifespans)
lifespan_mean = statistics.mean(lifespans)
lifespan_median = statistics.median(lifespans)
lifespan_stddev = statistics.stdev(lifespans)

print(f"Weight statistics: min={weight_min:.2f}, max={weight_max:.2f}, mean={weight_mean:.2f}, median={weight_median:.2f}, stddev={weight_stddev:.2f}")
print(f"Lifespan statistics: min={lifespan_min}, max={lifespan_max}, mean={lifespan_mean:.2f}, median={lifespan_median}, stddev={lifespan_stddev:.2f}")

# Create frequency table of country and breed
country_breed_counts = Counter()
for breed in breeds:
    country = breed['origin']
    breed_name = breed['name']
    country_breed_counts[(country, breed_name)] += 1

for (country, breed_name), count in country_breed_counts.most_common():
    print(f"{country}: {breed_name} - {count}")


## Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
import requests
response = requests.get('https://restcountries.com/v2/all')
data = response.json()

# Retrieve 10 largest countries
largest_countries = sorted(data, key=lambda x: x['area'], reverse=True)[:10]
print('10 Largest Countries:')
for country in largest_countries:
    print(country['name'])

# Retrieve 10 most spoken languages
languages = {}
for country in data:
    for language in country['languages']:
        if language['name'] in languages:
            languages[language['name']] += 1
        else:
            languages[language['name']] = 1
most_spoken_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]
print('\n10 Most Spoken Languages:')
for language, count in most_spoken_languages:
    print(language)

# Retrieve total number of languages
all_languages = set()
for country in data:
    for language in country['languages']:
        all_languages.add(language['name'])
total_languages = len(all_languages)
print(f'\nTotal Number of Languages: {total_languages}')


## UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). 
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send request and retrieve page content
response = requests.get(url)
content = response.content

# Parse page content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Print page title
print('Title:', soup.title.string)

# Find all dataset links on the page
links = soup.find_all('a', href=True)
datasets = []
for link in links:
    href = link['href']
    if 'datasets/' in href:
        datasets.append(href)

# Print all dataset links
print('\nDatasets:')
for dataset in datasets:
    print(dataset)