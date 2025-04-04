# Phishing URL Detection Using Machine Learning

This project is an end-to-end machine learning pipeline to detect phishing URLs. It covers everything from data preprocessing and feature engineering to model training, hyperparameter tuning, evaluation, and a final CLI-based tool for predictions using the model. Three different datasets were used with three different models analyzing them, and the best performance was used for a CLI prediction tool. 

## Problem Statement

Phishing is a common cyberattack that uses fraudulent URLs to deceive users. This kind of deceit may lead to identity theft, financial loss, and data breaches. Therefore, it's important to know which URLs are phishing before going to the website.

## Project Highlights

- **Exploratory Data Analysis (EDA):**
  - Visualized feature distributions and class imbalance
  - Identified correlation patterns and outlier effects

- **Feature Engineering:**
  - Extracted 19 features from one of the three datasets such as:
    - `url_length`, `n_dots`, `n_hyphens`, `n_slash`, `n_questionmark`, etc.
  - Used `RobustScaler` to normalize features with outliers
  - Selected top features using mutual information scores

- **Model Training & Evaluation:**
  - Trained and benchmarked three models:
    - `CatBoostClassifier`
    - `XGBoostClassifier`
    - `MLPClassifier` (Multi-layer Perceptron)
  - Used `GridSearchCV` for hyperparameter tuning
  - Best model: CatBoost and XGBoost with accuracy score of around 90% on two of three datasets
  - Evaluation metrics included classification report and confusion matrix

- **CLI-Based Tool:**
  - Extracts relevant features from input URLs
  - Applies robust scaling
  - Predicts phishing with confidence score

## Running The Project

1. Download repo:

```
git clone https://github.com/julian-ornelas/phishing-link-detection.git
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS/Linux:

```
source venv/bin/activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

## Using CLI Tool

Ensure you are in the `model_deployment` directory first:
```
python model_deployment/run.py "URL"
```