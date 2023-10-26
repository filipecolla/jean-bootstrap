DROP DATABASE IF EXISTS Clinica;

CREATE DATABASE Clinica;
USE Clinica;

CREATE TABLE Cadastro (

    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_nome TEXT(20) NOT NULL,
    user_sobrenome TEXT(20) NOT NULL,
    user_usuario TEXT(20) NOT NULL,
    user_email VARCHAR(100) NOT NULL,
    user_bairro TEXT(30) NOT NULL,
    user_rua TEXT(100) NOT NULL,
    user_estado VARCHAR(100) NOT NULL,
    user_cidade VARCHAR(100) NOT NULL
);

CREATE TABLE Pagamento (

    user2_id INT PRIMARY KEY AUTO_INCREMENT,
    user_nome TEXT(20) NOT NULL,
    user_sobrenome TEXT(20) NOT NULL,
    user_usuario TEXT(20) NOT NULL,
    user_email VARCHAR(100) NOT NULL,
    user_bairro TEXT(30) NOT NULL,
    user_rua VARCHAR(100) NOT NULL,
    user_estado VARCHAR(100) NOT NULL,
    user_cidade VARCHAR(100) NOT NULL,
    user_cep INT(11) NOT NULL,
    user_nomeCartao TEXT(100) NOT NULL,
    user_numeroCartao INT(20) NOt NULL,
    user_cartaoExpira DATE NOT NULL,
    user_cvv INT(3) NOT NULL
);