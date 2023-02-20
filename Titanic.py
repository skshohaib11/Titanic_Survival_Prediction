import streamlit as st
import pandas as pd
import pickle
import  numpy as np

model = pickle.load(open(r"C:\Users\sksho\Desktop\My Github Repo\Titanic Survival\Titanic.jpg","rb"))

# Main Function
def main():
    st.title("Titanic Survival Prediction")
    st.image(r"C:\Users\sksho\Desktop\Streamlit\streamlit Dev\Titanic_Sink.jpg", caption= 'Titanic')
    st.header("Check Out Your Chances of Survival, If You Had a Chance To Be OnBoard")

    # Sidebar configuration:
    st.sidebar.header("To Know More About Titanic Tragedy")
    st.sidebar.markdown("[Click Here](https://www.britannica.com/topic/Titanic)")

    # Adding Feature Inputs:

    age = st.slider("Please Select Your Age:",1,85,30)

    fare = st.slider("Please Selct your Fare: ",5,550,40)
    
    col1, col2 = st.columns(2)
    with col1:
        sibSp = st.selectbox("How many siblings or spouses are travelling with you?",[0,1,2,3,4,5,6,7,8])
    with col2:
        parch = st.selectbox("How many parents or childrens are travelling with you? ",[0,1,2,3,4,5,6,7,8])

    col3, col4 = st.columns(2)
    with col3:
        sex = st.selectbox('Select Your Gender:', ["male", "female"])
        if sex == "male":
            sex = 0
        else: 
            sex = 1    
    
    with col4:
        pclass = st.selectbox("Please Select Your Ticket Class",[1,2,3]) 

    
    
    Boarding_Location = st.selectbox("Please Select your Boarding Point",["Cherbourg","Southhampton","Queenstown"])
    if Boarding_Location == 'Cherbourg':
        Boarding_Location = 0
    elif Boarding_Location == 'Southampton':
        Boarding_Location = 1
    else:
        Boarding_Location = 2

    # Gathering the Data so that we can collect user entered inputs:
    data = {"Age":age,"Fare":fare,"SibSp":sibSp,"Parch":parch,"Sex":sex,"Pclass":pclass,'Embarked':Boarding_Location}
    df = pd.DataFrame(data, index=[0])   
    return df

data = main() 

# Prediction:
if st.button("Predict"):                                                                
    result = model.predict(data)                                                        
    proba=model.predict_proba(data)                                                        

    if result[0] == 1:
        st.write("Congratulations!!! You Are Alive.")
        #st.write("Probability of Your Survival Are :'Survived': {}%  'Not Survived': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))
    else:
        st.write("Unfortunately, You Are Dead.")
        #st.write("Probability of Your Survival Are :'Not Survived': {}%  'Survived': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))

# Prepared By.
st.write('Prepared By')
col5,col6 = st.columns(2)
with col5:
    #st.image(r"C:\Users\sksho\Desktop\Streamlit\streamlit Dev\Shohaib Shaikh.jpg", caption = 'Shohaib', width=600)
    st.write("Shohaib Shaikh")

with col6:
    #st.image(r"C:\Users\sksho\Desktop\Streamlit\streamlit Dev\Shohaib Shaikh.jpg", caption = 'Sanghana', width = 600)
    st.write('Saghana Shree')



