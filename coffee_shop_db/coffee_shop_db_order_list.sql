-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: coffee_shop_db
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `order_list`
--

DROP TABLE IF EXISTS `order_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_list` (
  `idorder_list` int NOT NULL AUTO_INCREMENT,
  `id_contrat` int DEFAULT NULL,
  `idmenu_list` varchar(45) DEFAULT NULL,
  `order_money` decimal(10,0) DEFAULT NULL,
  `order_qty` int DEFAULT NULL,
  `order_taste` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idorder_list`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_list`
--

LOCK TABLES `order_list` WRITE;
/*!40000 ALTER TABLE `order_list` DISABLE KEYS */;
INSERT INTO `order_list` VALUES (1,11,'menu0002',50,1,'หวานปกติ'),(2,11,'menu0003',50,1,'หวานปกติ'),(3,12,'menu0002',100,2,'หวานปกติ'),(4,12,'menu0005',50,1,'หวานปกติ'),(5,13,'menu0002',100,2,'หวานปกติ'),(6,13,'menu0003',50,1,'หวานปกติ'),(7,14,'menu0002',50,1,'หวานปกติ'),(8,14,'menu0003',50,1,'หวานปกติ'),(9,15,'menu0002',50,1,'หวานปกติ'),(10,15,'menu0003',50,1,'หวานปกติ'),(11,17,'menu0003',50,1,'หวานปกติ'),(12,18,'menu0002',200,4,'หวานปกติ'),(13,19,'menu0003',50,1,'หวานปกติ'),(14,20,'menu0002',50,1,'หวานปกติ'),(15,20,'menu0003',50,1,'หวานปกติ'),(16,21,'menu0002',100,2,'หวานน้อย'),(17,21,'menu0008',50,1,'หวานมาก'),(18,23,'menu0002',50,1,'หวานปกติ'),(19,23,'menu0003',50,1,'หวานปกติ'),(20,23,'menu0015',50,1,'หวานปกติ'),(21,24,'menu0015',50,1,'หวานปกติ'),(22,25,'menu0016',50,1,'หวานปกติ'),(23,25,'menu0015',50,1,'หวานปกติ'),(24,25,'menu0013',50,1,'หวานปกติ'),(25,26,'menu0002',50,1,'หวานปกติ'),(26,26,'menu0003',50,1,'หวานปกติ'),(27,26,'menu0008',50,1,'หวานปกติ'),(28,26,'menu0013',100,2,'หวานปกติ'),(29,27,'menu0002',100,2,'หวานปกติ'),(30,27,'menu0015',50,1,'หวานปกติ'),(31,28,'menu0003',50,1,'หวานปกติ'),(32,28,'menu0002',50,1,'หวานปกติ'),(33,29,'menu0003',50,1,'หวานปกติ'),(34,29,'menu0002',50,1,'หวานปกติ'),(35,30,'menu0003',50,1,'หวานปกติ'),(36,30,'menu0002',50,1,'หวานปกติ'),(37,31,'menu0003',50,1,'หวานปกติ'),(38,31,'menu0002',50,1,'หวานปกติ'),(39,32,'menu0003',50,1,'หวานปกติ'),(40,32,'menu0002',50,1,'หวานปกติ'),(41,33,'menu0008',50,1,'หวานปกติ'),(42,33,'menu0007',50,1,'หวานปกติ'),(43,34,'menu0015',50,1,'หวานปกติ'),(44,34,'menu0016',50,1,'หวานปกติ'),(45,35,'menu0015',50,1,'หวานมาก'),(46,35,'menu0016',50,1,'หวานน้อย'),(47,36,'menu0002',50,1,'หวานน้อย'),(48,37,'menu0002',50,1,'หวานปกติ'),(49,37,'menu0003',50,1,'หวานปกติ');
/*!40000 ALTER TABLE `order_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-10 11:52:41
