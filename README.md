# US Visa Approval 

**Problem Statement:**
Build a machine learning model that can predict visa approvals based on the provided information. Model can be used to streamline the application process for both immigration authorities and potential employers.

This repository contains an End-to-End implementation for predicting visa approvals for foreign workers in the US. The data at hand; provides features about both the applicant and the offered job, allowing you to build models to automate the approval process.
`DataSet` : [link](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)
**Data Summary:**
* **Applicant Information:**
    * `case_id`: Unique identifier for each visa application (categorical).
    * `continent`: Continent of origin for the applicant (categorical).
    * `education_of_employee`: Educational background of the applicant (categorical).
    * `has_job_experience` (Y/N): Indicates if the applicant has prior work experience (binary).
    * `requires_job_training` (Y/N): Indicates if the applicant requires job training upon arrival (binary).
* **Employer Information:**
    * `no_of_employees`: Number of employees at the applicant's potential employer's company (numerical).
    * `yr_of_estab`: Year the applicant's potential employer's company was established (numerical).
* **Job Details:**
    * `region_of_employment`: Intended region of employment within the US for the applicant (categorical).
    * `prevailing_wage`: Average wage offered for similar positions in the applicant's intended job location (numerical).
    * `unit_of_wage`: Unit in which the prevailing wage is measured (categorical - e.g., "Hourly", "Weekly").
    * `full_time_position` (Y/N): Indicates if the offered position is full-time (binary).
* **Decision:**
    * `case_status`: Indicates whether the visa application was approved or denied (binary - target variable).


## How to setup the code?

```bash
conda create -n visa python=3.8 -y
```

```bash
conda activate visa
```

```bash
pip install -r requirements.txt
```


## Task To Complete:-

- [x] Data Ingestion
- [x] Data Trasformation
- [x] Data Validation
- [x] Model Trainer
- [x] Model Evaluation
- [x] Model Pusher
- [ ] Prediction Pipeline 
- [ ] Source code analysis with LLM
- [ ] Integrate with the main prediction pipeline
- [ ] Streamlit application for user interation
- [ ] Deploy in Cloud
