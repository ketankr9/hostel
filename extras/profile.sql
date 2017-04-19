-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: hostelportal
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
-- Table structure for table `vishweshvarayya`
--

DROP TABLE IF EXISTS `vishweshvarayya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vishweshvarayya` (
  `roll_no` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `branch` varchar(20) DEFAULT NULL,
  `acad_fee` varchar(255) DEFAULT NULL,
  `mess_fee` varchar(255) DEFAULT NULL,
  `room_sec` varchar(10) DEFAULT NULL,
  `room_no` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL,
  `passing_year` int(4) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `bank_acount_no` varchar(20) DEFAULT NULL,
  `ifs_code` varchar(20) DEFAULT NULL,
  `branch_address` varchar(255) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `home_address` varchar(255) DEFAULT NULL,
  `home_phone` varchar(20) DEFAULT NULL,
  `guardian_phone` varchar(20) DEFAULT NULL,
  `guardian_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vishweshvarayya`
--

LOCK TABLES `vishweshvarayya` WRITE;
/*!40000 ALTER TABLE `vishweshvarayya` DISABLE KEYS */;
INSERT INTO `vishweshvarayya` VALUES (1111111,'abhishek','mnc',NULL,NULL,NULL,NULL,'abhishek.kumar.min15@iitbhu.ac.in','B.Tech',2020,'9151645962','SBI00000545845646546','SBIN01444','IT BHU, VARANASI, Uttar Pradesh','Ram Shayam Gupta','Sultan Pur, Varanasi, Uttar Pradesh','9234879652','9562314559','Panipat, Hariyana.'),(1277777,'vickey','cse',NULL,NULL,NULL,NULL,'bhvghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12345678,'adarsh','civil',NULL,NULL,NULL,NULL,'avvdv@gmail.com','btech',2019,'','','','kjdfj gdhgri uhdi dfhg hdihg ihighiu hih gihf ih gih ih giuhgidhi hihg ishg i hiuh ig','','','','',''),(12678678,'arun','civil',NULL,NULL,NULL,NULL,'avvghv@gmail.com','btech',2019,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(15074005,'hbbhhkhbk','mnc',NULL,NULL,NULL,NULL,'hbdsk@hdcbhdsm.com','PhD',2019,'41814844908','44518789766','SBIN0011445','jeehiehj','njk d vdd,sj','uergueruy','87494949','97499499494','yegciwgcik'),(15074014,'utsav','cse',NULL,NULL,NULL,NULL,'ketankr9@gmail.com','B.Tech',2020,'9151643206','SBI000255555455','SBIN01444','IT BHU','Krishna','Darbhanga','9234873965','9235689754','Panipat, Hariyana'),(15074015,'','',NULL,NULL,NULL,NULL,'','B.Tech',2020,'9999999999','0000000000','sh','','','','','',''),(16766958,'utkarsh','electrical',NULL,NULL,NULL,NULL,'mifbhghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `vishweshvarayya` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-19 21:38:46
