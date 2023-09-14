# ORM Peewee
import csv

from peewee import *



db = PostgresqlDatabase(database='test',
                        user='postgres',
                        password='1234',
                        host='localhost')


class Person(Model):
    id = IntegerField()
    name = CharField(max_length=20)
    born = IntegerField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([Person])

    with open('content.csv', 'r') as f:
        order = ['id', 'name', 'born']
        reader = csv.DictReader(f, fieldnames=order)
        
        peoples = list(reader)
        
        # for row in peoples:
        #     print(row)
        #     people = Person(id=row['id'],
        #                     name=row['name'],
        #                     born=row['born'])
        #     people.save()

        # with db.atomic(): # Context manager
        #     for row in peoples:
        #         Person.create(**row)

        # with db.atomic():
        #     for index in range(0, len(peoples), 10):
        #         Person.insert_many(peoples[index:index+10]).execute()


if __name__ == '__main__':
    main()
