import psycopg2
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    
    # the cursor for performing database operations
    #cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

        # create a new table 1 step
    
    #with connection.cursor() as cursor:
    #    cursor.execute(
    #        """CREATE TABLE clients(
    #        id_clients serial PRIMARY KEY,
    #        first_name varchar(20) not null,
    #        last_name varchar(20) not null,                
    #        nick_name varchar(30) not null,
    #        contacts  varchar(13) not null);"""
    #    ) 
    #    # connection.commit()
    #    print("[info] table created successfully")

    # insert data into a table 2 step             
    
    #with connection.cursor() as cursor:
    #    cursor.execute(
    #        """INSERT INTO clients (first_name, last_name, nick_name, contacts) VALUES                 
    #        ('Anna', 'Filatova', 'filatova3', '79857847812');"""
    #    ) 

    #    print("[INFO] Data was successfully inserted")


    
    # get data from a table 3 step
    
    #with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM clients;"""
    #     ) 

    #     print(cursor.fetchone())

   
     # delete a table 4 step
    with connection.cursor() as cursor:
         cursor.execute(
             """DROP TABLE clients;"""
         ) 

         print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")