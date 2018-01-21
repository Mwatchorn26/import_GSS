strInsertNewCategories="""
insert into product_uom_categ (create_uid, name, write_uid)
values ('1','Area','1'),
values ('1','Group','1');
"""

strInsertNewUoM = """
insert into product_uom (write_uid, active, uom_type, create_uid, name, rounding, factor, category_id)
values (1,true,'reference',1,'Sheet', 0.01, 1, 1),
values (1,true,'reference',1,'Roll', 0.01, 1, 1),
values (1,true,'smaller',1,'mm', 0.01, 1000, 4),
values (1,true,'bigger',1,'Week(s)', 0.01, 0.2, 3),
values (1,true,'smaller',1,'Minute(s)', 0.01, 480, 3),
values (1,true,'reference',1,'Square Inches', 0.01, 1, 6),
values (1,true,'bigger',1,'Square Feet', 0.01, 0.00694444, 6),
values (1,true,'reference',1,'Case', 0.01, 1, 7),
values (1,true,'reference',1,'Set', 0.01, 1, 7),
values (1,true,'reference',1,'Lot', 0.01, 1, 7),
values (1,true,'reference',1,'Box', 0.01, 1, 7);
"""



uom_conversions="""
case 
when "IN" then "Inch(es)"
when "EA" then "Unit(s)"
when "" then "Units(s)"
when "SI" then "Square Inches"
when "FT" then "Foot(ft)"
when "PK" then
when "MT" then "m"
when "HR" then "Hour(s)"
when "SH" then "Sheet(s)"
when "BX" then "Box(es)"
when "WK" then "Week(s)"
when "ST" then "Set(s)"
when "RL" then "Roll(es")
when "MM" then "mm"
when "LO" then "Lot(s)"
when "LT" then "Liter(s)"
else "Unit(s)"
end;\n """
strUpdateInvPurchUoM = """ update "gss_V_INVENTORY_MSTR" set "UM_PURCHASING"=""" + uom_conversions
strUpdateInvInvUoM = """ update "gss_V_INVENTORY_MSTR" set "UM_INVENTORY"=""" + uom_conversions
strUpdateSOLinesUoM = """ update "gss_V_ORDER_LINES" set "UM_INVENTORY"=""" + uom_conversions
strUpdatePOPurchUoM = """ update "gss_V_PO_LINES" set "UM_PURCHASING"=""" + uom_conversions
strUpdatePOInvUoM = """ update "gss_V_PO_LINES" set "UM_INVENTORY"=""" + uom_conversions

strUpdateUoM = strUpdateInvPurchUoM + strUpdateInvInvUoM + strUpdateSOLinesUoM + strUpdatePOPurchUoM + strUpdatePOInvUoM 


completeXref="""
Unit(s)  	EA
Hour(s)		HR
foot(ft)	FT
m		MT
Case		CS
lb(s)		LB
inch(es)	IN
Unit(s)  	PK
Roll		RL
Square Inches	SI
Sheet		SH
Minute(s)	MN
Liter(s)	LT
Box		BX
Square Feet	SF
gal(s)		GA
qt		QU
Week(s)		WK
Lot		LO
		DR
Unit(s)		PR
Set		ST
Day(s)		DA
mm		MM
kg		KG"""

