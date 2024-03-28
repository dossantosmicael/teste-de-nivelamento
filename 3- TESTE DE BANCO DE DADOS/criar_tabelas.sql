CREATE TABLE operadoras (
    cnpj VARCHAR(14) PRIMARY KEY,
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade_operadora VARCHAR(255),
    situacao VARCHAR(255),
    abertura DATETIME,
    status VARCHAR(255),
    registro_ans VARCHAR(255)
);

CREATE TABLE eventos_sinistros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj_operadora VARCHAR(14),
    trimestre INT,
    ano INT,
    valor DECIMAL(15, 2),
    FOREIGN KEY (cnpj_operadora) REFERENCES operadoras(cnpj)
);