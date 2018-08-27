

#Prepare PROCURE_METHOD AND SUPPLY_METHOD
translatePJFM = """UPDATE gss_V_INVENTORY_MASTER ("PROCURE_METHOD", "SUPPLY_METHOD")
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
strTrackLot = """  CASE WHEN FLAG_LOT='Y' THEN 'True' 
                   ELSE 'False' END AS TRACK_INCOMING,
              CASE WHEN FLAG_LOT='Y' THEN 'True' 
                   ELSE 'False' AS TRACK_PRODUCTION,
              CASE WHEN FLAG_LOT='Y','True' 
                   ELSE 'False' as TRACK_OUTGOING,"""


#createWorcentersResourcesTemplatesProducts="""
createTempGssParts="""
create table "temp_gss_parts"(id serial primary key, "prod_template" text not NULL, rev_name text null, "orig_part" text not null);

/* GSS PARTS WITH NO REVISION NUMBER */
insert into "temp_gss_parts" ("prod_template", "rev_name", "orig_part")
select prod_template, "rev_name", orig_part
from(
	select gs.prod_template, gs.rev as "rev_name", "PART" as orig_part
        from (
                select distinct trim(left(asdf."PART",length(asdf."PART") - asdf.LenFromEnd)) as prod_template,
                case when asdf.LenFromEnd > 0 then right(asdf."PART",asdf.LenFromEnd-1) else '' end as rev,
                asdf."PART"
                from (
                        select gss."PART",
                        case when strpos(gss."PART",' ')>9 and length(gss."PART")>=18 then strpos(reverse(gss."PART"),' ')
                        else '0' end as LenFromEnd
                        from "gss_V_INVENTORY_MSTR" as gss
                ) as asdf
                order by rev
      		) as gs
    ) as ddd
;

/* FINISHED PARTS WITH REV NUMBERS */
insert into "temp_gss_parts" ("prod_template", "rev_name", "orig_part")
select prod_template, "rev_name", orig_part
from(
        select gs.prod_template, gs.rev as "rev_name", "PART" as orig_part
        from (
                select distinct trim(left(asdf."PART",length(asdf."PART") - asdf.LenFromEnd)) as prod_template,
                case when asdf.LenFromEnd>0 then replace(right(asdf."PART",asdf.LenFromEnd-1),'*','') else '' end as rev,
                asdf."PART"
                from (
                        select gss."PART",
                        case when strpos(gss."PART",' ')>9 and length(gss."PART")>=18 then strpos(reverse(gss."PART"),' ')
                        else '0' end as LenFromEnd
                        from "gss_V_PO_LINES" as gss
                ) as asdf
                order by rev) as gs           
        ) as ddd
where prod_template not in (select prod_template from "temp_gss_parts")
order by prod_template
;


/* PARTS THAT WERE ONLY DEFINED AS ROUTERS IN GLOBALSHOP */
insert into "temp_gss_parts" ("prod_template", "rev_name", "orig_part")
select prod_template, "rev_name", orig_part
from(
        select gs.prod_template, gs.rev as "rev_name", "PART" as orig_part
        from (
                select distinct trim(left(asdf."PART",length(asdf."PART") - asdf.LenFromEnd)) as prod_template,
                case when asdf.LenFromEnd>0 then replace(right(asdf."PART",asdf.LenFromEnd-1),'*','') else '' end as rev,
                asdf."PART"
                from (
                        select gss."ROUTER" as "PART",
                        case when strpos(gss."ROUTER",' ')>9 and length(gss."ROUTER")>=18 then strpos(reverse(gss."ROUTER"),' ')
                        else '0' end as LenFromEnd
                        from "gss_V_ROUTER_HEADER" as gss
                ) as asdf
                order by rev) as gs           
        ) as ddd
where prod_template not in (select prod_template from "temp_gss_parts")
order by prod_template
;
"""

insertResoucesFromWorkCenter="""
/*CREATE WORK CENTER RESOURCES*/
insert into resource_resource (create_uid, time_efficiency , "name", company_id, write_uid , create_date, write_date, active, resource_type)
select 1 as create_uid, 1 as time_efficiency, gss."MACHINE" as "name", 1 as company_id, 1 as write_uid, clock_timestamp() as create_date, clock_timestamp() as write_date, true as active, 'material' as resource_type
from "gss_V_WORKCENTERS" as gss
where gss."MACHINE" not in (select "name" from resource_resource where resource_type='material');"""


