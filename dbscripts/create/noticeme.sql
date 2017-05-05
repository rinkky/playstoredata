-- Server version	5.5.54-0ubuntu0.14.04.1

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
-- Table structure for table `tb_apps`
--

DROP TABLE IF EXISTS `tb_apps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_apps` (
  `app_id` int(11) NOT NULL AUTO_INCREMENT,
  `app_uniq_name` varchar(100) CHARACTER SET utf8 NOT NULL,
  `app_name` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `app_isfree` tinyint(1) NOT NULL,
  `app_price_id` int(11) DEFAULT NULL,
  `app_price` float NOT NULL,
  PRIMARY KEY (`app_id`),
  UNIQUE KEY `apps_full_name_UNIQUE` (`app_uniq_name`),
  UNIQUE KEY `apps_id_UNIQUE` (`app_id`),
  KEY `app_price_id_idx` (`app_price_id`),
  CONSTRAINT `fk_app_price_id` FOREIGN KEY (`app_price_id`) REFERENCES `tb_prices` (`price_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tb_apps_notice`
--

DROP TABLE IF EXISTS `tb_apps_notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_apps_notice` (
  `app_id` int(11) NOT NULL,
  `time` date DEFAULT NULL,
  PRIMARY KEY (`app_id`),
  UNIQUE KEY `app_id_UNIQUE` (`app_id`),
  CONSTRAINT `fk_app_notice` FOREIGN KEY (`app_id`) REFERENCES `tb_apps` (`app_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tb_prices`
--

DROP TABLE IF EXISTS `tb_prices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_prices` (
  `price_id` int(11) NOT NULL AUTO_INCREMENT,
  `price_1` float DEFAULT NULL,
  `time_1` date DEFAULT NULL,
  `price_2` float DEFAULT NULL,
  `time_2` date DEFAULT NULL,
  `price_3` float DEFAULT NULL,
  `time_3` date DEFAULT NULL,
  `price_4` float DEFAULT NULL,
  `time_4` date DEFAULT NULL,
  `price_5` float DEFAULT NULL,
  `time_5` date DEFAULT NULL,
  `price_6` float DEFAULT NULL,
  `time_6` date DEFAULT NULL,
  `price_7` float DEFAULT NULL,
  `time_7` date DEFAULT NULL,
  `price_8` float DEFAULT NULL,
  `time_8` date DEFAULT NULL,
  `price_9` float DEFAULT NULL,
  `time_9` date DEFAULT NULL,
  `price_10` float DEFAULT NULL,
  `time_10` date DEFAULT NULL,
  `more_price_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`price_id`),
  KEY `fk_more_price_id_idx` (`more_price_id`),
  CONSTRAINT `fk_more_price_id` FOREIGN KEY (`more_price_id`) REFERENCES `tb_prices` (`price_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-05 16:20:55
