# ETL Data Validation Framework

## Overview

This project demonstrates ETL Testing and Data Validation using Python, SQL, and Pandas. It validates data between source and target systems to ensure data quality and accuracy after ETL processing.

## Features

* Record Count Validation
* Null Validation
* Duplicate Validation
* Source-to-Target Data Comparison
* Incremental Load Validation
* Data Quality Checks

## Technologies Used

* Python
* SQL (Oracle SQL)
* Pandas
* Git
* GitHub

## Project Structure

ETL-data-validation-framework

├── scripts
│   ├── record_count_validation.py
│   ├── null_validation.py
│   ├── duplicate_validation.py
│   └── data_comparison.py

├── sql
│   ├── duplicate_check.sql
│   ├── null_check.sql
│   ├── record_count_validation.sql
│   ├── incremental_load.sql
│   ├── city_wise_customer_count.sql
│   └── unique_customer_validation.sql

├── source_data
│   └── customers_source.csv

├── target_data
│   └── customers_target.csv

├── requirements.txt
├── README.md
└── .gitignore


## Sample Validations

### Record Count Validation
Validates that source and target tables contain the same number of records.

### Null Validation
Checks for unexpected NULL values in critical columns.

### Duplicate Validation
Identifies duplicate customer records.

### Incremental Load Validation
Validates newly loaded records based on the last updated date.

### City-wise Customer Count
Calculates the number of customers in each city.

### Unique Customer Validation
Validates that customer IDs are unique and identifies duplicate IDs.

## Author

Abdulla As

ETL Tester | SQL | Python | Data Warehouse Testing
