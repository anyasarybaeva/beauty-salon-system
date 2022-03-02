import psycopg2
conn = psycopg2.connect(dbname='салон красоты', user='annasarybaeva', 
                         host='localhost')
cursor = conn.cursor()
status="Активная"
#cursor.execute('SELECT * FROM airport WHERE city_code = %s', ('ALA', ))
i=0
cursor.execute('SELECT Название FROM Услуга WHERE Статус=%s',('Активная',))
for row in cursor:
    i+=1
    print(row)
print(i)
cursor.close()
conn.close()