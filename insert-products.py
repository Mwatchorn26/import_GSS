

#Prepare PROCURE_METHOD AND SUPPLY_METHOD
queryPJFM = """UPDATE gss_V_INVENTORY_MASTER ("PROCURE_METHOD", "SUPPLY_METHOD")
               VALUES CASE WHEN INV2."CODE_SOURCE"='P' THEN 'Purchase To Stock'
                           WHEN INV2."CODE_SOURCE"='J' THEN 'Purchase To Order'
                       	   WHEN INV2."CODE_SOURCE"='F' THEN 'Make To Order'
                           WHEN INV2."CODE_SOURCE"='M' THEN 'Make To Stock'
                      END AS "PROCURE_METHOD",
                      CASE WHEN INV2."CODE_SOURCE"='P' THEN 'Buy'
                           WHEN INV2."CODE_SOURCE"='J' THEN 'Buy'
                           WHEN INV2."CODE_SOURCE"='F' THEN 'Manufacture'
                           WHEN INV2."CODE_SOURCE"='M' THEN 'Manufacture' 
                      END AS "SUPPLY_METHOD"
		;"""

#Prepare Flag_Lot
strLot = """  CASE WHEN FLAG_LOT='Y' THEN 'True' 
                   ELSE 'False' END AS TRACK_INCOMING,
              CASE WHEN FLAG_LOT='Y' THEN 'True' 
                   ELSE 'False' AS TRACK_PRODUCTION,
              CASE WHEN FLAG_LOT='Y','True' 
                   ELSE 'False' as TRACK_OUTGOING,"""


#Prepare all the other fields
strOtherFields = """  CASE WHEN "PRODUCT_LINE"='ZA' THEN 'Consumable'
                           ELSE 'Stockable'
                      END  AS TYPE,
                      'Unit(s)' AS UOM_PO_ID,
                      'Unit(s)' AS UOM_ID,
                       "QTY_ONHAND" AS "QTY_AVAILABLE",
                 ;"""

#Assemble the full query using the blocks from above to limit the number of multi-line sections use. (VBA has a limit)
sqlProductTemplate_PARTIAL = """INSERT INTO product_product 
                  FROM (   SELECT 'True' as ACTIVE, 'False' AS PURCHASE_OK, 'False' AS RENTAL, 'True' AS SALE_OK, 
                           INV.PART AS DEFAULT_CODE, 
                           INV.DESCRIPTION AS NAME,
                """
                            & strOtherFields &
                            & strLot &
                            & strPJFM & 
                """        '' AS UM_PURCHASING, 'Unit(s)' AS UM_INVENTORY, '' AS VENDOR, TRIM(INV.AMT_COST) AS INV_COST, CDATE(TRIM(INV.DATE_LAST_CHG)) AS DATE_LAST_RECEIVED, CDATE(TRIM(INV.DATE_LAST_CHG)) AS DATE_ORDER
                           
                           FROM (gss_V_INVENTORY_MSTR AS INV 
                           LEFT JOIN gss_V_INVENTORY_MST2 AS INV2 ON (INV.PART = INV2.PART AND INV.LOCATION = INV2.LOCATION))
                           WHERE INV2.CODE_SOURCE IN ('F','M')
                       );"""



strTravelExpensesList = """Snack, Food, Meal, Dinner, Supper, Lunch, Breakfast, Car, Car Rental, Gas, Gasoline, Fair, Toll, Hotel, Train, Taxi, Airplane, Flight"""





sqlInsertProductTemplate = """INSERT INTO "product_template" VALUES (
	warranty float8 NULL,
	uos_id int4 NULL,
	list_price numeric NULL,
	weight numeric NULL,
	color int4 NULL,
	image bytea NULL,
	write_uid int4 NULL,
	mes_type varchar NULL,
	uom_id int4 NOT NULL,
	description_purchase text NULL,
	create_date timestamp NULL,
	uos_coeff numeric NULL,
	create_uid int4 NULL,
	rental bool NULL,
	product_manager int4 NULL,
	message_last_post timestamp NULL,
	company_id int4 NULL,
	state varchar NULL,
	uom_po_id int4 NOT NULL,
	"type" varchar NOT NULL,
	description text NULL,
	weight_net numeric NULL,
	volume float8 NULL,
	write_date timestamp NULL,
	active bool NULL,
	categ_id int4 NOT NULL,
	sale_ok bool NULL,
	image_medium bytea NULL,
	"name" varchar NOT NULL,
	description_sale text NULL,
	image_small bytea NULL,
	loc_row varchar(16) NULL,
	loc_rack varchar(16) NULL,
	track_incoming bool NULL,
	sale_delay float8 NULL,
	track_all bool NULL,
	track_outgoing bool NULL,
	loc_case varchar(16) NULL,
	purchase_ok bool NULL,
	track_production bool NULL,
	produce_delay float8 NULL,
	hr_expense_ok bool NULL,
VALUES (
);"""


sqlInsertProductProduct="""INSERT INTO product_product (
	id serial NOT NULL,
	create_uid int4 NULL,
	create_date timestamp NULL,
	ean13 varchar(13) NULL,
	write_uid int4 NULL,
	message_last_post timestamp NULL,
	default_code varchar NULL,
	write_date timestamp NULL,
	name_template varchar NULL,
	active bool NULL,
	product_tmpl_id int4 NOT NULL,
	image_variant bytea NULL,









