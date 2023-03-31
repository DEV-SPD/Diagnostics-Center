import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# LOADING THE SAVED MODELS
with open('diabetes', 'rb') as f:
    diabetes_model = pickle.load(f)
with open('HEART_DISEASE', 'rb') as f:
    heart_disease = pickle.load(f)

def main():

# sidebar for navigation
 with st.sidebar:
     selected = option_menu('DIAGNOSTICS CENTER',
                            ['CARDIOVASCULAR DISEASE PREDICTION', 'DIABETES PREDICTION'],
                             icons =['heart', 'activity'])


 if selected == 'CARDIOVASCULAR DISEASE PREDICTION':
     img = Image.open('heart.jpg')
     st.image(img)
     st.header('CARDIOVASCULAR DISEASE PREDICTION')
     age = st.number_input('AGE:')
     gender = st.number_input('GENDER:')
     cp = st.number_input('chest pain type:')
     restbp = st.number_input('rest blood pressure:')
     chol = st.number_input('Cholestrol:')
     fbs = st.number_input('fasting blood sugar:')
     restecg = st.number_input('REST ECG RESULT:')
     thalach = st.number_input('maximum heart rate achieved:')
     exang = st.number_input('exercise induced angina:')
     oldpeak = st.number_input('OLD PEAK:')
     slope = st.number_input('SLOPE:')
     ca = st.number_input('Number of major vessels colored by florosopy:')
     thal = st.number_input('THAL(0/1/2):')

     if st.button('submit'):
         a = heart_disease.predict([[age, gender, cp, restbp, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
         if a == 0:
             st.success('SAFE')
         else:
             st.error('CARDIOVASCULAR DISEASE DETECTED')

 if selected == 'DIABETES PREDICTION':
     img = Image.open('DIABETES_1.jpg')
     st.image(img)
     st.header('DIABETES PREDICTION')
     Pregnancies = st.text_input('NO. OF PREGNANCIES : ')
     Glucose = st.text_input('GLUCOSE LEVEL : ')
     BloodPressure = st.text_input('BLOOD PRESSURE : ')
     SkinThickness = st.text_input('SKIN THICKNESS : ')
     Insulin = st.text_input('INSULIN LEVEL : ')
     BMI = st.text_input('BMI : ')
     DPC = st.text_input('DiabetesPedigreeFunction : ')
     Age = st.text_input('AGE :')

     diagonosis = ''

     if st.button('Diabetes Test Result'):
        diagonosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPC, Age]])
        if diagonosis == 1:
            st.error('POSITIVE')
        else:
            st.success('NEGATIVE')






if __name__ == '__main__':
    main()