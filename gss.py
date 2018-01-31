#!/usr/bin/python
import psycopg2
import time
import pandas as pd
#from tabulate import tabulate
import json
import pudb
import initialize
import res_partner
import mrp

#conn_string=''

#Ensure you have this json in a file called config.json in the same directory (I only use databse, user and passw).
#{
#  "database": "db_name",
#  "user": "user_name",
#  "passw": "user_password"
#}

def run():

    #INITIALIZE SYSTEM
#    initialize.run_init.init_sys()

    #SELECTION CRITERIA

    #EMPLOYEE PARTNERS

    #CUSTOMER PARTNERS
#    res_partners.run_res_partners

    #VENDOR PARTNERS
#    res_partner.run_res_partner.run_res_partner(conn_string)

    #PROJECTS

    #ROUTERS

    #PRODUCTS
    mrp.run_products.run_products()

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

