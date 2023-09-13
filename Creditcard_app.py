import numpy as np
import streamlit as st
from PIL import Image
import pickle
import streamlit.components.v1 as components

tab0,tab1, tab2 = st.tabs(["Home","Application Form", "Help"])

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def run():
     
      #st.title("Credit Card Approval Prediction using Machine Learning")
      #img1 = Image.open('images.jpg')
      #st.image(img1, use_column_width=False)

      with tab0:
         
         st.markdown("<h2 style='text-align: center; color: black;'>Credit Card Approval Prediction using Machine Learning</h2>", unsafe_allow_html=True)
         
         st.markdown("<p style='text-align: justify;'>The project aims to develop a machine learning model to forecast whether a credit card application will be approved or rejected. By examining historical credit card application data, the model will evaluate an individual's creditworthiness and provide effective intuitions to financial institutions or users for making updated decisions about credit card approvals. By using the predictive model, design and develop a user-friendly interface for end-users to input applicant information and receive credit card approval predictions. Then deploy the trained and optimized model in a production environment, allowing real-time credit card approval predictions based on new applicant data along with the user interface.</p>", unsafe_allow_html=True)
   
         st.markdown("<h6 style='text-align: left; color: black;'>Renjini Balachandran</h6>", unsafe_allow_html=True)
         st.markdown("<h6 style='text-align: left; color: black;'>Master of science in Data Science, Grand Canyon University</h6>", unsafe_allow_html=True)
         
         homeBottomImg = Image.open('home_bottom_image.jpg')
         st.image(homeBottomImg, use_column_width=False)



      with tab1:
         #st.markdown("<h1 style='text-align: center; color: red;'>Credit Card Approval Prediction using Machine Learning</h1>", unsafe_allow_html=True)
         # declaring all variables
         st.markdown("<b><h3 style='text-align: center; color: black;'>Welcome to Credit Card Prediction System!</h3></b>", unsafe_allow_html=True)

         AMT_INCOME_TOTAL = 0
         FLAG_WORK_PHONE	= 0
         FLAG_LAND_PHONE = 0
         YEARS_OF_EMPLOYMENT = 0
         CODE_GENDER_F = False
         FLAG_OWN_REALTY_NO = False
         INCOME_TYPE_COMM_ASSOCIATE  = False
         INCOME_TYPE_PENSIONER = False
         INCOME_TYPE_STATE_SERVANT = False
         INCOME_TYPE_STUDENT = False
         EDUCATION_TYPE_HIGHER_EDU = False
         EDUCATION_TYPE_ACADEMIC_DEGREE = False
         EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU = False
         EDUCATION_TYPE_LOWER_SECONDARY = False
         FAMILY_STATUS_CIVIL_MARRIAGE = False
         FAMILY_STATUS_MARRIED = False
         FAMILY_STATUS_SINGLE = False
         FAMILY_STATUS_SEPARATED = False
         HOUSING_TYPE_SHARE_APT = False
         HOUSING_TYPE_HOUSE_APT = False
         HOUSING_TYPE_MUNICIPAL_APT = False
         HOUSING_TYPE_OFFICE_APT = False
         HOUSING_TYPE_RENTED_APT = False

         approved_message = ", your Credit card application is approved"
         declined_message = ", your Credit card application not approved"
         loaded_model = pickle.load(open('trained_model.sav', 'rb'))

         #url = "./help.html"
         #st.write("check out this [link](%s)" % url)
         #st.markdown("check out this [link](%s)" % url)


         # Full Name
         full_name = st.text_input('Full Name')

         # AMT_INCOME_TOTAL(3)
         AMT_INCOME_TOTAL = st.number_input("Applicant's Annual Income($)", value=0)

         # FLAG_WORK_PHONE(22)
         own_workphone = ('Yes', 'No')
         options = list(range(len(own_workphone)))
         FLAG_WORK_PHONE = st.selectbox("Do you have work phone", options, format_func=lambda x: own_workphone[x])


         # FLAG_PHONE(23)
         own_phone = ('Yes', 'No')
         options = list(range(len(own_phone)))
         FLAG_LAND_PHONE = st.selectbox("Do you have land phone", options, format_func=lambda x: own_phone[x])

         # YEARS_EMPLOYED(21)
         YEARS_OF_EMPLOYMENT = st.number_input("Years of employment", value=0)

         # For CODE_GENDER(1)
         gen_display = ('Male', 'Female')
         options = list(range(len(gen_display)))
         gen = st.selectbox("Gender", options, format_func=lambda x: gen_display[x])

         # for FLAG_OWN_REALTY_NO(2)
         own_realty = ('Yes', 'No')
         options = list(range(len(own_realty)))
         realty = st.selectbox("Do you own realty", options, format_func=lambda x: own_realty[x])

         # INCOME_TYPE(4-7)
         income_type = ('Commercial associate', 'Pensioner', 'State servant', 'Student')
         options = list(range(len(income_type)))
         income = st.selectbox("Type of Income", options, format_func=lambda x: income_type[x])

         # EDUCATION_TYPE(8-11)
         education_type = ('Higher education', 'Academic degree', 'Incomplete higher education','Lower secondary')
         options = list(range(len(education_type)))
         education = st.selectbox("Type of Education", options, format_func=lambda x: education_type[x])

         # FAMILY_STATUS(12-15)
         family_status = ('Civil marriage', 'Married', 'Single / not married', 'Separated')
         options = list(range(len(family_status)))
         family = st.selectbox("Family Status", options, format_func=lambda x: family_status[x])

         # HOUSING_TYPE(16-20)
         housing_type = ('Share Apt.', 'House Apt.', 'Municipal Apt.', 'Office Apt.', 'Rented Apt.')
         options = list(range(len(housing_type)))
         housing = st.selectbox("Housing Type", options, format_func=lambda x: housing_type[x])


         if st.button("Submit"):

            if(FLAG_WORK_PHONE == 0):
               FLAG_WORK_PHONE = 1
            else:
               FLAG_WORK_PHONE = 0
         ####################################
            if(FLAG_LAND_PHONE == 0):
               FLAG_LAND_PHONE = 1
            else:
               FLAG_LAND_PHONE = 0
         ####################################
            if(gen == 0):
               CODE_GENDER_F = False
            else:
               CODE_GENDER_F = True
         ####################################
            if(realty == 0):
               FLAG_OWN_REALTY_NO = False
            else:
               FLAG_OWN_REALTY_NO = True
         ####################################
            if(income == 0):
               INCOME_TYPE_COMM_ASSOCIATE = True
            elif(income == 1):
               INCOME_TYPE_PENSIONER = True
            elif(income == 2):
               INCOME_TYPE_STATE_SERVANT = True
            else:
               INCOME_TYPE_STUDENT = True
         ####################################
            if(education == 0):
               EDUCATION_TYPE_HIGHER_EDU = True
            elif(education == 1):
               EDUCATION_TYPE_ACADEMIC_DEGREE = True
            elif(education == 2):
               EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU = True
            else:
               EDUCATION_TYPE_LOWER_SECONDARY = True
         ####################################
            if(family == 0):
               FAMILY_STATUS_CIVIL_MARRIAGE = True
            elif(family == 1):
               FAMILY_STATUS_MARRIED = True
            elif(family == 2):
               FAMILY_STATUS_SINGLE = True
            else:
               FAMILY_STATUS_SEPARATED = True
         ####################################
            if(housing == 0):
               HOUSING_TYPE_SHARE_APT = True
            elif(housing == 1):
               HOUSING_TYPE_HOUSE_APT = True
            elif(housing == 2):
               HOUSING_TYPE_MUNICIPAL_APT = True
            elif(housing == 3):
               HOUSING_TYPE_OFFICE_APT = True
            else:
               HOUSING_TYPE_RENTED_APT = True

            #Checking income and employment condition and declining if not meeting the minimum value
            if(AMT_INCOME_TOTAL < 12000 or YEARS_OF_EMPLOYMENT <=2):
                st.success(full_name+declined_message)
            else:
                input_data =(AMT_INCOME_TOTAL, FLAG_WORK_PHONE, FLAG_LAND_PHONE, YEARS_OF_EMPLOYMENT, CODE_GENDER_F, FLAG_OWN_REALTY_NO, INCOME_TYPE_COMM_ASSOCIATE, INCOME_TYPE_PENSIONER, INCOME_TYPE_STATE_SERVANT, INCOME_TYPE_STUDENT, EDUCATION_TYPE_HIGHER_EDU, EDUCATION_TYPE_ACADEMIC_DEGREE, EDUCATION_TYPE_INCOMPLETE_HIGHER_EDU, EDUCATION_TYPE_LOWER_SECONDARY, FAMILY_STATUS_CIVIL_MARRIAGE, FAMILY_STATUS_MARRIED, FAMILY_STATUS_SINGLE, FAMILY_STATUS_SEPARATED, HOUSING_TYPE_SHARE_APT, HOUSING_TYPE_HOUSE_APT, HOUSING_TYPE_MUNICIPAL_APT, HOUSING_TYPE_OFFICE_APT, HOUSING_TYPE_RENTED_APT)
                #input_data =(315000.0, 0, 0, 2, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)
                #input_data =(157500.0, 0, 1, 3, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False)
                input_data_as_numpy_array = np.asarray(input_data)
                input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
                prediction = loaded_model.predict(input_data_reshaped)

                if (prediction[0] == 0):
                    st.success(full_name+approved_message)
                else:
                    st.success(full_name+declined_message)

      with tab2:
            st.markdown("<b><h1 style='text-align: center; color: black;'>General Information and Help.</h1></b>", unsafe_allow_html=True)
            helpImg = Image.open('help_image.jpg')
            st.image(helpImg, use_column_width=False)
            #HtmlFile = open('help.html','r',encoding='utf-8')
            #source_code = HtmlFile.read() 
            #print(source_code)
            #components.html(source_code)

            st.markdown("<b><h4 style='text-align: left; color: black;'>General Information.</h4></b>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: justify;'>The Predicting Credit Card Approval System User Guide section provides a comprehensive overview of the system's purpose, features, and benefits. This System is designed to assist users in making informed decisions when applying for credit cards. By inputting relevant application data, users can receive predictions on whether their credit card application is likely to be approved or rejected.</p>", unsafe_allow_html=True)
            st.markdown("<b><h4 style='text-align: left; color: black;'>System Summary.</h4></b>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: justify;'>The Predicting Credit Card Approval System is a user-friendly application designed to assist users in predicting whether their credit card applications are likely to be approved or rejected. By inputting relevant application data, users receive predictions with associated confidence scores. The system employs machine learning algorithms to provide predictions based on historical data and user input. Each prediction is accompanied by a confidence score indicating the model's level of certainty in the outcome. Users can provide feedback on prediction accuracy, contributing to the system's ongoing improvement.</p>", unsafe_allow_html=True)
            st.markdown("<b><h4 style='text-align: left; color: black;'>Getting Started.</h4></b>", unsafe_allow_html=True)
            st.markdown("<ol>", unsafe_allow_html=True)
            st.markdown("<li>Access the system by using the Google search engine.</li>", unsafe_allow_html=True)
            st.markdown("<li>System requirements include a compatible web browser and a stable internet connection.</li>", unsafe_allow_html=True)
            st.markdown("<li>Applicants are individuals interested in evaluating their credit card approval chances and System Administrators are responsible for maintaining system functionality. </li>", unsafe_allow_html=True)
            st.markdown("</ol>", unsafe_allow_html=True)
            st.markdown("<b><h4 style='text-align: left; color: black;'>Using the System</h4></b>", unsafe_allow_html=True)
            st.markdown("<ol>", unsafe_allow_html=True)
            st.markdown("<li>Open the system.</li>", unsafe_allow_html=True)
            st.markdown("<li>Navigate to the prediction interface.</li>", unsafe_allow_html=True)
            st.markdown("<li>Enter accurate application data information including income, employment status, education status, etc.</li>", unsafe_allow_html=True)
            st.markdown("<li>Submit the data for prediction.</li>", unsafe_allow_html=True)
            st.markdown("<li>Upon submission, the system provides a prediction outcome (Approved or Not approved).</li>", unsafe_allow_html=True)
            st.markdown("<li>Pay attention to the outcome results.</li>", unsafe_allow_html=True)
            st.markdown("<li>The feedback is valuable in improving the system's accuracy. Provide the feedback through the email provided in the Help and Contact Details.</li>", unsafe_allow_html=True)
            st.markdown("<li>Use the system responsibly and provide truthful input data.</li>", unsafe_allow_html=True)
            st.markdown("<li>Understand that predictions are based on historical data and are not guarantees of actual approval outcomes.</li>", unsafe_allow_html=True)
            st.markdown("<li>Your personal data is handled with utmost confidentiality.</li>", unsafe_allow_html=True)
            st.markdown("</ol>", unsafe_allow_html=True)
            st.markdown("<b><h4 style='text-align: left; color: black;'>Troubleshooting</h4></b>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>1. Application Data Not Accepted</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Solution:</b></i> Verify that all mandatory fields are filled correctly. Check for special characters or incorrect formats in your input.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>2. Inaccurate Predictions</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Solution:</b>Ensure accurate input of data, especially income, credit score, and employment status. Also, consider providing more accurate and detailed information.</i> uuuuuu.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>3. Slow Loading Times</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Solution:</b>Check your internet connection. If the problem persists, try using a different browser or clearing your browser cache.</i> uuuuuu.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: left; color: black;'>4. Tips for Successful Troubleshooting:</h6>", unsafe_allow_html=True)
            st.markdown("<ol>", unsafe_allow_html=True)
            st.markdown("<li>Double-check your input data for accuracy before application submission.</li>", unsafe_allow_html=True)
            st.markdown("<li>Clear your browser cache and cookies if you experience slow loading times.</li>", unsafe_allow_html=True)
            st.markdown("<li>Keep your internet connection stable to ensure smooth system operation.</li>", unsafe_allow_html=True)
            st.markdown("<li>Ensure that you're using a supported browser and up-to-date software.</li>", unsafe_allow_html=True)
            st.markdown("</ol>", unsafe_allow_html=True)
            st.markdown("<b><h4 style='text-align: left; color: black;'>FAQ (Frequently Asked Questions):</h4></b>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>1. What is the purpose of the credit card approval prediction system?</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Answer:</b></i> The system predicts whether a credit card application is likely to be approved or rejected based on the provided application data, helping users make informed decisions.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>2. How accurate are the predictions?</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Answer:</b></i> The accuracy of predictions varies based on the quality and accuracy of the input data. Providing precise and detailed information improves prediction accuracy.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>3. Why did I receive a Not Approved prediction despite having a good credit score?</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Answer:</b></i> Credit card approval depends on multiple factors, including income, employment status, and debt-to-income ratio. A good credit score is just one aspect.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>4. What if my internet connection is unstable? Will it affect the predictions?</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Answer:</b></i> An unstable internet connection can impact the system's performance. We recommend having a stable connection for accurate results.</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)
            st.markdown("<dl>", unsafe_allow_html=True)
            st.markdown("<dt>5.Can I modify my application data after submission? Will it affect the predictions?</dt>", unsafe_allow_html=True)
            st.markdown("<dd><b><i>Answer:</b></i>Unfortunately, once you submit your application data, you cannot modify it. Ensure accuracy before submitting.Help and Contact Details</dd>", unsafe_allow_html=True)
            st.markdown("</dl>", unsafe_allow_html=True)

            st.markdown("<b><h4 style='text-align: left; color: black;'>Contact Details.</h4></b>", unsafe_allow_html=True)
            st.markdown("<p>Email: support@creditprediction.com and respond within 48 business hours.</p>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: left; color: black;'>Glossary</h4>", unsafe_allow_html=True)
            st.markdown("<ol>", unsafe_allow_html=True)
            st.markdown("<li>Application Data: Data provided by the user, including income, employment status, credit score, and other relevant information used for credit card approval predictions.</li>", unsafe_allow_html=True)
            st.markdown("<li>Data Preprocessing: The process of cleaning, transforming, and preparing raw data for analysis. In the context of this system, it involves preparing user input data for prediction.</li>", unsafe_allow_html=True)
            st.markdown("<li>Machine Learning Model: A computational algorithm that learns patterns from data and makes predictions or decisions based on those patterns.</li>", unsafe_allow_html=True)
            st.markdown("<li>User Interface (UI): The visual and interactive components of the system that users interact with to input data and receive predictions.</li>", unsafe_allow_html=True)
            st.markdown("<li>Model Training: The process of training a machine learning model using historical data to learn patterns and relationships for making predictions.</li>", unsafe_allow_html=True)
            st.markdown("</ol>", unsafe_allow_html=True)

            

run()