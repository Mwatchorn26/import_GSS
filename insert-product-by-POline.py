
    'Prepare Procurement and Supply Methods:
    strPJFM = "  SWITCH(LN.RECV_TO_JOB<>'Y', 'Purchase To Stock'," & vbCrLf & _
              "         LN.RECV_TO_JOB='Y', 'Purchase To Order') AS PROCURE_METHOD, " & vbCrLf & _
              "  'Buy' AS SUPPLY_METHOD, "


    'Prepare Flag_Lot
    strLot = "  IIF(FLAG_LOT='Y','True','False') as TRACK_INCOMING, " & vbCrLf & _
             "  IIF(FLAG_LOT='Y','True','False') as TRACK_PRODUCTION, " & vbCrLf & _
             "  IIF(FLAG_LOT='Y','True','False') as TRACK_OUTGOING, "

'* * * * * * * *
'  THERE IS MUCH MORE WORK TO BE DONE ON THE PRODUCT LINE SHOWN BELOW
'* * * * * * * *

    'Prepare all the other fields
    strOtherFields = """CASE WHEN LN."PRODUCT_LINE"='ZA','Consumable','Stockable') AS TYPE, 
                     CASE WHEN LN."UM_PURCHASING" = 'BX' THEN 'Box(s)' 
                                 LN."UM_PURCHASING" = 'EA' THEN 'Unit(s)'
                                 LN."UM_PURCHASING" = 'IN' THEN 'IN'  
                                 LN."UM_PURCHASING" = 'PK' THEN 'Box(s)'
                                 LN."UM_PURCHASING" = 'SI' THEN 'SI'   
                                 LN."UM_PURCHASING" = 'MT' THEN 'm' 
                     END AS "UOM_PO_ID", 
                     CASE WHEN   LN."UM_INVENTORY"  = 'BX' THEN 'Box(s)' 
                                 LN."UM_INVENTORY"  = 'EA' THEN 'Unit(s)'
                                 LN."UM_INVENTORY"  = 'IN' THEN 'IN'     
                                 LN."UM_INVENTORY"  = 'PK' THEN 'Box(s)' 
                                 LN."UM_INVENTORY"  = 'SI' THEN 'SI'     
                                 LN."UM_INVENTORY"  = 'MT' THEN 'm' 
                      END AS "UOM_ID",
                     TRIM(INV."QTY_ONHAND") AS QTY_AVAILABLE, """
                     
    strFrom = "           FROM ((((gss_V_PO_LINES AS LN " & vbCrLf & _
                "           LEFT JOIN gss_V_PO_HEADER AS HDR ON (LN.PURCHASE_ORDER = HDR.PURCHASE_ORDER)) " & vbCrLf & _
                "           LEFT JOIN gss_V_INVENTORY_MSTR AS INV ON (LN.PURCHASE_ORDER = INV.PART AND INV.LOCATION=''))" & vbCrLf & _
                "           LEFT JOIN gss_V_INVENTORY_MST2 AS INV2 ON (INV.PART = INV2.PART AND INV.LOCATION = INV2.LOCATION))" & vbCrLf & _
                "           INNER JOIN (SELECT DISTINCT MAX(G1.PURCHASE_ORDER) AS PURCHASE_ORDER, MAX(G1.RECORD_NO) AS RECORD_NO, G1.PART, MAX(G1.INV_COST) AS INV_COST, MAX(G1.DATE_LAST_RECEIVED) AS DATE_LAST_RECEIVED" & vbCrLf & _
                "                       FROM gss_V_PO_LINES AS G1" & vbCrLf & _
                "                       GROUP BY PART) AS UNIQ ON (UNIQ.PURCHASE_ORDER = LN.PURCHASE_ORDER " & vbCrLf & _
                "                                                                            AND UNIQ.RECORD_NO = LN.RECORD_NO " & vbCrLf & _
                "                                                                            AND UNIQ.PART = LN.PART))"

                     

'                "UNIQ.PURCHASE_ORDER AS UNIQ_PO, LN.PURCHASE_ORDER AS LN_PO, " & vbCrLf & _
'                "UNIQ.RECORD_NO AS UNIQ_LINE , LN.RECORD_NO AS LN_LINE, " & vbCrLf & _
    'Assemble the full query using the blocks from above to limit the number of multi-line sections use. (VBA has a limit)
    sqlString = "SELECT * INTO odoo_product_product_polines " & vbCrLf & _
                "  FROM (   SELECT DISTINCT 'True' as ACTIVE, 'True' AS PURCHASE_OK, 'False' AS RENTAL, 'True' AS SALE_OK, " & vbCrLf & _
                "           UCASE(TRIM(LN.PART)) AS DEFAULT_CODE, " & vbCrLf & _
                "           STRCONV(TRIM(LN.DESCRIPTION),3) AS NAME," & vbCrLf & _
                            strOtherFields & vbCrLf & _
                            strLot & vbCrLf & _
                            strPJFM & vbCrLf & _
                "           TRIM(LN.UM_PURCHASING) AS UM_PURCHASING, TRIM(LN.UM_INVENTORY) AS UM_INVENTORY, TRIM(LN.VENDOR) AS VENDOR, TRIM(LN.INV_COST) AS INV_COST, CDATE(TRIM(LN.DATE_LAST_RECEIVED)) AS DATE_LAST_RECEIVED, CDATE(TRIM(HDR.DATE_ORDER)) AS DATE_ORDER" & vbCrLf & _
                            strFrom & vbCrLf & _
                "           WHERE LN.PART NOT LIKE '???-?????-??*' " & vbCrLf & _
                "           AND HDR.DATE_ORDER > #2014-01-01#" & vbCrLf & _
                "       );"


