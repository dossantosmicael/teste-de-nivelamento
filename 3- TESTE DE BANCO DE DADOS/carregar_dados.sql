-- Comandos para carregar os dados
LOAD DATA INFILE '/caminho/para/operadoras.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/caminho/para/eventos_sinistros.csv'
INTO TABLE eventos_sinistros
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
