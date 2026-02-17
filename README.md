# Machine Learning for V2X Communication Data



## Overview
This repository represents an application of Machine Learning (ML) on V2X communication data. Vehicle-to-Everything (V2X) data collected in urban environments often contains missing values due to interference, obstructions, weather conditions, and sensor failures. Since creating a complete real-world dataset is not practical, this project applies ML techniques to reconstruct missing data and generate realistic V2X measurements.

## 

### Objective
The main objectives of this project are:
1. Data Imputation:
   Recover missing values in V2X measurements.
   The [Berlin V2X implementation](https://github.com/adikansara23-oss/ML-V2X-Project/tree/main/Berlin%20V2X%20Implementation) demonstrates the complete data imputation pipeline, including preprocessing, feature engineering, and application of ML models for filling missing data.
   The [V2I implementation](https://github.com/adikansara23-oss/ML-V2X-Project/tree/main/V2I%20Implementation) applies forward fill, backward fill, and KNN imputation methods to a similar dataset for handling missing values.
2. Synthetic Data Generation:
   Generate realistic, high-resolution data using deep learning models.

### 

### Dataset
This project uses the Berlin V2X dataset ([cellular data](https://github.com/adikansara23-oss/ML-V2X-Project/blob/82355affedeed0ff971406fedc9bded8c64a964a/Berlin%20V2X%20Implementation/cellular_dataframe.parquet)), which contains spatial-temporal communication measurements collected in an urban environment and includes inherent missing data. Each feature of the dataset is described in the [Feature Description](https://github.com/adikansara23-oss/ML-V2X-Project/blob/82355affedeed0ff971406fedc9bded8c64a964a/Feature%20Description.xlsx) file. These features have been sorted for the process of data imputation and data generation based on the priority ranking and percentage of missing values, as detailed in the [Feature Analysis](https://github.com/adikansara23-oss/ML-V2X-Project/blob/82355affedeed0ff971406fedc9bded8c64a964a/Feature%20Analysis.xlsx) file.

### 

### Methodology
* Machine Learning models for missing data imputation
* Deep Learning models such as GANs and VAEs for synthetic data generation
* Spatial-temporal learning to reconstruct realistic communication patterns
