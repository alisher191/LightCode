class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.8
    
    # def give_discount(self):
    #     if self.customer == 'vip':
    #         return self.price * 0.6
    

class VIPDiscount(Discount):
    def give_discount(self):
        return super().give_discount() * 0.6
    