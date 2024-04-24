import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Preprocessing function
def preprocess_data(df):
    df.drop(['User_ID', 'Product_ID', 'Gender', 'City_Category',
             'Marital_Status', 'Product_Category_3'], axis = 1, inplace = True)

    df['Product_Category_2'].fillna(df['Product_Category_2'].median(), inplace = True)
    df['Product_Category_2'] = df['Product_Category_2'].astype('int')

    df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].apply(lambda x : str(x).replace('4+', '4'))
    df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].astype('int')

    df['Age'] = df['Age'].map(
        {'0-17' : 1,
         '18-25' : 2,
         '26-35' : 3,
         '36-45' : 4,
         '46-50' : 5,
         '51-55' : 6,
         '55+' : 7
         })

    return df

# Load and preprocess training data (adjust the path if needed)
train = pd.read_csv('train.csv')
train = preprocess_data(train.copy()) 

# Feature scaling (assuming you have a scaler object)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = train.drop('Purchase', axis = 1)
X = scaler.fit_transform(X) 

# Streamlit App
st.title("Customer Purchase Prediction 🌼")

age = st.selectbox("Select Age Range", 
                   ['0-17', '18-25', '26-35', '36-45', '46-50', '51-55', '55+'])

occupation_code = st.number_input("Occupation Code", min_value=0)  
stay_in_city = st.number_input("Years in Current City", min_value=0)
product_category_1 = st.number_input("Product Category 1", min_value=0) 
product_category_2 = st.number_input("Product Category 2", min_value=0)

if st.button('Predict'):
    age_value = {'0-17': 1, '18-25': 2, '26-35':3, '36-45':4, '46-50':5, '51-55': 6, '55+':7 }[age]

    features = [age_value, occupation_code, stay_in_city, product_category_1, product_category_2]
    final_features = [np.array(features)]
    prediction = model.predict(scaler.transform(final_features))[0]

    st.success(f'Predicted purchase amount: ${round(prediction)}')
