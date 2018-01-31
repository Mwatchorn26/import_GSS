import insert_products
import pudb
from  psyQuery import qry



def run_products():
    print("\n\nUPDATING PRODUCTS")
    print("Inserting new vendors into res_partner")

    print("insert_product.translatePJFM")
    qry(insert_products.translatePJFM)

    print("insert_product.translateProductLine")
    qry(insert_products.translateProductLine)

    print("insert_product.translatePJFM")
    qry(insert_products.translatePJFM)

    print("insert_product.insertTemplates")
    qry(insert_products.insertTemplates)
    print("insert_product.insertProductProduct")
    qry(insert_products.insertProductProoduct")




    print("\nPRODUCTS COMPLETE\n")

#if __name__ == '__main__':
#    run_res_partner()

