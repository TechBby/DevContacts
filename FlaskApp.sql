-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 11, 2016 at 06:25 AM
-- Server version: 10.1.10-MariaDB
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `FlaskApp`
--

-- --------------------------------------------------------

--
-- Table structure for table `Developers`
--

CREATE TABLE `Developers` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `matricule` varchar(10) NOT NULL,
  `technology` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Developers`
--

INSERT INTO `Developers` (`id`, `userid`, `name`, `matricule`, `technology`) VALUES
(1, 1, 'ARNAV SIGN RAHIZADA', 'FE12A183', 'Python Flask'),
(2, 2, 'ARNOLD SCHWARCH NIGGER', 'FE12A040', 'Python Django'),
(3, 3, 'ASANTA HINI OSEE-TUTU', 'FE12A049', 'Web Lararvel'),
(4, 4, 'JAMES BOND', 'FE10A111', 'C++'),
(6, 6, 'CHRISTIANO RONALDINO', 'FE12A049', 'Android'),
(7, 7, 'MICHELLE OBAMA MBONG', 'FE12A124', 'Web CI');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(256) NOT NULL,
  `admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `username`, `email`, `password`, `admin`) VALUES
(1, 'nasali', 'nasali@gmail.com', '$5$rounds=535000$afanG6FuHBD0PHbn$sPj12ywuSQA2Oz8gwHemvuuaQ2ERiB8k2./d1ihJaE4', 1),
(2, 'waba', 'waba@gmail.com', '$5$rounds=535000$cVR46gairuftThOh$0XuPBQIaTnbL88QNA/7rQ7.O50Pqi2cx3RCpncnijY2', 0),
(3, 'theophilus', 'theophilus@gmail.com', '$5$rounds=535000$/FT2GBzQb.k.kVor$8TLTQvXw5c/Xa.jqpxDdLS39T5AKavew2kGmGDbrj/C', 0),
(9, 'root', 'root@gmail.com', '$5$rounds=535000$YZjf6FnqXKUdt1as$sPlJgrbhddGQ4Ok5ZdeJ09/InTzieGnqD/q0FLVqIz8', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Developers`
--
ALTER TABLE `Developers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Developers`
--
ALTER TABLE `Developers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
