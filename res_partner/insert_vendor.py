subQuery_VENDOR_PHONE = """ ( SELECT VEND_NO AS VENDOR,
                       IIF(BUY_PHONE=PAY_PHONE,
                            IIF(LEN(TRIM(PAY_PHONE))=10,
                                  MID(PAY_PHONE,1,3) & '-' &  MID(PAY_PHONE,4,3)  & '-' &  MID(PAY_PHONE,7,4),
                                 PAY_PHONE),
                            IIF(LEN(TRIM(PAY_PHONE))=10,
                                 'BUY: ' & MID(BUY_PHONE,1,3) & '-' &  MID(BUY_PHONE,4,3)  & '-' &  MID(BUY_PHONE,7,4)   & '    PAYMENTS: ' & MID(PAY_PHONE,1,3) & '-' &  MID(PAY_PHONE,4,3)  & '-' &  MID(PAY_PHONE,7,4),
                                 'BUY: ' & BUY_PHONE & '    PAYMENTS: ' & PAY_PHONE)
                           ) AS PHONE 
                         FROM gss_V_VEND_MSTR_ADDL 
                       )"""
                
subQuery_VENDOR_FAX = """ ( SELECT VEND_NO AS VENDOR,
                       IIF(BUY_FAX=PAY_FAX,
                            IIF(LEN(TRIM(PAY_FAX))=10,
                                  MID(PAY_FAX,1,3) & '-' &  MID(PAY_FAX,4,3)  & '-' &  MID(PAY_FAX,7,4),
                                 PAY_FAX)," & vbCrLf & _
                            IIF(LEN(TRIM(PAY_FAX))=10,
                                 'BUY: ' & MID(BUY_FAX,1,3) & '-' &  MID(BUY_FAX,4,3)  & '-' &  MID(BUY_FAX,7,4)   & '    PAYMENTS: ' & MID(PAY_FAX,1,3) & '-' &  MID(PAY_FAX,4,3)  & '-' &  MID(PAY_FAX,7,4),
                                 'BUY: ' & BUY_FAX & '    PAYMENTS: ' & PAY_FAX)
                           ) AS FAX 
                         FROM gss_V_VEND_MSTR_ADDL 
                       )"""
    
    
query_VENDOR_MASTER = """SELECT * INTO res_partner 
                 FROM( SELECT TRIM(MSTR.VENDOR) AS EXTERNAL_ID, TRIM(NAME_VENDOR) AS NAME, TRIM(ADDRESS1) AS STREET, TRIM(ADDRESS2) AS STREET2, TRIM(MSTR.CITY) AS CITY, TRIM(MSTR.STATE) AS STATE, TRIM(CODE_ZIP) AS ZIP, strconv(TRIM(MSTR.COUNTRY),3) AS COUNTRY, 
                 IIF( ATTENTION='','','ATTENTION: ' & ATTENTION ) AS COMMENT, 'TRUE' AS IS_COMPANY , 'TRUE' AS SUPPLIER, 'TRUE' AS ACTIVE, 
                 TRIM(ADL1.EMAIL) AS EMAIL, 
                 TRIM(ADL2.PHONE) AS PHONE, 
                 TRIM(ADL3.FAX) AS FAX 
                 FROM (((gss_V_VENDOR_MASTER AS MSTR
                 LEFT JOIN gss_V_VENDOR_ADDL AS ADL1 ON (ADL1.VENDOR = MSTR.VENDOR))
                 LEFT JOIN """ + subQuery_VENDOR_PHONE + """ AS ADL2 ON (ADL2.VENDOR = MSTR.VENDOR))
                 LEFT JOIN """ + subQuery_VENDOR_FAX + """ AS ADL3 ON (ADL3.VENDOR = MSTR.VENDOR))
                 WHERE MSTR.VENDOR <> '');"""

