import streamlit as st
import joblib
import pandas as pd

st.write("TSA Prediction")

gender = st.selectbox("Garcon ?", ["Oui", "Non"])
col1, col2, col3 = st.columns(3)

# Getting user input

age = col2.number_input("Votre age")

education = col3.selectbox("Est-ce que votre enfant vous regarde lorsque vous l’appelez?",["Toujours", "Habituellement", "Parfois", "Rarement", "Jamais"])

isSmoker = col1.selectbox("A quel point est-ce facile d’avoir un contact visuel avec votre enfant?",["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"])

yearsSmoking = col2.number_input("Nombre ")

BPMeds = col3.selectbox("Est-ce que votre enfant joue à faire semblant? (Comme jouer avec des poupées, parler dans un téléphone jouet?",["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"])

stroke = col1.selectbox("Est-ce que votre enfant regarde dans la direction que vous regardez?",["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"])

hyp = col2.selectbox("Si vous ou quelqu’un de votre famille est triste ou bouleversé, est-ce que votre enfant essaie de le réconforter??",["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"])

diabetes = col3.selectbox("Est-ce que votre enfant utilise spontanément des gestes simples de communication, comme saluer de la main?",["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"])

chol = col1.selectbox("Est-ce que les premiers mots de votre enfant étaient :",["Très typique", "Plutôt typique", "Légèrement inhabituel", "Très inhabituel", "Mon enfant ne parle pas"])

sys_bp = col2.number_input("Une question2")

dia_bp = col3.number_input("Une question3")

bmi = col1.number_input("Une question4")

heart_rate = col2.number_input("Une question5")

glucose = col3.number_input("Une question6")

df_pred = pd.DataFrame([[gender,age,education,isSmoker,yearsSmoking,BPMeds,stroke,hyp,diabetes,chol,sys_bp,dia_bp,bmi,heart_rate,glucose]],

columns= ['male','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])

df_pred['male'] = df_pred['male'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)

def transform(data):
    result = 3
    if(data=='Toujours'):
        result = 0
    elif(data=='Parfois'):
        result = 1
    elif(data=='Habituellement'):
        result = 2
    return(result)
df_pred['education'] = df_pred['education'].apply(transform)

#model = joblib.load('fhs_rf_model.pkl')
#prediction = model.predict(df_pred)

prediction = [1,1,0,1,0,1]

if st.button('Predict'):
    if(prediction[0]==0):
        st.write('<p class="big-font">Vous n'etes probablement pas atteint d'Autisme.</p>',unsafe_allow_html=True)
    else:
        st.write('<p class="big-font">Vous etes probablement atteint d'Autisme.</p>',unsafe_allow_html=True)
