import AA_sql
import projects_sql
import tasks_sql

from psyQuery import qry
import datetime

def add_analytic_view(strName,strCode):
    L1="""insert into "public_account_analytic_account" (name,code,company_id,active,description,parent_id,state,type,"""
    L2="""use_tasks, use_issues, user_id, partner_id, write_uid,use_timesheets,date_start, write_date, create_date)"""
    L3="""values ({},{},1,1,{},1,"open","view",1,1,1,0,1,1,{},{},{})""".format(strName,strCode,strName,datetime.datetime.now(),datetime.datetime.now(),datetime.datetime.now())
    strQuery = L1+L2+L3
    qry(strQuery)



def load():
# Not needed, work gets done in preceeding VBA #    qry(AA_sql.insertAnalyticAccountParents)
# Not needed, work gets done in preceeding VBA #    qry(AA_sql.insertAnalyticAccountChildren)
#    add_analytic_view("Automated Assembly", "AA")
#    add_analytic_view("Contract Manufacturing", "CM")
#    add_analytic_view("IT", "AA_IT")

#    qry(projects_sql.insertProjects1_MailAlias)
   qry(projects_sql.insertProjects2_ProjectProject)
#   qry(projects_sql.insertProjects3_MailAlias)
#    qry(projects_sql.insertProjects4_TaskStages)


#    qry(tasks_sql.insertTasks)


def add_analytic_account(strName,strCode):
    L1="""insert into "public_account_analytic_account" (name,code,company_id,active,description,parent_id,state,type,"""
    L2="""use_tasks, use_issues, user_id, partner_id, write_uid,use_timesheets,date_start, write_date, create_date)"""
    L3="""values ({},{},1,1,{},1,"open","contract",1,1,1,0,1,1,(select ),{},{})""".format(strName,strCode,strName,datetime.datetime.now(),datetime.datetime.now(),datetime.datetime.now())
    strQuery = L1+L2+L3
    qry(strQuery)



var123="""(insert into "public_account_analytic_account" (name,code,company_id,active,description,parent_id,state,type,
    use_tasks, use_issues, user_id, partner_id, write_uid,use_timesheets,date_start, write_date, create_date)
    values (
    select "PHASE_DESCR", "PROJECT", "PHASE", "SUFFIX", "JOB", "PRJ_DESCR", "PART", "DATE_CREATED",
    case when length(trim("PHASE_DESCR")) > 0 Then
                Trim(concat(upper(trim("PROJECT"))) , "  - " , initcap(trim("PHASE_DESCR")))
    	else
    			trim(concat(upper(Trim("PROJECT")) , "  (" , upper(trim("PRJ_DESCR")) , ")") end as odooName,
    case when length(trim("PHASE_DESCR")) > 0 then
    			Trim(concat(upper(Trim("PROJECT")) , " - " , Trim("PHASE")))
            Else
                upper(Trim("PROJECT")) end as odooCode
    from "gss_ANALYTIC_ACCOUNTS"))) """



