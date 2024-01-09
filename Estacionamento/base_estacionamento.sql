CREATE DATABASE  IF NOT EXISTS `estacionamento`; 
USE `estacionamento`;

DROP TABLE IF EXISTS `pavimentos`;
CREATE TABLE `pavimentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome_pavimento` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
); 

INSERT INTO `pavimentos` (`nome_pavimento`) VALUES ('Terreo'),('G1'),('G2');

DROP TABLE IF EXISTS `vagas`;
CREATE TABLE `vagas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_pavimento` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `ocupada` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `id_pavimento` (`id_pavimento`),
  CONSTRAINT `vagas_ibfk_1` FOREIGN KEY (`id_pavimento`) REFERENCES `pavimentos` (`id`)
);

INSERT INTO `vagas` (`id`, `id_pavimento`, `numero`, `ocupada`) VALUES
(1, 1, 1, 0),
(2, 1, 2, 0),
(3, 1, 3, 0),
(4, 1, 4, 0),
(5, 1, 5, 0),
(6, 1, 6, 0),
(7, 1, 7, 0),
(8, 1, 8, 0),
(9, 1, 9, 0),
(10, 1, 10, 0),
(11, 2, 1, 0),
(12, 2, 1, 0),
(13, 2, 2, 0),
(14, 2, 3, 0),
(15, 2, 4, 0),
(16, 2, 5, 0),
(17, 2, 6, 0),
(18, 2, 7, 0),
(19, 2, 8, 0),
(20, 2, 9, 0),
(21, 2, 10, 0),
(22, 3, 1, 0),
(23, 3, 2, 0),
(24, 3, 3, 0),
(25, 3, 4, 0),
(26, 3, 5, 0),
(27, 3, 6, 0),
(28, 3, 7, 0),
(29, 3, 8, 0),
(30, 3, 9, 0),
(31, 3, 10, 0);