insertWorkCenterFromWorkCenters="""
/*CREATE MRP WORKCENTERS BASED ON MATERIAL RESOURCES*/
insert into mrp_workcenter (create_uid, capacity_per_cycle, time_start, resource_id, time_stop, note, costs_hour, costs_cycle, write_date, create_date, write_uid, time_cycle)
select 1 as create_uid, 1 as capacity_per_cycle, 0 as time_start, rr.id as resource_id, 0 as time_stop, gss."MACHINE" || ' ' || gss."WC_NAME" as note, cast(gss."STANDARD_COST" as float) as costs_hour, 0 as costs_cycle, clock_timestamp() as write_date, clock_timestamp() as create_date, 1 as write_uid, 0 as time_cycle
from "gss_V_WORKCENTERS" as gss
left join resource_resource as rr on rr.resource_type='material' and gss."MACHINE"=rr."name"
where rr.id not in (select resource_id from mrp_workcenter);"""

insertMissingResourses="""
/*ADD MISSING RESOURCES */
insert into resource_resource (create_uid, time_efficiency, "name", company_id, write_uid, create_date, write_date, active, resource_type)
values  (1 , 1 , 'SL-G', 1 , 1 , clock_timestamp() , clock_timestamp() , true , 'material' ),
        (1 , 1 , 'VFCM', 1 , 1 , clock_timestamp() , clock_timestamp() , true , 'material' ),
        (1 , 1 , 'RE01', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'SOFT', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'DESS', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'DEBU', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'DRAF', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'CNCP', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'RE02', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'ASSE', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'ELE2', 1 , 1 , clock_timestamp() , clock_timestamp() , false, 'material' ),
        (1 , 1 , 'GR-G', 1 , 1 , clock_timestamp() , clock_timestamp() , true , 'material' ),
        (1 , 1 , 'ELE1', 1 , 1 , clock_timestamp() , clock_timestamp() , false , 'material' ),
        (1 , 1 , 'DES2', 1 , 1 , clock_timestamp() , clock_timestamp() , false, 'material' ),
        (1 , 1 , 'MACH', 1 , 1 , clock_timestamp() , clock_timestamp() , false, 'material' ),
        (1 , 1 , 'SLCM', 1 , 1 , clock_timestamp() , clock_timestamp() , false, 'material' );                
                
/* ADD MISSING MRP WORKCENTERS BASED ON MISSING RESOURCES*/
insert into mrp_workcenter (create_uid, capacity_per_cycle, time_start, resource_id, time_stop, note, costs_hour, costs_cycle, write_date, create_date, write_uid, time_cycle)
values  (1, 1, 0, (select id from resource_resource where "name"='SL-G'), 0 , 'SL-G' || ' ' || 'Lathe Group' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='VFCM'), 0 , 'VFCM' || ' ' || 'CM Mill Group' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='RE01'), 0 , 'RE01' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='SOFT'), 0 , 'SOFT' || ' ' || 'Software' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='DESS'), 0 , 'DESS' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='DEBU'), 0 , 'DEBU' || ' ' || 'Deburring' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='DRAF'), 0 , 'DRAF' || ' ' || 'Drafting' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='CNCP'), 0 , 'CNCP', 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='RE02'), 0 , 'RE02', 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='ASSE'), 0 , 'ASSE' || ' ' || 'Assembly' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='ELE2'), 0 , 'ELE2' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='GR-G'), 0 , 'GR-G' || ' ' || 'Grinder Group' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='ELE1'), 0 , 'ELE1', 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='DES2'), 0 , 'DES2' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='MACH'), 0 , 'MACH' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
        (1, 1, 0, (select id from resource_resource where "name"='SLCM'), 0 , 'SLCM' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 )
;
"""

