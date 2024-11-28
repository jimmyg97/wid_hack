import streamlit as st
import numpy as np


# import joblib  # For loading the pre-trained model

# model = joblib.load('your_model.joblib')

def main():
    st.image('voteforus.png')
    st.title('Investment recommendation tool')

    invest = 'N'

    # Create input fields for the features
    feature1 = st.radio("Please select your gender: ", ('Male', 'Female', 'Non-binary'))
    feature2 = st.number_input('Please provide your age:', min_value=0, max_value=100, value=1)
    feature3 = st.radio('Please provide your highest level of education type:',
                        ('No education', 'GCSEs', 'A levels', 'Apprenticeship', 'BSc', 'MSc', 'PhD'))
    feature4 = st.text_input('Please the region you live in:')
    feature5 = st.number_input('Please select your annual income (before tax):', min_value=0, value=1)
    feature6 = st.radio('Please select your employment status:', ('Employed', 'Unemployed', 'Self-Employed'))
    feature7 = st.radio('Please select your relationship status', ('Single', 'Married', 'In a relationship'))
    feature8 = st.number_input('How much do you save annually?', min_value=0, value=1)
    feature9 = st.number_input('How much do you invest annually?', min_value=0, value=1)
    feature10 = st.radio('Please select your investment risk appetite', ('Low', 'Medium', 'High'))
    feature11 = st.radio('Please select your investment experience', ('None', 'Some', 'A lot'))
    feature12 = st.text_input('What is your overall goal with investing?')

    # Collect the inputs into a numpy array
    input_data = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                            feature9, feature10, feature11, feature12]])

    # Make prediction
    if st.button('Should I invest?'):
        if feature9 / feature5 < 0.20:
            st.write(":green[Yes! We think you should invest to help maximise your returns.]")
            invest = 'Y'
        else:
            st.write(":blue[Actually, we think you are investing very well. Keep it up!]")
            invest = 'N'

    if invest == 'Y':
        if 'stock' in str(feature12):
            st.write("We recommend you invest in stocks (STOCKS HERE)")
        elif 'shares' in str(feature12):
            st.write("We recommend you invest in shares (SHARES HERE)")
        elif 'crypto' in str(feature12):
            st.write("We recommend you invest in crypto (SHARES HERE)")


if __name__ == '__main__':
    main()
