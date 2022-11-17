USE oleos;
CREATE TABLE correntes_anp (
ide INT PRIMARY KEY AUTO_INCREMENT,
Corrente VARCHAR(50) NOT NULL,
Tipo VARCHAR(20) DEFAULT 'Petroleo',
Bacia VARCHAR(30) NOT NULL,
API DECIMAL(3,1),
UNIQUE(Corrente)
);

ALTER TABLE correntes_anp ADD COLUMN (Nafta DEC(4,1), Medios DEC(4,1), Resíduo DEC(4,1)) ;
SELECT * FROM correntes_anp;
SELECT Tipo, COUNT(Tipo) AS Tipos FROM correntes_anp GROUP BY Tipo;
SELECT MAX(API) As Max_API FROM correntes_anp;
SELECT Corrente, MIN(API) As Min_API FROM correntes_anp;
SELECT Bacia, COUNT(Bacia) AS Quantidade FROM correntes_anp GROUP BY Bacia ORDER BY Quantidade DESC;

SELECT Tipo, AVG(Nafta) AS Nafta_media, AVG(Medios) AS Diesel_media, AVG(Resíduo) AS Residuo_media FROM correntes_anp GROUP BY Tipo;
SELECT Bacia, AVG(Nafta) AS Nafta_media, AVG(Medios) AS Diesel_media, AVG(Resíduo) AS Residuo_media FROM correntes_anp GROUP BY Bacia;


/*----------------Tabela de login-------------------*/
CREATE TABLE Logando (Nome VARCHAR(100) PRIMARY KEY, Senha VARCHAR(100) NOT NULL);
INSERT INTO Logando VALUES ('admin','admin');

