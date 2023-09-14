# Bad SRP
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

# Good SRP
class User:
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class UserModelDB:
    def save_in_db(self):
        # Save user in DB
        pass
