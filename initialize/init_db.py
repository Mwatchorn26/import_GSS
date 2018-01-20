import cust_to_lead
import uom
import gss_tables
from .. import psyQuery as qry
import time

def init_pg:
    qry.sqlQuery(gss_tables.create_gss_tables)

    #wait for data to be copied over to the new tables...
    x=1000
    while x<1
        sleep 10
        x=x+1

    qry.sqlQuery(cust_to_lead.strInsertIntoLeads)
    qry.sqlQuery(cust_to_lead.strCopyOverTags)
    qry.sqlQuery(cust_to_lead.strDeleteTagsFromLeads)
    qry.sqlQuery(cust_to_lead.strDeleteLeadsFromCustomers)

    qry.sqlQuery(uom.strInsertNewCategories)
    qry.sqlQuery(uom.strInsertNewUoM)
