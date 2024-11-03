# Spotify-End-to-End-Data Engineering Project
## Introduction
In this project, we've developed a comprehensive data pipeline on Amazon Web Services (AWS) utilizing data extracted from kaggle dataset. The raw datasets (5 csv files) includes a wide range of artist and songs-related information which requires a lot of data cleaning (cleaned and normalised down into 3 csv files) before loading the the refined data into an AWS S3. Our focus remains on optimizing data processing while upholding security and accessibility standards within the AWS environment, enabling robust analytics and decision-making capabilities for the top spotify songs dataset and beyond.

## Architecture
![Architechtural Diagram](https://github.com/binodkshetry/Spotify-end-to-end-data-engineering-project/blob/main/Architechture.PNG)

## About Data
I have extracted raw data file from kaggle dataset and performed the cleaning job with power BI transformation tool providing the comprehendive dataset about the artist, tracks and albums in 3 respective .csv (artists.csv, albums.csv and tracks.csv) file that is ready to staged in AWS S3 bucket for further analysis and processing using AWS Glue (ETL job). This data can be utilized for a variety of purposes, including statistical analysis, visualization, and machine learning applications within the domain of songs and entertainment.

