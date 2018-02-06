#subQuery_VENDOR_PHONE = """ ( SELECT VEND_NO AS VENDOR,
#                       IIF(BUY_PHONE=PAY_PHONE,
#                            IIF(LEN(TRIM(PAY_PHONE))=10,
#                                  MID(PAY_PHONE,1,3) & '-' &  MID(PAY_PHONE,4,3)  & '-' &  MID(PAY_PHONE,7,4),
#                                 PAY_PHONE),
#                            IIF(LEN(TRIM(PAY_PHONE))=10,
#                                 'BUY: ' & MID(BUY_PHONE,1,3) & '-' &  MID(BUY_PHONE,4,3)  & '-' &  MID(BUY_PHONE,7,4)   & '    PAYMENTS: ' & MID(PAY_PHONE,1,3) & '-' &  MID(PAY_PHONE,4,3)  & '-' &  MID(PAY_PHONE,7,4),
#                                 'BUY: ' & BUY_PHONE & '    PAYMENTS: ' & PAY_PHONE)
#                           ) AS PHONE 
#                         FROM gss_V_VEND_MSTR_ADDL 
#                       )"""
#                
#subQuery_VENDOR_FAX = """ ( SELECT VEND_NO AS VENDOR,
#                       IIF(BUY_FAX=PAY_FAX,
#                            IIF(LEN(TRIM(PAY_FAX))=10,
#                                  MID(PAY_FAX,1,3) & '-' &  MID(PAY_FAX,4,3)  & '-' &  MID(PAY_FAX,7,4),
#                                 PAY_FAX)," & vbCrLf & _
#                            IIF(LEN(TRIM(PAY_FAX))=10,
#                                 'BUY: ' & MID(BUY_FAX,1,3) & '-' &  MID(BUY_FAX,4,3)  & '-' &  MID(BUY_FAX,7,4)   & '    PAYMENTS: ' & MID(PAY_FAX,1,3) & '-' &  MID(PAY_FAX,4,3)  & '-' &  MID(PAY_FAX,7,4),
#                                 'BUY: ' & BUY_FAX & '    PAYMENTS: ' & PAY_FAX)
#                           ) AS FAX 
#                         FROM gss_V_VEND_MSTR_ADDL 
#                       )"""
#    
#    
#query_VENDOR_MASTER = """SELECT * INTO res_partner 
#                 FROM( SELECT TRIM(MSTR.VENDOR) AS EXTERNAL_ID, TRIM(NAME_VENDOR) AS NAME, TRIM(ADDRESS1) AS STREET, TRIM(ADDRESS2) AS STREET2, TRIM(MSTR.CITY) AS CITY, TRIM(MSTR.STATE) AS STATE, TRIM(CODE_ZIP) AS ZIP, strconv(TRIM(MSTR.COUNTRY),3) AS COUNTRY, 
#                 IIF( ATTENTION='','','ATTENTION: ' & ATTENTION ) AS COMMENT, 'TRUE' AS IS_COMPANY , 'TRUE' AS SUPPLIER, 'TRUE' AS ACTIVE, 
#                 TRIM(ADL1.EMAIL) AS EMAIL, 
#                 TRIM(ADL2.PHONE) AS PHONE, 
#                 TRIM(ADL3.FAX) AS FAX 
#                 FROM (((gss_V_VENDOR_MASTER AS MSTR
#                 LEFT JOIN gss_V_VENDOR_ADDL AS ADL1 ON (ADL1.VENDOR = MSTR.VENDOR))
#                 LEFT JOIN """ + subQuery_VENDOR_PHONE + """ AS ADL2 ON (ADL2.VENDOR = MSTR.VENDOR))
#                 LEFT JOIN """ + subQuery_VENDOR_FAX + """ AS ADL3 ON (ADL3.VENDOR = MSTR.VENDOR))
#                 WHERE MSTR.VENDOR <> '');"""



query_VENDOR_MASTER = """SELECT * INTO res_partner 
                 FROM(SELECT TRIM("MSTR"."VENDOR") AS "EXTERNAL_ID", TRIM("NAME_VENDOR") AS "NAME", TRIM("ADDRESS1") AS "STREET", TRIM("ADDRESS2") AS "STREET2", TRIM("MSTR"."CITY") AS "CITY", TRIM("MSTR"."STATE") AS "STATE", TRIM("CODE_ZIP") AS "ZIP", INITCAP(TRIM("MSTR"."COUNTRY")) AS "COUNTRY",
                 case when TRIM("ATTENTION")='' then ''
                      else concat('ATTENTION: ' , TRIM("ATTENTION")) 
                 end AS COMMENT, 'TRUE' AS "IS_COMPANY" , 'TRUE' AS "SUPPLIER", 'TRUE' AS "ACTIVE",
                 TRIM("ADL1"."EMAIL") AS "EMAIL",
                 TRIM("ADL2"."PHONE") AS "PHONE",
                 TRIM("ADL3"."FAX") AS "FAX"
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
                 WHERE "MSTR"."VENDOR" <> '') as outer;

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

