#import insert_routers
#import insert_products
import products_sql
import routers_sql
import workcenters_sql
import pudb
from  psyQuery import qry, open_conn, use_conn, close_conn


def load_mrp():

    #qry(products_sql.createWorcentersResourcesTemplatesProducts)
    qry(products_sql.createTempGssParts)
    qry(products_sql.insertResourcesFromWorkCenter)
    qry(products_sql.insertWorkCenterFromWorkCenters)
    qry(products_sql.insertMissingResources)

    # PRODUCTS #
    qry(products_sql.updateProductLines)
    qry(products_sql.insertProductTemplates)
    qry(products_sql.insertProductProduct)
    qry(products_sql.insertPOLineProductTemplate)
    qry(products_sql.insertPOLineProductProduct)
    qry(products_sql.insertProductAttributeLines)
    qry(products_sql.insertProductAttrbuteValues)
    qry(products_sql.insertProdAttValProdProdRel) 

    print("\nMRP / PRODUCTS COMPLETE\n")
    return
