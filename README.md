# WorkSpot Preference Estimation using Machine Learning based on Activity-Based Workplaces

## Overview

This project predicts an employee's preferred workplace using Machine Learning techniques based on workplace behavior, demographic factors, and work-life balance attributes.

The application helps organizations understand employee workplace preferences in Activity-Based Work Environments and supports better workspace planning and employee satisfaction.

The project uses Machine Learning algorithms such as Random Forest and XGBoost to classify workplace preferences into multiple categories.

---

## Preferred Workplace Categories

* Home
* Office
* Remote
* Hybrid
* Co-working Space

---

## Features

* Balanced multi-class classification dataset
* Data preprocessing and encoding
* Random Forest model with Hyperparameter Tuning
* XGBoost model implementation
* Model comparison and evaluation
* Dynamic prediction using Streamlit UI
* Real-time workplace preference prediction
* Interactive and user-friendly web application

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Matplotlib
* Joblib

---

## Dataset Features

The dataset contains the following features:

| Feature                 | Description                       |
| ----------------------- | --------------------------------- |
| Age                     | Employee age                      |
| Gender                  | Male/Female                       |
| Working Hours           | Daily working hours               |
| Commute Time            | Travel time to office (minutes)   |
| Distance from Home      | Distance from workplace (km)      |
| Work Experience         | Years of experience               |
| Department              | Employee department               |
| Work-Life Balance Score | Employee work-life balance rating |
| Preferred Workplace     | Target prediction variable        |

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Label Encoding for categorical features
4. Train-Test Split
5. Model Training
6. Hyperparameter Tuning
7. Model Evaluation
8. Model Comparison
9. Deployment using Streamlit

---

## Algorithms Used

### Random Forest Classifier

* Ensemble learning algorithm
* Handles multi-class classification efficiently
* Used with hyperparameter tuning for improved performance

### XGBoost Classifier

* Gradient boosting algorithm
* Provides high accuracy and strong performance
* Effective for structured/tabular datasets

---

## Model Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Cross Validation

---

## Streamlit Application

The project includes a Streamlit-based web application where users can:

* Enter employee details dynamically
* Predict workplace preference instantly
* Interact with a simple and responsive UI

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jayavardhan-sv/workspot-estimation.git
```

Move into the project directory:

```bash
cd workspot-estimation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Deployment

The project is deployed using Streamlit Cloud.

Live App : https://workspot-estimation-ixbomyuhyqh8ujyv9sqnwk.streamlit.app/

---
Output :

<img width="619" height="439" alt="Image" src="https://github.com/user-attachments/assets/c8281ddb-6172-43ae-b4bd-bd3d5b1b949c" />

---
## Future Enhancements

* Add deep learning models
* Add employee analytics dashboard
* Add recommendation system for workspace optimization
* Deploy using Docker and Cloud platforms
* Integrate real-world HR datasets

---

## Business Impact

This project can help organizations:

* Improve employee productivity
* Enhance workplace flexibility
* Optimize workspace allocation
* Support hybrid work strategies
* Improve employee satisfaction and work-life balance

---

## Author

Jayavardhan

Data Science and Machine Learning Enthusiast
