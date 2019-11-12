import sys
import time
import random
import requests
import feedparser

m = 1
M = 2
region = ['IN', 'AT', 'PT', 'CL', 'SA', 'TH', 'VN', 'TW', 'ZA', 'KR', 'ID', 'PH', 'SG', 'US', 'NZ', 'CA', 'BE', 'AU', 'BR', 'JP', 'FR', 'DE', 'IT', 'NG', 'CH']
print("Curious Chirag Is Here To Distort Your Traffic\n")

while True :
    r = random.choice(region)
    d = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=' + r)
    shelf = [[0 for i in range(2)] for j in range(10)]
    try :
        for i in range(10):
            shelf[i][0] = d['entries'][i]['title']
            shelf[i][1] = d['entries'][i]['ht_news_item_url']

    except IndexError :
        print(f"No News From {r}\n")

    else :
        print(f"What's Happening In {r} ?")
        for s in shelf:
            print(f"\n{s[0]} Seems To Be Trending")
            try :
                response = requests.get(s[1],timeout=4)
            except Exception as err :
                print(f'Other error occurred: {err}')
            else :
                if response.status_code == 200 :
                    print("Found An Article")
                else :
                    print("Nothing Found")
            t = random.randrange(m, M)
            print(f"Taking {t} Seconds To Read\n")
            time.sleep(t)
