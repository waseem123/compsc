-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 22, 2022 at 04:28 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mpscdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_employee`
--

CREATE TABLE `tbl_employee` (
  `emp_id` int(11) NOT NULL,
  `emp_name` varchar(60) NOT NULL,
  `emp_designation` varchar(100) NOT NULL,
  `emp_organization` varchar(200) NOT NULL,
  `emp_mobileno` varchar(13) NOT NULL,
  `emp_aadhar` varchar(12) NOT NULL,
  `emp_email` varchar(50) NOT NULL,
  `emp_status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_employee`
--

INSERT INTO `tbl_employee` (`emp_id`, `emp_name`, `emp_designation`, `emp_organization`, `emp_mobileno`, `emp_aadhar`, `emp_email`, `emp_status`) VALUES
(1, 'गोरनाळे एस. ए', 'अधिव्याख्याता स्थापत्य', 'शासकिय तंत्रनिकेतन महाविद्यालय सोलापूर', '9860351815', '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_employe_institut_mapping`
--

CREATE TABLE `tbl_employe_institut_mapping` (
  `mapping_id` int(11) NOT NULL,
  `exam_center_id` int(11) NOT NULL,
  `emp_id` int(11) NOT NULL,
  `appointed_designation` varchar(50) NOT NULL,
  `exam_date` date NOT NULL,
  `no_of_sessions` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `training_date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_employe_institut_mapping`
--

INSERT INTO `tbl_employe_institut_mapping` (`mapping_id`, `exam_center_id`, `emp_id`, `appointed_designation`, `exam_date`, `no_of_sessions`, `status`, `training_date`) VALUES
(1, 1, 1, 'केंद्रप्रमुख', '2022-08-21', 2, 1, '2022-08-20');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_examcenter`
--

CREATE TABLE `tbl_examcenter` (
  `center_id` int(11) NOT NULL,
  `center_name` varchar(200) NOT NULL,
  `center_code` varchar(10) NOT NULL,
  `center_address` varchar(500) NOT NULL,
  `center_contact_person` varchar(50) NOT NULL,
  `center_contact` varchar(13) NOT NULL,
  `center_email` varchar(50) NOT NULL,
  `center_availability` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_examcenter`
--

INSERT INTO `tbl_examcenter` (`center_id`, `center_name`, `center_code`, `center_address`, `center_contact_person`, `center_contact`, `center_email`, `center_availability`) VALUES
(1, 'एस. व्ही. सी. एस. हायस्कूल अँड ज्युनिअर कॉलेज, एम. आय. डी. सी. अक्कलकोट रोड सोलापूर', '', 'अक्कलकोट रोड सोलापूर', '', '', '', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_employee`
--
ALTER TABLE `tbl_employee`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `tbl_employe_institut_mapping`
--
ALTER TABLE `tbl_employe_institut_mapping`
  ADD PRIMARY KEY (`mapping_id`),
  ADD KEY `emp_id` (`emp_id`),
  ADD KEY `exam_center_id` (`exam_center_id`);

--
-- Indexes for table `tbl_examcenter`
--
ALTER TABLE `tbl_examcenter`
  ADD PRIMARY KEY (`center_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_employee`
--
ALTER TABLE `tbl_employee`
  MODIFY `emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_employe_institut_mapping`
--
ALTER TABLE `tbl_employe_institut_mapping`
  MODIFY `mapping_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_examcenter`
--
ALTER TABLE `tbl_examcenter`
  MODIFY `center_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_employe_institut_mapping`
--
ALTER TABLE `tbl_employe_institut_mapping`
  ADD CONSTRAINT `tbl_employe_institut_mapping_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `tbl_employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_employe_institut_mapping_ibfk_2` FOREIGN KEY (`exam_center_id`) REFERENCES `tbl_examcenter` (`center_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
