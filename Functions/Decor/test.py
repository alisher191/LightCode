import os

login = input("Login: ")
password = input("Password: ")
photo = input("Photo: ")
b = photo.split('.')

file = open('text.txt', 'w+')

if os.path.exists(photo):
    if b[-1] == 'jpeg' or b[-1] == 'jpg' or b[-1] == 'png':
        a = {"Login": login,
             "Password": password,
             "Photo path": photo
             }
        file.write(str(a))
        print("Регистрация успешна!")
else:
    print("Такого файла не существует или расширение не поддерживается!")
file.close()
