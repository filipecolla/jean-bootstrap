DROP DATABASE IF EXISTS Clinica;

CREATE DATABASE Clinica;
USE Clinica;

CREATE TABLE Cadastro (

    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_nome TEXT(20) NOT NULL,
    user_sobrenome TEXT(20) NOT NULL,
    user_usuario TEXT(20) NOT NULL,
    user_email TEXT(100) NOT NULL,
    user_senha TEXT(100) NOT NULL,
    user_confSenha TEXT(100) NOT NULL,
    user_bairro TEXT(30) NULL,
    user_rua TEXT(100) NULL,
    user_cep INT(11) NULL,
    user_estado VARCHAR(100) NOT NULL,
    user_cidade VARCHAR(100) NOT NULL
);

CREATE TABLE Pagamento (

    user2_id INT PRIMARY KEY AUTO_INCREMENT,
    user_nome TEXT(30) NOT NULL,
    user_sobrenome TEXT(30) NOT NULL,
    user_email VARCHAR(100) NOT NULL,
    user_nomeCartao TEXT(100) NOT NULL,
    user_numeroCartao INT(16) NOt NULL,
    user_cvv INT(3) NOT NULL
);