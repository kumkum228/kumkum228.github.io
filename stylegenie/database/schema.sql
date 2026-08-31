-- ============================================================================
-- StyleGenie – Database bootstrap (PHASE 1)
-- ============================================================================
-- This file currently just creates the empty database.
-- In PHASE 5 we will fill it with all tables (users, products, categories,
-- brands, cart, wishlist, orders, reviews, conversations, ...) and 40-50
-- sample products.
--
-- How to run it:
--   Option A (command line):
--       mysql -u root -p < schema.sql
--   Option B (phpMyAdmin / XAMPP):
--       Open phpMyAdmin -> Import -> choose this file -> Go
-- ============================================================================

CREATE DATABASE IF NOT EXISTS stylegenie_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE stylegenie_db;

-- Tables and sample data will be added here in PHASE 5.
