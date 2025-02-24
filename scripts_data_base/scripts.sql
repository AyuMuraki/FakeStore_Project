
CREATE DATABASE loja_fake

USE loja_fake

CREATE TABLE produtos (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    price DECIMAL(10, 2),
    category VARCHAR(255),
    description TEXT,
    image VARCHAR(255),
    timestamp DATETIME
);

SELECT * FROM produtos;

DELIMITER $$

CREATE PROCEDURE BuscarProdutosPorCategoria(IN categoria VARCHAR(200))
BEGIN
    SELECT * FROM produtos WHERE category = categoria;
END $$

DELIMITER ;
