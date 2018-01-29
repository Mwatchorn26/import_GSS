strInsertNewCategories="""
insert into product_uom_categ (create_uid, name, write_uid)
values ('1','Area','1'),
values ('1','Group','1');
"""

strInsertNewUoM = """
insert into product_uom (write_uid, active, uom_type, create_uid, name, rounding, factor, category_id)
values (1,true,'reference',1,'Sheet(s)', 0.01, 1, 1),
values (1,true,'reference',1,'Roll(es)', 0.01, 1, 1),
values (1,true,'smaller',1,'mm', 0.01, 1000, 4),
values (1,true,'bigger',1,'Week(s)', 0.01, 0.2, 3),
values (1,true,'smaller',1,'Minute(s)', 0.01, 480, 3),
values (1,true,'reference',1,'Square Inches', 0.01, 1, 6),
values (1,true,'bigger',1,'Square Feet', 0.01, 0.00694444, 6),
values (1,true,'reference',1,'Case(s)', 0.01, 1, 7),
values (1,true,'reference',1,'Set(s)', 0.01, 1, 7),
values (1,true,'reference',1,'Lot(s)', 0.01, 1, 7),
values (1,true,'reference',1,'Box', 0.01, 1, 7);
"""

uom_conversions="""
case\n
when 'EA' then 'Unit(s)'\n
when 'HR' then 'Hour(s)'\n
when 'FT' then 'foot(ft)'\n
when 'MT' then 'm'\n
when 'CS' then 'Case'\n
when 'LB' then 'lb(s)'\n
when 'IN' then 'inch(es)'\n
when 'PK' then 'Unit(s)'\n
when 'RL' then 'Roll'\n
when 'SI' then 'Square Inches'\n
when 'SH' then 'Sheet'\n
when 'MN' then 'Minute(s)'\n
when 'LT' then 'Liter(s)'\n
when 'BX' then 'Box'\n
when 'SF' then 'Square Feet'\n
when 'GA' then 'gal(s)'\n
when 'QU' then 'qt'\n
when 'WK' then 'Week(s)'\n
when 'LO' then 'Lot'\n
when 'DR' then 'Unit(s)'\n
when 'PR' then 'Unit(s)'\n
when 'ST' then 'Set'\n
when 'DA' then 'Day(s)'\n
when 'MM' then 'mm'\n
when 'KG' then 'kg'\n
else ''\n
end;\n
"""

strUpdateInvPurchUoM = """ update "gss_V_INVENTORY_MSTR" set "UM_PURCHASING"=""" + uom_conversions
strUpdateInvInvUoM = """ update "gss_V_INVENTORY_MSTR" set "UM_INVENTORY"=""" + uom_conversions
strUpdateSOLinesUoM = """ update "gss_V_ORDER_LINES" set "UM_INVENTORY"=""" + uom_conversions
strUpdatePOPurchUoM = """ update "gss_V_PO_LINES" set "UM_PURCHASING"=""" + uom_conversions
strUpdatePOInvUoM = """ update "gss_V_PO_LINES" set "UM_INVENTORY"=""" + uom_conversions

strUpdateUoM = strUpdateInvPurchUoM + strUpdateInvInvUoM + strUpdateSOLinesUoM + strUpdatePOPurchUoM + strUpdatePOInvUoM 

