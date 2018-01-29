

#Prepare PROCURE_METHOD AND SUPPLY_METHOD
queryPJFM = """UPDATE gss_V_INVENTORY_MASTER ("PROCURE_METHOD", "SUPPLY_METHOD")
               VALUES CASE WHEN INV2."CODE_SOURCE"='P' THEN 'Purchase To Stock'
                           WHEN INV2."CODE_SOURCE"='J' THEN 'Purchase To Order'
                       	   WHEN INV2."CODE_SOURCE"='F' THEN 'Make To Order'
                           WHEN INV2."CODE_SOURCE"='M' THEN 'Make To Stock'
                      END AS "PROCURE_METHOD",
                      CASE WHEN INV2."CODE_SOURCE"='P' THEN 'Buy'
                           WHEN INV2."CODE_SOURCE"='J' THEN 'Buy'
                           WHEN INV2."CODE_SOURCE"='F' THEN 'Manufacture'
                           WHEN INV2."CODE_SOURCE"='M' THEN 'Manufacture' 
                      END AS "SUPPLY_METHOD"
		;"""

#Prepare Flag_Lot
strLot = """  CASE WHEN FLAG_LOT='Y' THEN 'True' 
                   ELSE 'False' END AS TRACK_INCOMING,
              CASE WHEN FLAG_LOT='Y' THEN 'True' 
                   ELSE 'False' AS TRACK_PRODUCTION,
              CASE WHEN FLAG_LOT='Y','True' 
                   ELSE 'False' as TRACK_OUTGOING,"""

fixProductLine="""
/* FIX PRODUCT LINE (aka categ_id) */
update "gss_V_INVENTORY_MSTR"
set "PRODUCT_LINE" = 
case
when "PRODUCT_LINE"='ZH' then 'Advertising & Promotion'
when "PRODUCT_LINE"='AA' then 'Automated Assembly'
when "PRODUCT_LINE"='BI' then 'Bin Inventory'
when "PRODUCT_LINE"='BP' then 'Build To Print'
when "PRODUCT_LINE"='ZI' then 'Computer Equipment'
when "PRODUCT_LINE"='ZJ' then 'Computer Licenses'
when "PRODUCT_LINE"='ZK' then 'Computer Software'
when "PRODUCT_LINE"='ZA' then 'Consumables'
when "PRODUCT_LINE"='CM' then 'Contract Manufacturing'
when "PRODUCT_LINE"='CR' then 'Contract Repair'
when "PRODUCT_LINE"='EC' then 'Electrical Components'
when "PRODUCT_LINE"='ES' then 'Engineering Services'
when "PRODUCT_LINE"='EQ' then 'Equipment Rental'
when "PRODUCT_LINE"='FB' then 'Freight & Brokerage'
when "PRODUCT_LINE"='HC' then 'Hydraulic Components'
when "PRODUCT_LINE"='ZL' then 'Indirect Labour Accounts'
when "PRODUCT_LINE"='IN' then 'Innovations'
when "PRODUCT_LINE"='LS' then 'Lab Services'
when "PRODUCT_LINE"='ZC' then 'Laboratory Expenses'
when "PRODUCT_LINE"='MP' then 'Machined Parts'
when "PRODUCT_LINE"='MC' then 'Mechanical Components'
when "PRODUCT_LINE"='SP' then 'OEM Spare Parts (why non-Inv?)'
when "PRODUCT_LINE"='ZM' then 'Office Supplies'
when "PRODUCT_LINE"='SD' then 'Payroll Deduction'
when "PRODUCT_LINE"='PI' then 'Platform Inventory'
when "PRODUCT_LINE"='PC' then 'Pneumatic Components'
when "PRODUCT_LINE"='ZD' then 'Quality Expenditures'
when "PRODUCT_LINE"='ZN' then 'R&M Building'
when "PRODUCT_LINE"='ZO' then 'R&M Equipment - On Demand'
when "PRODUCT_LINE"='ZP' then 'R&M Equipment - Prevenative'
when "PRODUCT_LINE"='RM' then 'Raw Material'
when "PRODUCT_LINE"='ZQ' then 'Safety & Environmental Costs'
when "PRODUCT_LINE"='ZR' then 'Shop Equipment >$500'
when "PRODUCT_LINE"='ZE' then 'Shop Supplies'
when "PRODUCT_LINE"='ZF' then 'Shop Tools <$500'
when "PRODUCT_LINE"='SU' then 'Subcontractors'
when "PRODUCT_LINE"='TA' then 'Tool Allowance'
when "PRODUCT_LINE"='ZG' then 'Tooling'
when "PRODUCT_LINE"='ZS' then 'Training & Seminars'
when "PRODUCT_LINE"='ZT' then 'Waste Removal'
else ''
end;
"""



insertTemplates="""
insert into product_template (warranty, list_price, write_uid, mes_type, uom_id,description_purchase, create_date, uos_coeff, create_uid, rental, company_id, uom_po_id, "type", description, write_date, active, categ_id, sale_ok, "name", description_sale, track_incoming, sale_delay, track_all, track_outgoing, purchase_ok, track_production, produce_delay, hr_expense_ok);

select distinct 0 as warranty,0.00 as list_price, 1 as write_uid, 'fixed' as mes_type, (select id from product_uom where "name"=im."UM_INVENTORY") as uom_id,
im."DESCRIPTION" as description_purchase, clock_timestamp() as create_date, 1.0 as uos_coeff, 1 as create_uid, false as rental, 1 as company_id, 
(select id from product_uom where "name"=im."UM_PURCHASING") as uom_po_id, 'product' as "type", im."DESCRIPTION" as description, 
clock_timestamp() as write_date, true as active, (select id from product_category where "name"= im."PRODUCT_LINE" limit 1) as categ_id, true as sale_ok, 
case when im."PART" like '___-_____-__%' then
				left(im."PART",12)
			else
				im."PART"
			end  as "name", 
im."DESCRIPTION" as description_sale, 
false as track_incoming, false as sale_delay, false as track_all, false as track_outgoing, 
(select case when im."PART" like '___-_____-__%' then false else true end) as purchase_ok, false as track_production, 1 as produce_delay, 
(select case when upper(im."PART") like 'EX:%'  then true else false end) as hr_expense_ok
from "gss_V_INVENTORY_MSTR" as im
where case when im."PART" like '___-_____-__%' then
				concat(left(im."PART",12),im."DESCRIPTION")
			else
				concat(im."PART",im."DESCRIPTION")
			end not in (select concat("name",description_purchase) as "exists" from product_template)
and im."PART" like '001%';
"""

insertProductProduct="""
insert into product_product (create_uid, create_date,write_uid, default_code, write_date, name_template, active, product_tmpl_id);

select 1 as create_uid, clock_timestamp() as create_date, 1 as write_uid, 
case when gss."PART" like '___-_____-__%' then
				case when length(gss."PART")>12 then 
						left(gss."PART",12) || ' (' || trim(right(gss."PART",3)) || ')' 
					else
						left(gss."PART",12) end
			else
				gss."PART"
			end 
as default_code, clock_timestamp() as write_date,   
case when gss."PART" like '___-_____-__%' then
				left(gss."PART",12)
			else
				gss."PART"
			end 
as name_template, 
true as active,
(select id from product_template as pt where left(pt."name",12)= left(gss."PART",12)) as product_tmpl_id
from "gss_V_INVENTORY_MSTR" as gss;
"""
