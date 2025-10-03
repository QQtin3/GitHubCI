USE CarPart;

CREATE TABLE commande (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idClient INT NOT NULL,
    description VARCHAR(2000),
    price FLOAT NOT NULL,
    purchaseDate VARCHAR(50) NOT NULL
);