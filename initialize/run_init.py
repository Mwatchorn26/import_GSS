import cust_to_lead
import uom
import gss_tables
from gss import psyQuery as qry
from time import sleep
import psycopg2
import pudb
import pandas as pd
import sys
import phoneNumbers as tel

def init_sys(conn_string):
    print("\n\nINITIALIZING SYSTEM")
    print("\nCreating GSS tables")
#TEMPORARILY COMMENTED OUT    qry(gss_tables.create_gss_tables)

    #wait for data to be copied over to the new tables...

    while not gssDone():
        sleep(1)
        sys.stdout.write(".")

    return

    print("\nMoving customers to leads")
    print("    Inserting Into Leads")
    qry(cust_to_lead.strInsertIntoLeads)
    print("    Copying over tags"
    qry(cust_to_lead.strCopyOverTags)
    print("    Deleting tags from customers")
    qry(cust_to_lead.strDeleteTagsFromLeads)
    print("    Deleting leads from customers table\n")
    qry(cust_to_lead.strDeleteLeadsFromCustomers)

    print("\nInserting new categories")
    qry(uom.strInsertNewCategories)
    print("Inserting new Units of Measure")
    qry(uom.strInsertNewUoM)
    print("Converting old to new Units of Measure")
    qry(uom.strUpdateUoM)

    tel.cleanPhoneNumbers("gss_V_CUSTOMER_MASTER","TELEPHONE")
    tel.cleanPhoneNumbers("gss_v_EMPLOYEES","PHONE")
    tel.cleanPhoneNumbers("gss_v_PROJECT_MASTER","PHONE")
    tel.cleanPhoneNumbers("gss_v_VEND_MSTR_ADDL","BUY_PHONE")
    tel.cleanPhoneNumbers("gss_v_VEND_MSTR_ADDL","BUY_FAX")
    tel.cleanPhoneNumbers("gss_v_VEND_MSTR_ADDL","PAY_PHONE")
    tel.cleanPhoneNumbers("gss_v_VEND_MSTR_ADDL","PAY_FAX")



    print("\nINITIALIZE COMPLETE\n")

def gssDone(conn_string):
    #conn_string = "dbname={} user={} password={}".format(conf['database'], conf['user'], conf['passw'])

    try:
#        conn = psycopg2.connect(conn_string)

        # create a cursor
#        cur = conn.cursor()

        # execute the create tables queries
#        cur.execute(initialize.strInsertNewCategories)
        df = pd.read_sql('select * from "gss_migration_status" where "gss_done" is not null', con=psycopg2.connect(conn_string))

        # close the communication with the PostgreSQL
        cur.close()
        conn.commit()
        #for notice in conn.notices:
        #    print(notice)

    except (Exception, psycopg2.DatabaseError) as error:
        print()
        print("ERROR")
        print(error)
        print()
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    return df.empty
