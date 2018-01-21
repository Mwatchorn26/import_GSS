
create_gss_tables = """CREATE TABLE public."gss_ANALYTIC_ACCOUNTS" (
	"EXTERNAL_ID" text NULL,
	"AA" text NULL,
	"PROJECT" text NULL,
	"PRJ_DESCR" text NULL,
	"PHASE_DESCR" text NULL,
	"PHASE" text NULL,
	"DATE_CREATED" timestamptz NULL,
	"JOB" text NULL,
	"SUFFIX" text NULL,
	"HDR_PHASE" text NULL,
	"PART" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_BALANCING_GROUP" (
	"BAL_GROUP" text NULL,
	"TYPE" text NULL,
	"DESCR" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_BOM_MSTR" (
	"PARENT" text NULL,
	"SEQUENCE_BOM" text NULL,
	"INSERT_BOM" text NULL,
	"DATE_MAINTENANCE" timestamptz NULL,
	"COST" float8 NULL,
	"QUANTITY" float8 NULL,
	"PART" text NULL,
	"DATE_START" timestamptz NULL,
	"DATE_STOP" timestamptz NULL,
	"BM_SERIAL_START" text NULL,
	"BM_SERIAL_STOP" text NULL,
	"UM_INVENTORY" text NULL,
	"PURGE_FLAG" text NULL,
	"ORDR_USR_FLAG" text NULL,
	"QUANTITY_6" float8 NULL,
	"DRAWING" text NULL,
	"TAG" text NULL,
	"CATEGORY" text NULL,
	"SOURCE" text NULL,
	"FREQUENCY" float8 NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"TIME_LAST_CHG" timestamptz NULL,
	"LAST_CHG_BY" text NULL,
	"LAST_CHG_PROG" text NULL,
	"DRAWING_SIZE" text NULL,
	"REQ_TRACE" text NULL,
	"COST_DATE" timestamptz NULL,
	"BOM_COMPLETE" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_BOM_TEXT" (
	"PARENT" text NULL,
	"PARENT_SEQ" text NULL,
	"PARENT_INS" int4 NULL,
	"BOM_SEQ" text NULL,
	"PART" text NULL,
	"TEXT" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_CUSTOMER_MASTER" (
	"CUSTOMER" text NULL,
	"REC" text NULL,
	"NAME_CUSTOMER" text NULL,
	"ADDRESS1" text NULL,
	"ADDRESS2" text NULL,
	"CITY" text NULL,
	"STATE" text NULL,
	"ZIP" text NULL,
	"COUNTRY" text NULL,
	"COUNTY" text NULL,
	"ATTENTION" text NULL,
	"SALESPERSON" text NULL,
	"INTL_ADDR" text NULL,
	"TERRITORY" text NULL,
	"CODE_AREA" text NULL,
	"CREDIT" text NULL,
	"TELEPHONE" text NULL,
	"TAX_CODE1" text NULL,
	"NORMAL_GL_ACCOUNT" text NULL,
	"FLAG_CREDIT_HOLD" text NULL,
	"TAX_STATE" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_DEPARTMENTS" (
	"DEPT_ID" text NULL,
	"DEPT_NAME" text NULL,
	"LAST_DATE_CHG" timestamptz NULL,
	"LAST_TIME_CHG" timestamptz NULL,
	"LAST_USER_CHG" text NULL,
	"PUBLIC_HR_DEPTARTMENT_ID" text NULL,
	"LAST_PRGM_CHG" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_EMPLOYEES" (
	"EMPLOYEE" int4 NULL,
	"ADDRESS" text NULL,
	"NAME" text NULL,
	"CITY" text NULL,
	"PHONE" text NULL,
	"STATE" text NULL,
	"ZIP_CODE" text NULL,
	"BIRTHDATE" timestamptz NULL,
	"ACTIVE" int4 NULL,
	"SEX" text NULL,
	"DATE_HIRE" timestamptz NULL,
	"DATE_TERMINATION" timestamptz NULL,
	"DEPT_EMPLOYEE" text NULL,
	"MARITAL_STATUS" text NULL,
	"RATE" float8 NULL,
	"SHIFT" int4 NULL,
	"EMPL_INITIALS" text NULL,
	"PR_USER_ID" text NULL,
	"PR_BALANCE_GROUP" text NULL,
	"FIRST_NAME" text NULL,
	"MIDDLE_NAME" text NULL,
	"LAST_NAME" text NULL,
	"EMAIL" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_INVENTORY_MST2" (
	"PART" text NULL,
	"LOCATION" text NULL,
	"QTY_MAXIMUM" int4 NULL,
	"HRS_STANDARD" float8 NULL,
	"LBS" float8 NULL,
	"CODE_SOURCE" text NULL,
	"NAME_VENDOR" text NULL,
	"TEXT_INFO1" text NULL,
	"TEXT_INFO2" text NULL,
	"DESCRIPTION_2" text NULL,
	"DESCRIPTION_3" text NULL,
	"AMT_COST_1" float8 NULL,
	"AMT_COST_2" float8 NULL,
	"AMT_COST_3" float8 NULL,
	"DATE_CYCLE" timestamptz NULL,
	"LIFO_BASE" float8 NULL,
	"SIX_DECIMAL_COST" float8 NULL,
	"WT_PER_FOOT" float8 NULL,
	"CUTTING_CHARGE" float8 NULL,
	"SHP_CNV_FACTOR" float8 NULL,
	"SHIP_UM" text NULL,
	"LENGTH" float8 NULL,
	"WIDTH" float8 NULL,
	"WARRANTY_TYPE" text NULL,
	"PROP_CODE" text NULL,
	"REQUIRES_INSP" text NULL,
	"BASE_PART" text NULL,
	"PRICE_CATG" text NULL,
	"ISSUE_UM" text NULL,
	"PART_PRICE_CODE" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_INVENTORY_MSTR" (
	"PART" text NULL,
	"LOCATION" text NULL,
	"CODE_ABC" text NULL,
	"PRODUCT_LINE" text NULL,
	"BIN" text NULL,
	"DESCRIPTION" text NULL,
	"UM_PURCHASING" text NULL,
	"UM_INVENTORY" text NULL,
	"FACTOR_CONVERSION" float8 NULL,
	"QTY_ORDER" float8 NULL,
	"QTY_SAFETY" float8 NULL,
	"QTY_ONHAND" float8 NULL,
	"QTY_REORDER" float8 NULL,
	"QTY_ONORDER_PO" float8 NULL,
	"QTY_ONORDER_WO" float8 NULL,
	"QTY_REQUIRED" float8 NULL,
	"AMT_COST" float8 NULL,
	"AMT_ALT_COST" float8 NULL,
	"PRIOR_USAGE" float8 NULL,
	"DATE_LAST_USAGE" timestamptz NULL,
	"AMT_PRICE" float8 NULL,
	"OBSOLETE_FLAG" text NULL,
	"CODE_BOM" text NULL,
	"CODE_TOTAL" text NULL,
	"CODE_SORT" text NULL,
	"QTY_LAST_ONHAND" float8 NULL,
	"AMT_LAST_COST" float8 NULL,
	"FLAG_LOT" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_JOB_COMMITMENTS" (
	"PART" text NULL,
	"LOCATION" text NULL,
	"JOB" text NULL,
	"SUFFIX" text NULL,
	"DATE_COMMITMENT" timestamptz NULL,
	"SEQUENCE" text NULL,
	"CUSTOMER" text NULL,
	"QTY_COMMITTED" float8 NULL,
	"DATE_ISSUED" text NULL,
	"QTY_ISSUED" float8 NULL,
	"DATE_DUE" timestamptz NULL,
	"UNIT_COST" float8 NULL,
	"CLOSED" text NULL,
	"JOB_PARENT" text NULL,
	"FLAG_SHORT" text NULL,
	"START_DATE" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_JOB_DETAIL" (
	"JOB" text NULL,
	"SUFFIX" text NULL,
	"SEQ" text NULL,
	"DATE_SEQUENCE" timestamptz NULL,
	"SEQUENCE_KEY" text NULL,
	"EMPLOYEE" text NULL,
	"DESCRIPTION" text NULL,
	"DEPT_WORKCENTER" text NULL,
	"RATE_WORKCENTER" float8 NULL,
	"DEPT_EMP" text NULL,
	"RATE_EMPLOYEE" float8 NULL,
	"TRAN" float8 NULL,
	"IDENTIFIER" text NULL,
	"EMPL" text NULL,
	"MACHINE" text NULL,
	"PART" text NULL,
	"HOURS_WORKED" float8 NULL,
	"FLAG_OPT" text NULL,
	"PIECES_SCRAP" float8 NULL,
	"PIECES_COMPLTD" float8 NULL,
	"AMOUNT_LABOR" float8 NULL,
	"AMT_OVERHEAD" float8 NULL,
	"AMT_STANDARD" float8 NULL,
	"REFERENCE" text NULL,
	"FLAG_CLOSED" text NULL,
	"UM" text NULL,
	"FLAG_INDIRECT" text NULL,
	"LMO" text NULL,
	"RATE_TYPE" text NULL,
	"AMT_SCRAP" float8 NULL,
	"LOCATION" text NULL,
	"QTY_COMMITTED" float8 NULL,
	"AMT_COMMITTED" float8 NULL,
	"LINE_BILLED" text NULL,
	"BILL_DATE" timestamptz NULL,
	"QUALITY_NUMBER" text NULL,
	"DTL_TYPE_FLAG" text NULL,
	"EDITED_WO_DTL" text NULL,
	"START_MIN" float8 NULL,
	"END_MIN" float8 NULL,
	"SCRAP_REASON" text NULL,
	"CREW_ID" text NULL,
	"MACHINE_HRS" float8 NULL,
	"TYPE_TIME" text NULL,
	"BALANCED_AS_DATE" timestamptz NULL,
	"MULTIPLE_FLAG" text NULL,
	"CHARGE_DATE" timestamptz NULL,
	"LUNCH_TAKEN" text NULL,
	"MULTIPLE_FRACTION" float8 NULL,
	"START_TIME" text NULL,
	"END_TIME" text NULL,
	"DATE_OUT" timestamptz NULL,
	"RATE_SCALE" text NULL,
	"SHIFT_SHIFT" text NULL,
	"SHIFT_DEPT" text NULL,
	"SHIFT_GROUP" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_JOB_HEADER" (
	"JOB" text NULL,
	"SUFFIX" text NULL,
	"PART" text NULL,
	"LOCATION" text NULL,
	"PRODUCT_LINE" text NULL,
	"ROUTER" text NULL,
	"PRIORITY" text NULL,
	"DESCRIPTION" text NULL,
	"CUSTOMER" text NULL,
	"SALESPERSON_OLD" text NULL,
	"CUSTOMER_PO" text NULL,
	"QTY_ORDER" float8 NULL,
	"QTY_COMPLETED" float8 NULL,
	"DATE_OPENED" timestamptz NULL,
	"DATE_DUE" timestamptz NULL,
	"DATE_CLOSED" timestamptz NULL,
	"DATE_START" timestamptz NULL,
	"DATE_SCH_CMPL_INF" timestamptz NULL,
	"DATE_SCH_CMPL_FIN" timestamptz NULL,
	"DATE_LAST_SCH_INF" timestamptz NULL,
	"DATE_ORIG_DUE" timestamptz NULL,
	"AMT_PRICE_PER_UNIT" float8 NULL,
	"AMT_SALES" float8 NULL,
	"AMT_MATERIAL" float8 NULL,
	"NUM_HOURS" float8 NULL,
	"AMT_LABOR" float8 NULL,
	"AMT_OVERHEAD" float8 NULL,
	"COMMENTS_1" text NULL,
	"COMMENTS_2" text NULL,
	"FLAG_PURGE" text NULL,
	"PART_CUSTOMER" text NULL,
	"DRAWING_CUSTOMER" text NULL,
	"AMT_PARTIAL_SHPMNT" float8 NULL,
	"CODE_SORT" text NULL,
	"CODE_SORT_OTHER" text NULL,
	"DATE_START_OTHER" timestamptz NULL,
	"HOUR_START" float8 NULL,
	"SYSTEM_PRIORITY" float8 NULL,
	"USER_SCHEDULE" text NULL,
	"AMT_BILLED_DATE" float8 NULL,
	"UNITS_BILLED_DATE" float8 NULL,
	"DATE_SHIP_1" timestamptz NULL,
	"DATE_SHIP_2" timestamptz NULL,
	"QTY_SHIP_1" float8 NULL,
	"QTY_SHIP_2" float8 NULL,
	"DATE_LAST_SCH_FIN" timestamptz NULL,
	"BIN" text NULL,
	"DATE_DUE_NEW" timestamptz NULL,
	"COMMENTS_3" text NULL,
	"DATE_MATL_ORDER" timestamptz NULL,
	"PARTIAL_MATERIAL" float8 NULL,
	"PARTIAL_LABOR" float8 NULL,
	"PARTIAL_OVERHEAD" float8 NULL,
	"FLAG_HOLD" text NULL,
	"SCH_GRP" text NULL,
	"PARENT_WO" text NULL,
	"PARENT_SUFFIX_PARENT" text NULL,
	"DATE_RELEASED" timestamptz NULL,
	"PART_DESCRIPTION" text NULL,
	"SALES_ORDER" text NULL,
	"SALES_ORDER_LINE" text NULL,
	"OUTS" float8 NULL,
	"PARTIAL_OUTSIDE" float8 NULL,
	"SCHEDULED_DUE_DATE" timestamptz NULL,
	"PROJECT" text NULL,
	"LOT_TO_LOT" text NULL,
	"PHASE" text NULL,
	"JOB_TYPE" text NULL,
	"PROCESS_GRP" text NULL,
	"SHIPD_FLG" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_OP_CODES" (
	"LMO" text NULL,
	machine text NULL,
	"OPERATION" text NULL,
	"DESCRIPTION" text NULL,
	"STANDARD_SETUP" float8 NULL,
	"STANDARD_RUNTIME" float8 NULL,
	"UNIT_MEASURE" text NULL,
	"FREQUENCY" float8 NULL,
	"MULTIPLE" float8 NULL,
	"RATE" float8 NULL,
	"OVERLAP" float8 NULL,
	"WC_FACTOR" float8 NULL,
	"CONVER_FACTOR" float8 NULL,
	"STD_LEAD_TIME" float8 NULL,
	"CREW_SIZE" int4 NULL,
	"PROJ_GROUP" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_ORDER_HEADER" (
	"ORDER_NO" text NULL,
	"RECORD_NO" text NULL,
	"ORDER_SHIP_ID" text NULL,
	"RECORD_TYPE" text NULL,
	"CUSTOMER" text NULL,
	"SHIP_ID" text NULL,
	"INVOICE" text NULL,
	"DATE_ORDER" timestamptz NULL,
	"DATE_DUE" timestamptz NULL,
	"INSURANCE" text NULL,
	"ORDER_TYPE" text NULL,
	"ORDER_SUFFIX" text NULL,
	"CUSTOMER_PO" text NULL,
	"MARK_INFO" text NULL,
	"CODE_FOB" text NULL,
	"TERMS" text NULL,
	"WAY_BILL" text NULL,
	"LAST_REC_NO" float8 NULL,
	"DATE_SHIPPED" timestamptz NULL,
	"FLAG_PRINT" text NULL,
	"CODE_SORT" text NULL,
	"FLAG_SHIPPED" text NULL,
	"TRANS_METHOD" text NULL,
	"CERT_ENCL" text NULL,
	"EXPIRATION" text NULL,
	"FLAG_NO_BACKORDER" text NULL,
	"SALESPERSON" text NULL,
	"BRANCH" text NULL,
	"AREA" text NULL,
	"FREIGHT_ZONE" text NULL,
	"SHIP_VIA" text NULL,
	"ORDER_DISCOUNT" float8 NULL,
	"PRICE_CLASS" text NULL,
	"PRICE_CLASS_DISC" float8 NULL,
	"TYPE_COMMISSION" text NULL,
	"GL_ACCOUNT" text NULL,
	"TAX_SOURCE" text NULL,
	"TAX_STATE" text NULL,
	"TAX_ZIP" text NULL,
	"TAX_GEO_CODE" text NULL,
	"TAX_1" text NULL,
	"TAX_2" text NULL,
	"TAX_APPLY_1" text NULL,
	"TAX_APPLY_2" text NULL,
	"CONTRACT" float8 NULL,
	"ORDER_SORT_2" text NULL,
	"QUOTE" text NULL,
	"FLAG_TIME_MATL" text NULL,
	"ORDER_LOCATION" text NULL,
	"FLAG_IN_PROCESS" text NULL,
	"FLAG_PL_TYPE" text NULL,
	"PRICE_CATEGORY" text NULL,
	"COMPANY_CURRENCY" text NULL,
	"CATALOG_CURRENCY" text NULL,
	"ORDER_CURRENCY" text NULL,
	"DATE_EXCH_FO_TC" timestamptz NULL,
	"EXCH_RATE_FO_TC" float8 NULL,
	"DATE_EXCH_FC_TO" timestamptz NULL,
	"EXCH_RATE_FC_TO" float8 NULL,
	"DATE_EXCH_FL_TO" timestamptz NULL,
	"EXCH_RATE_FL_TO" float8 NULL,
	"DATE_EXCH_FL_TC" timestamptz NULL,
	"EXCH_RATE_FL_TC" float8 NULL,
	"PAYMENT_TYPE" text NULL,
	"PREPAID_INVOICE" text NULL,
	"BLANKET_NO" text NULL,
	"TRACKING_NO" text NULL,
	"TRACKING_FLAG" text NULL,
	"ETA_DATE" timestamptz NULL,
	"CARTONS" int4 NULL,
	"WEIGHT" float8 NULL,
	"COMPLETE_SHIP" text NULL,
	"PROJECT" text NULL,
	"CARRIER_ACCT" text NULL,
	"CARRIER_CD" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_ORDER_LINES" (
	"ORDER_NO" text NULL,
	"RECORD_NO" text NULL,
	"ORDER_SHIP_ID" text NULL,
	"RECORD_TYPE" text NULL,
	"CUSTOMER" text NULL,
	"LINE_TYPE" text NULL,
	"QTY_ORDER" float8 NULL,
	"QTY_SHIPPED" float8 NULL,
	"QTY_BO" float8 NULL,
	"WEIGHT" float8 NULL,
	"UM_ORDER" text NULL,
	"PART" text NULL,
	"ORDER_WON" text NULL,
	"PRICE" float8 NULL,
	"COST" float8 NULL,
	"UM_INVENTORY" text NULL,
	"DATE_SHIP" timestamptz NULL,
	"CODE_SORT" text NULL,
	"FLAG_SO_TO_WO" text NULL,
	"DESCRIPTION" text NULL,
	"FLAG_BILLING_PRICE" text NULL,
	"PRICE_CODE" text NULL,
	"FLAG_USE_MQD" text NULL,
	"GL_ACCOUNT" int4 NULL,
	"TAX_SOURCE" text NULL,
	"TAX_STATE" text NULL,
	"TAX_ZIP" text NULL,
	"TAX_1" text NULL,
	"TAX_APPLY_1" text NULL,
	"ORIG_ORDER_LINE" int4 NULL,
	"SO_LINE" text NULL,
	"QTY_ORIGINAL" float8 NULL,
	"DATE_ORDER" timestamptz NULL,
	"DATE_ITEM_PROM" timestamptz NULL,
	"ITEM_PROMISE_DT" timestamptz NULL,
	"FLAG_COGS" text NULL,
	"FLAG_TAX_STATUS" text NULL,
	"CUSTOMER_PART" text NULL,
	"INFO_2" text NULL,
	"FLAG_PURCHASED" text NULL,
	"ORDER_CURR_CD" text NULL,
	"EXTENSION" float8 NULL,
	"MARGIN" float8 NULL,
	"FLAG_BOM" text NULL,
	"BOM_PARENT" text NULL,
	"PRODUCT_LINE" text NULL,
	"LIKELY_TO_WIN" text NULL,
	"DISCOUNT_PRICE" text NULL,
	"PRICE_ORDER" float8 NULL,
	"PRICE_DISC_ORD" float8 NULL,
	"EXTENSION_ORDER" float8 NULL,
	"DD250_CLIN_NO" int4 NULL,
	"LOTBIN_FLG" text NULL,
	"APPLY_MATL_SCHRG" text NULL,
	"PRICE_BOM_COMP_FLG" text NULL,
	"FLAG_ALWAYS_DISCOUNT" text NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"LAST_CHG_BY" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_ORDER_TEXT" (
	"ORDER_NO" text NULL,
	"ORDER_SUFFIX" text NULL,
	"LINE_CHAR_3" text NULL,
	"ORDER_LINE" text NULL,
	"FLAG_SALES_ORDER" text NULL,
	"FLAG_PACK_LIST" text NULL,
	"FLAG_INVOICE" text NULL,
	"FLAG_QUOTE" text NULL,
	"TEXT_SEQ" text NULL,
	"TEXT" text NULL,
	"TEXT_TYPE" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_PO_HEADER" (
	"PURCHASE_ORDER" text NULL,
	"ORDER_TAX" text NULL,
	"FLAG_INSURANCE" text NULL,
	"BUYER" text NULL,
	"SHIP_VIA" text NULL,
	"CODE_FOB" text NULL,
	"TERMS" text NULL,
	"JOB" text NULL,
	"SEQUENCE" text NULL,
	"FLAG_RECV_CLOSED" text NULL,
	"CODE_SORT" text NULL,
	"DATE_ORDER" timestamptz NULL,
	"DATE_REQ" timestamptz NULL,
	"DATE_DUE" timestamptz NULL,
	"GL_ACCOUNT" text NULL,
	"FLAG_ACCT_CLOSE_A" text NULL,
	"SB_PAID" float8 NULL,
	"FLAG_PRINT" text NULL,
	"SUFFIX" text NULL,
	"PO_SEQ" text NULL,
	"VENDOR" text NULL,
	"FLAG_CERTS_REQD" text NULL,
	"PREV_SEQ" text NULL,
	"CHANGE_DATE" timestamptz NULL,
	"DIFF_DUE_DATE" text NULL,
	"PHYS_CHEM" text NULL,
	"SHIP_DATE" timestamptz NULL,
	"PAY_WITH_CCARD" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_PO_LINES" (
	"PURCHASE_ORDER" text NULL,
	"RECORD_NO" text NULL,
	"PO_TYPE" text NULL,
	"PART" text NULL,
	"LOCATION" text NULL,
	"DESCRIPTION" text NULL,
	"UM_PURCHASING" text NULL,
	"FLAG_ACCT_CLOSED" text NULL,
	"JOB" text NULL,
	"SEQUENCE" text NULL,
	"REQUISITION_NO" text NULL,
	"CODE_ITEM_SORT" text NULL,
	"GL_ACCOUNT_LINE" int4 NULL,
	"PRODUCT_LINE" text NULL,
	"DATE_DUE_LINE" timestamptz NULL,
	"DATE_LAST_RECEIVED" timestamptz NULL,
	"COST" float8 NULL,
	"QTY_ORDER" float8 NULL,
	"QTY_RECEIVED" float8 NULL,
	"QTY_REJECT" float8 NULL,
	"EXTENSION" float8 NULL,
	"QTY_RECV_ALT" float8 NULL,
	"FLAG_RECV_CLOSE" text NULL,
	"SUFFIX" text NULL,
	"PART_MFG_NO" text NULL,
	"MGF_NAME" text NULL,
	"QTY_ALT_ORDER" float8 NULL,
	"UM_INVENTORY" text NULL,
	"VENDOR" text NULL,
	"EXCHANGE_CURR" text NULL,
	"EXCHANGE_EXT" float8 NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"CHANGED_BY" text NULL,
	"DUE_DATE_L" timestamptz NULL,
	"DATE_EXCHANGE" timestamptz NULL,
	"EXCHANGE_COST2" float8 NULL,
	"EXCHANGE_RATE" float8 NULL,
	"COST_6_DEC" float8 NULL,
	"REQUISITION_LINE" int4 NULL,
	"ORIG_DUE_DATE" timestamptz NULL,
	"SHIP_DATE_L" timestamptz NULL,
	"COST_SOURCE" text NULL,
	"INV_COST" float8 NULL,
	"RECV_TO_JOB" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_PO_RECEIVER" (
	"RECEIVER_NO" text NULL,
	"PURCHASE_ORDER" text NULL,
	"PO_LINE" text NULL,
	"PO_LINE4" text NULL,
	"DATE_RECEIVED" timestamptz NULL,
	"PART" text NULL,
	"LOCATION" text NULL,
	"EXTENDED_COST" float8 NULL,
	"QTY_RECEIVED" float8 NULL,
	"GL_ACCOUNT" text NULL,
	"JOB" text NULL,
	"SUFFIX" text NULL,
	"SEQUENCE" text NULL,
	"VENDOR" text NULL,
	"DESCRIPTION" text NULL,
	"QTY_INVOICED" float8 NULL,
	"COST_INVOICED" float8 NULL,
	"EXTENDED_STD_COST" float8 NULL,
	"DATE_TRANSACTION" timestamptz NULL,
	"EXCHANGE_CURRENCY" text NULL,
	"DATE_EXCHANGE" timestamptz NULL,
	"EXCHANGE_RATE" float8 NULL,
	"EXCH_EXT_COST" float8 NULL,
	"EXCH_COST_INV" float8 NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"LAST_CHG_BY" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PO_TEXT" (
	"PURCHASE_ORDER" text NULL,
	"PO_SUFFIX" text NULL,
	"PO_LINE" text NULL,
	"FLAG_PO" text NULL,
	"POTXT_SEQ" text NULL,
	"TEXT" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PO_WO_XREF" (
	"PO" text NULL,
	"PO_LINE" text NULL,
	"WO" text NULL,
	"WO_SUFF" text NULL,
	"WO_SEQ" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PRODUCT_LINE" (
	"KEY_DATA" text NULL,
	"PRODUCT_LINE" text NULL,
	"PRODUCT_LINE_DESC" text NULL,
	"PRODUCT_LINE_NAME" text NULL,
	"F_DECIMAL" float8 NULL,
	"SALES_ACCOUNT" text NULL,
	"PURCHASING_ACCOUNT" text NULL,
	"ACCT_REST" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PROJECT_GROUP" (
	"F_GROUP" text NULL,
	"DESCR" text NULL,
	"STD_LABOR_RATE" float8 NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PROJECT_MASTER" (
	"PROJECT" text NULL,
	"DESCR" text NULL,
	"ORIG_SALES" int4 NULL,
	"ORIG_MATL" int4 NULL,
	"ORIG_LABR" int4 NULL,
	"ORIG_HOURS" int4 NULL,
	"ORIG_START" timestamptz NULL,
	"ORIG_END" timestamptz NULL,
	"STD_LABOR_RATE" int4 NULL,
	"CUSTOMER" text NULL,
	"PHONE" text NULL,
	"PHONE_EXT" text NULL,
	"DATE_CREATED" timestamptz NULL,
	"TIME_CREATED" timestamptz NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PROJECT_PHASE" (
	"PROJECT" text NULL,
	"PHASE" text NULL,
	"POS" int4 NULL,
	"DESCR" text NULL,
	"ORIG_SALES" float8 NULL,
	"ORIG_MATL" float8 NULL,
	"ORIG_OUTS" float8 NULL,
	"ORIG_HOURS" float8 NULL,
	"ORIG_START" timestamptz NULL,
	"ORIG_END" timestamptz NULL,
	"DATE_CREATED" timestamptz NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_PROJECT_XREF" (
	"PROJECT" text NULL,
	"PHASE" text NULL,
	"F_GROUP" text NULL,
	"SEQ" text NULL,
	"TYPE" text NULL,
	"QUOTE" text NULL,
	"QUOTE_LINE" text NULL,
	"IVC" text NULL,
	"SO" text NULL,
	"SO_SEQ" text NULL,
	"SO_LINE" text NULL,
	"BATCH" text NULL,
	"WO" text NULL,
	"WO_SUFF" text NULL,
	"WO_SEQ" text NULL,
	"WO_ACTIVE" text NULL,
	"WO_SHPD" text NULL,
	"PO" text NULL,
	"CREATED_DATE" timestamptz NULL,
	"CREATED_BY" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_QUOTE_HEADER" (
	"QUOTE_NO" text NULL,
	"CUSTOMER" text NULL,
	"DATE_QUOTE" timestamptz NULL,
	"DATE_DUE" timestamptz NULL,
	"INSURANCE" text NULL,
	"QUOTE_TYPE" text NULL,
	"CUSTOMER_PO" text NULL,
	"MARK_INFO" text NULL,
	"CODE_FOB" text NULL,
	"TERMS" text NULL,
	"LAST_REC_NO" int4 NULL,
	"FLAG_PRINT" text NULL,
	"CODE_SORT" text NULL,
	"EXPIRATION" text NULL,
	"SALESPERSON" text NULL,
	"SHIP_VIA" text NULL,
	"GL_ACCOUNT" text NULL,
	"TAX_SOURCE" text NULL,
	"TAX_STATE" text NULL,
	"TAX_ZIP" text NULL,
	"TAX_GEO_CODE" text NULL,
	"TAX_1" text NULL,
	"TAX_APPLY_1" text NULL,
	"QUOTE_SORT_2" text NULL,
	"DATE_QUOTE_CNV" timestamptz NULL,
	"DATE_DUE_CNV" timestamptz NULL,
	"FLAG_SPCD" text NULL,
	"COMPANY_CURRENCY" text NULL,
	"CATALOG_CURRENCY" text NULL,
	"QUOTE_CURRENCY" text NULL,
	"DATE_EXCH_FO_TC" timestamptz NULL,
	"EXCH_RATE_FO_TC" float8 NULL,
	"DATE_EXCH_FC_TO" timestamptz NULL,
	"EXCH_RATE_FC_TO" float8 NULL,
	"DATE_EXCH_FL_TO" timestamptz NULL,
	"EXCH_RATE_FL_TO" float8 NULL,
	"DATE_EXCH_FL_TC" timestamptz NULL,
	"QTE_CREATED_BY" text NULL,
	"QTE_CREATED_DATE" timestamptz NULL,
	"QUOTE_WON_LOSS_DATE" timestamptz NULL,
	"PROJECT" text NULL,
	"PROCESS_GRP" text NULL,
	"FLAG_ALWAYS_DISCOUNT" text NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"TIME_LAST_CHG" time NULL,
	"LAST_CHG_BY" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_QUOTE_LINES" (
	"QUOTE_NO" text NULL,
	"RECORD_NO" text NULL,
	"QUOTE_SHIP_ID" text NULL,
	"RECORD_TYPE" text NULL,
	"CUSTOMER" text NULL,
	"SHIP_ID" text NULL,
	"INVOICE" text NULL,
	"LINE_TYPE" text NULL,
	"QTY_QUOTED" float8 NULL,
	"QTY_SHIPPED" float8 NULL,
	"QTY_BO" float8 NULL,
	"UM_QUOTE" text NULL,
	"PART" text NULL,
	"QUOTE_WON" text NULL,
	"PRICE" float8 NULL,
	"COST" float8 NULL,
	"UM_INVENTORY" text NULL,
	"DESCRIPTION" text NULL,
	"PRICE_CODE" text NULL,
	"GL_ACCOUNT" text NULL,
	"TAX_SOURCE" text NULL,
	"TAX_STATE" text NULL,
	"TAX_1" text NULL,
	"TAX_APPLY_1" text NULL,
	"QTY_ORIGINAL" float8 NULL,
	"DATE_QUOTE" timestamptz NULL,
	"DATE_ITEM_PROM" timestamptz NULL,
	"FLAG_COGS" text NULL,
	"FLAG_TAX_STATUS" text NULL,
	"CUSTOMER_PART" text NULL,
	"EXCHANGE_CURRENCY" text NULL,
	"EXTENSION" float8 NULL,
	"MARGIN" float8 NULL,
	"PRODUCT_LINE" text NULL,
	"DISCOUNT_PRICE" float8 NULL,
	"PRICE_ORDER" float8 NULL,
	"PRICE_DISC_ORD" float8 NULL,
	"EXTENSION_ORDER" float8 NULL,
	"DD250_MARK_FOR" text NULL,
	"PRICE_BOM_COMP_FLG" text NULL,
	"FLAG_ALWAYS_DISCOUNT" text NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"TIME_LAST_CHG" timetz NULL,
	"LAST_CHG_BY" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_QUOTE_NOTES" (
	"QUOTE_NO" text NULL,
	"QUOTE_LINE" text NULL,
	"NOTES_SEQ" text NULL,
	"TEXT" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_QUOTE_TEXT" (
	"QUOTE_NO" text NULL,
	"QUOTE_LINE" text NULL,
	"FLAG_SALES_QUOTE" text NULL,
	"FLAG_PACK_LIST" text NULL,
	"FLAG_INVOICE" text NULL,
	"FLAG_QUOTE" text NULL,
	"TEXT_SEQ" text NULL,
	"TEXT" text NULL,
	"TEXT_TYPE" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_RECEIVER_LOG" (
	"RECEIVER" text NULL,
	"PO" text NULL,
	"PO_LINE" text NULL,
	"LOG_DATE" timestamptz NULL,
	"LOG_TIME" timetz NULL,
	"VENDOR" text NULL,
	"INVOICE" text NULL,
	"EXT_COST" float8 NULL,
	"QTY" float8 NULL,
	"QTY_INVOICED" float8 NULL,
	"COST_INVOICED" float8 NULL,
	"PROGRAM" text NULL,
	"USER_FLD" text NULL,
	"ACTION" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_ROUTER_DESC" (
	"ROUTER" text NULL,
	"DESC_ROUTER_1" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_ROUTER_HEADER" (
	"ROUTER" text NULL,
	"DESCRIPTION_ROUTER" text NULL,
	"PROD_LINE" text NULL,
	"CUSTOMER" text NULL,
	"DRAWING_CUSTOMER" text NULL,
	"DATE_ORIGINAL" timestamptz NULL,
	"UM_INVENTORY" text NULL,
	"PURGE_FLAG" int4 NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_ROUTER_LINE" (
	"ROUTER" text NULL,
	"LINE_ROUTER" text NULL,
	"LMO" text NULL,
	"PART_WC_OUTSIDE" text NULL,
	"OPERATION" text NULL,
	"SETUP" float8 NULL,
	"RUN_TIME" float8 NULL,
	"RATE" float8 NULL,
	"DESC_RT_LINE" text NULL,
	"UM_INVENTORY" text NULL,
	"AMT_MINIMUM" float8 NULL,
	"LEAD_TIME" float8 NULL,
	"SORT_CODE" text NULL,
	"PROJ_GROUP" text NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public."gss_V_TIME_ATTENDANCE" (
	"EMPLOYEE" text NULL,
	"CHARGE_DATE" timestamptz NULL,
	"IN_TS_MIN" text NULL,
	"OUT_TS_MIN" text NULL,
	"DATE_IN" timestamptz NULL,
	"TIME_IN" time NULL,
	"DATE_OUT" timestamptz NULL,
	"TIME_OUT" time NULL,
	"NAME" text NULL,
	"DEPT" text NULL,
	"SHIFT" text NULL,
	"REC_GROUP" text NULL,
	"REC_TYPE" text NULL,
	"EARNINGS_CODE" text NULL,
	"PAID" text NULL,
	"EXCUSED" text NULL,
	"ABSENCE_DESC" text NULL,
	"CLOCKED_IN" text NULL,
	"BAL_AS_DATE" timestamptz NULL,
	"DATE_LAST_CHG" timestamptz NULL,
	"TIME_LAST_CHG" timestamptz NULL,
	"LAST_CHG_BY" text NULL,
	"HOURS_HH" float8 NULL,
	"HOURS_MM" float8 NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_VENDOR_ADDL" (
	"VENDOR" text NULL,
	"RESV" text NULL,
	"REC" text NULL,
	"ID_FEDERAL" text NULL,
	"DATE_LAST_CHANGED" timestamptz NULL,
	"TIME_LAST_CHANGED" time NULL,
	"WHO_LAST_CHANGED" text NULL,
	"TERM_LAST_CHANGED" text NULL,
	"EMAIL" text NULL,
	"GEO_CODE" text NULL,
	"ISO_STATUS" text NULL,
	"ISO_CERT_DATE" timestamptz NULL,
	"CRITICAL_SUPPL" text NULL,
	"APPROVED_SUPPL" text NULL,
	"APPROVED_SUP_DT" timestamptz NULL,
	"BI_PO_RPT_ID" text NULL,
	"FREIGHT_VENDOR" text NULL,
	"CUSTOMS_VENDOR" text NULL,
	"EXTERNAL_ID" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_VENDOR_CURR" (
	"CURRENCY" text NULL,
	"VENDOR" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_VENDOR_MASTER" (
	"VENDOR" text NULL,
	"NAME_VENDOR" text NULL,
	"ADDRESS1" text NULL,
	"ADDRESS2" text NULL,
	"CITY" text NULL,
	"STATE" text NULL,
	"CODE_ZIP" text NULL,
	"COUNTRY" text NULL,
	"COUNTY" text NULL,
	"ATTENTION" text NULL,
	"CODE_SORT" text NULL,
	"CODE_SORT_2" text NULL,
	"TAX1" text NULL,
	"TAX_STATE" text NULL,
	"TAX_ZIP" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_VEND_MSTR_ADDL" (
	"VEND_NO" text NULL,
	"BUY_PHONE" text NULL,
	"BUY_FAX" text NULL,
	"PAY_PHONE" text NULL,
	"PAY_FAX" text NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public."gss_V_WORKCENTERS" (
	"MACHINE" text NULL,
	"STANDARD_COST" text NULL,
	"STANDARD_BILL" text NULL,
	"FIXED_OVHD" text NULL,
	"HOURS_MO" int8 NULL,
	"HOURS_YR" int8 NULL,
	"WC_DEPT" text NULL,
	"WC_NAME" text NULL
)
WITH (
	OIDS=FALSE
) ;



CREATE TABLE public."gss_migration_status" (
        "id" serial NOT NULL, 
	"odoo_ready_to_receive" text NULL,
	"gss_done" text NULL
)
WITH (
	OIDS=FALSE
) ;



INSERT INTO gss_migration_status (odoo_ready_to_receive)
VALUES ('1');


GRANT ALL PRIVILEGES ON TABLE gss_migration_status TO odoo;
GRANT ALL PRIVILEGES ON TABLE gss_migration_status TO gss;


"""





#RENAME THE DOUBLE OCCURANCES OF 
#update "res_partner"
#set state_id = (select id from "res_country_state" where name='Ontario' limit 1) --52
#where state_id = (select id from "res_country_state" where name='ONTARIO' limit 1) --66
#;
#
#DELETE FROM res_country_state where name='ONTARIO'
#delete from "res_country_state" where "name"='ONTARIO';

# GIVE COUNTRY NAME FOR PARTNERS WITH JUST A PROVINCE OR STATE PROVIDED.
#UPDATE res_partner set "country_id"=(select id from res_country where "name"='United States') WHERE "state_id" IN (select "id" from res_country_state where country_id = (select id from res_country where "name"='United States'));
#UPDATE res_partner set "country_id"=(select id from res_country where "name"='Canada') WHERE "state_id" IN (select "id" from res_country_state where country_id = (select id from res_country where "name"='Canada'));






