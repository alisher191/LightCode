import requests


"""
                Как сделать POST-запрос
Мы используем запрос POST для добавления новых данных в REST API. 
Данные отправляются на сервер в формате JSON, 
который выглядит как словарь Python. Согласно документации Fake Store API, 
у продукта есть следующие атрибуты: title (название), price (цена), 
description (описание), image (изображение) и category (категория).
"""
# new_product = {
#     "title": 'test product',
#     "price": 13.5,
#     "description": 'lorem ipsum set',
#     "image": 'https://i.pravatar.cc',
#     "category": 'electronic'
# }

"""Мы можем отправить запрос POST с помощью метода requests.post() следующим образом:"""

# BASE_URL = 'https://fakestoreapi.com'
# new_product = {
#     "title": 'test product',
#     "price": 13.5,
#     "description": 'lorem ipsum set',
#     "image": 'https://i.pravatar.cc',
#     "category": 'electronic'
# }
# response = requests.post(f"{BASE_URL}/products", json=new_product)
# print(response.json())
"""
В методе request.post() мы можем передавать данные JSON с помощью аргумента json. 
Использование аргумента json автоматически устанавливает в 
Content-Type значение Application/JSON в заголовке запроса.

Как только мы сделаем запрос POST в конечной точке /products, 
мы получим объект продукта с идентификатором в ответе.
"""

##############################################

"""Если мы не используем аргумент json, мы должны сделать запрос POST следующим образом:"""
# import json
# BASE_URL = 'https://fakestoreapi.com'
# new_product = {
#     "title": 'test product',
#     "price": 13.5,
#     "description": 'lorem ipsum set',
#     "image": 'https://i.pravatar.cc',
#     "category": 'electronic'
# }
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.post(f"{BASE_URL}/products", data=json.dumps(new_product), headers=headers)
# print(response.json())
"""
В этом случае, когда мы используем аргумент data вместо json, 
нам нужно явно установить Content-Type на application/json в заголовке. 
Когда мы используем аргумент json, нам не нужно сериализовать данные, 
но в данном случае это необходимо и делается с помощью json.dumps().
"""

##############################################
