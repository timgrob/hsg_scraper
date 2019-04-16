#code to print url of NYT articles containing a specific keyword in a given time period with start_date and end_date
#import libraries
import requests
import time

#stating api_id, api_key and keyword

app_id = 'ebd056b2-12ba-4233-9673-b35102f9a4dc'
api_key = 'yLQx1LlB0u5YAqjus1vYhBDa6ILAXObk'
keyword = 'libya'

#since NYT only responds with 10 articles per request and a maximum of 10requests per minute working with a while statement, counter and time.sleep function to iterate through pages 'p'

counter = 0
flag = True
p=0
#while requests deliver a response, iterate through pages 'p', get url and print in json file
while flag:
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=libya&facet_field=day_of_week&facet=true&begin_date=20111023&end_date=20111123&api-key=yLQx1LlB0u5YAqjus1vYhBDa6ILAXObk&page={}'.format(p)
    response = requests.get(url)
    data = response.json()

#if requests come back with empty response, no url, then break (BUG.. code needs fixing here, won't break properly)
    if not 'response' in data:
        flag = False
        break
#continuesly print url printed while iterating through pages
for i in data['response']['docs']:
    print(i['web_url'])
    counter +=1
#sleep 60 seconds after every 10 pages
    if (p+1)%10==0:
    time.sleep(60)
#loop through requests, add page number to search beyond 10 responses per request
  p+=1
#print count of urls so we know number of article in stated time period
  print(counter)