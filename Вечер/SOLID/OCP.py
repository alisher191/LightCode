# Пример первый: Класс отвечающий за скидку
# Плохой пример
class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price
    
    def give_discount(self):
        return self.price * 0.8
    # Надо добавить вип скидку
    def give_discount(self):
        if self.customer == 'vip':
            return self.price * 0.6
        
# Хороший пример
class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price
    
    def give_discount(self):
        return self.price * 0.8
    

class VIPDiscount(Discount):
    def give_discount(self):
        return super().give_discount() * 0.6