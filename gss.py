#!/usr/bin/python
import psycopg2
import time
import pandas as pd
#from tabulate import tabulate
import json
import initialize
import pudb



#RENAME THE DOUBLE OCCURANCES OF 
#update "res_partner"
#set state_id = (select id from "res_country_state" where name='Ontario' limit 1) --52
#where state_id = (select id from "res_country_state" where name='ONTARIO' limit 1) --66
#;
#
#DELETE FROM res_country_state where name='ONTARIO'
#delete from "res_country_state" where "name"='ONTARIO';

# GIVE COUNTRY NAME FOR PARTNERS WITH JUST A PROVINCE OR STATE PROVIDED.
#UPDATE res_partner set "country_id"=(select id from res_country where "name"='United States') WHERE "state_id" IN (select "id" from res_country_state where country_id = (select id from res_country where "name"='United States'));
#UPDATE res_partner set "country_id"=(select id from res_country where "name"='Canada') WHERE "state_id" IN (select "id" from res_country_state where country_id = (select id from res_country where "name"='Canada'));


def RunMyQuery(cur, sqlQuery):
    cur.execute(sqlQuery)
    return




#Ensure you have this json in a file called config.json in the same directory (I only use databse, user and passw).
#{
#  "database": "db_name",
#  "schema": "schema_name",
#  "user": "user_name",
#  "host": "host_url",
#  "port": "port_num",
#  "passw": "user_password"
#}




def run():
    with open('config.json') as f:
        conf = json.load(f)
    pudb.set_trace()
    conn_string = "dbname={} user={} password={}".format(conf['database'], conf['user'], conf['passw'])
    #conn_string = "dbname=fix_me user=fix_me password=fix_me"

    #if conn_string == "dbname=fix_me user=fix_me password=fix_me":
    #    print("OOPS: You forgot to set the DB name, DB user and DB password")
    #    return

    try:
        conn = psycopg2.connect(conn_string)
   
     
        # create a cursor
        cur = conn.cursor()
        
        # execute the create tables queries
        cur.execute(initialize.strInsertNewCategories)

        #initialize(cur)



    
        # execute a statement
        #print('PostgreSQL database version:')
        #cur.execute('SELECT version()')
        #BOM_TEXT = pd.read_sql('SELECT * from gss_migration_status WHERE gss_done', conn)
	#print tabulate(BOM_TEXT, headers='keys', tablefmt='psql')
        
        # display the PostgreSQL database server version
        #db_version = cur.fetchone()
        #print(db_version)
 
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
            
if __name__ == '__main__':
    run()
