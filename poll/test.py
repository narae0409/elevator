import requests, json
from datetime import datetime, timedelta
from time import mktime, strptime

url = "http://210.119.145.22/data/"
d = {'number': 5057510}
res = requests.post(url, data=d)
mybytes = res.text
mybytes = json.loads(mybytes)

latest = mybytes[-1]
late = mybytes[-2]

result = ((float)(latest['current_altitude']) - (float)(latest['base_altitude']))/(float)(latest['height'])
print(result)