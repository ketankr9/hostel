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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'admin');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add auth group',7,'add_authgroup'),(20,'Can change auth group',7,'change_authgroup'),(21,'Can delete auth group',7,'delete_authgroup'),(22,'Can add auth group permissions',8,'add_authgrouppermissions'),(23,'Can change auth group permissions',8,'change_authgrouppermissions'),(24,'Can delete auth group permissions',8,'delete_authgrouppermissions'),(25,'Can add auth permission',9,'add_authpermission'),(26,'Can change auth permission',9,'change_authpermission'),(27,'Can delete auth permission',9,'delete_authpermission'),(28,'Can add auth user',10,'add_authuser'),(29,'Can change auth user',10,'change_authuser'),(30,'Can delete auth user',10,'delete_authuser'),(31,'Can add auth user groups',11,'add_authusergroups'),(32,'Can change auth user groups',11,'change_authusergroups'),(33,'Can delete auth user groups',11,'delete_authusergroups'),(34,'Can add auth user user permissions',12,'add_authuseruserpermissions'),(35,'Can change auth user user permissions',12,'change_authuseruserpermissions'),(36,'Can delete auth user user permissions',12,'delete_authuseruserpermissions'),(37,'Can add django admin log',13,'add_djangoadminlog'),(38,'Can change django admin log',13,'change_djangoadminlog'),(39,'Can delete django admin log',13,'delete_djangoadminlog'),(40,'Can add django content type',14,'add_djangocontenttype'),(41,'Can change django content type',14,'change_djangocontenttype'),(42,'Can delete django content type',14,'delete_djangocontenttype'),(43,'Can add django migrations',15,'add_djangomigrations'),(44,'Can change django migrations',15,'change_djangomigrations'),(45,'Can delete django migrations',15,'delete_djangomigrations'),(46,'Can add django session',16,'add_djangosession'),(47,'Can change django session',16,'change_djangosession'),(48,'Can delete django session',16,'delete_djangosession'),(49,'Can add limbdi2016',17,'add_limbdi2016'),(50,'Can change limbdi2016',17,'change_limbdi2016'),(51,'Can delete limbdi2016',17,'delete_limbdi2016'),(52,'Can add limbdi hostel',19,'add_limbdihostel'),(53,'Can change limbdi hostel',19,'change_limbdihostel'),(54,'Can delete limbdi hostel',19,'delete_limbdihostel'),(55,'Can add limbdi mess odd',20,'add_limbdimessodd'),(56,'Can change limbdi mess odd',20,'change_limbdimessodd'),(57,'Can delete limbdi mess odd',20,'delete_limbdimessodd'),(58,'Can add profile',18,'add_profile'),(59,'Can change profile',18,'change_profile'),(60,'Can delete profile',18,'delete_profile'),(61,'Can add dhanraj hostel',21,'add_dhanrajhostel'),(62,'Can change dhanraj hostel',21,'change_dhanrajhostel'),(63,'Can delete dhanraj hostel',21,'delete_dhanrajhostel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$SLogrre3qhzH$+c72imYmgFQQ4zoE0LNqpHm8d3dpHc8fvTRhLXJHVPI=','2017-03-07 10:34:50.589379',1,'hostel','','','',1,1,'2017-03-02 16:15:07.191838'),(2,'pbkdf2_sha256$30000$aQ36k4HrMiRB$1/R5HN7IGerumZl6NdxgXI2pfKhrdJFpE7v0bG9UIUQ=','2017-03-05 12:51:12.391337',0,'15074014','','','',0,1,'2017-03-05 12:48:41.121749'),(3,'pbkdf2_sha256$30000$tNeZ1gfhLhdn$sNxSeHZBIp2FNRRenGNgEwLnwsKQ/3AIEgSPIz7udPY=','2017-03-07 14:12:16.330357',0,'15074015','','','',0,1,'2017-03-07 12:14:02.553260');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-03-02 16:15:43.326300','1','301',1,'[{\"added\": {}}]',17,1),(2,'2017-03-05 13:03:25.881420','1','admin',1,'[{\"added\": {}}]',4,1),(3,'2017-03-05 16:57:55.650285','1111111','Profile object',2,'[]',18,1),(4,'2017-03-05 16:58:05.879890','1111111','Profile object',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',18,1),(5,'2017-03-05 16:58:17.017465','1111111','Profile object',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',18,1),(6,'2017-03-05 17:05:53.713422','1111111','Profile object',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',18,1),(7,'2017-03-05 17:06:30.598450','1111111','Profile object',2,'[{\"changed\": {\"fields\": [\"mobile\", \"bank_acount_no\", \"ifs_code\", \"branch_address\"]}}]',18,1),(8,'2017-03-05 17:07:29.695596','1111111','Profile object',2,'[{\"changed\": {\"fields\": [\"father_name\", \"home_address\", \"home_phone\", \"guardian_phone\", \"guardian_address\"]}}]',18,1),(9,'2017-03-07 11:04:03.990351','15074015','15074015 ',3,'',18,1),(10,'2017-03-07 11:05:10.189218','12345678','12345678 adarsh',2,'[{\"changed\": {\"fields\": [\"branch_address\"]}}]',18,1),(11,'2017-03-07 12:01:56.842271','1111111','1111111 abhishek',2,'[{\"changed\": {\"fields\": [\"branch\", \"course\"]}}]',18,1),(12,'2017-03-07 12:02:18.007844','1111111','1111111 abhishek',2,'[]',18,1),(13,'2017-03-07 12:03:09.124901','15074014','LimbdiMessOdd object',1,'[{\"added\": {}}]',20,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(21,'appadmin','dhanrajhostel'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(7,'myapp','authgroup'),(8,'myapp','authgrouppermissions'),(9,'myapp','authpermission'),(10,'myapp','authuser'),(11,'myapp','authusergroups'),(12,'myapp','authuseruserpermissions'),(13,'myapp','djangoadminlog'),(14,'myapp','djangocontenttype'),(15,'myapp','djangomigrations'),(16,'myapp','djangosession'),(17,'myapp','limbdi2016'),(19,'myapp','limbdihostel'),(20,'myapp','limbdimessodd'),(18,'myapp','profile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-03-02 16:13:30.824697'),(2,'auth','0001_initial','2017-03-02 16:13:39.181892'),(3,'admin','0001_initial','2017-03-02 16:13:40.905285'),(4,'admin','0002_logentry_remove_auto_add','2017-03-02 16:13:41.018081'),(5,'contenttypes','0002_remove_content_type_name','2017-03-02 16:13:42.159210'),(6,'auth','0002_alter_permission_name_max_length','2017-03-02 16:13:42.865277'),(7,'auth','0003_alter_user_email_max_length','2017-03-02 16:13:43.503331'),(8,'auth','0004_alter_user_username_opts','2017-03-02 16:13:43.552386'),(9,'auth','0005_alter_user_last_login_null','2017-03-02 16:13:44.164048'),(10,'auth','0006_require_contenttypes_0002','2017-03-02 16:13:44.197775'),(11,'auth','0007_alter_validators_add_error_messages','2017-03-02 16:13:44.246619'),(12,'auth','0008_alter_user_username_max_length','2017-03-02 16:13:44.913279'),(13,'myapp','0001_initial','2017-03-02 16:13:45.262062'),(14,'myapp','0002_remove_limbdi2016_name','2017-03-02 16:13:45.853747'),(15,'sessions','0001_initial','2017-03-02 16:13:46.390391'),(16,'myapp','0003_auto_20170305_1655','2017-03-05 16:55:32.055789'),(17,'myapp','0004_auto_20170307_1007','2017-03-07 10:34:11.559250'),(18,'appadmin','0001_initial','2017-03-07 11:09:37.138036'),(19,'appadmin','0002_auto_20170307_1115','2017-03-07 11:15:24.012276');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('cl6a545gzyeups3p35u2a55yd9cm8t3g','OTY5YzA4OTAwOTlkNmE4ZTFhYzVkMWE4ODkwMzk0N2ZhZmM0NWE0YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjIzYzgwNzU2NjdjNzBlMTA1Y2FiY2JiMmI5MDU1MDhjY2YxZWVmZGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-03-19 16:51:50.645682'),('qfxyfo6urq7x3hi548jkr59iqvzhjyvi','MGJjYTMxZTBkYWZlZmYyNGVmZTlhNDc4Y2I5Njg3Mzc0NTM4NzZlMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjI3OGRhNWZkZjdhZDY0MTFkYjg2Y2UwZTg1ZWVhYmQ5Zjk2ZTFmNzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2017-03-21 14:12:16.379066');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `limbdi2016`
--

DROP TABLE IF EXISTS `limbdi2016`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `limbdi2016` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `room` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `limbdi2016`
--

LOCK TABLES `limbdi2016` WRITE;
/*!40000 ALTER TABLE `limbdi2016` DISABLE KEYS */;
INSERT INTO `limbdi2016` VALUES (1,301),(2,333),(3,444),(4,405),(5,696);
/*!40000 ALTER TABLE `limbdi2016` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `limbdi_mess_odd` VALUES (15074014,'700','800','700','800','700','900','500','4400','800','88','888','965');
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
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1111111,'abhishek','mnc','abhishek.kumar.min15@iitbhu.ac.in','B.Tech',2020,'9151645962','SBI00000545845646546','SBIN01444','IT BHU, VARANASI, Uttar Pradesh','Ram Shayam Gupta','Sultan Pur, Varanasi, Uttar Pradesh','9234879652','9562314559','Panipat, Hariyana.'),(1277777,'vickey','cse','bhvghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12345678,'adarsh','civil','avvdv@gmail.com','btech',2019,'','','','kjdfj gdhgri uhdi dfhg hdihg ihighiu hih gihf ih gih ih giuhgidhi hihg ishg i hiuh ig','','','','',''),(12678678,'arun','civil','avvghv@gmail.com','btech',2019,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(15074014,'utsav','cse','ketankr9@gmail.com','idd',2020,'9151643206','SBI000255555455','SBIN01444','IT BHU','Krishna','Darbhanga','9234873965','9235689754','Panipat, Hariyana'),(15074015,'','','','B.Tech',2020,'9999999999','0000000000','sh','','','','','',''),(16766958,'utkarsh','electrical','mifbhghv@gmail.com','IDD',2020,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
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

-- Dump completed on 2017-03-07 22:38:30
