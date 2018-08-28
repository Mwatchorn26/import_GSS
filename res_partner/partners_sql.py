insertSuppliers = """insert INTO res_partner ("name", "street", "street2", "city", "state_id","zip","country_id",
						"comment", "is_company", "supplier", "active","email","phone","fax","company_id","notify_email"
,"create_date","color","use_parent_address","employee","type","lang","create_uid","write_date","write_uid","display_name","customer","opt_out","vat_subjected"
) 
                 SELECT TRIM("NAME_VENDOR") AS "NAME", TRIM("ADDRESS1") AS "STREET", TRIM("ADDRESS2") AS "STREET2", TRIM("MSTR"."CITY") AS "CITY", 
		(select id from res_country_state as rcs where (rcs.code = TRIM("MSTR"."STATE")) limit 1) AS "STATE_id", TRIM("CODE_ZIP") AS "ZIP", 
		(select id from res_country as rc where (rc."name" = INITCAP(TRIM("MSTR"."COUNTRY"))) limit 1) AS "country_id",
                 case when TRIM("ATTENTION")='' then ''
                      else concat('ATTENTION: ' , TRIM("ATTENTION")) 
                 end AS COMMENT, 'TRUE' AS "IS_COMPANY" , 'TRUE' AS "SUPPLIER", 'TRUE' AS "ACTIVE",
                 TRIM("ADL1"."EMAIL") AS "EMAIL",
                 TRIM("ADL2"."PHONE") AS "PHONE",
                 TRIM("ADL3"."FAX") AS "FAX",
		 '1' as "company_id",
		 'always' as "notify_email",
		now() as "create_date", 
		0 as "color", 
		'false' as "use_parent_address",
		'false' as "employee", 'contact' as "type", 'en_US' as "lang", '1' as "create_uid", 
		now() as  "write_date", '1' as write_uid, trim("NAME_VENDOR") as "display_name", 
		'false' as "customer", 'false' as "opt_out", 
		case when INITCAP("MSTR"."COUNTRY")='France' then true
                	 when INITCAP("MSTR"."COUNTRY")='Ireland' then true
                	 when INITCAP("MSTR"."COUNTRY")='Germany' then true
                	 when INITCAP("MSTR"."COUNTRY")='Italy' then true
                	 when INITCAP("MSTR"."COUNTRY")='Netherlands' then true
                else false  end as "vat_subjected"

                 FROM ((("gss_V_VENDOR_MASTER" AS "MSTR"
                 LEFT JOIN "gss_V_VENDOR_ADDL" AS "ADL1" ON ("ADL1"."VENDOR" = "MSTR"."VENDOR"))
                 LEFT JOIN  ( SELECT "VEND_NO" AS "VENDOR",
			                       case when "BUY_PHONE"="PAY_PHONE" then
			                            case when length(TRIM("PAY_PHONE"))=10 then concat(substring("PAY_PHONE",1,3) , '-' ,  substring("PAY_PHONE",4,3)  , '-' ,  substring("PAY_PHONE",7,4))
											 else trim("PAY_PHONE") end
									else
			                            case when length(TRIM("BUY_PHONE"))=10 then
			                                 concat('BUY: ' , substring("BUY_PHONE",1,3) , '-' ,  substring("BUY_PHONE",4,3)  , '-' ,  substring("BUY_PHONE",7,4)   , '    PAYMENTS: ' , substring("PAY_PHONE",1,3) , '-' ,  substring("PAY_PHONE",4,3)  , '-' ,  substring("PAY_PHONE",7,4))
			                                 else
			                                 concat('BUY: ' , trim("BUY_PHONE") , '    PAYMENTS: ' , trim("PAY_PHONE"))
			                                 end
                           			end AS "PHONE"
                         FROM "gss_V_VEND_MSTR_ADDL"
                       ) AS "ADL2" ON ("ADL2"."VENDOR" = "MSTR"."VENDOR"))
                 LEFT JOIN  ( SELECT "VEND_NO" AS "VENDOR",
                       case when "BUY_FAX"="PAY_FAX" then
                            case when length(TRIM("PAY_FAX"))=10 then concat(substring("PAY_FAX",1,3) , '-' ,  substring("PAY_FAX",4,3)  , '-' ,  substring("PAY_FAX",7,4))
								 else "PAY_FAX" end
							else
                            case when length(TRIM("BUY_FAX"))=10 then
                                 concat('BUY: ' , substring("BUY_FAX",1,3) , '-' ,  substring("BUY_FAX",4,3)  , '-' ,  substring("BUY_FAX",7,4)   , '    PAYMENTS: ' , substring("PAY_FAX",1,3) , '-' ,  substring("PAY_FAX",4,3)  , '-' ,  substring("PAY_FAX",7,4))
                                 else
                                 concat('BUY: ' , "BUY_FAX" , '    PAYMENTS: ' , "PAY_FAX")
                                 end
                           end AS "FAX"
                         FROM "gss_V_VEND_MSTR_ADDL"
                       ) AS "ADL3" ON ("ADL3"."VENDOR" = "MSTR"."VENDOR"))
                 WHERE "MSTR"."VENDOR" <> '';

"""










