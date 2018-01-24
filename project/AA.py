insertAnalyticAccountParents="""
nsert into "account_analytic_account" ("name",code,company_id,description,parent_id,state,"type",
    use_tasks, use_issues, user_id, write_uid,use_timesheets,date_start, write_date, create_date)
      select "odooName" as "name", "odooCode" as code,1 as company_id,
    upper(trim(GSS1."PROJECT")) || ' ' || upper(trim(GSS1."PRJ_DESCR")) || E'\n' || 'Section: ' || upper(trim(GSS1."PHASE")) || ' - ' || initcap(trim(GSS1."PHASE_DESCR"))
    as description,
    case when GSS1."SUBACCOUNT"=0 then
    		(select id from account_analytic_account where "name" = 'Automated Assembly')
    	else
    		(select id from account_analytic_account where code= upper(trim(GSS1."PROJECT")) limit 1)
    	end as parent_id,		'open' as state,			'contract' as "type",
    true as use_tasks,    		true as use_issues,		    1 as user_id,
    1 as write_uid,			    true as use_timesheets,     GSS1."DATE_CREATED" as date_start,
    clock_timestamp() as write_date,	    				clock_timestamp() as create_date
    from (select distinct "AA", position(E'\\' in "AA") as "SUBACCOUNT", "PHASE_DESCR", "PROJECT", "PHASE", "PRJ_DESCR", "DATE_CREATED", "JOB",
    case when length(trim("PHASE_DESCR")) > 0 then
                trim(concat(upper(trim("PROJECT")) , ' > ' , initcap(trim("PHASE_DESCR"))))
    	else
    			trim(concat(upper(Trim("PROJECT")) , ' (' , upper(trim("PRJ_DESCR")) , ')')) 
        end as "odooName",
    case when length(trim("PHASE_DESCR")) > 0 then
    			trim(concat(upper(trim("PROJECT")) , ' > ' , trim("PHASE")))
         Else
                upper(trim("PROJECT")) 
         end as "odooCode",
         (select id from account_analytic_account where code= upper(trim("PROJECT")) limit 1) as parent_id
    from "gss_ANALYTIC_ACCOUNTS" where trim("JOB")='' and position(E'\\' in "AA")=0 order by "PROJECT","PHASE","JOB"
    ) as GSS1
    ;"""

insertAnalyticAccountChildren="""
insert into "account_analytic_account" ("name",code,company_id,description,parent_id,state,"type",
    use_tasks, use_issues, user_id, write_uid,use_timesheets,date_start, write_date, create_date)
      select "odooName" as "name", "odooCode" as code,1 as company_id,
    upper(trim(GSS1."PROJECT")) || ' ' || upper(trim(GSS1."PRJ_DESCR")) || E'\n' || 'Section: ' || upper(trim(GSS1."PHASE")) || ' - ' || initcap(trim(GSS1."PHASE_DESCR"))
    as description,
    case when GSS1."SUBACCOUNT"=0 then
    		(select id from account_analytic_account where "name" = 'Automated Assembly')
    	else
    		(select id from account_analytic_account where code= upper(trim(GSS1."PROJECT")) limit 1)
    	end as parent_id,		'open' as state,			'contract' as "type",
    true as use_tasks,    		true as use_issues,		    1 as user_id,
    1 as write_uid,			    true as use_timesheets,     GSS1."DATE_CREATED" as date_start,
    clock_timestamp() as write_date,	    				clock_timestamp() as create_date
    from (select distinct "AA", position(E'\\' in "AA") as "SUBACCOUNT", "PHASE_DESCR", "PROJECT", "PHASE", "PRJ_DESCR", "DATE_CREATED", "JOB",
    case when length(trim("PHASE_DESCR")) > 0 then
                trim(concat(upper(trim("PROJECT")) , ' > ' , initcap(trim("PHASE_DESCR"))))
    	else
    			trim(concat(upper(Trim("PROJECT")) , ' (' , upper(trim("PRJ_DESCR")) , ')')) 
        end as "odooName",
    case when length(trim("PHASE_DESCR")) > 0 then
    			trim(concat(upper(trim("PROJECT")) , ' > ' , trim("PHASE")))
         Else
                upper(trim("PROJECT")) 
         end as "odooCode",
         (select id from account_analytic_account where code= upper(trim("PROJECT")) limit 1) as parent_id
    from "gss_ANALYTIC_ACCOUNTS" where trim("JOB")='' and position(E'\\' in "AA")<>0 order by "PROJECT","PHASE","JOB"
    ) as GSS1
    ;"""