updateProductLines="""
/* FIX PRODUCT LINE (aka categ_id) */
update "gss_V_INVENTORY_MSTR" 
set "PRODUCT_LINE" = 
case
when trim("PRODUCT_LINE")='ZH' then 'Advertising & Promotion'
when trim("PRODUCT_LINE")='AA' then 'Automated Assembly'
when trim("PRODUCT_LINE")='BI' then 'Bin Inventory'
when trim("PRODUCT_LINE")='BP' then 'Build To Print'
when trim("PRODUCT_LINE")='ZI' then 'Computer Equipment'
when trim("PRODUCT_LINE")='ZJ' then 'Computer Licenses'
when trim("PRODUCT_LINE")='ZK' then 'Computer Software'
when trim("PRODUCT_LINE")='ZA' then 'Consumables'
when trim("PRODUCT_LINE")='CM' then 'Contract Manufacturing'
when trim("PRODUCT_LINE")='CR' then 'Contract Repair'
when trim("PRODUCT_LINE")='EC' then 'Electrical Components'
when trim("PRODUCT_LINE")='ES' then 'Engineering Services'
when trim("PRODUCT_LINE")='EQ' then 'Equipment Rental'
when trim("PRODUCT_LINE")='FB' then 'Freight & Brokerage'
when trim("PRODUCT_LINE")='HC' then 'Hydraulic Components'
when trim("PRODUCT_LINE")='ZL' then 'Indirect Labour Accounts'
when trim("PRODUCT_LINE")='IN' then 'Innovations'
when trim("PRODUCT_LINE")='LS' then 'Lab Services'
when trim("PRODUCT_LINE")='ZC' then 'Laboratory Expenses'
when trim("PRODUCT_LINE")='MP' then 'Machined Parts'
when trim("PRODUCT_LINE")='MC' then 'Mechanical Components'
when trim("PRODUCT_LINE")='SP' then 'OEM Spare Parts (why non-Inv?)'
when trim("PRODUCT_LINE")='ZM' then 'Office Supplies'
when trim("PRODUCT_LINE")='SD' then 'Payroll Deduction'
when trim("PRODUCT_LINE")='PI' then 'Platform Inventory'
when trim("PRODUCT_LINE")='PC' then 'Pneumatic Components'
when trim("PRODUCT_LINE")='ZD' then 'Quality Expenditures'
when trim("PRODUCT_LINE")='ZN' then 'R&M Building'
when trim("PRODUCT_LINE")='ZO' then 'R&M Equipment - On Demand'
when trim("PRODUCT_LINE")='ZP' then 'R&M Equipment - Prevenative'
when trim("PRODUCT_LINE")='RM' then 'Raw Material'
when trim("PRODUCT_LINE")='ZQ' then 'Safety & Environmental Costs'
when trim("PRODUCT_LINE")='ZR' then 'Shop Equipment  >$500'
when trim("PRODUCT_LINE")='ZE' then 'Shop Supplies'
when trim("PRODUCT_LINE")='ZF' then 'Shop Tools  <$500'
when trim("PRODUCT_LINE")='SU' then 'Subcontractors'
when trim("PRODUCT_LINE")='TA' then 'Tool Allowance'
when trim("PRODUCT_LINE")='ZG' then 'Tooling'
when trim("PRODUCT_LINE")='ZS' then 'Training & Seminars'
when trim("PRODUCT_LINE")='ZT' then 'Waste Removal'
else 'Raw Material'
end;

/* FIX PRODUCT LINE (aka categ_id) */
update "gss_V_PO_LINES" 
set "PRODUCT_LINE" = 
case
when trim("PRODUCT_LINE")='ZH' then 'Advertising & Promotion'
when trim("PRODUCT_LINE")='AA' then 'Automated Assembly'
when trim("PRODUCT_LINE")='BI' then 'Bin Inventory'
when trim("PRODUCT_LINE")='BP' then 'Build To Print'
when trim("PRODUCT_LINE")='ZI' then 'Computer Equipment'
when trim("PRODUCT_LINE")='ZJ' then 'Computer Licenses'
when trim("PRODUCT_LINE")='ZK' then 'Computer Software'
when trim("PRODUCT_LINE")='ZA' then 'Consumables'
when trim("PRODUCT_LINE")='CM' then 'Contract Manufacturing'
when trim("PRODUCT_LINE")='CR' then 'Contract Repair'
when trim("PRODUCT_LINE")='EC' then 'Electrical Components'
when trim("PRODUCT_LINE")='ES' then 'Engineering Services'
when trim("PRODUCT_LINE")='EQ' then 'Equipment Rental'
when trim("PRODUCT_LINE")='FB' then 'Freight & Brokerage'
when trim("PRODUCT_LINE")='HC' then 'Hydraulic Components'
when trim("PRODUCT_LINE")='ZL' then 'Indirect Labour Accounts'
when trim("PRODUCT_LINE")='IN' then 'Innovations'
when trim("PRODUCT_LINE")='LS' then 'Lab Services'
when trim("PRODUCT_LINE")='ZC' then 'Laboratory Expenses'
when trim("PRODUCT_LINE")='MP' then 'Machined Parts'
when trim("PRODUCT_LINE")='MC' then 'Mechanical Components'
when trim("PRODUCT_LINE")='SP' then 'OEM Spare Parts (why non-Inv?)'
when trim("PRODUCT_LINE")='ZM' then 'Office Supplies'
when trim("PRODUCT_LINE")='SD' then 'Payroll Deduction'
when trim("PRODUCT_LINE")='PI' then 'Platform Inventory'
when trim("PRODUCT_LINE")='PC' then 'Pneumatic Components'
when trim("PRODUCT_LINE")='ZD' then 'Quality Expenditures'
when trim("PRODUCT_LINE")='ZN' then 'R&M Building'
when trim("PRODUCT_LINE")='ZO' then 'R&M Equipment - On Demand'
when trim("PRODUCT_LINE")='ZP' then 'R&M Equipment - Prevenative'
when trim("PRODUCT_LINE")='RM' then 'Raw Material'
when trim("PRODUCT_LINE")='ZQ' then 'Safety & Environmental Costs'
when trim("PRODUCT_LINE")='ZR' then 'Shop Equipment  >$500'
when trim("PRODUCT_LINE")='ZE' then 'Shop Supplies'
when trim("PRODUCT_LINE")='ZF' then 'Shop Tools  <$500'
when trim("PRODUCT_LINE")='SU' then 'Subcontractors'
when trim("PRODUCT_LINE")='TA' then 'Tool Allowance'
when trim("PRODUCT_LINE")='ZG' then 'Tooling'
when trim("PRODUCT_LINE")='ZS' then 'Training & Seminars'
when trim("PRODUCT_LINE")='ZT' then 'Waste Removal'
else 'Raw Material'
end;
"""

