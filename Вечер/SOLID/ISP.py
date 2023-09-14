"""
Создавайте детализированные 'интерфейсы, специфичные' для конкретного клиента.
"""
# Плохой пример
class Shape:
    def draw_circle(self):
        raise NotImplemented
    
    def draw_square(self):
        raise NotImplemented
    

class Circle(Shape):
    def draw_circle(self):
        pass
    
    def draw_square(self):
        pass


# Пример хороший
class Shape:
    def draw(self):
        raise NotImplemented
    

class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass
    