from django.conf import settings
from django.shortcuts import render, redirect
import pandas as pd
from .models import UserRegistrationModel
from django.contrib import messages


def UserRegisterActions(request):
    if request.method == 'POST':
        user = UserRegistrationModel(
            name=request.POST['name'],
            loginid=request.POST['loginid'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            locality=request.POST['locality'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            status='waiting'
        )
        user.save()
        messages.success(request,"Registration successful!")
    return render(request, 'UserRegistrations.html') 


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                data = {'loginid': loginid}
                print("User id At", check.id, status)
                return render(request, 'users/userbase.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

def forgotPassword(request):
    if request.method=="POST":
        loginid=request.POST.get('loginid')
        newpassword= request.POST.get('newpassword')
        conformpassword=request.POST.get('conformpassword')
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid)
            if newpassword==conformpassword:
                check.password=newpassword
                check.save()
                messages.success(request,'password saved successfully')
                return render(request, 'UserLogin.html')

            else:
                messages.error(request,"PasswordMismatched")
                return render(request,"users/forgot.html")
        except:
            messages.error(request,'Loginid not found please enter carefully')
            return render(request,"users/forgot.html")
    else:
        return render(request,"users/forgot.html")
    
import pandas as pd
from django.shortcuts import render

def dataset_view(request):
    df = pd.read_csv('media\DigitalPay_balanced_dataset (1).csv')  # Adjust path if needed
    df = df.head(100)  # Limit rows for performance
    context = {'df': df}
    return render(request, 'users/datasetview.html', context)


def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})

def index(request):
    return render(request,"index.html")


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from django.shortcuts import render

def training(request):
    # Load dataset
    df = pd.read_csv(r'media\DigitalPay_balanced_dataset (1).csv')

    # Drop ID and unused columns
    df.drop(['Customer_ID', 'LTV'], axis=1, inplace=True)

    # Define top 8 features
    selected_features = [
        'Cashback_Received',
        'Min_Transaction_Value',
        'Issue_Resolution_Time',
        'Avg_Transaction_Value',
        'Max_Transaction_Value',
        'Last_Transaction_Days_Ago',
        'Total_Spent',
        'Loyalty_Points_Earned'
    ]

    # Prepare dataset
    X = df[selected_features]
    y = df['Customer_Satisfaction_Score']

    # Train/Test split
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    train_X_scaled = scaler.fit_transform(train_X)
    test_X_scaled = scaler.transform(test_X)

    # Train model
    model = GradientBoostingRegressor()
    model.fit(train_X_scaled, train_y)

    # ✅ Save the model
    with open('rg.pkl', 'wb') as f:
        pickle.dump(model, f)

    # ✅ Save the scaler
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    # Evaluate model
    test_predictions = model.predict(test_X_scaled)
    mae = mean_absolute_error(test_y, test_predictions)
    mse = mean_squared_error(test_y, test_predictions)
    r2 = r2_score(test_y, test_predictions)

    print("\n📊 Regression Metrics on Test Set:")
    print(f"• Mean Absolute Error (MAE): {mae:.2f}")
    print(f"• Mean Squared Error (MSE): {mse:.2f}")
    print(f"• R² Score: {r2:.4f}")

    return render(request, 'users/accuracy.html',{})
    return render(request, 'users/training.html', {"mae": mae, "mse": mse, 'r2': r2})

import pickle
import pandas as pd
from django.shortcuts import render

def prediction(request):
    score = None
    if request.method == "POST":
        # Load model and scaler
        with open('rg.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        # Get data from form
        new_customer = pd.DataFrame([{
            'Cashback_Received': float(request.POST['Cashback_Received']),
            'Min_Transaction_Value': float(request.POST['Min_Transaction_Value']),
            'Issue_Resolution_Time': float(request.POST['Issue_Resolution_Time']),
            'Avg_Transaction_Value': float(request.POST['Avg_Transaction_Value']),
            'Max_Transaction_Value': float(request.POST['Max_Transaction_Value']),
            'Last_Transaction_Days_Ago': float(request.POST['Last_Transaction_Days_Ago']),
            'Total_Spent': float(request.POST['Total_Spent']),
            'Loyalty_Points_Earned': float(request.POST['Loyalty_Points_Earned'])
        }])

        # Predict score
        new_scaled = scaler.transform(new_customer)
        score = model.predict(new_scaled)[0]

    return render(request, 'users/prediction.html', {'score': score})