insertProductTemplates="""
/* Insert Product Templates */
insert into product_template (warranty, list_price, write_uid, mes_type, uom_id,description_purchase, create_date, uos_coeff, create_uid, rental, company_id, uom_po_id, "type", description, write_date, active, categ_id, sale_ok, "name", description_sale, track_incoming, sale_delay, track_all, track_outgoing, purchase_ok, track_production, produce_delay, hr_expense_ok)
select distinct 0 as warranty,0.00 as list_price, 1 as write_uid, 'fixed' as mes_type, (select id from product_uom where "name"=im."UM_INVENTORY") as uom_id,
im."DESCRIPTION" as description_purchase, clock_timestamp() as create_date, 1.0 as uos_coeff, 1 as create_uid, false as rental, 1 as company_id,
(select id from product_uom where "name"=im."UM_PURCHASING") as uom_po_id, 'product' as "type", im."DESCRIPTION" as description,
clock_timestamp() as write_date, (SELECT case when im."DATE_LAST_USAGE" >= '2016-01-01'::date then true else false end) as active, (select id from product_category where "name"= im."PRODUCT_LINE" limit 1) as categ_id, (select case when im."PART" like '___-_____-__%' then true else false end) as sale_ok,
tgp."prod_template"  as "name",
im."DESCRIPTION" as description_sale,
false as track_incoming, 0 as sale_delay, false as track_all, false as track_outgoing,
(select case when im."PART" like '___-_____-__%' then false else true end) as purchase_ok, false as track_production, 1 as produce_delay,
(select case when upper(im."PART") like 'EX:%'  then true else false end) as hr_expense_ok
from "gss_V_INVENTORY_MSTR" as im
left join "temp_gss_parts" as tgp on tgp."orig_part" = im."PART"
where tgp."prod_template" not in (select concat("name",description_purchase) as "exists" from product_template)
;"""

insertProductProduct="""
/* INSERT PRODUCT PRODUCT */
insert into product_product (create_uid, create_date,write_uid, default_code, write_date, name_template, active, product_tmpl_id)
select 1 as create_uid, clock_timestamp() as create_date, 1 as write_uid,
case when tgp."rev_name" <> '' then
                              tgp."prod_template" || ' (' || tgp."rev_name" || ')'
                        else
                                tgp."prod_template"
                        end
as default_code, clock_timestamp() as write_date,
tgp.prod_template as name_template,
pt."active" as active,
pt."id" as product_tmpl_id
from "gss_V_INVENTORY_MSTR" as gss
left join "temp_gss_parts" as tgp on tgp."orig_part" = gss."PART"
left join product_template as pt on pt."name" = tgp."prod_template"
;"""

