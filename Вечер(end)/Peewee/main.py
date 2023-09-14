import csv

from peewee import *


db = PostgresqlDatabase(database='test',
                        user='postgres',
                        password='1234',
                        host='localhost'
                        )


class House(Model):
    pub_no = CharField(max_length=100)
    title = CharField(max_length=255)
    link = TextField()
    image = TextField()
    description = TextField()
    price = CharField(max_length=255)
    city = CharField(max_length=100)
    location = CharField(max_length=255)
    date_added = CharField(max_length=100)

    class Meta:
        database = db


def main():

    db.connect()
    db.create_tables([House])

    with open('content.csv', 'r') as f:
        # order = ['Публикация №', 'Заголовок', 'Ссылка на публикацию', 'Изображение', 'Описание', 'Цена', 'Город', 
        #         'Расположение', 'Дата добавления']
        order = ['pub_no', 'title', 'link', 'image', 'description', 'price', 'city', 
                'location', 'date_added']
        reader = csv.DictReader(f, fieldnames=order)

        houses = list(reader)

        # for row in houses:
        #     # print(row)
        #     house = House(pub_no=row['Публикация №'], title=row['Заголовок'], link=row['Ссылка на публикацию'],
        #                   image=row['Изображение'], description=row['Описание'], price=row['Цена'], city=row['Город'],
        #                   location=row['Расположение'], date_added=row['Дата добавления'])
        #     house.save()

        # with db.atomic(): # Context manager
        #     for row in houses:
        #         # print(row)
        #         House.create(**row)

        with db.atomic(): # Context manager
            for index in range(0, len(houses), 10):
                House.insert_many(houses[index:index+10]).execute()


if __name__ == '__main__':
    main()

# pg_dump -U postgres -h 127.0.0.1 test > houses.sql # dump > sql