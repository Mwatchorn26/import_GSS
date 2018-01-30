#!/usr/bin/python
import psycopg2
import time
import pandas as pd
#from tabulate import tabulate
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

def run():
    with open('config.json') as f:
        conf = json.load(f)
    #pudb.set_trace()
    global conn_string
    conn_string = "dbname={} user={} password={}".format(conf['database'], conf['user'], conf['passw'])

    #INITIALIZE SYSTEM
    initialize.run_init.init_sys(conn_string)

    #SELECTION CRITERIA

    #EMPLOYEE PARTNERS

    #CUSTOMER PARTNERS
    #partners

    #VENDOR PARTNERS
#    res_partner.run_res_partner.run_res_partner(conn_string)

    #PROJECTS

    #ROUTERS

    #PRODUCTS

    #BOM

    #QUOTES

    #SALES ORDER

    #PURCHASE ORDERS

    #RECEIVING

    #TIME & ATTENDANCE

    #MANUFACTURING ORDERS


    return
            
if __name__ == '__main__':
    run()

