-- Create the schema
CREATE SCHEMA bank;

-- Create bank_mapping table with unique bank_shortcode
DROP TABLE IF EXISTS bank.bank_mapping;
CREATE TABLE bank.bank_mapping (
    bank_name VARCHAR(255) NOT NULL UNIQUE,
    bank_short_code VARCHAR(10) NOT NULL UNIQUE,
    created_on BIGINT NOT NULL,  -- epoch timestamp IST
    PRIMARY KEY (bank_short_code)
);

-- Create bank_branch_mapping table with direct references from bank_mapping
DROP TABLE IF EXISTS bank.bank_branch_mapping;
CREATE TABLE bank.bank_branch_mapping (
    bank_name VARCHAR(255) NOT NULL REFERENCES bank.bank_mapping(bank_name),
    bank_name_shortcode VARCHAR(10) NOT NULL REFERENCES bank.bank_mapping(bank_short_code),
    branch_name VARCHAR(255) NOT NULL,
    branch_shortcode VARCHAR(10) NOT NULL UNIQUE,
    created_on BIGINT NOT NULL,  -- epoch timestamp IST
    unique_id VARCHAR(50) NOT NULL UNIQUE,  -- unique_id as per specification
    PRIMARY KEY (unique_id)
);

-- Create user_details table with references to previous tables
DROP TABLE IF EXISTS bank.user_details;
CREATE TABLE bank.user_details (
    incrementing_number SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    social_security_number VARCHAR(11) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    pin_code VARCHAR(10) NOT NULL,
    created_on_epoch_ist BIGINT NOT NULL,
    branch_shortcode VARCHAR(10) NOT NULL REFERENCES bank.bank_branch_mapping(branch_shortcode),
    unique_id VARCHAR(50) NOT NULL UNIQUE
);
