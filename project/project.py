insertProjects="""

nsert into mail_alias (alias_defaults, alias_contact, alias_model_id, create_uid, alias_parent_thread_id, write_uid, alias_parent_model_id, alias_user_id, write_date,create_date)
select '{''project_id'': ' || id ||'}' as alias_defaults, 
		'everyone' as alias_contact,
		 (select id from "ir_model" where "name"='Task') as alias_model_id,
		1 as create_uid,0 as alias_parent_thread_id,1 as write_uid,
		(select id from "ir_model" where "name"='Project') as alias_parent_model_id, 1 as alias_user_id, clock_timestamp() as write_date, clock_timestamp() as create_date 
from account_analytic_account 
where parent_id in (select id 
					from account_analytic_account 
					where parent_id=(select id 
									 from account_analytic_account 
									 where "name"='Automated Assembly'))
					or
						  id in (select id 
						  		 from account_analytic_account 
						  		 where parent_id=(select id from account_analytic_account where "name"='Automated Assembly'));

;
/*CREATE PROJECTS */
insert into project_project (alias_model, alias_id, write_uid, effective_hours, planned_hours, active,analytic_account_id, create_uid, progress_rate, "sequence",privacy_visibility, total_hours, state)
select 'project.task' as alias_model, 
		(select id from mail_alias as ma where ma.alias_defaults ='{''project_id'': ' || aaa.id ||'}') as alias_id, 
		1 as write_uid, 
		0 as effective_hours, 
		0 as planned_hours, true as active, id as analytic_account_id, 1 as create_uid, 0 as progress_rate, 10 as "sequence", 'employees' as privacy_visibility, 0 as total_hours, 'open' as state  
from account_analytic_account as aaa
where parent_id in (select id from account_analytic_account where parent_id=
                     (select id from account_analytic_account where "name"='Automated Assembly'))
	  or
	  id in (select id from account_analytic_account where parent_id=
                     (select id from account_analytic_account where "name"='Automated Assembly'))
                     ;


insert into "mail_alias" (alias_defaults, alias_contact, alias_model_id, create_uid, alias_parent_thread_id, write_uid, alias_parent_model_id, alias_user_id, write_date,create_date)
values ('{}','everyone',(select id from "ir_model" where "name"='Task'),
        1,0,1,(select id from "ir_model" where "name"='Project'), 1,
		clock_timestamp() , clock_timestamp() )
returning id as alias_id;


/*Add Project Task Stages(types?wft!Who named that): Created, Active, Cancelled, Shelved, Done*/
insert into project_task_type_rel
select account_analytic_account.id as project_id, project_task_type.id as task_id
from account_analytic_account 
left join project_task_type on project_task_type.id<>-1
where project_task_type."name" in ('Active','Done','Cancelled','Created','Shelved');


"""
