import psycopg2
conn = psycopg2.connect(dbname='салон красоты', user='annasarybaeva', 
                         host='localhost')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Услуга')
for row in cursor:
    print(row)
cursor.close()
conn.close()