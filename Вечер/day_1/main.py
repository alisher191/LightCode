with open("info.txt") as f:
    users = f.read()

users = users.split(",")
user = {
    'name': users[0],
    'password': users[1],
    'email': users[2]
}

