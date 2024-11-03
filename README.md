# Spotify-End-to-End-Data Engineering Project
## Introduction
In this project, we've developed a comprehensive data pipeline on Amazon Web Services (AWS) utilizing data extracted from kaggle dataset. The raw datasets (5 csv files) includes a wide range of artist and songs-related information which requires a lot of data cleaning (cleaned and normalised down into 3 csv files) before loading the the refined data into an AWS S3. Our focus remains on optimizing data processing while upholding security and accessibility standards within the AWS environment, enabling robust analytics and decision-making capabilities for the top spotify songs dataset and beyond.

## Pre-requisites
1. [AWS Account](https://aws.amazon.com/console/) (most of the services used are FREE, You can run the ETL and query job for less than a dollar)
2. Setting up IAM, roles and attached relavant policies to the user.
3. Basic knowledge of PySpark for Data Modelling and ETL job (or Visual ETL can make it more easy to perform ETL job)

## Architecture
![Architechtural Diagram](https://github.com/binodkshetry/Spotify-end-to-end-data-engineering-project/blob/main/Architechture.PNG)

## About Data
I have extracted raw data file from kaggle dataset and performed the cleaning job with power BI transformation tool providing the comprehendive dataset about the artist, tracks and albums in 3 respective .csv (artists.csv, albums.csv and tracks.csv) file that is ready to staged in AWS S3 bucket for further analysis and processing using AWS Glue (ETL job). This data can be utilized for a variety of purposes, including statistical analysis, visualization, and machine learning applications within the domain of songs and entertainment.

## Data Modelling & ETL
In this project we build data pipeline using Amazon S3 bucket as a data source, AWS Glue detects the schema of the data at the specified source location, perform ETL job (in this project, we use inner join, and drop fields to avoid redundancy in data) and stored the transformed data into the destination directory inside S3 bucket which then crawler used to create metadata tables in your data catalog. Amazon Athena then makes it easy to analyze data by instantly querying data using data catalogue for further visualization.
![AWS Glue ETL job](https://github.com/binodkshetry/Spotify-end-to-end-data-engineering-project/blob/main/ETL.PNG)

## Services Used
* AWS S3 (Simple Storage Service): Amazon S3 (Simple Storage Service) is a highly scalable object storage service that can store and retrieve any amount of data from anywhere on the web. It is commonly used to store and distribute large media files, data backups and static website files.

* AWS Glue: AWS Glue is a serverless data integration service that makes it easy for analytics users to discover, prepare, move, and integrate data from multiple sources. You can use it for analytics, machine learning, and application development.

* AWS CloudWatch: Amazon CloudWatch is a monitoring service for AWS resources and the applications you run on them. You can use CloudWatch to collect and track metrics, collect and monitor log files, and set alarms.

* Glue Crawler: AWS Glue Crawler is a fully managed service that automatically crawls your data sources, identifies data formats, and infers schemas to create an AWS Glue Data Catalog.

* AWS Glue Data Catalog: AWS Glue Data Catalog is a fully managed metadata repository that makes it easy to discover and manage data in AWS. You can use the Glue Data Catalog with other AWS services, such as Athena.

* Amazon Athena: Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. You can use Athena to analyze data in your Glue Data Catalog or in other S3 buckets.

* Amazon Quicksight: Amazon QuickSight is a fast business analytics service to build visualizations, perform ad hoc analysis, and quickly get business insights from your data.
  

## Project Execution Flow
* Stores Raw Data in AWS S3 -> Trigger Transform Fuction (Run spotify-ETL-PySpark code to transform the raw staging data) -> Stores Transformed Data in AWS S3 (Destination Directory)-> AWS Glue Crawler runs on the Transformed Data and Generated AWS Glue Data Catalog -> Query the Data using Athena -> Visualization using QuickSight
