insertWCandRouters="""

/*CREATE WORK CENTER RESOURCES*/
insert into resource_resource (create_uid, time_efficiency , "name", company_id, write_uid , create_date, write_date, active, resource_type)
select 1 as create_uid, 1 as time_efficiency, gss."MACHINE" as "name", 1 as company_id, 1 as write_uid, clock_timestamp() as create_date, clock_timestamp() as write_date, true as active, 'material' as resource_type
from "gss_V_WORKCENTERS" as gss
where gss."MACHINE" not in (select "name" from resource_resource where resource_type='material');


/*CREATE MRP WORKCENTERS BASED ON MATERIAL RESOURCES*/
insert into mrp_workcenter (create_uid, capacity_per_cycle, time_start, resource_id, time_stop, note, costs_hour, costs_cycle, write_date, create_date, write_uid, time_cycle)
select 1 as create_uid, 1 as capacity_per_cycle, 0 as time_start, rr.id as resource_id, 0 as time_stop, gss."MACHINE" || ' ' || gss."WC_NAME" as note, cast(gss."STANDARD_COST" as float) as costs_hour, 0 as costs_cycle, clock_timestamp() as write_date, clock_timestamp() as create_date, 1 as write_uid, 0 as time_cycle
from "gss_V_WORKCENTERS" as gss
left join resource_resource as rr on rr.resource_type='material' and gss."MACHINE"=rr."name"
where rr.id not in (select resource_id from mrp_workcenter);

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
        (1 , 1 , 'SLCM', 1 , 1 , clock_timestamp() , clock_timestamp() , false, 'material' )

                
                
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

/*select id from resource_resource where "name"='VF-G';*/
"""

alterTableMrpRouting="""
ALTER TABLE mrp_routing ALTER COLUMN code TYPE varchar(25);
"""

insertRoutingHeaders="""
/* ADD ROUTING (HEADERS) */
insert into mrp_routing (code, create_date,write_uid,write_date,active,create_uid,"name",company_id,note)
select case when tgp."rev_name" <> '' then
                              tgp."prod_template" || ' (' || tgp."rev_name" || ')'
                        else
                                tgp."prod_template"
                        end as code,
gss."DATE_ORIGINAL" as create_date, 1 as write_uid, gss."DATE_ORIGINAL" as write_date, true as active, 1 as create_uid, gss."ROUTER" as "name", 1 as company_id, gss."DESCRIPTION_ROUTER" as note
from "gss_V_ROUTER_HEADER" as gss
left join "temp_gss_parts" as tgp on tgp."orig_part" = gss."ROUTER"
where tgp."orig_part" is not null
order by create_date desc;
"""

insertRoutingLines="""
/* ADD ROUTING LINES */
insert into mrp_routing_workcenter (create_uid,cycle_nbr,"name","sequence",company_id,note,create_date,write_date,routing_id,workcenter_id,write_uid,hour_nbr)
select 1 as create_uid, 1 as cycle_nbr, GSS."PART_WC_OUTSIDE" as "name",
cast(gss."LINE_ROUTER" as integer) as "sequence", 1 as company_id, gss."DESC_RT_LINE" as note, clock_timestamp() as create_date, clock_timestamp() as write_date,
mr_id as routing_id,
mrpwc.wc_id as workcenter_id,
1 as write_uid, 
gss."SETUP" + gss."RUN_TIME" as hour_nbr
from  (select case when tgp."rev_name" <> '' then
                              tgp."prod_template" || ' (' || tgp."rev_name" || ')'
                        else
                                tgp."prod_template"
                        end as "router_with_rev",
               rl."ROUTER", rl."PART_WC_OUTSIDE", rl."SETUP", rl."RUN_TIME", rl."DESC_RT_LINE", rl."LINE_ROUTER"
        from "gss_V_ROUTER_LINE" as rl 
        left join "temp_gss_parts" as tgp on tgp."orig_part" = rl."ROUTER"
        where trim(rl."LMO") in ('L')
        ) as gss
left join  (select wc.id as wc_id, wc.resource_id as wc_res_id, rr.id, rr."name" 
			from mrp_workcenter as wc 
			left join resource_resource as rr on rr.id = wc.resource_id) as mrpwc 
			on mrpwc."name" = gss."PART_WC_OUTSIDE"
left join (select id as mr_id, "code" from mrp_routing) as mr on (mr."code"=gss."router_with_rev" and mr_id is not null)
order by routing_id, sequence;
"""
