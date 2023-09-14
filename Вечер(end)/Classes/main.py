import psycopg2


con = psycopg2.connect(
    database='testdb',
    user='postgres',
    host='127.0.0.1',
    port='5432',
    password='12345'
)
# print('Done!')


cur = con.cursor()  # отвечает за все операции с бд

cur.execute('CREATE TABLE person(name VARCHAR(10), age INT);')
con.commit()
cur.execute('select * from person;')
result = cur.fetchall()
print(result)
