-- MySQL dump 10.14  Distrib 5.5.60-MariaDB, for Linux (x86_64)
--
-- Host: 192.168.31.13    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Components`
--

DROP TABLE IF EXISTS `Components`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Components` (
  `idComponents` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  PRIMARY KEY (`idComponents`),
  UNIQUE KEY `idComponents_UNIQUE` (`idComponents`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Components`
--

LOCK TABLES `Components` WRITE;
/*!40000 ALTER TABLE `Components` DISABLE KEYS */;
INSERT INTO `Components` (`idComponents`, `name`, `version`) VALUES (1,'mass','1.1.1.1'),(2,'mass','1.1.1.1'),(3,'mass','1.1.1.1'),(4,'mass','1.1.1.1'),(5,'mass','1.1.1.1'),(6,'mass','1.1.1.1'),(7,'','mass'),(8,'mass','1.1.1.1'),(9,'mass','1.1.2.1'),(10,'mass','1.1.2.3');
/*!40000 ALTER TABLE `Components` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test`
--

DROP TABLE IF EXISTS `Test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Test` (
  `idTest` int(11) NOT NULL AUTO_INCREMENT,
  `test_name` varchar(255) NOT NULL,
  `test_type` varchar(255) NOT NULL,
  PRIMARY KEY (`idTest`),
  UNIQUE KEY `idTest_UNIQUE` (`idTest`),
  UNIQUE KEY `test_name_UNIQUE` (`test_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test`
--

LOCK TABLES `Test` WRITE;
/*!40000 ALTER TABLE `Test` DISABLE KEYS */;
INSERT INTO `Test` (`idTest`, `test_name`, `test_type`) VALUES (1,'mats_telecom','voice'),(4,'mts_telecom','voice'),(5,'beeline','voice'),(6,'1.5-pre','comand_libssrv');
/*!40000 ALTER TABLE `Test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test_has_Test_results`
--

DROP TABLE IF EXISTS `Test_has_Test_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Test_has_Test_results` (
  `Test_idTest` int(11) NOT NULL,
  `Test_results_idTest_result` int(11) NOT NULL,
  PRIMARY KEY (`Test_idTest`,`Test_results_idTest_result`),
  KEY `fk_Test_has_Test_results_Test_results1_idx` (`Test_results_idTest_result`),
  KEY `fk_Test_has_Test_results_Test1_idx` (`Test_idTest`),
  CONSTRAINT `fk_Test_has_Test_results_Test1` FOREIGN KEY (`Test_idTest`) REFERENCES `Test` (`idTest`),
  CONSTRAINT `fk_Test_has_Test_results_Test_results1` FOREIGN KEY (`Test_results_idTest_result`) REFERENCES `Test_results` (`idTest_result`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test_has_Test_results`
--

LOCK TABLES `Test_has_Test_results` WRITE;
/*!40000 ALTER TABLE `Test_has_Test_results` DISABLE KEYS */;
/*!40000 ALTER TABLE `Test_has_Test_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test_results`
--

DROP TABLE IF EXISTS `Test_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Test_results` (
  `idTest_result` int(11) NOT NULL AUTO_INCREMENT,
  `case_name` varchar(255) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `Test_resultscol` varchar(45) DEFAULT NULL,
  `components_id` int(11) DEFAULT NULL,
  `reason` varchar(4000) DEFAULT NULL,
  PRIMARY KEY (`idTest_result`),
  UNIQUE KEY `idTest_result_UNIQUE` (`idTest_result`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test_results`
--

LOCK TABLES `Test_results` WRITE;
/*!40000 ALTER TABLE `Test_results` DISABLE KEYS */;
/*!40000 ALTER TABLE `Test_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test_results_has_Components`
--

DROP TABLE IF EXISTS `Test_results_has_Components`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Test_results_has_Components` (
  `Test_results_idTest_result` int(11) NOT NULL,
  `Components_idComponents` int(11) NOT NULL,
  PRIMARY KEY (`Test_results_idTest_result`,`Components_idComponents`),
  KEY `fk_Test_results_has_Components_Components1_idx` (`Components_idComponents`),
  KEY `fk_Test_results_has_Components_Test_results1_idx` (`Test_results_idTest_result`),
  CONSTRAINT `fk_Test_results_has_Components_Components1` FOREIGN KEY (`Components_idComponents`) REFERENCES `Components` (`idComponents`),
  CONSTRAINT `fk_Test_results_has_Components_Test_results1` FOREIGN KEY (`Test_results_idTest_result`) REFERENCES `Test_results` (`idTest_result`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test_results_has_Components`
--

LOCK TABLES `Test_results_has_Components` WRITE;
/*!40000 ALTER TABLE `Test_results_has_Components` DISABLE KEYS */;
/*!40000 ALTER TABLE `Test_results_has_Components` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'mydb'
--
/*!50003 DROP PROCEDURE IF EXISTS `add_component` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `add_component`(
    OUT o_rc        INTEGER, 
    IN comp_name   VARCHAR(100),
    IN comp_version   VARCHAR(100)
)
BEGIN
	DECLARE tmp_id INTEGER;
	IF EXISTS(select * from mydb.Components where name=comp_name and version=comp_version) 
		THEN
		set tmp_id=0;
	ELSE
		insert into mydb.Components(name,version)
		VALUES (comp_name,comp_version);
        select idComponents from mydb.Components where name=comp_name and version=comp_version into tmp_id;
	END IF;
    set o_rc=tmp_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_test` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `add_test`(
    OUT o_rc        INTEGER, 
    IN t_name   VARCHAR(100),
    IN t_type   VARCHAR(100)
)
BEGIN
	DECLARE tmp_id INTEGER;
	IF EXISTS(select * from mydb.Test where test_type=t_name and test_type=t_type) 
		THEN
		set tmp_id=0;
	ELSE
		insert into mydb.Test(test_name,test_type)
		VALUES (t_name,t_type);
        select idTest from mydb.Test where test_name=t_name and test_type=t_type into tmp_id;
	END IF;
    set o_rc=tmp_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-14 17:36:15
