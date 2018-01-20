import cust_to_lead
import uom
import gss_tables
from gss import psyQuery as qry
import time

import pandas as pd

def init_pg(config):
    import pudb; pudb.set_trace()
    qry.sqlQuery(gss_tables.create_gss_tables)

    #wait for data to be copied over to the new tables...

    gss_status={}
    while not gss_status:
        sleep(100)
        gss_status = UpdatePgDbStatus(config)

    qry.sqlQuery(cust_to_lead.strInsertIntoLeads)
    qry.sqlQuery(cust_to_lead.strCopyOverTags)
    qry.sqlQuery(cust_to_lead.strDeleteTagsFromLeads)
    qry.sqlQuery(cust_to_lead.strDeleteLeadsFromCustomers)

    qry.sqlQuery(uom.strInsertNewCategories)
    qry.sqlQuery(uom.strInsertNewUoM)

def UpdatePgDbStatus(config):
    conn_string = "dbname={} user={} password={}".format(conf['database'], conf['user'], conf['passw'])

    try:
        conn = psycopg2.connect(conn_string)

        # create a cursor
        cur = conn.cursor()

        # execute the create tables queries
        cur.execute(initialize.strInsertNewCategories)

        df = pd.read_sql('select * from gss_migration_status where ', con=conn_string)
   
        pudb.set_trace() 

        # close the communication with the PostgreSQL
        cur.close()
        conn.commit()
        for notice in conn.notices:
            print(notice)
        return df

    except (Exception, psycopg2.DatabaseError) as error:
        print()
        print("ERROR")
        print(error)
        print()
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

