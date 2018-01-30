#!/usr/bin/python
import psycopg2
import time
import json
import pudb
import initialize
import res_partner

conn_string=''

#Ensure you have this json in a file called config.json in the same directory (I only use databse, user and passw).
#{
#  "database": "db_name",
#  "user": "user_name",
#  "passw": "user_password"
#}

def psyQuery(sqlQuery):

    global conn_string

    if conn_string=='':
        with open('config.json') as f:
            conf = json.load(f)
            conn_string = "dbname={} user={} password={}".format(conf['database'], conf['user'], conf['passw'])

    try:
        conn = psycopg2.connect(conn_string)
     
        # create a cursor
        cur = conn.cursor()
        
        # execute the create tables queries
        cur.execute(sqlQuery)
 
        # close the communication with the PostgreSQL
        cur.close()
        conn.commit()
        for notice in conn.notices:
            print(notice)

    except (Exception, psycopg2.DatabaseError) as error:
        print()
        print("ERROR")
        print(error)
        print()
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return
