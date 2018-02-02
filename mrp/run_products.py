import insert_products
import pudb
from  psyQuery import qry


def run_products():
    print("\n\nUPDATING PRODUCTS")
    print("Inserting new vendors into res_partner")
    '''
    print("insert_product.translatePJFM")
    qry(insert_products.translatePJFM)
    '''
    print("insert_product.updateProductLineInvMstr")
    qry(insert_products.updateProductLineInvMstr)

    print("insert_product.updateProductLinePOLine")
    qry(insert_products.updateProductLinePOLine)
    '''
    print("insert_product.translatePJFM")
    qry(insert_products.translatePJFM)

    print("insert_product.insertTemplates")
    qry(insert_products.insertTemplates)
    print("insert_product.insertProductProduct")
    qry(insert_products.insertProductProduct)

    print("\n\n************** NEED TO ADD VARIANTS **********")
    print("(although the productProduct queries SHOULD be doing this\n\n")

    print("insert_product.insertPOLineProductTemplate")
    qry(insert_products.insertPOLineProductTemplate)
    print("insert_product.insertPOLineProductProduct")
    qry(insert_products.insertPOLineProductProduct)


    '''

    print("\nPRODUCTS COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

