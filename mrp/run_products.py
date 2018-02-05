import insert_products
import pudb
from  psyQuery import qry


def run_products():
    print("\n\nUPDATING PRODUCTS")
    print("Preparing to insert products.")
 
    print("insert_products.translatePJFM")
    qry(insert_products.translatePJFM)
    
    print("insert_products.updateProductLineInvMstr")
    qry(insert_products.updateProductLineInvMstr)

    print("insert_products.updateProductLinePOLine")
    qry(insert_products.updateProductLinePOLine)
    
    print("insert_products.translatePJFM")
    qry(insert_products.translatePJFM)


    print("Actually Insert Products")
    print("insert_products.insertTemplates")
    qry(insert_products.insertTemplates)
    #print("insert_products.insertProductProduct")
    #qry(insert_products.insertProductProduct)

    print("\n\n************** NEED TO ADD VARIANTS **********")
    print("(although the productProduct queries SHOULD be doing this\n\n")

    print("insert_products.insertPOLineProductTemplate")
    qry(insert_products.insertPOLineProductTemplate)
    #print("insert_products.insertPOLineProductProduct")
    #qry(insert_products.insertPOLineProductProduct)
    

    print("\nPRODUCTS COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

