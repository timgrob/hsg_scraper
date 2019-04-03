import requests
import datetime
import time

app_id = 'ebd056b2-12ba-4233-9673-b35102f9a4dc'
api_key = 'yLQx1LlB0u5YAqjus1vYhBDa6ILAXObk'
keyword = 'libya'

# helper function to iterate through dates
def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={}&api-key={}'.format(keyword, api_key)
response = requests.get(url)
data = response.json()
print(len(data["response"]["docs"]))

for i in data['response']['docs']:
    print(i['web_url'])