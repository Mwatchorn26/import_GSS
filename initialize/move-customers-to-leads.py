

strInsertIntoLeads =  """
insert into "crm_lead" ("name", "partner_name", "street", "street2", "city", "state_id", "country_id", "zip", "user_id", "title", "function", "phone", "fax", "opt_out", "linkedin_url", "mobile", "company_website", "email_from", "type", "active") 
select distinct rp.name, substring(company_name.name for 64), rp.street, rp.street2, rp.city, rp.state_id, rp.country_id, rp.zip, rp.user_id, rp.title, rp.function, 
rp.phone, rp.fax, rp.opt_out, rp.linkedin_url, rp.mobile, rp.website, rp.email, 'lead',true
from "res_partner" as "rp"
left join "res_partner" as "company_name" on company_name."id"=rp."parent_id"
left join "gss_V_CUSTOMER_MASTER" as gss on upper(gss."NAME_CUSTOMER") = upper("rp"."name")
where "rp".customer='1'
and gss."NAME_CUSTOMER" is null ;"""

strCopyOverTags = """
nsert into crm_lead_category_rel (lead_id,category_id)
select distinct leads.id, ccc.id as ccc_cat_id 
from res_partner as rp
left join res_partner_res_partner_category_rel as rpcr on rpcr.partner_id = rp.id
left join res_partner_category as rpc on rpc.id = rpcr.category_id
left join crm_case_categ as ccc on rpc."name"=ccc."name"
left join "gss_V_CUSTOMER_MASTER" as gss on upper(gss."NAME_CUSTOMER") = upper("rp"."name")
left join crm_lead as leads on leads."name"=rp."name"
where "rp".customer='1'
and gss."NAME_CUSTOMER" is null
and rpc."name" is not null;"""



#/*Identify which partners to remove from the re_partner_category_rel table*/
strDeleteTagsFromLeads = """
delete from res_partner_res_partner_category_rel where partner_id in (
select rp.id
from res_partner as rp
left join res_partner_res_partner_category_rel as rpcr on rpcr.partner_id = rp.id
left join res_partner_category as rpc on rpc.id = rpcr.category_id
left join crm_case_categ as ccc on rpc."name"=ccc."name"
left join "gss_V_CUSTOMER_MASTER" as gss on upper(gss."NAME_CUSTOMER") = upper("rp"."name")
left join crm_lead as leads on leads."name"=rp."name"
where "rp".customer='1'
and gss."NAME_CUSTOMER" is null);"""

#/*Identify which partners to remove from the re_partner table*/ 
strDeleteLeadsFromCustomers = """
delete from res_partner where id in (
select rp.id
from res_partner as rp
left join res_partner_res_partner_category_rel as rpcr on rpcr.partner_id = rp.id
left join "gss_V_CUSTOMER_MASTER" as gss on upper(gss."NAME_CUSTOMER") = upper("rp"."name")
left join crm_lead as leads on leads."name"=rp."name"
left join res_users as users on users."partner_id"=rp."id"
left join sale_order as so on so."partner_invoice_id" = rp."id"
where "rp".customer='1'
and gss."NAME_CUSTOMER" is null
and users.login is null
and so."partner_invoice_id" is null
);
);"""

