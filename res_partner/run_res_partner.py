import insert_vendor
#import psyQuery as qry
import pudb

#from psyQuery import psyQuery as qry
import psyQuery



def run_res_partner(conn_string):
    print("\n\nUPDATING RES_PARTNER")
    print("Inserting new vendors into res_partner")

    print(insert_vendor.query_VENDOR_MASTER)
    pudb.set_trace()
    qry(insert_vendor.query_VENDOR_MASTER)

    print("\nRES_PARTNER COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

