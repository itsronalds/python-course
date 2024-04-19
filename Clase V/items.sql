# BOOKS PRODUCTS
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (1, 'Grief Is For People', 'LIB001', 29.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (1, 'Come and Get It', 'LIB002', 19.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (1, 'James', 'LIB003', 24.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (1, 'Real Americans', 'LIB004', 34.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (1, 'Funny Story', 'LIB005', 27.99);

# CLOTHES PRODUCTS
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (2, 'Camiseta', 'ROP001', 19.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (2, 'Pantalón', 'ROP002', 39.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (2, 'Vestido', 'ROP003', 49.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (2, 'Camisa', 'ROP004', 29.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (2, 'Zapatos', 'ROP005', 59.99);

# FOOD PRODUCTS
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (3, 'Manzana', 'COM001', 0.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (3, 'Pan', 'COM002', 1.99);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (3, 'Lechuga', 'COM003', 2.49);
INSERT INTO product (CategoryID, Name, Code, Price)
VALUES (3, 'Arroz', 'COM004', 3.99);

# CATEGORIES INSERTS 
INSERT INTO category (Name, Code)
VALUES ('Libros', 'LIB');
INSERT INTO category (Name, Code)
VALUES ('Ropa', 'ROP');
INSERT INTO category (Name, Code)
VALUES ('Comida', 'COM');