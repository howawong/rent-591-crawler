import requests
import pandas as pd
URL = 'https://rent.591.com.hk/?m=home&c=search&a=rslist&v=new&type=1&region=2&section=34&hasimg=1&searchtype=1&p=%d'


page = 1
all_details = set()
all_items = []
while True:
    url = URL % (page)
    print(url)
    headers = {'X-Requested-With': 'XMLHttpRequest', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    j = r.json()
    #print(r.text)
    items = j['items']
    no_new_item = True
    for item in items:
        detail_url = item['detailUrl']
        if detail_url not in all_details:
            all_details.add(detail_url)
            no_new_item = False
            all_items.append(item)
    print('Page %d, Number of Items %d' % (page, len(all_items)))
    page += 1
    if no_new_item:
        break

df = pd.DataFrame(all_items)
df.to_csv('output.csv', index=False, encoding='utf-8')
