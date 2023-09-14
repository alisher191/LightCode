import requests
import json


# get
#########################################################################

BASE_URL = "https://fakestoreapi.com"

# new_product = {
#     "title": "Tom",
#     "price": 10000,
#     "description": "Soft doll",
#     "category": "Luxury",
#     "image": "https://i.pravatar.cc/",
#     "rating": {"rate": 4.6,  "count": 400}
# }
updatet_product = {
    'title': "Updated",
    "category": "Electronic"

}

response = requests.delete(f'{BASE_URL}/products/21')

print(response.json())


#########################################################################

# query_params = {
#     "limit": 2
# }
# response = requests.get(f'{BASE_URL}/products', params=query_params)

# with open("res_limit.txt", "w") as file:
#     file.write(str(response.json()))

#########################################################################

#########################################################################

