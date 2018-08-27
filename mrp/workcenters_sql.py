insertWCs="""
/*CREATE WORK CENTER RESOURCES*/
insert into resource_resource (create_uid , 	 time_efficiency , "name"                , 		company_id, 	 write_uid , create_date         			, 	write_date          		 , active		 , resource_type)
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
values 	(1 , 1 , 'SL-G', 1 , 1 , clock_timestamp() , clock_timestamp() , true , 'material' ),
		(1 , 1 , 'VFCM', 1 , 1 , clock_timestamp() , clock_timestamp() , true , 'material' ),
		(1 , 1 , 'MACH', 1 , 1 , clock_timestamp() , clock_timestamp() , true , 'material' )

/* ADD MISSING MRP WORKCENTERS BASED ON MISSING RESOURCES*/
insert into mrp_workcenter (create_uid, capacity_per_cycle, time_start, resource_id, time_stop, note, costs_hour, costs_cycle, write_date, create_date, write_uid, time_cycle)
values 	(1, 1, 0, (select id from resource_resource where "name"='SL-G'), 0 , 'SL-G' || ' ' || 'Lathe Group' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
	(1, 1, 0, (select id from resource_resource where "name"='VFCM'), 0 , 'VFCM' || ' ' || 'CM Mill Group' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 ),
	(1, 1, 0, (select id from resource_resource where "name"='MACH'), 0 , 'MACH' || ' ' || 'Shop Machine' , 50.0 , 0 , clock_timestamp() , clock_timestamp() , 1 , 0 )
;

"""
