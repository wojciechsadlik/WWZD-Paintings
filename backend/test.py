import requests

BASE = 'http://127.0.0.1:5000/'

#response = requests.post(BASE + 'painting', {'x': 0.0, 'y': 0.0, 'style': 'abstract'})
#response = requests.post(BASE + 'painting', {'x': 1.0, 'y': 0.0, 'style': 'marina'})
#response = requests.post(BASE + 'painting', {'x': 0.0, 'y': 1.0, 'style': 'abstract'})

response = requests.get(BASE + 'painting/0')
print(response.json())

response = requests.get(BASE + 'painting/1')
print(response.json())

response = requests.get(BASE + 'painting/2')
print(response.json())

response = requests.get(BASE + 'painting/3')
print(response.json())

response = requests.get(BASE + 'painting/100')
print(response.json())

response = requests.get(BASE + 'paintings_list')
print(response.json())