# Digital Payment Platform Prediction System

A Django based Machine Learning web application for analyzing digital payment related data and generating prediction results using a trained Gradient Boosting Regressor model.

## Overview

The Digital Payment Platform Prediction System combines Python, Django, data preprocessing, and Machine Learning into a web based application.

The system allows users to register, log in, view transaction data, analyze features, train the Machine Learning model, and generate predictions through a web interface.

The project focuses on digital payment platforms including:

- Paytm
- Google Pay
- PhonePe
- Amazon Pay

The system is designed to analyze digital payment related information and provide data driven prediction results.

---

## Objectives

The main objectives of this project are:

- Analyze digital payment related data.
- Predict digital payment related outcomes.
- Identify important factors affecting digital payment usage.
- Apply Machine Learning to transaction and customer data.
- Build a web based prediction application.
- Provide separate user and admin functionality.
- Allow users to view and analyze datasets.
- Train and evaluate the Machine Learning model.
- Generate predictions using user input.

---

## Key Features

### User Module

- User registration
- User login
- User dashboard
- Dataset viewing
- Machine Learning training
- Analytics
- Prediction
- Logout

### Admin Module

- Admin login
- View registered users
- Manage users
- Activate users
- Delete users
- Monitor application data

### Machine Learning

- Data preprocessing
- Feature selection
- Feature scaling
- Gradient Boosting Regressor
- Model training
- Model evaluation
- Saved Machine Learning model
- Prediction using user input

### Analytics

- Dataset analysis
- Feature analysis
- Correlation analysis
- Feature importance
- Prediction analysis

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Framework | Django |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Machine Learning Model | Gradient Boosting Regressor |
| Preprocessing | StandardScaler |
| Development Tool | Visual Studio Code |
| Version Control | Git, GitHub |

---

## Machine Learning Workflow


Dataset
   |
   v
Data Preprocessing
   |
   v
Feature Selection
   |
   v
Train/Test Split
   |
   v
StandardScaler
   |
   v
Gradient Boosting Regressor
   |
   v
Model Training
   |
   v
Model Evaluation
   |
   v
Save Trained Model
   |
   v
User Input
   |
   v
   ---

## Project Highlights

### Backend

The backend is developed using Django and handles:

- User authentication
- Admin authentication
- Database operations
- Dataset processing
- Machine Learning integration
- Prediction requests
- Application routing

### Machine Learning

The Machine Learning component handles:

- Data preprocessing
- Feature scaling
- Model training
- Model evaluation
- Prediction generation
- Model persistence

### Web Application

The web interface provides:

- User registration
- User login
- Dashboard
- Dataset viewer
- Training interface
- Analytics interface
- Prediction interface
- Admin dashboard

---

## Important Files

| File | Purpose |
|---|---|
| `manage.py` | Django project management |
| `digital_payment/settings.py` | Django configuration |
| `digital_payment/urls.py` | URL routing |
| `admins/views.py` | Admin related views |
| `users/views.py` | User related views |
| `users/models.py` | User database models |
| `rg.pkl` | Trained Machine Learning model |
| `scaler.pkl` | Feature scaling model |
| `.gitignore` | Files excluded from Git |

---

## Prediction Pipeline

User enters values
        |
        v
Input validation
        |
        v
Feature preprocessing
        |
        v
StandardScaler
        |
        v
Load rg.pkl
        |
        v
Gradient Boosting Regressor
        |
        v
Generate prediction
        |
        v
Display result
Prediction
   |
   v
Display Result

## Key Learning Outcomes

Through this project, the following technical areas were implemented:

- Python programming
- Django web development
- Django MVT architecture
- User authentication
- Admin management
- Database operations
- Data preprocessing
- Feature scaling
- Machine Learning model training
- Model evaluation
- Prediction integration
- Git and GitHub

---

## Project Outcome

The project demonstrates how a Machine Learning model can be integrated into a Django web application to process user input and generate prediction results.

The application provides separate user and admin functionality together with dataset viewing, model training, analytics, and prediction features. :chatgpt-content-reference{index="0"}

---

## Future Improvements

- Deploy the application to a cloud platform
- Add a larger dataset
- Compare multiple Machine Learning algorithms
- Add interactive data visualizations
- Develop REST APIs
- Improve application security
- Add automated model retraining
- Add real time prediction
- Add production database support

---

## Project Team

**C. Darshini**  
**CH. Poojitha**  
**G. Kavyasree**  
**A. Sahithya**  
**C. Aravind**

### Project Guide

**Dr. Y. Ravi Kumar, Ph.D, PDF (USA)**  
Professor  
Department of Computer Science and Engineering  
Sree Rama Engineering College

---

## Author

**CH. Poojitha**

GitHub:  
https://github.com/ppoojitha76

Project Repository:  
https://github.com/ppoojitha76/digital-payment-platform

---

## License

This project is licensed under the MIT License.

Important: only use the screenshot paths after you actually create the screenshots folder and upload those images. Otherwise the images will show as broken links on GitHub. Your project presentation has the corresponding application screens, including training, dataset, and prediction.  FINAL REVIEW PPT (1)
