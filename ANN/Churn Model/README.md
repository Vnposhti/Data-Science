# Customer Churn Prediction and Salary Estimation Using ANN

## Overview
This repository contains an Artificial Neural Network (ANN) model designed to predict customer churn in a banking context. The model identifies whether a bank customer is likely to leave (churn) based on various features. Additionally, the repository includes a regression model to estimate customer salaries using a similar ANN approach.

## Main Components
The main components of this repository include:

- **`Churn_Modelling.csv`**: Contains the data used for both the churn prediction and salary estimation models.
- **`Churn_modelling.ipynb`**: Jupyter Notebook implementing the ANN model for churn prediction.
- **`Churn_Prediction.ipynb`**: Script to make predictions using the trained models.
- **`app.py`**: A user-friendly Streamlit web application to interact with the models.
- **`Churn_hyperparametertuning.ipynb`**: Jupyter Notebook for hyperparameter tuning to optimize model performance.
- **Preprocessing Files**: Includes Pickle files for encoders and scalers used during data preprocessing.

## How to Use
1. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the web application:
    ```bash
    streamlit run app.py
    ```

3. Explore the notebooks for detailed analysis and model building.

---

### Feel free to contribute to this project by submitting issues or pull requests!