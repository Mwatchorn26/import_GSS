insertTasks="""
/*TASKS:*/
insert into project_task (create_date, "sequence", write_uid, create_uid, date_start, company_id, project_id, description, 
						kanban_state, write_date, active, stage_id, "name", reviewer_id, notes)
select clock_timestamp() as create_date, 10 as sequence, 1 as write_uid, 1 as create_uid, 
job_hdr."DATE_START" as date_start, 1 as company_id, (select id from project_project where analytic_account_id =aaa.id) as project_id, job_hdr."DESCRIPTION" as description,
'normal' as kanban_state, clock_timestamp() as write_date, true as active, (select id from project_task_type where "name"='Active') as stage_id,
job_hdr."DESCRIPTION" as "name", 1 as reviewer_id, job_hdr."DESCRIPTION" as "notes"
from (
select distinct "AA", position(E'\\' in "AA") as "SUBACCOUNT", "PHASE_DESCR", "PROJECT", "PHASE", "PRJ_DESCR", "DATE_CREATED", "JOB", "SUFFIX",
    case when length(trim("PHASE_DESCR")) > 0 then
                trim(concat(upper(trim("PROJECT")) , ' > ' , initcap(trim("PHASE_DESCR"))))
    	else
    			trim(concat(upper(Trim("PROJECT")) , ' (' , upper(trim("PRJ_DESCR")) , ')')) 
        end as "odooName",
    case when length(trim("PHASE_DESCR")) > 0 then
    			trim(concat(upper(trim("PROJECT")) , ' > ' , trim("PHASE")))
         Else
                upper(trim("PROJECT")) 
         end as "odooCode"    
    from "gss_ANALYTIC_ACCOUNTS" where trim("JOB")<>'' and position(E'\\' in "AA")>0 ) as gaa
left join (select "JOB", "SUFFIX", "DATE_START", "DESCRIPTION" from "gss_V_JOB_HEADER") as job_hdr on job_hdr."JOB"=gaa."JOB" and job_hdr."SUFFIX"=gaa."SUFFIX"
left join (select id, code from account_analytic_account) as aaa on aaa.code = gaa."odooCode"
where job_hdr."SUFFIX"<>'' and job_hdr."JOB"<>''
;


"""
