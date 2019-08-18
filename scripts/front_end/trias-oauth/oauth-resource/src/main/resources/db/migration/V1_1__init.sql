/*
Navicat MySQL Data Transfer

Source Server         : localhost-trias
Source Server Version : 50644
Source Host           : 192.168.199.126:3306
Source Database       : trias_cli

Target Server Type    : MYSQL
Target Server Version : 50644
File Encoding         : 65001

Date: 2019-05-17 15:01:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for trias_resource
-- ----------------------------
CREATE TABLE `trias_resource` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `root_name` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `del_flag` int(1) NOT NULL DEFAULT '0',
  `description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for trias_role
-- ----------------------------
CREATE TABLE `trias_role` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `role_type` varchar(255) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for trias_role_resource
-- ----------------------------
CREATE TABLE `trias_role_resource` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `resource_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_role_id` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
