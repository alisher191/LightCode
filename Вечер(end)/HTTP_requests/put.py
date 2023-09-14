import requests


BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    'title': 'Updated product',
    'category': 'Toy'
}

response = requests.put(f'{BASE_URL}/products/21', json=updated_product)
print(response.json())
