-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Amazon
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Amazon
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Amazon` DEFAULT CHARACTER SET utf8 ;
USE `Amazon` ;

-- -----------------------------------------------------
-- Table `Amazon`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Amazon`.`Category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Action_figure` VARCHAR(45) NULL,
  `Items_ordered` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW (),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW (),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Amazon`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Amazon`.`Product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Product_name` VARCHAR(45) NULL,
  `Number_of_items` INT NULL,
  `Created_at` DATETIME NULL DEFAULT NOW(),
  `Updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW (),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Amazon`.`Category_has_Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Amazon`.`Category_has_Product` (
  `Category_id` INT NOT NULL,
  `Product_id` INT NOT NULL,
  PRIMARY KEY (`Category_id`, `Product_id`),
  INDEX `fk_Category_has_Product_Product1_idx` (`Product_id` ASC) VISIBLE,
  INDEX `fk_Category_has_Product_Category1_idx` (`Category_id` ASC) VISIBLE,
  CONSTRAINT `fk_Category_has_Product_Category1`
    FOREIGN KEY (`Category_id`)
    REFERENCES `Amazon`.`Category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Category_has_Product_Product1`
    FOREIGN KEY (`Product_id`)
    REFERENCES `Amazon`.`Product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
