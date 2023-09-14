"""
Пример работы с JSON Python
Для тестового API, мы воспользуемся JSONPlaceholder, 
отличный источник фейковых данных JSON для практических целей.
"""

import json
import requests

"""
Идем дальше и создаем запрос в API JSONPlaceholder для конечной 
точки GET /todos.Это должно выглядеть следующим образом:
"""


# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)

# print(todos == response.json()) # True
# print(type(todos)) # <class 'list'>
 
# print(todos[:10]) # ...

"""
Хорошо, теперь перейдем к действиям. Вы можете видеть структуру данных 
полученную от тестового API, посетив адрес в браузере https://jsonplaceholder.typicode.com/todos.
"""

"""
Здесь несколько пользователей, каждый из которых имеет уникальный userId, 
а каждая задача имеет свойство Boolean. Можете определить, 
какие пользователи выполнили большую часть задач?
"""

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
# Соотношение userId с числом выполненных пользователем задач.
todos_by_user = {}
 
# Увеличение выполненных задач каждым пользователем.
for todo in todos:
    if todo["completed"]:
        try:
            # Увеличение количества существующих пользователей.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # Новый пользователь, ставим кол-во 1.
            todos_by_user[todo["userId"]] = 1
print(f'todos_by_user {todos_by_user}')
# Создание отсортированного списка пар (userId, num_complete).
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

print(f'top_users {top_users}')

#Получение максимального количества выполненных задач.
max_complete = top_users[0][1]
print(f'max_complete {max_complete}')
# Создание списка всех пользователей, которые выполнили
# максимальное количество задач.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
print(f'users {users}')

max_users = " and ".join(users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")
