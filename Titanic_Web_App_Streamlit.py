import streamlit as st
import pandas as pd
import pickle
import  numpy as np

model = pickle.load(open(r"Titanic.pkl","rb"))

# Main Function
def main():
    st.title("Titanic Survival Prediction")
    st.header("Check Out Your Chances of Survival, If You Had a Chance To Be OnBoard")

    # Sidebar configuration:
    st.sidebar.header("To Know More About Titanic Tragedy")
    st.sidebar.markdown("[Click Here](https://www.britannica.com/topic/Titanic)")

    # Adding Feature Inputs:
    
    col1, col2 = st.columns(2)
    with col1:
        pclass = st.selectbox("Please Select Your Ticket Class",[1,2,3])
    
    with col2:
        sex = st.selectbox('Select Your Gender:', ["male", "female"])
        if sex == "male":
            sex = 0
        else: 
            sex = 1    
    
    
    age = st.slider("Please Select Your Age:",1,85,30)

    col3, col4 = st.columns(2)
    with col3:
        sibSp = st.selectbox("How many siblings or spouses are travelling with you?",[0,1,2,3,4,5,6,7,8])
    
    with col4:
        parch = st.selectbox("How many parents or childrens are travelling with you? ",[0,1,2,3,4,5,6,7,8])
    
    fare = st.slider("Please Select your Fare: ",5,550,40)
    
    Boarding_Location = st.selectbox("Please Select your Boarding Point",["Cherbourg","Southhampton","Queenstown"])
    if Boarding_Location == 'Cherbourg':
        Boarding_Location = 0
    elif Boarding_Location == 'Southampton':
        Boarding_Location = 1
    else:
        Boarding_Location = 2

    # Gathering the Data so that we can collect user entered inputs:
    data = {"Pclass":pclass,"Sex":sex,"Age":age,"SibSp":sibSp,"Parch":parch,"Fare":fare,'Embarked':Boarding_Location}
    df = pd.DataFrame(data, index=[0])   
    return df

data = main() 

# Prediction:
if st.button("Predict"):                                                                
    result = model.predict(data)                                                        
    proba=model.predict_proba(data)                                                        

    if result[0] == 1:
        st.write("Congratulations!!! You Are Alive.")
    else:
        st.write("Unfortunately, You Are Dead.")

# Prepared By.
st.subheader('Prepared By')
st.write("Shohaib Shaikh")



