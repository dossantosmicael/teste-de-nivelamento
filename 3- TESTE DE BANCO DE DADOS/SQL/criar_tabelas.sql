-- Active: 1711734655493@@127.0.0.1@3306@teste
CREATE TABLE operadoras_saude (
    Registro_ANS VARCHAR(50),
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(50),
    Logradouro VARCHAR(255),
    Numero VARCHAR(50),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF VARCHAR(2),
    CEP VARCHAR(20),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE
);


CREATE TABLE eventos_sinistros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj_operadora VARCHAR(20),
    trimestre INT,
    ano INT,
    valor DECIMAL(15, 2),
    FOREIGN KEY (cnpj_operadora) REFERENCES operadoras(cnpj)
);