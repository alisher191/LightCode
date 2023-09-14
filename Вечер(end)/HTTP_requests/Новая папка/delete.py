import requests


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