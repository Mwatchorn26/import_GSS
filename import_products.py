#Import Products
import xmlrpclib
import csv

username= "admin"
pwd = "admin"
dbname = "xubuntu-dev"

sock_common = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/common")

uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/object")

reader = csv.reader(open('products.csv', 'rb'))

for row in reader:
    print row[1] #return 2nd item, 0th based array
    
    product_template = {
                        'name':row[1],
                        'standard_price':row[2],
                        'list_price':row[2],
                        'mes_type':'fixed',
                        'uom_id':1,
                        'uom_po_id':1,
                        'type':'product',
                        'procure_method':'make_to_stock',
                        'cost_method':'standard',
                        'categ_id':1
                        }
    template_id = sock.execute(dbname, uid, pwd, 'product.template', 'create', product_template)
    
    product_product = {
                       'product_tmpl_id': template_id,
                       'default_code': row[0],
                       'active':True,
                       }
    product_id = sock.execute(dbname, uid, pwd, 'product.product', 'create', product_product)