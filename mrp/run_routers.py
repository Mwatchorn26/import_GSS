import routes
import pudb
from  psyQuery import qry



def run_routes():
    print("\n\nUPDATING ROUTES")
    print("Inserting new routes into mrp_routing")

    print("routes.insertRoutes")
    qry(routes.insertRoutes)


    print("\nROUTES COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

