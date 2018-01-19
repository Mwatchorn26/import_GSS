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
values (1,true,'bigger',1,'Week', 0.01, 0.2, 3),
values (1,true,'smaller',1,'min', 0.01, 480, 3),
values (1,true,'reference',1,'Square Inches', 0.01, 1, 6),
values (1,true,'bigger',1,'Square Feet', 0.01, 0.00694444, 6),
values (1,true,'reference',1,'Case', 0.01, 1, 7),
values (1,true,'reference',1,'Set', 0.01, 1, 7),
values (1,true,'reference',1,'Lot', 0.01, 1, 7),
values (1,true,'reference',1,'Box', 0.01, 1, 7);
"""
