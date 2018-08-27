import insert_routers
import pudb
from  psyQuery import qry



def run_routers():
    print("\n\nUPDATING ROUTES")
    print("Inserting new routes into mrp_routing")

    print("insert_products.createTempPartsTable")
    qry(insert_products.createTempPartsTable)

    print("routes.insertRoutes")
    qry(insert_routers.insertRoutes)


    print("\nROUTES COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

