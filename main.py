import requests

url = 'http://wttr.in/london?nTqu&lang=en'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'http://wttr.in/Шереметьево?nTqm&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'http://wttr.in/Череповец?nTqm&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)