# Machine Learning for V2X Communication Data



### Overview

This repository represents an application of Machine Learning (ML) on V2X communication data. Vehicle-to-Everything (V2X) data collected in urban environments often contains missing values due to interference, obstructions, weather conditions, and sensor failures. Since creating a complete real-world dataset is not practical, this project applies ML techniques to reconstruct missing data and generate realistic V2X measurements.

### 

#### Objective

The main objectives of this project are:

1. Data Imputation:
   Recover missing values in V2X measurements.
   The [Berlin V2X implementation](https://github.com/adikansara23-oss/ML-V2X-Project/tree/main/Berlin%20V2X%20Implementation) demonstrates the complete data imputation pipeline, including preprocessing, feature engineering, and application of ML models for filling missing data.
   The [V2I implementation](https://github.com/adikansara23-oss/ML-V2X-Project/tree/main/V2I%20Implementation) applies forward fill, backward fill, and KNN imputation methods to a similar dataset for handling missing values.
2. Synthetic Data Generation:

 	Generate realistic, high-resolution data using deep learning models.

### 

#### Dataset

This project uses the Berlin V2X dataset (\[cellular data](Berlin V2X Implementation/cellular\_dataframe.parquet)), which contains spatial-temporal communication measurements collected in an urban environment and includes inherent missing data. Each feature of the dataset is described in the \[Feature Description](Feature Description.xlsx) file. Features are prioritized for data imputation and synthetic data generation based on their importance ranking and percentage of missing values, as detailed in the \[Feature Analysis](Feature Analysis.xlsx) file.

### 

#### Methodology

* Machine Learning models for missing data imputation
* Deep Learning models such as GANs and VAEs for synthetic data generation
* Spatial-temporal learning to reconstruct realistic communication patterns
