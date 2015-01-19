import xmlrpclib
import csv

username = 'admin' #the user
pwd = 'admin'      #the password of the user
dbname = 'Dev_LEAD_GEN2'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

#reader = csv.reader(open('data/leads_from_insightly.csv', 'rb'))
#reader = csv.reader(open('data/leads_from_zoho.csv', 'rb'))
#reader = csv.reader(open('data/leads_from_outlook.csv', 'rb'))
#reader = csv.reader(open('data/leads_from_gen1_lead_generator.csv', 'rb'))

files = ['data/leads_from_insightly.csv', 
         'data/leads_from_zoho.csv',
         'data/leads_from_outlook.csv',
         'data/leads_from_gen1_lead_generator.csv']

for file in files:
    reader = csv.reader(open(file, 'rb'))
    ImportCSV(reader)

def ImportFile(reader):
    for row in reader:
        print row[0] #return 2nd item, 0th based array
        lead = {
    #            'name': 'Email Blitz',
    #            'contact_name':row[0],
    #            'partner_name':row[1],
    #            'email_from':row[2],
    #            'function':row[3],
    #            'referred':row[4],
        
        
            'id':row[0],                #A
            'name':row[1],              #B     ('Subject', required=True,
            'email_from':row[2],        #C    'Email help="Email address of the contact"
            'description':row[3],       #D    : fields.text('Notes'),
            'categ_ids':row[4],         #E    tags 
        
            # Fields for address, due to separation from crm and res.partner
            'street':row[5],            #F
            'street2':row[6],           #G
            'zip':row[7],               #H
            'city':row[8],              #I
            'state_id':row[9],          #J    ("res.country.state", 'State'),
            'country_id':row[10],       #K    'res.country', 'Country'),
            'phone':row[11],            #L    'Phone'),
            'fax':row[12],              #M    ('Fax'),
            'mobile':row[13],           #N: fields.char('Mobile'),
            'function':row[14],         #O
            'company_id':row[15],       #P Company
            
           
            'partner_id':row[16],       #Q     help="Linked partner (optional). Usually created when converting the lead."),
            'contact_name':row[17],     #R    'Contact Name', size=64),
            'partner_name':row[18],     #S    "Customer Name", help='The name of the future partner company that will be created while converting the lead into opportunity',),
            'opt_out':row[19],          #T
            'type':row[20],             #U     selection([ ('lead','Lead'), ('opportunity','Opportunity'), ]
            'priority':row[21],         #V     selection(crm.AVAILABLE_PRIORITIES, 'Priority', select=True),
            'stage_id':row[22],         #W
            'user_id':row[23],          #X     'Salesperson'
    
            'email_status':row[24],     #Y      Selection([('unknown', 'Unknown'),('valid', 'Valid'),('accepted', 'Server Accepted'), ('bad_mailbox', 'Bad Mailbox')] default='unknown',
            'lead_validated_by':row[25],#Z     Salesman 'res.users'
            'linkedin_url':row[26],     #AA
            'email_domain':row[27],     #AB
            'company_website':row[28],  #AC
        
            
            # Only used for type opportunity
    #        'probability':row[29],           #Q     float
    #        'planned_revenue':row[30],       #R     fields.float('Expected Revenue', track_visibility='always'),
    #        'ref':row[31],                   #S     fields.reference('Reference', selection=openerp.addons.base.res.res_request.referencable_models),
    #        'ref2':row[32],                  #T     fields.reference('Reference 2', selection=openerp.addons.base.res.res_request.referencable_models),
    #        'phone':row[33],                 #U     fields.char("Phone", size=64),
    #        'date_deadline':row[34],         #V     fields.date('Expected Closing', help="Estimate of the date on which the opportunity will be won."),
    #        'partner_address_name':row[35],  #W     fields.related('partner_id', 'name', type='char', string='Partner Contact Name', readonly=True),
    #        'partner_address_email':row[36], #X     fields.related('partner_id', 'email', type='char', string='Partner Contact Email', readonly=True),
    #        'company_currency':row[37],      #Y     "res.currency"),
    #        
    #        'project_code':row[38],          #Z      help="Six digit code for each project like 'ABC026'")    
    #        'project_name':row[39],          #AA     Char('Project Name', size=128, required=False, help="Typically the customer's name for the product or their name for the machine.")
    #        'machine_rate':row[40],          #AB     Integer('Machine Rate', required=False, help="Number of parts per minute requested by the client.")
    #        'machine_model':row[41],         #AC     Many2one('crm_eto.eto_model', string="Machine Model",required=False, help="Select the most appropriate model")
    #        'scrap_rate':row[42],            #AD     Char('Scrap Rate', size=50, required=False, help="The acceptable scrap rate as defined by the customer at the outset of the project.")
    #        'oppor_change_reason':row[43],   #AE     Selection('concept', 'delivery','distance','lack_of_funding', 'no_quote','poor_fit','price','re-opened','relationship','timing','unknown','was_only_budgetary','other')required=False, 
    #        'oppor_other_reason':row[44],    #AF     Char('Other Reason', size=25, help="Enter the reason for the state change")
    #        'price_model':row[45],           #AG     Selection([('fixed_price','t&m','other', required=False
    #        'oppor_job_type':row[46],        #AH     Selection([('retrofit','budgetary','build_only','design_and_build','engineering_only','other','Other')], required=False
    #        'proposal_date':row[47],         #AI     help="Date the [next] proposal is due.")
    #        'concept_date':row[48],          #AJ     help="Date the concept drawings are due.")
    #        'animation_date':row[49],        #AK     help="Date the animation file(s) are due.")
    #        'decision_date':row[50],         #AL     help="Date the client anticipates a decision will be made.")
    #        'delivery_date':row[51],         #AM     help="Date the client anticipates delivery to their facility.")
    
            
    }        

    lead_id = sock.execute(dbname, uid, pwd, 'crm.lead', 'create', lead)
