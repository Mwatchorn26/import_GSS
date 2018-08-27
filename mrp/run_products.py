import insert_routers
import insert_products
import products_sql
import workcenters
import pudb
from  psyQuery import qry, open_conn, use_conn, close_conn


def run_products():

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
    return 

    conn = open_conn()


    print("PREPARING TEMP PARTS TABLE")
    print("insert_products.createTempPartsTable")
    use_conn(conn, insert_products.createTempPartsTable)
    print("TEMP PARTS TABLE COMPLETE")

    print("\n\nUPDATING MRP / ROUTES")
    print("Inserting new routes into mrp_routing")
    use_conn(conn, insert_routers.insertWCandRouters)
    print("\nMRP / ROUTES COMPLETE\n")

    print("\n\nUPDATING MRP / PRODUCTS")
    print("Preparing to insert products.")
 
    #not needed now need to figure this out in the future though.
    #print("insert_products.translatePJFM")
    #qry(insert_products.translatePJFM)
    
    print("insert_products.updateProductLineInvMstr")
    use_conn(conn, insert_products.updateProductLineInvMstr)

    print("insert_products.updateProductLinePOLine")
    use_conn(conn, insert_products.updateProductLinePOLine)

    print("Actually Insert Products")
    print("insert_products.insertTemplates")
    use_conn(conn, insert_products.insertTemplates)
    print("insert_products.insertProductProduct")
    use_conn(conn, insert_products.insertProductProduct)

    print("\n\n************** NEED TO ADD VARIANTS **********")
    print("(although the productProduct queries SHOULD be doing this\n\n")

    print("insert_products.insertPOLineProductTemplate")
    use_conn(conn, insert_products.insertPOLineProductTemplate)
    #print("insert_products.insertPOLineProductProduct")
    #qry(insert_products.insertPOLineProductProduct)
    close_conn(conn)

    print("\nMRP / PRODUCTS COMPLETE\n")

