/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80026
Source Host           : localhost:3306
Source Database       : fuzzy_join

Target Server Type    : MYSQL
Target Server Version : 80026
File Encoding         : 65001

Date: 2023-04-16 22:32:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for data
-- ----------------------------
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dataname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `attribute1` int DEFAULT NULL,
  `attribute2` varchar(255) DEFAULT NULL,
  `attribute3` varchar(255) DEFAULT NULL,
  `attribute4` varchar(255) DEFAULT NULL,
  `attribute5` varchar(255) DEFAULT NULL,
  `attribute6` varchar(255) DEFAULT NULL,
  `attribute7` varchar(255) DEFAULT NULL,
  `attribute8` varchar(255) DEFAULT NULL,
  `attribute9` varchar(255) DEFAULT NULL,
  `attribute10` varchar(255) DEFAULT NULL,
  `attribute11` varchar(255) DEFAULT NULL,
  `attribute12` varchar(255) DEFAULT NULL,
  `attribute13` varchar(255) DEFAULT NULL,
  `attribute14` varchar(255) DEFAULT NULL,
  `attribute15` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `KEY1` (`username`),
  KEY `KEY2` (`dataname`),
  CONSTRAINT `KEY1` FOREIGN KEY (`username`) REFERENCES `mapping` (`username`),
  CONSTRAINT `KEY2` FOREIGN KEY (`dataname`) REFERENCES `mapping` (`dataname`)
) ENGINE=InnoDB AUTO_INCREMENT=96714 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for mapping
-- ----------------------------
DROP TABLE IF EXISTS `mapping`;
CREATE TABLE `mapping` (
  `username` varchar(50) NOT NULL,
  `dataname` varchar(50) NOT NULL,
  `th_id` int NOT NULL,
  `th_name` varchar(100) NOT NULL,
  PRIMARY KEY (`username`,`dataname`,`th_id`),
  KEY `username` (`username`),
  KEY `dataname` (`dataname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for revoked_tokens
-- ----------------------------
DROP TABLE IF EXISTS `revoked_tokens`;
CREATE TABLE `revoked_tokens` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jti` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `tusername` varchar(20) NOT NULL,
  `tpassword` varchar(150) NOT NULL,
  `gender` int DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `create_user` varchar(20) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `modified_user` varchar(20) DEFAULT NULL,
  `modified_time` datetime DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `tusername` (`tusername`),
  UNIQUE KEY `tpassword` (`tpassword`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
