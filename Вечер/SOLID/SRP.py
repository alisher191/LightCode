# Пример первый: класс, который записывает и получает пользователя из бд
# Так делать не хорошо
class User: 
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name
    
    def save_in_db(self):
        # Save user in DB
        pass


# А так делать лучший вариант
class User:
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name
    

class UserModelDB:
    def get_user_from_db(self, user_id):
        pass

    def save_in_db(self):
        # Save user in DB
        pass
#################################################################

# Пример второй: функция, которая считает процент слов
# Так делать не хорошо
def percentage_of_word(search, file):
    search = search.lower()
    with open(file, 'r') as f:
        content = f.read()
    words = content.split()
    number_of_words = len(words)
    occurences = 0
    for word in words:
        if word.lower() == search:
            occurences += 1
    return occurences/number_of_words

# А так делать лучший вариант
def read_localfile(file):
    with open(file, 'r') as f:
        content = f.read()
    return content

def number_of_words(content):
    return len(content.split())

def count_word_occurences(word, content):
    counter = 0
    for i in content.split():
        if word.lower() == i.lower():
            counter += 1
    return counter

def percentage_of_word_in_localfile(word, file):
    content = read_localfile(file)
    return percentage_of_word(word, content)
