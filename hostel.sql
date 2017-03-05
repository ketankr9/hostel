-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: hostel
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.1

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
-- Table structure for table `limbdi_hostel`
--

DROP TABLE IF EXISTS `limbdi_hostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `limbdi_hostel` (
  `room_no` int(11) NOT NULL,
  `A` varchar(10) DEFAULT NULL,
  `B` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `limbdi_hostel`
--

LOCK TABLES `limbdi_hostel` WRITE;
/*!40000 ALTER TABLE `limbdi_hostel` DISABLE KEYS */;
INSERT INTO `limbdi_hostel` VALUES (1,'shailendra','shivam'),(2,'utsav','utkarsh'),(3,'rahul','abhijeet'),(4,'shubham','dhaval'),(5,'vikas','arpit');
/*!40000 ALTER TABLE `limbdi_hostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `limbdi_mess_odd`
--

DROP TABLE IF EXISTS `limbdi_mess_odd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `limbdi_mess_odd` (
  `roll_no` int(11) NOT NULL,
  `jan` varchar(10) DEFAULT NULL,
  `feb` varchar(10) DEFAULT NULL,
  `mar` varchar(10) DEFAULT NULL,
  `apr` varchar(10) DEFAULT NULL,
  `may` varchar(10) DEFAULT NULL,
  `jun` varchar(10) DEFAULT NULL,
  `jul` varchar(10) DEFAULT NULL,
  `aug` varchar(10) DEFAULT NULL,
  `sep` varchar(10) DEFAULT NULL,
  `oct` varchar(10) DEFAULT NULL,
  `nov` varchar(10) DEFAULT NULL,
  `dece` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `limbdi_mess_odd`
--

LOCK TABLES `limbdi_mess_odd` WRITE;
/*!40000 ALTER TABLE `limbdi_mess_odd` DISABLE KEYS */;
/*!40000 ALTER TABLE `limbdi_mess_odd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profile` (
  `roll_no` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `branch` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL,
  `passing_year` int(4) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `bank_acount_no` varchar(20) DEFAULT NULL,
  `ifs_code` varchar(20) DEFAULT NULL,
  `branch_address` varchar(100) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `home_address` varchar(100) DEFAULT NULL,
  `home_phone` varchar(20) DEFAULT NULL,
  `guardian_phone` varchar(20) DEFAULT NULL,
  `guardian_address` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1111111,'abhishek','mining','mininghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1277777,'vickey','cse','bhvghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12345678,'adarsh','civil','avvdv@gmail.com','btech',2019,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12678678,'arun','civil','avvghv@gmail.com','btech',2019,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(16766958,'utkarsh','electrical','mifbhghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-05 23:55:02
