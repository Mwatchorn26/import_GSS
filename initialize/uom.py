strInsertNewCategories="""
insert into product_uom_categ (create_uid, name, write_uid, create_date, write_date)
values ('1','Area','1', clock_timestamp(), clock_timestamp()),
       ('1','Group','1', clock_timestamp(), clock_timestamp());
"""

strInsertNewUoM = """
insert into product_uom (write_uid, active, uom_type, create_uid, name, rounding, factor, category_id, create_date, write_date)
values (1,true,'reference',1,'Sheet(s)', 0.01, 1, 1, clock_timestamp(), clock_timestamp()),
       (1,true,'reference',1,'Roll(es)', 0.01, 1, 1, clock_timestamp(), clock_timestamp()),
       (1,true,'smaller',1,'mm', 0.01, 1000, 4, clock_timestamp(), clock_timestamp()),
       (1,true,'bigger',1,'Week(s)', 0.01, 0.2, 3, clock_timestamp(), clock_timestamp()),
       (1,true,'smaller',1,'Minute(s)', 0.01, 480, 3, clock_timestamp(), clock_timestamp()),
       (1,true,'reference',1,'Square Inches', 0.01, 1, 6, clock_timestamp(), clock_timestamp()),
       (1,true,'bigger',1,'Square Feet', 0.01, 0.00694444, 6, clock_timestamp(), clock_timestamp()),
       (1,true,'reference',1,'Case(s)', 0.01, 1, 7, clock_timestamp(), clock_timestamp()),
       (1,true,'reference',1,'Set(s)', 0.01, 1, 7, clock_timestamp(), clock_timestamp()),
       (1,true,'reference',1,'Lot(s)', 0.01, 1, 7, clock_timestamp(), clock_timestamp()),
       (1,true,'reference',1,'Box', 0.01, 1, 7, clock_timestamp(), clock_timestamp());
"""

uom_conversions_inv="""
case\n
when "UM_INVENTORY" = 'EA' then 'Unit(s)'\n
when "UM_INVENTORY" = 'HR' then 'Hour(s)'\n
when "UM_INVENTORY" = 'FT' then 'foot(ft)'\n
when "UM_INVENTORY" = 'MT' then 'm'\n
when "UM_INVENTORY" = 'CS' then 'Case'\n
when "UM_INVENTORY" = 'LB' then 'lb(s)'\n
when "UM_INVENTORY" = 'IN' then 'inch(es)'\n
when "UM_INVENTORY" = 'PK' then 'Unit(s)'\n
when "UM_INVENTORY" = 'RL' then 'Roll'\n
when "UM_INVENTORY" = 'SI' then 'Square Inches'\n
when "UM_INVENTORY" = 'SH' then 'Sheet'\n
when "UM_INVENTORY" = 'MN' then 'Minute(s)'\n
when "UM_INVENTORY" = 'LT' then 'Liter(s)'\n
when "UM_INVENTORY" = 'BX' then 'Box'\n
when "UM_INVENTORY" = 'SF' then 'Square Feet'\n
when "UM_INVENTORY" = 'GA' then 'gal(s)'\n
when "UM_INVENTORY" = 'QU' then 'qt'\n
when "UM_INVENTORY" = 'WK' then 'Week(s)'\n
when "UM_INVENTORY" = 'LO' then 'Lot'\n
when "UM_INVENTORY" = 'DR' then 'Unit(s)'\n
when "UM_INVENTORY" = 'PR' then 'Unit(s)'\n
when "UM_INVENTORY" = 'ST' then 'Set'\n
when "UM_INVENTORY" = 'DA' then 'Day(s)'\n
when "UM_INVENTORY" = 'MM' then 'mm'\n
when "UM_INVENTORY" = 'KG' then 'kg'\n
else 'Unit(s)'\n
end;\n
"""

uom_conversions_pur="""
case\n
when "UM_PURCHASING" = 'EA' then 'Unit(s)'\n
when "UM_PURCHASING" = 'HR' then 'Hour(s)'\n
when "UM_PURCHASING" = 'FT' then 'foot(ft)'\n
when "UM_PURCHASING" = 'MT' then 'm'\n
when "UM_PURCHASING" = 'CS' then 'Case'\n
when "UM_PURCHASING" = 'LB' then 'lb(s)'\n
when "UM_PURCHASING" = 'IN' then 'inch(es)'\n
when "UM_PURCHASING" = 'PK' then 'Unit(s)'\n
when "UM_PURCHASING" = 'RL' then 'Roll'\n
when "UM_PURCHASING" = 'SI' then 'Square Inches'\n
when "UM_PURCHASING" = 'SH' then 'Sheet'\n
when "UM_PURCHASING" = 'MN' then 'Minute(s)'\n
when "UM_PURCHASING" = 'LT' then 'Liter(s)'\n
when "UM_PURCHASING" = 'BX' then 'Box'\n
when "UM_PURCHASING" = 'SF' then 'Square Feet'\n
when "UM_PURCHASING" = 'GA' then 'gal(s)'\n
when "UM_PURCHASING" = 'QU' then 'qt'\n
when "UM_PURCHASING" = 'WK' then 'Week(s)'\n
when "UM_PURCHASING" = 'LO' then 'Lot'\n
when "UM_PURCHASING" = 'DR' then 'Unit(s)'\n
when "UM_PURCHASING" = 'PR' then 'Unit(s)'\n
when "UM_PURCHASING" = 'ST' then 'Set'\n
when "UM_PURCHASING" = 'DA' then 'Day(s)'\n
when "UM_PURCHASING" = 'MM' then 'mm'\n
when "UM_PURCHASING" = 'KG' then 'kg'\n
else 'Unit(s)'\n
end;\n
"""



strUpdateInvPurchUoM = """ update "gss_V_INVENTORY_MSTR" set "UM_PURCHASING"=""" + uom_conversions_pur
strUpdateInvInvUoM = """ update "gss_V_INVENTORY_MSTR" set "UM_INVENTORY"=""" + uom_conversions_inv
strUpdateSOLinesUoM = """ update "gss_V_ORDER_LINES" set "UM_INVENTORY"=""" + uom_conversions_inv
strUpdatePOPurchUoM = """ update "gss_V_PO_LINES" set "UM_PURCHASING"=""" + uom_conversions_pur
strUpdatePOInvUoM = """ update "gss_V_PO_LINES" set "UM_INVENTORY"=""" + uom_conversions_inv

strUpdateUoM = strUpdateInvPurchUoM + strUpdateInvInvUoM + strUpdateSOLinesUoM + strUpdatePOPurchUoM + strUpdatePOInvUoM 

