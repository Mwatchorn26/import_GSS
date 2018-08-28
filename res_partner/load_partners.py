import partners_sql
from psyQuery import qry
import pudb

#from psyQuery import psyQuery as qry
import psyQuery



def load():
    print("\n\nUPDATING RES_PARTNER")
    print("Inserting new vendors into res_partner")

    print("Inserting Suppliers next...")
#    pudb.set_trace()
#    qry(partners_sql.insertSuppliers)
    print("Inserting Customers next...")
    qry(partners_sql.insertCustomers)


    print("\nRES_PARTNER COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

