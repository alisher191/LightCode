import requests

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