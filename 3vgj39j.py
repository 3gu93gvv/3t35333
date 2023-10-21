import requests
from datetime import datetime
#KEY LINK
components = ip.split(".")
ip_total = sum(int(component) for component in components)
day = datetime.now().strftime('%d')
month = datetime.now().strftime('%m')
year = datetime.now().strftime('%y')
day_digits = [int(digit) for digit in str(day)]
month_digits = [int(digit) for digit in str(month)]
year_digits = [int(digit) for digit in str(year)]
total = sum(day_digits) + sum(month_digits) + sum(year_digits) + 84485783
result = (total + ip_total) * 1342009
keylink = "NORI" + str(result)

url = f'https://noritool.000webhostapp.com/key.html?key={keylink}'
link = requests.get(f'https://api.1short.io/public/links?token=T9WAU9ga3oMVT9wyc8ixttpQaN0sHjXM&url={url}&method_level=level_super_vip').json()
if link['status']=="error": 
	print(link['message'])
	quit()
else:
	link_key = link['shortenedUrl']
	print(link_key)
