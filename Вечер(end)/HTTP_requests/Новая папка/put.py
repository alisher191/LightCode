import requests


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
