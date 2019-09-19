import requests
import feedparser

region = 'IN'
d = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=' + region)
shelf = [[0 for i in range(2)] for j in range(10)] 

for i in range(10):
    shelf[i][0] = d['entries'][i]['title']
    shelf[i][1] = d['entries'][i]['ht_news_item_url']

for s in shelf:
    print(s[0] + " : ")
    try:
        response = requests.get(s[1],timeout=4)
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(response.status_code)
    print()
