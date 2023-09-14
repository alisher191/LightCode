"""
Зависеть от 'абстракций', а не от реализации.
"""
# Предположим пример, представим, что мы проводим генеалогичесое исследование
# Создадим Enum, которое будет определять отношение между двумя людьми
from enum import Enum
from abc import abstractmethod

# Плохой пример
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


# Теперь нам нужен низкоуровневый модуль, т.е. модуль, 
# со всеми деталями реализации всей семантикой хранения и всем другим, 
# что нужно для хранения отношений между разными людьми
class Relationships: # класс для хранения всех отношений
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )


class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}.")

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)


Research(relationships)

print("#"*30)

# Пример хороший
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser): # low level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f"John has a child called {p}.")


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
