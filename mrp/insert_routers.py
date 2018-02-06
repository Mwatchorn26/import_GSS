insertRoutes="""
/* ROUTING STEP 1: ALTER TABLE TO HOLD OUR CODE VALUE */
ALTER TABLE mrp_routing ALTER COLUMN code TYPE varchar(25);

/* ADD ROUTING (HEADERS) */
insert into mrp_routing (code, create_date,write_uid,write_date,active,create_uid,"name",company_id,note)
select case when gss."ROUTER" like '___-_____-__%' then
				case when length(gss."ROUTER")>12 then 
						left(gss."ROUTER",12) || ' rev ' || trim(right(gss."ROUTER",3)) 
					else
						left(gss."ROUTER",12) end
			else
				gss."ROUTER"
end as code, 
gss."DATE_ORIGINAL" as create_date, 1 as write_uid, gss."DATE_ORIGINAL" as write_date, true as active, 1 as create_uid, gss."ROUTER" as "name", 1 as company_id, gss."DESCRIPTION_ROUTER" as note
from "gss_V_ROUTER_HEADER" as gss
order by create_date desc;

/* ADD ROUTING LINES */
insert into mrp_routing_workcenter (create_uid,cycle_nbr,"name","sequence",company_id,note,create_date,write_date,routing_id,workcenter_id,write_uid,hour_nbr)
select 1 as create_uid, 1 as cycle_nbr, GSS."PART_WC_OUTSIDE" as "name", 
cast(gss."LINE_ROUTER" as integer) as "sequence", 1 as company_id, gss."DESC_RT_LINE" as note, clock_timestamp() as create_date, clock_timestamp() as write_date, 
(select id from mrp_routing as mr where mr."code"=gss."router_with_rev") as routing_id,
(select wc.id from mrp_workcenter as wc left join resource_resource as rr on rr.id = wc.resource_id where rr."name" = gss."PART_WC_OUTSIDE") as workcenter_id,
1 as write_uid,
gss."SETUP" + gss."RUN_TIME" as hour_nbr
from  (select case when "ROUTER" like '___-_____-__%' then
		case when length("ROUTER")>12 then 
				left("ROUTER",12) || ' rev ' || trim(right("ROUTER",3)) 
			else
				left("ROUTER",12) end
	else
		"ROUTER"
	end as "router_with_rev", "ROUTER", "PART_WC_OUTSIDE","SETUP","RUN_TIME", "DESC_RT_LINE", "LINE_ROUTER" from "gss_V_ROUTER_LINE" where trim("LMO") in ('L')) as gss
order by routing_id, sequence ;
"""
