import requests
import json

##############################################

"""
Как сделать запрос GET
Это один из наиболее распространенных методов HTTP-запросов, 
с которыми вы столкнетесь. Это операция только для чтения, 
позволяющая получать данные из API.

Давайте попробуем использовать запрос GET на первой конечной 
точке из упомянутых выше. 
Она должна вернуть список продуктов.
"""
# BASE_URL = 'https://fakestoreapi.com'

# response = requests.get(f"{BASE_URL}/products")
# with open('resp.txt', 'w') as file:
#     file.write(str(response.json()))
# print(response.json())
# print(response.status_code)
"""
В приведенном выше сценарии используется метод requests.get() 
для отправки запроса GET в конечную точку API /products. 
Данный запрос возвращает нам список всех продуктов. 
Затем мы вызываем метод .json(), чтобы просмотреть 
полученный ответ JSON.
"""

##############################################

"""
Поскольку конечная точка /products возвращает много данных, 
давайте ограничим эти данные только тремя продуктами.

Для этого у нас есть конечная точка /products?limit=x, 
где x – это положительное целое число. 
limit (лимит, ограничение) — параметр запроса. 
Давайте посмотрим, как мы можем добавить этот параметр в наш запрос:
"""
# BASE_URL = 'https://fakestoreapi.com'
# query_params = {
#     "limit": 3
# }
# response = requests.get(f"{BASE_URL}/products", params=query_params)
# print(response.json())
"""
Метод requests.get() принимает параметр с именем params, 
в котором мы можем указать параметры нашего запроса в формате словаря Python. 
Таким образом, мы создаем словарь с именем query_params и 
передаем limit в качестве ключа и 3 в качестве значения. 
Затем мы передаем этот словарь query_params в request.get().
"""
##############################################

"""
Таким образом, у нас есть данные об ответах, 
ограниченные всего тремя продуктами. Попробуем получить только один товар, 
id которого равен 18.
"""
# BASE_URL = 'https://fakestoreapi.com'
# response = requests.get(f"{BASE_URL}/products/18")
# print(response)
"""
Поскольку у нас есть конечная точка /products/<product_id>, 
мы можем передать идентификатор 18 в URL-адресе API и сделать для него запрос GET.
"""

##############################################

#delete
"""
                Как сделать запрос DELETE
Как следует из названия, если вы хотите удалить ресурс из API, 
вы можете использовать запрос DELETE. Удалим товар с идентификатором, 
равным 21:
"""
# BASE_URL = 'https://fakestoreapi.com'
# response = requests.delete(f"{BASE_URL}/products/21")
# print(response.json())
"""
Метод requests.delete() помогает нам сделать запрос 
DELETE к конечной точке /products/<product_id>.
"""

#patch
"""
            Как сделать PATCH-запрос
Иногда нам не нужно полностью заменять старые данные. 
Скорее мы хотим изменить только определенные поля. 
В этом случае мы используем запрос PATCH.

Давайте обновим категорию (category) продукта обратно с 
clothing (одежды) на electronic (электронику), 
сделав запрос PATCH к конечной точке products/<product_id>.
"""
# BASE_URL = 'https://fakestoreapi.com'
# updated_product = {
#     "category": 'electronic'
# }
# response = requests.patch(f"{BASE_URL}/products/21", json=updated_product)
# print(response.json())
"""
В этом случае мы используем метод requests.patch(), 
который возвращает такой ответ:
{
  "id": "21",
  "title": "updated_product",
  "category": "electronic"
}
Обратите внимание, что на этот раз все данные не изменились – 
обновилось только поле category (категория).
"""


#post
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

#put
"""
            Как сделать запрос PUT
Нам часто требуется обновить существующие данные в API. 
Используя запрос PUT, мы можем обновить данные полностью. 
Это означает, что, когда мы делаем запрос PUT, 
он заменяет все старые данные новыми.

В запросе POST мы создали новый продукт с идентификатором 21. 
Давайте обновим старый продукт на новый, сделав запрос PUT 
к конечной точке products/<product_id>.
"""
# BASE_URL = 'https://fakestoreapi.com'
# updated_product = {
#     "title": 'updated_product',
#     "category": 'clothing'
# }
# response = requests.put(f"{BASE_URL}/products/21", json=updated_product)
# print(response.json())
"""
Когда мы делаем запрос PUT с updated_product с помощью метода 
requests.put(), он возвращает нам следующие данные JSON:
{
  "id": "21",
  "title": "updated_product",
  "category": "clothing"
}
Обратите внимание, что старый продукт был полностью заменен обновленным продуктом.
"""

