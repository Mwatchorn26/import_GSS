insertAnalyticAccounts="""insert into "account_analytic_account" ("name",code,company_id,description,parent_id,state,"type",
    use_tasks, use_issues, user_id, write_uid,use_timesheets,date_start, write_date, create_date)
    select "odooName" as "name", "odooCode" as code,1 as company_id,
    upper(trim(GSS1."PROJECT")) || ' ' || upper(trim(GSS1."PRJ_DESCR")) || E'\n' || 'Section:' || upper(trim(GSS1."PHASE")) || E'\n' || 'Description:' || initcap(trim(GSS1."PHASE_DESCR"))
    as description,
    case when length(trim(GSS1."JOB"))>0 then 
    		(select id from account_analytic_account where code= upper(trim(GSS1."PROJECT")) limit 1)
        else
    		(select id from account_analytic_account where "name" = 'Automated Assembly')
    	end as parent_id,
	'open' as state,
    'contract' as "type",
    true as use_tasks,
    true as use_issues,
    1 as user_id,
    1 as write_uid,
    true as use_timesheets,
    GSS1."DATE_CREATED" as date_start,
    clock_timestamp() as write_date,
    clock_timestamp() as create_date
    from 
    (select distinct "PHASE_DESCR", "PROJECT", "PHASE", "PRJ_DESCR", "DATE_CREATED", 
    case when length(trim("PHASE_DESCR")) > 0 then
                trim(concat(upper(trim("PROJECT")) , '  § ' , initcap(trim("PHASE_DESCR"))))
    	else
    			trim(concat(upper(Trim("PROJECT")) , '  (' , upper(trim("PRJ_DESCR")) , ')')) 
        end as "odooName",
    case when length(trim("PHASE_DESCR")) > 0 then
    			trim(concat(upper(trim("PROJECT")) , ' § ' , trim("PHASE")))
         Else
                upper(trim("PROJECT")) 
         end as "odooCode"
    from "gss_ANALYTIC_ACCOUNTS"    ) as GSS1
    ;"""



junk="""
    upper(trim(GSS1."PROJECT")) || ' ' || upper(trim(GSS1."PRJ_DESCR")) || E'\n' || upper(trim(GSS1."JOB")) ||    '-' || upper(trim(GSS1."SUFFIX")) || ' ' || initcap(trim(GSS1."PHASE_DESCR")) || E'\n' || initcap(trim(GSS1."PART"))
"""
