import cust_to_lead
import uom
import gss_tables
import phonenumbers as tel
from   psyQuery import qry
from time import sleep
import pudb
import sys
import pandas as pd

def init_sys():
    print("\n\nINITIALIZING SYSTEM")
    print("\nCreating GSS tables")
    '''
    qry(gss_tables.create_gss_tables)

    #wait for data to be copied over to the new tables...

    while not gssDone():
        sleep(10)
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
    '''
    
    print("\nStandardizing Phone Numbers")
    print("Standardizing Customer Master Phone Numbers")
    tel.cleanPhoneNumbers("gss_V_CUSTOMER_MASTER","TELEPHONE")
    print("Standardizing Customer Master Phone Numbers")
    tel.cleanPhoneNumbers("gss_V_EMPLOYEES","PHONE")
    print("Standardizing Customer Master Phone Numbers")
    tel.cleanPhoneNumbers("gss_v_PROJECT_MASTER","PHONE")
    print("Standardizing Vendor Master ADDL Phone Numbers")
    tel.cleanPhoneNumbers("gss_V_VEND_MSTR_ADDL","BUY_PHONE")
    tel.cleanPhoneNumbers("gss_V_VEND_MSTR_ADDL","BUY_FAX")
    tel.cleanPhoneNumbers("gss_V_VEND_MSTR_ADDL","PAY_PHONE")
    tel.cleanPhoneNumbers("gss_V_VEND_MSTR_ADDL","PAY_FAX")
    


    print("\nINITIALIZE COMPLETE\n")

def gssDone(conn_string):

    conn_string=''

    if conn_string=='':
        with open('../config.json') as f:
            conf = json.load(f)
            conn_string = "dbname={} user={} password={}".format(conf['database'], conf['user'], conf['passw'])

    try:
        df = pd.read_sql('select * from "gss_migration_status" where "gss_done" is not null', con=psycopg2.connect(conn_string))

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
