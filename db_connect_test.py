import psycopg2


conn = psycopg2.connect(
    host="bhtravel-server.postgres.database.azure.com",
    database="hotel_trip_advisor",
    user="formallizard4",
    password="ka5tZUd2x4uQaitGAE3trg")

conn.autocommit = True
cursor = conn.cursor()
  
sql = '''SELECT *
        FROM reviews; '''
  
cursor.execute(sql)
results = cursor.fetchall()
print(results)
  
conn.commit()
conn.close()
