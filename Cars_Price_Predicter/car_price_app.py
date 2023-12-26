import pandas as pd
import streamlit as st
import pickle

cars_df = pd.read_csv("car-price.csv")

st.write(
    """
    # Cars24 Used Car Price Prediction
    """
)

# creating a dictionary to encode categorical features
encode_dict = {
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "seller_type": {"Dealer":1, "Individual":2, "Trustmark Dealer":3},
    "transmission_type": {"Manual":1, "Automatic":2}
}

def model_pred(fuel_type, transmission_type, engine, seller_type):

    # loading the model
    with open('car_pred.pkl', mode = 'rb') as file:
        reg_model = pickle.load(file)

    input_features = [[2018.0, seller_type, 40000, fuel_type, transmission_type, 19.70, engine, 86.3]]
    return reg_model.predict(input_features)

# Layout
col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col1.slider("Set the engine power", 500, 5000, step=100)

transmission_type = col2.selectbox("Select transmission type", ["Manual", "Automatic"])
seller_type = col2.selectbox("Select seller type", ["Dealer", "Individual", "Trustmark Dealer"])

if(st.button("Predict Price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    seller_type = encode_dict['seller_type'][seller_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seller_type)
    st.text(f"Predicted price of the car: {price}")


st.dataframe(cars_df.head())


# adding my name
c1, c2, c3, c4 = st.columns(4)
with c4:
    st.markdown(
        """
        ---
        **Made by :-** *Swapnil G.*
        """
    )


