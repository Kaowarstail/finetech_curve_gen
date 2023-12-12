import nasdaqdatalink
import requests
import json 
import matplotlib.pyplot as plt

res = requests.get('https://data.nasdaq.com/api/v3/datasets/FRED/GDP.json')
response = json.loads(res.text)
data = response['dataset']['data']

dates = [row[0] for row in data]
values = [row[1] for row in data]

plt.plot(dates, values)
plt.xlabel('Date')
plt.ylabel('GDP (Billions of Dollars)')
plt.title('Gross Domestic Product')
plt.xticks(rotation=45)
plt.show()
