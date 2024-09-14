import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load('autism_rf_model.pkl')

st.write("Autism Screening (Q-CHAT-10)")

# Get user inputs
col1, col2, col3 = st.columns(3)

questions = {
    "Est-ce que votre enfant vous regarde lorsque vous l’appelez?": ["Toujours", "Habituellement", "Parfois", "Rarement", "Jamais"],
    "A quel point est-ce facile d’avoir un contact visuel avec votre enfant?": ["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"],
    "Est-ce que votre enfant joue à faire semblant?": ["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"],
    "Est-ce que votre enfant regarde dans la direction que vous regardez?": ["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"],
    "Est-ce que votre enfant essaie de vous réconforter?": ["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"],
    "Est-ce que votre enfant utilise spontanément des gestes simples de communication, comme saluer de la main?": ["Plusieurs fois par jour", "Quelques fois par jours", "Quelques fois par semaine", "Moins d’une fois par semaine", "Jamais"],
    "Est-ce que les premiers mots de votre enfant étaient": ["Très typique", "Plutôt typique", "Légèrement inhabituel", "Très inhabituel", "Mon enfant ne parle pas"]
}

user_data = []

for i, (question, options) in enumerate(questions.items()):
    if i % 3 == 0:
        user_data.append(col1.selectbox(question, options))
    elif i % 3 == 1:
        user_data.append(col2.selectbox(question, options))
    else:
        user_data.append(col3.selectbox(question, options))

# Transform the inputs into numerical format
def transform_response(response):
    mapping = {
        'Toujours': 0, 'Habituellement': 2, 'Parfois': 1, 'Rarement': 3, 'Jamais': 4,
        'Très typique': 0, 'Plutôt typique': 1, 'Légèrement inhabituel': 2, 'Très inhabituel': 3, 'Mon enfant ne parle pas': 4
    }
    return mapping.get(response, 3)

# Prepare data for prediction
data_for_prediction = [transform_response(answer) for answer in user_data]

# Create a DataFrame to match the input structure of the model
df_pred = pd.DataFrame([data_for_prediction], columns=[f'Q{i+1}' for i in range(len(questions))])

# Predict the likelihood of autism
if st.button("Predict"):
    prediction = model.predict(df_pred)[0]  # 0 or 1

    # Display prediction result
    if prediction == 1:
        st.write("Au vu de vos reponses, vous souffrez probablement d'autisme.")
    else:
        st.write("Au vu de vos reponses, vous ne souffrez probablement pas d'autisme.")
