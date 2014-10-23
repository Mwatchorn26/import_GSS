import xmlrpclib
import csv

username = 'admin' #the user
pwd = 'admin'      #the password of the user
dbname = 'xubuntu-dev'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')


reader = csv.reader(open('leads.csv', 'rb'))

for row in reader:
    print row[0] #return 2nd item, 0th based array
    lead = {
       'name': 'Email Blitz',
       'contact_name':row[0],
       'partner_name':row[1],
       'email_from':row[2],
       'function':row[3],
       'referred':row[4],
    }

    lead_id = sock.execute(dbname, uid, pwd, 'crm.lead', 'create', lead)
