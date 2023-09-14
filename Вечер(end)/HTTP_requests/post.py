import requests
import json


BASE_URL = 'https://fakestoreapi.com'


new_product = {
    'title': 'Test product',
    'price': 16.5,
    'description': 'Lorem ipsum',
    'image': 'https://i.pravatar.cc/',
    'category': 'Doll'
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(f'{BASE_URL}/products', data=json.dumps(new_product), headers=headers)
print(response.json())

# response = requests.post(f'{BASE_URL}/products', json=new_product)
# print(response.json())
