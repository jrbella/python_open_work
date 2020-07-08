import mysql.connector

#Documentation
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

"""
This documentation is just a reference for future use
and an exercise on basic SQL interaction using python
nothing here is intended to actually work but serve as
a framework.

"""

con = mysql.connector.connect(
    user = "test_user", #pass user
    password = "some_crazy_password", #Pass authentication
    host = "some_crazy_ip_address", #Put ip here
    database = "some_crazy_database" #put db name here
)

cursor = con.cursor()

query_1 = "SELECT * FROM some_crazy_database"

query = cursor.execute(query_1)
results = cursor.fetchall()

print(results)