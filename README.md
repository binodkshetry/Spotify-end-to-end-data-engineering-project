# Spotify-End-to-End-Data Engineering Project
## Introduction
In this project, we've developed a comprehensive data pipeline on Amazon Web Services (AWS) utilizing data extracted from kaggle dataset. The raw datasets (5 csv files) includes a wide range of artist and songs-related information which requires a lot of data cleaning (cleaned and normalised down into 3 csv files) before loading the the refined data into an AWS S3. Our focus remains on optimizing data processing while upholding security and accessibility standards within the AWS environment, enabling robust analytics and decision-making capabilities for the top spotify songs dataset and beyond.

## Architecture
![Architechtural Diagram](https://github.com/binodkshetry/Spotify-end-to-end-data-engineering-project/blob/main/Architechture.PNG)

## About Data
I have extracted raw data file from kaggle dataset and performed the cleaning job with power BI transformation tool providing the comprehendive dataset about the artist, tracks and albums in 3 respective .csv (artists.csv, albums.csv and tracks.csv) file that is ready to staged in AWS S3 bucket for further analysis and processing using AWS Glue (ETL job). This data can be utilized for a variety of purposes, including statistical analysis, visualization, and machine learning applications within the domain of songs and entertainment.

## ETL
In this project we build data pipeline using Amazon S3 bucket as a data source, AWS Glue detects the schema of the data at the specified location (created directories for both staging and transformed data)from one of the files, or by using the file you specify as a sample file. Schema detection occurs when we use the Infer schema button. If you change the Amazon S3 location or the sample file, then you must choose Infer schema again to perform the schema detection using the new information. Here GLue ETL performs required transformation before storing the transformed data into S3 bucket.
![AWS Glue ETL job](https://github.com/binodkshetry/Spotify-end-to-end-data-engineering-project/blob/main/ETL.PNG)

## Services Used
* AWS S3 (Simple Storage Service): Amazon S3 (Simple Storage Service) is a highly scalable object storage service that can store and retrieve any amount of data from anywhere on the web. It is commonly used to store and distribute large media files, data backups and static website files.

* AWS Glue: AWS Glue is a serverless data integration service that makes it easy for analytics users to discover, prepare, move, and integrate data from multiple sources. You can use it for analytics, machine learning, and application development.

* AWS CloudWatch: Amazon CloudWatch is a monitoring service for AWS resources and the applications you run on them. You can use CloudWatch to collect and track metrics, collect and monitor log files, and set alarms.

* Glue Crawler: AWS Glue Crawler is a fully managed service that automatically crawls your data sources, identifies data formats, and infers schemas to create an AWS Glue Data Catalog.

* AWS Glue Data Catalog: AWS Glue Data Catalog is a fully managed metadata repository that makes it easy to discover and manage data in AWS. You can use the Glue Data Catalog with other AWS services, such as Athena.

* Amazon Athena: Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. You can use Athena to analyze data in your Glue Data Catalog or in other S3 buckets.

* Amazon Quicksight: Amazon QuickSight is a fast business analytics service to build visualizations, perform ad hoc analysis, and quickly get business insights from your data.