#     vvvv                N E W       C O D E       B E L O W            vvvv

abandonedExtensionStuff ="""/*    case when Left(phone, 1) = "+" And Len(phone) = 11 Then              '+90 1234 5678'
        phone = Replace(phone, "+", "")
        PhoneFormat = "+" & Left(phone, 2) & " " & substring(phone, 3, 4) & " " & Right(phone, 4)
        case Length(ext) > 0 Then PhoneFormat = concat(PhoneFormat , " EXT " , ext )
        'Debug.Print PhoneFormat'
        'Exit Function'
    end */"""
  
phone = """	update "TABLE" set phone = replace(phone, '+', '');  
	update "TABLE" set phone = replace(phone, '(', '');  
	update "TABLE" set phone = replace(phone, ')', '');  
	update "TABLE" set phone = replace(phone, '-', '');  
	update "TABLE" set phone = replace(phone, ' ', '');
	update "TABLE" set phone = 
    case when Length(phone) = 10 Then                                       /* '(123) 456-7890'*/
        	concat( "(" , left(phone, 3) , ") " , substring(phone, 4, 3) , "-" , right(phone, 4))
    	when left(phone,3)="613" then
    	    concat( "(" , left(phone, 3) , ") " , substring(phone, 4, 3) , "-" , substring(phone,7, 4), right(phone,11))
    
    	when  Length(phone) = 12 Then                                    /* '0123 12 34 5678', '0123 12 34 5678 x90123' */
        	concat( "+" , left(phone, 4) , " " , substring(phone, 5, 4) , " " , right(phone, 4))
    	when Length(phone) = 14 then                                    /* '0123 4563 78 9012' */
        	concat( "+" & left(phone, 4) , " " , substring(phone, 3, 2) , " " , substring(phone, 6, 4) , "-" , right(phone, 4))
    	when Length(phone) > 4 then                                                           /*'01234567891'*/
        	concat(left(phone, Length(phone) - 4) , "-" , right(phone, 4))
    	else
        	phone
    	end;"""
ext = """    /*case when  Length(ext) > 0 Then concat(PhoneFormat ," EXT " , ext) end;*/"""


insertCustomers = """
UPDATE "gss_V_CUSTOMER_MASTER" set "COUNTRY" = 'United States' where "COUNTRY"='United State';


update "gss_V_CUSTOMER_MASTER" as "gss_cust" 
set "COUNTRY"=(	select "country_id" 
		from "res_country_state" as "rcs" 
		where "gss_cust"."STATE"="rcs"."code" 
		and "rcs"."country_id"<>254)
where "COUNTRY" is null;



INSERT INTO res_partner ("name", "street", "street2", "city", "state_id", "zip", "country_id",
				"comment", "is_company", "customer", "active", "company_id", "notify_email", "phone","create_date","color","use_parent_address","employee","type","lang","create_uid","write_date","write_uid","display_name","supplier","opt_out","vat_subjected"
)
SELECT TRIM("NAME_CUSTOMER") AS "NAME", 
	TRIM("ADDRESS1") AS "STREET", 
	TRIM("ADDRESS2") AS "STREET2", 
	TRIM("MSTR"."CITY") AS "CITY", 
	(select id from res_country_state as rcs where (rcs.code = TRIM("MSTR"."STATE")) limit 1) AS "STATE_id", 
	TRIM("ZIP") AS "ZIP", 
	(select id from res_country as rc where (rc."name" = INITCAP(TRIM("MSTR"."COUNTRY"))) limit 1) AS "COUNTRY_id",
        case when TRIM("ATTENTION")='' then ''
        	else concat('ATTENTION: ' , TRIM("ATTENTION"))
            end AS "COMMENT", 
	'TRUE' AS "IS_COMPANY" , 
	'TRUE' AS "CUSTOMER", 
	'TRUE' AS "ACTIVE",
	'1' AS "company_id",
	'always' as "notify_email",
        TRIM("MSTR"."TELEPHONE") AS "PHONE",
	now() as "create_date", 
	0 as "color", 
	'false' as "use_parent_address",
	'false' as "employee", 'contact' as "type", 'en_US' as "lang", '1' as "create_uid", 
	now() as  "write_date", '1' as write_uid, trim("NAME_CUSTOMER") as "display_name", 
	'false' as "supplier", 'false' as "opt_out", 
	case when INITCAP("MSTR"."COUNTRY")='France' then true
               	 when INITCAP("MSTR"."COUNTRY")='Ireland' then true
               	 when INITCAP("MSTR"."COUNTRY")='Germany' then true
               	 when INITCAP("MSTR"."COUNTRY")='Italy' then true
               	 when INITCAP("MSTR"."COUNTRY")='Netherlands' then true
        else false  end as "vat_subjected"
       FROM "gss_V_CUSTOMER_MASTER" AS "MSTR";
"""