insertPOLineProductTemplate="""
/* INSERT PO LINE PRODUCT TEMPLATE */
insert into product_template (warranty, list_price, write_uid, mes_type, uom_id,description_purchase, create_date, uos_coeff, create_uid, rental, company_id, uom_po_id, "type", description, write_date, active, categ_id, sale_ok, "name", description_sale, track_incoming, sale_delay, track_all, track_outgoing, purchase_ok, track_production, produce_delay, hr_expense_ok)
select distinct 0 as warranty,0.00 as list_price, 1 as write_uid, 'fixed' as mes_type, (select id from product_uom where "name"=gss."UM_INVENTORY") as uom_id,
gss."DESCRIPTION" as description_purchase, gss."DATE_DUE_LINE" as create_date, 1.0 as uos_coeff, 1 as create_uid, false as rental, 1 as company_id,
(select id from product_uom where "name"=gss."UM_PURCHASING") as uom_po_id, 'product' as "type", gss."DESCRIPTION" as description,
clock_timestamp() as write_date, (SELECT case when gss."DATE_DUE_LINE" >= '2016-01-01'::date then true else false end) as active, (select id from product_category where "name"= gss."PRODUCT_LINE" limit 1) as categ_id, true as sale_ok,
tgp."prod_template"  as "name",
gss."DESCRIPTION" as description_sale,
false as track_incoming, 0 as sale_delay, false as track_all, false as track_outgoing,
true as purchase_ok, false as track_production, 1 as produce_delay,
(select case when upper(gss."PART") like 'EX:%'  then true else false end) as hr_expense_ok
from "gss_V_PO_LINES" as gss
left join "temp_gss_parts" as tgp on tgp."orig_part" = gss."PART"
where tgp."prod_template" not in (select "name" as "exists" from product_template)
order by gss."DATE_DUE_LINE" desc
;
"""

insertPOLineProductProduct="""
insert into product_product (create_uid, create_date,write_uid, default_code, write_date, name_template, active, product_tmpl_id)
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
(select id from product_template as pt where left(pt."name",12)= left(gss."PART",12) limit 1) as product_tmpl_id
from "gss_V_PO_LINES" as gss
order by gss."DATE_DUE_LINE" desc;
"""

insertProductAttibuteLines="""
/* Associate all the templates like ___-_____-__ with attribute id 1 (aka Revision) */
insert into product_attribute_line (create_uid, create_date, write_uid, product_tmpl_id, attribute_id, write_date)
select 1 as create_uid, clock_timestamp() as create_date, 1 as write_uid, pt.id as product_tmpl_id, 1 as attribute_id, clock_timestamp() as write_date
from product_template as pt where "name" like '___-_____-__%'
and pt.id not in (select product_tmpl_id from product_attribute_line);"""

insertProductAttributeValues="""
insert into product_attribute_value (create_date, write_uid, write_date, create_uid, "name", attribute_id)
select clock_timestamp() as create_date, 1 as write_uid, clock_timestamp() as write_date, 1 as create_uid, gs.rev as "name", 1 as attribute_id
from (
select distinct right(asdf."PART",asdf.LenFromEnd-1) as rev from (
select gss."PART", 
case when strpos(gss."PART",' ')>9 and length(gss."PART")>=18 then strpos(reverse(gss."PART"),' ') 
     else '0' end as LenFromEnd
from "gss_V_INVENTORY_MSTR" as gss
) as asdf
where LenFromEnd <= 4 and LenFromEnd>0 
order by rev) as gs
where gs.rev not in (select "name" from product_attribute_value);
"""

insertProdAttValProdProdRel="""
/*obviously as there's no "INSERT INTO" this is incomplete. */

select (select id from product_attribute_value as pav where ddd."rev_name" =  pav."name") as att_id,
(select "default_code" from product_product as pp where pp."default_code" = orig_part limit 1) as prod_id
,(select "default_code" from product_product as pp where orig_part = pp."default_code" limit 1) as sorta_prod_id
,prod_template, "rev_name", orig_part
from(
	select gs.prod_template, gs.rev as "rev_name", "PART" as orig_part
	from (
		select distinct trim(left(asdf."PART",length(asdf."PART") - asdf.LenFromEnd-1)) as prod_template, 
		right(asdf."PART",asdf.LenFromEnd-1) as rev,
		asdf."PART" 
		from (
			select gss."PART", 
			case when strpos(gss."PART",' ')>9 and length(gss."PART")>=18 then strpos(reverse(gss."PART"),' ') 
		     	else '0' end as LenFromEnd
			from "gss_V_INVENTORY_MSTR" as gss
		) as asdf
		where LenFromEnd <= 4 and LenFromEnd>0 
		order by rev) as gs
	) as ddd
;
"""

