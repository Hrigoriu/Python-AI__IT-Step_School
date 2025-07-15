import psycopg2

connection = psycopg2.connect(
    dbname='Northwind',
    user='postgres',
    password='admin',
    host='localhost',
    port='5432'

)
cursor = connection.cursor()
cursor.execute('SELECT * from customers')
for row in cursor .fetchall():
    print(row)

connection.close()






