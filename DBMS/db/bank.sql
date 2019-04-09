-- MySQL dump 10.11
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	5.0.45-community-nt

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `cid` int(11) NOT NULL,
  `c_last_name` varchar(20) NOT NULL,
  `c_mid_name` varchar(20) default NULL,
  `c_first_name` varchar(20) NOT NULL,
  `account_no` int(11) NOT NULL,
  `account_type` varchar(10) NOT NULL,
  `amount` int(11) default NULL,
  `bank` char(10) NOT NULL,
  `c_email` varchar(25) default NULL,
  PRIMARY KEY  (`cid`),
  UNIQUE KEY `account_no` (`account_no`),
  UNIQUE KEY `c_email` (`c_email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (101,'Swarnkar','','Lavish',5001,'SAVINGS',110250,'SBI','lavishswarnkar@gmail.com'),(103,'Gupta','','Sparsh',5003,'DEMAT',21000,'BOI','sparshgupta@gmail.com'),(104,'Agrawal','','Sarthak',5004,'DEMAT',21000,'ICICI','sarthakagrawal@gmail.com'),(105,'Dwivedi','','Pradhyumn',5005,'SAVINGS',15750,'ICICI','pradhyumnd@gmail.com'),(106,'Sharma','','Sachin',5006,'SAVINGS',26250,'ICICI','sachinsharma@gmail.com'),(107,'Agrawal','','Abhishek',5007,'SAVINGS',36750,'ICICI','abhishek.a@gmail.com'),(108,'Heda','','Keshav',5008,'CURRENT',10500,'BOI','keshavheda111@gmail.com'),(109,'Prahladka','','Tarun',5009,'CURRENT',10500,'BOI','tarunprahladka@gmail.com'),(110,'Choubisa','','Divyansh',5010,'CURRENT',21000,'BOI','divyanshch111@gmail.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `e_id` int(11) NOT NULL,
  `e_last_name` char(25) NOT NULL,
  `e_mid_name` varchar(20) default NULL,
  `e_first_name` varchar(20) NOT NULL,
  `e_email_id` varchar(30) default NULL,
  `e_department` varchar(10) NOT NULL,
  `e_manager_id` int(11) default NULL,
  PRIMARY KEY  (`e_id`),
  UNIQUE KEY `e_email_id` (`e_email_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (10001,'Ratan','','Dr. Ram','ram.ratan@jecrcu.edu.in','Admin',NULL),(10002,'Hemrajani','','Dr. Naveen','naveen.hemrajani@jecrcu.edu.in','CSE',10001),(10003,'Sethi','','Dr. Dinesh','dinesh.sethi@jecrcu.edu.in','ECE',10001),(10004,'Singh','','Dr. Jagdev','jagdev.singh@jecrcu.edu.in','Maths',10001),(10005,'Jain','','Mr. Pankaj','pankaj.jain@jecrcu.edu.in','CSE',10002),(10006,'Kulshreshtha','','Mr. Peeyush','peeyush.kul@jecrcu.edu.in','CSE',10002),(10007,'Mishra','','Mrs. Neha','neha.mishra@jecrcu.edu.in','CSE',10002),(10008,'Sharma','','Mrs. Anuja','anuja.sharma@jecrcu.edu.in','CSE',10002),(10009,'Singh','','Mr. Amandeep','amandeep.singh@jecrcu.edu.in','ECE',10003),(10010,'Sharma','Prasad','Dr. Ram','rp.sharma@jecrcu.edu.in','Maths',10004);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2001-12-31 20:05:31
