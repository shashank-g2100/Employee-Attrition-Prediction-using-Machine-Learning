# import streamlit as st
# import requests

# st.title("Employee Attrition Prediction")

# st.subheader("Enter Employee Details")

# age = st.number_input("Age",18,60,30)

# income = st.number_input(
# "Monthly Income",1000,20000,5000)

# job_level = st.selectbox(
# "Job Level",[1,2,3,4,5])

# years = st.number_input(
# "Years at Company",0,40,5)

# worklife = st.selectbox(
# "Work Life Balance",[1,2,3,4])

# job_sat = st.selectbox(
# "Job Satisfaction",[1,2,3,4])

# overtime = st.selectbox(
# "OverTime",["Yes","No"])

# department = st.selectbox(
# "Department",
# ["Sales","Research & Development","Human Resources"]
# )

# if st.button("Predict Attrition"):

#     data = {

#         "Age":age,
#         "DailyRate":800,
#         "DistanceFromHome":5,
#         "Education":3,
#         "EnvironmentSatisfaction":3,
#         "HourlyRate":60,
#         "JobInvolvement":3,
#         "JobLevel":job_level,
#         "JobSatisfaction":job_sat,
#         "MonthlyIncome":income,
#         "MonthlyRate":15000,
#         "NumCompaniesWorked":2,
#         "PercentSalaryHike":13,
#         "PerformanceRating":3,
#         "RelationshipSatisfaction":3,
#         "StockOptionLevel":1,
#         "TotalWorkingYears":10,
#         "TrainingTimesLastYear":2,
#         "WorkLifeBalance":worklife,
#         "YearsAtCompany":years,
#         "YearsInCurrentRole":3,
#         "YearsSinceLastPromotion":1,
#         "YearsWithCurrManager":3,

#         "BusinessTravel":"Travel_Rarely",
#         "Department":department,
#         "EducationField":"Life Sciences",
#         "Gender":"Male",
#         "JobRole":"Sales Executive",
#         "MaritalStatus":"Single",
#         "OverTime":overtime

#     }

#     response = requests.post(

#         "http://127.0.0.1:8000/predict",

#         json=data

#     )

#     result = response.json()

#     st.success(result)


# import streamlit as st
# import requests
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import joblib
# import os

# st.set_page_config(
#     page_title="Attrition Dashboard",
#     layout="wide"
# )

# st.title("Employee Attrition Prediction System")

# # ======================
# # Load Model Files
# # ======================

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# model_path = os.path.join(BASE_DIR,"models","attrition_model.pkl")
# scaler_path = os.path.join(BASE_DIR,"models","scaler.pkl")
# columns_path = os.path.join(BASE_DIR,"models","columns.pkl")

# try:

#     model = joblib.load(model_path)
#     scaler = joblib.load(scaler_path)
#     columns = joblib.load(columns_path)

# except:

#     model = None
#     scaler = None
#     columns = None

#     st.warning("Model files not found")

# tab1, tab2, tab3 = st.tabs(
# ["Prediction", "CSV Analytics", "HR Analytics Dashboard"]
# )

# # ======================
# # Prediction Tab
# # ======================

# with tab1:

#     st.subheader("Predict Employee Attrition")

#     col1,col2 = st.columns(2)

#     with col1:

#         age = st.slider("Age",18,60,30)

#         income = st.number_input(
#         "Monthly Income",1000,20000,5000)

#         job_level = st.selectbox(
#         "Job Level",[1,2,3,4,5])

#         years = st.slider(
#         "Years at Company",0,40,5)

#     with col2:

#         job_sat = st.selectbox(
#         "Job Satisfaction",[1,2,3,4])

#         worklife = st.selectbox(
#         "Work Life Balance",[1,2,3,4])

#         overtime = st.selectbox(
#         "OverTime",["Yes","No"])

#         department = st.selectbox(
#         "Department",
#         ["Sales",
#         "Research & Development",
#         "Human Resources"]
#         )

#     if st.button("Predict Attrition Risk"):

#         data = {

#         "Age":age,
#         "DailyRate":800,
#         "DistanceFromHome":5,
#         "Education":3,
#         "EnvironmentSatisfaction":3,
#         "HourlyRate":60,
#         "JobInvolvement":3,
#         "JobLevel":job_level,
#         "JobSatisfaction":job_sat,
#         "MonthlyIncome":income,
#         "MonthlyRate":15000,
#         "NumCompaniesWorked":2,
#         "PercentSalaryHike":13,
#         "PerformanceRating":3,
#         "RelationshipSatisfaction":3,
#         "StockOptionLevel":1,
#         "TotalWorkingYears":10,
#         "TrainingTimesLastYear":2,
#         "WorkLifeBalance":worklife,
#         "YearsAtCompany":years,
#         "YearsInCurrentRole":3,
#         "YearsSinceLastPromotion":1,
#         "YearsWithCurrManager":3,

#         "BusinessTravel":"Travel_Rarely",
#         "Department":department,
#         "EducationField":"Life Sciences",
#         "Gender":"Male",
#         "JobRole":"Sales Executive",
#         "MaritalStatus":"Single",
#         "OverTime":overtime

#         }

#         try:

#             response = requests.post(
#             "http://127.0.0.1:8000/predict",
#             json=data
#             )

#             result = response.json()

#             if result["Prediction"]=="Attrition Risk":

#                 st.error("High Attrition Risk")

#             else:

#                 st.success("Low Attrition Risk")

#             st.metric(
#             "Probability",
#             result["Probability"]
#             )

#             st.info(
#             "Risk Level: "+result["Risk Level"]
#             )

#         except:

#             st.error("API not running")

# # ======================
# # CSV Analytics
# # ======================

# with tab2:

#     st.subheader("Upload Employee Dataset")

#     uploaded_file = st.file_uploader(
#     "Upload CSV file",
#     type=["csv"]
#     )

#     if uploaded_file is not None:

#         try:

#             uploaded_file.seek(0)

#             df = pd.read_csv(uploaded_file)

#             if df.empty:

#                 st.error("Uploaded file is empty")

#             else:

#                 st.write("Dataset Preview")

#                 st.dataframe(df.head())

#                 if model is not None:

#                     df_original = df.copy()

#                     df_encoded = pd.get_dummies(df)

#                     df_encoded = df_encoded.reindex(
#                     columns=columns,
#                     fill_value=0
#                     )

#                     df_scaled = scaler.transform(df_encoded)

#                     df_original['Prediction'] = model.predict(df_scaled)

#                     df_original['Probability'] = model.predict_proba(df_scaled)[:,1]

#                     df_original['Prediction'] = df_original[
#                     'Prediction'
#                     ].map({

#                     0:"No Attrition",
#                     1:"Attrition"

#                     })

#                     st.subheader("Prediction Results")

#                     st.dataframe(df_original.head())

#                     st.subheader("Attrition Distribution")

#                     st.bar_chart(
#                     df_original['Prediction'].value_counts()
#                     )

#                     st.subheader("Department Impact")

#                     dept_attrition = pd.crosstab(
#                         df_original['Department'],
#                         df_original['Prediction']
#                     )

#                     st.bar_chart(dept_attrition)

#                     st.subheader("Income vs Attrition")

#                     fig = plt.figure()

#                     sns.boxplot(

#                     x='Prediction',
#                     y='MonthlyIncome',
#                     data=df_original

#                     )

#                     st.pyplot(fig)

#                     st.download_button(

#                     "Download Results",

#                     df_original.to_csv(index=False),

#                     "attrition_predictions.csv"

#                     )

#                     st.success(
#                     "Predictions generated successfully"
#                     )

#         except Exception as e:

#             st.error("Error reading file")

# # ======================
# # Analytics Dashboard
# # ======================

# # with tab3:

# #     st.subheader("HR Analytics Dashboard")

# #     try:

# #         df = pd.read_csv(
# #         "data/HR_Analytics.csv"
# #         )

# #         col1,col2 = st.columns(2)

# #         with col1:

# #             st.write("Attrition Distribution")

# #             fig = plt.figure()

# #             sns.countplot(
# #             x="Attrition",
# #             data=df
# #             )

# #             st.pyplot(fig)

# #         with col2:

# #             st.write("Attrition vs Overtime")

# #             fig = plt.figure()

# #             sns.countplot(
# #             x="OverTime",
# #             hue="Attrition",
# #             data=df
# #             )

# #             st.pyplot(fig)

# #         st.write("Income vs Attrition")

# #         fig = plt.figure()

# #         sns.boxplot(
# #         x="Attrition",
# #         y="MonthlyIncome",
# #         data=df
# #         )

# #         st.pyplot(fig)

# #         st.write("Department Attrition")

# #         fig = plt.figure()

# #         sns.countplot(
# #         x="Department",
# #         hue="Attrition",
# #         data=df
# #         )

# #         plt.xticks(rotation=45)

# #         st.pyplot(fig)

# #     except:

# #         st.error("Dataset not found")

# with tab3:

#     st.subheader("HR Analytics Dashboard")

#     try:

#         df = pd.read_csv("data/HR_Analytics.csv")

#         # ================= KPI METRICS =================

#         total_emp = len(df)

#         attrition_rate = (
#         df['Attrition'].value_counts(normalize=True)['Yes']*100
#         )

#         avg_income = df['MonthlyIncome'].mean()

#         avg_years = df['YearsAtCompany'].mean()

#         col1,col2,col3,col4 = st.columns(4)

#         col1.metric(
#         "Total Employees",
#         total_emp
#         )

#         col2.metric(
#         "Attrition Rate",
#         f"{attrition_rate:.2f}%"
#         )

#         col3.metric(
#         "Avg Monthly Income",
#         f"{int(avg_income)}"
#         )

#         col4.metric(
#         "Avg Years at Company",
#         f"{avg_years:.1f}"
#         )

#         st.divider()

#         # ================= CHARTS =================

#         col1,col2 = st.columns(2)

#         with col1:

#             st.write("Attrition Distribution")

#             fig = plt.figure()

#             sns.countplot(
#             x="Attrition",
#             data=df
#             )

#             st.pyplot(fig)

#         with col2:

#             st.write("Overtime Impact")

#             fig = plt.figure()

#             sns.countplot(

#             x="OverTime",

#             hue="Attrition",

#             data=df

#             )

#             st.pyplot(fig)

#         st.divider()

#         # Income distribution

#         col1,col2 = st.columns(2)

#         with col1:

#             st.write("Income vs Attrition")

#             fig = plt.figure()

#             sns.boxplot(

#             x="Attrition",

#             y="MonthlyIncome",

#             data=df

#             )

#             st.pyplot(fig)

#         with col2:

#             st.write("Department Attrition")

#             fig = plt.figure()

#             sns.countplot(

#             x="Department",

#             hue="Attrition",

#             data=df

#             )

#             plt.xticks(rotation=45)

#             st.pyplot(fig)

#         st.divider()

#         # Job satisfaction

#         st.write("Job Satisfaction Impact")

#         fig = plt.figure()

#         sns.countplot(

#         x="JobSatisfaction",

#         hue="Attrition",

#         data=df

#         )

#         st.pyplot(fig)

#         # Worklife balance

#         st.write("Work Life Balance Impact")

#         fig = plt.figure()

#         sns.countplot(

#         x="WorkLifeBalance",

#         hue="Attrition",

#         data=df

#         )

#         st.pyplot(fig)

#     except:

#         st.error("Dataset not found")



# import streamlit as st
# import requests
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import joblib
# import os

# st.set_page_config(
#     page_title="Employee Attrition Analytics Platform",
#     layout="wide"
# )

# st.title("Employee Attrition Analytics Platform")

# st.markdown(
# "Predict employee attrition risk and generate HR insights using Machine Learning."
# )

# # ======================
# # Load Model Files
# # ======================

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# model_path = os.path.join(BASE_DIR,"models","attrition_model.pkl")
# scaler_path = os.path.join(BASE_DIR,"models","scaler.pkl")
# columns_path = os.path.join(BASE_DIR,"models","columns.pkl")

# try:

#     model = joblib.load(model_path)
#     scaler = joblib.load(scaler_path)
#     columns = joblib.load(columns_path)

# except:

#     model=None
#     scaler=None
#     columns=None

#     st.warning("Model files not found")

# tab1, tab2 = st.tabs([

# "Single Prediction",
# "HR Analytics Dashboard"

# ])

# # ======================
# # TAB 1 PREDICTION
# # ======================

# with tab1:

#     st.subheader("Predict Employee Attrition")

#     col1,col2 = st.columns(2)

#     with col1:

#         age = st.slider("Age",18,60,30)

#         income = st.number_input(
#         "Monthly Income",1000,20000,5000)

#         job_level = st.selectbox(
#         "Job Level",[1,2,3,4,5])

#         years = st.slider(
#         "Years at Company",0,40,5)

#     with col2:

#         job_sat = st.selectbox(
#         "Job Satisfaction",[1,2,3,4])

#         worklife = st.selectbox(
#         "Work Life Balance",[1,2,3,4])

#         overtime = st.selectbox(
#         "OverTime",["Yes","No"])

#         department = st.selectbox(

#         "Department",

#         ["Sales",
#         "Research & Development",
#         "Human Resources"]

#         )

#     if st.button("Predict Attrition Risk"):

#         data = {

#         "Age":age,
#         "DailyRate":800,
#         "DistanceFromHome":5,
#         "Education":3,
#         "EnvironmentSatisfaction":3,
#         "HourlyRate":60,
#         "JobInvolvement":3,
#         "JobLevel":job_level,
#         "JobSatisfaction":job_sat,
#         "MonthlyIncome":income,
#         "MonthlyRate":15000,
#         "NumCompaniesWorked":2,
#         "PercentSalaryHike":13,
#         "PerformanceRating":3,
#         "RelationshipSatisfaction":3,
#         "StockOptionLevel":1,
#         "TotalWorkingYears":10,
#         "TrainingTimesLastYear":2,
#         "WorkLifeBalance":worklife,
#         "YearsAtCompany":years,
#         "YearsInCurrentRole":3,
#         "YearsSinceLastPromotion":1,
#         "YearsWithCurrManager":3,

#         "BusinessTravel":"Travel_Rarely",
#         "Department":department,
#         "EducationField":"Life Sciences",
#         "Gender":"Male",
#         "JobRole":"Sales Executive",
#         "MaritalStatus":"Single",
#         "OverTime":overtime

#         }

#         try:

#             response = requests.post(

#             "http://127.0.0.1:8000/predict",

#             json=data

#             )

#             result = response.json()

#             if result["Prediction"]=="Attrition Risk":

#                 st.error("High Attrition Risk")

#             else:

#                 st.success("Low Attrition Risk")

#             st.metric(

#             "Attrition Probability",

#             result["Probability"]

#             )

#             st.info(

#             "Risk Level: "+result["Risk Level"]

#             )

#         except:

#             st.error("API not running")

# # ======================
# # TAB 2 HR ANALYTICS
# # ======================

# with tab2:

#     st.header("HR Analytics Dashboard")

#     uploaded_file = st.file_uploader(

#     "Upload Employee Dataset",

#     type=["csv"]

#     )

    # if uploaded_file:

    #     df = pd.read_csv(uploaded_file)

    #     st.subheader("Dataset Preview")

    #     st.dataframe(df.head())

    #     st.write("Dataset Shape:",df.shape)

    #     if model:

    #         df_original = df.copy()

    #         df_encoded = pd.get_dummies(df)

    #         df_encoded = df_encoded.reindex(

    #         columns=columns,

    #         fill_value=0

    #         )

    #         df_scaled = scaler.transform(df_encoded)

    #         df_original['Prediction']=model.predict(df_scaled)

    #         df_original['Probability']=model.predict_proba(df_scaled)[:,1]

    #         df_original['Prediction']=df_original[
    #         'Prediction'
    #         ].map({

    #         0:"No Attrition",
    #         1:"Attrition"

    #         })

    #         st.subheader("Prediction Results")

    #         st.dataframe(df_original.head())

#             # ================= KPI METRICS =================

#             st.subheader("HR Summary Metrics")

#             col1,col2,col3,col4=st.columns(4)

#             col1.metric(

#             "Total Employees",

#             len(df_original)

#             )

#             col2.metric(

#             "Attrition Count",

#             (df_original['Prediction']=="Attrition").sum()

#             )

#             col3.metric(

#             "Attrition Rate",

#             round(

#             (df_original['Prediction']=="Attrition")
#             .mean()*100,2

#             )

#             )

#             col4.metric(

#             "Average Income",

#             int(df_original['MonthlyIncome'].mean())

#             )

#             st.divider()

#             # ================= INSIGHTS =================

#             st.subheader("Attrition Insights")

#             col1,col2=st.columns(2)

#             with col1:

#                 st.write("Attrition Distribution")

#                 st.bar_chart(

#                 df_original['Prediction']
#                 .value_counts()

#                 )

#             with col2:

#                 st.write("Department Impact")

#                 dept=pd.crosstab(

#                 df_original['Department'],

#                 df_original['Prediction']

#                 )

#                 st.bar_chart(dept)

#             st.subheader("Income Analysis")

#             fig=plt.figure()

#             sns.boxplot(

#             x='Prediction',

#             y='MonthlyIncome',

#             data=df_original

#             )

#             st.pyplot(fig)

#             # ================= BUSINESS INSIGHTS =================

#             st.subheader("Key Insights")

#             st.markdown("""

# • Employees working overtime show higher attrition

# • Lower salary employees show higher risk

# • Employees with low satisfaction leave more

# • Early tenure employees show higher turnover

# """)

#             # ================= HR RECOMMENDATIONS =================

#             st.subheader("HR Recommendations")

#             st.markdown("""

# ### Recommended Actions

# **Reduce overtime workload**

# **Improve employee engagement**

# **Review compensation policies**

# **Provide career development programs**

# **Improve work-life balance**

# ### Business Impact:

# These actions can reduce attrition and improve retention.

# """)

#             # ================= DOWNLOAD =================

#             st.subheader("Export Results")

#             st.download_button(

#             "Download Predictions",

#             df_original.to_csv(index=False),

#             "attrition_predictions.csv"

#             )

#             st.success(
#             "Analysis completed successfully"
#             )



#########################################
# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
# import joblib
# import os

# st.set_page_config(
#     page_title="HR Attrition Analytics",
#     page_icon="📊",
#     layout="wide"
# )

# st.title("HR Attrition Analytics Platform")

# st.caption(
# "AI driven workforce analytics and attrition prediction system"
# )

# # Sidebar

# st.sidebar.title("Dashboard")

# page = st.sidebar.radio(

# "Navigation",

# ["Prediction","Analytics Dashboard"]

# )

# st.sidebar.divider()

# st.sidebar.success(
# "Model: Logistic Regression"
# )

# # Load model

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# model = joblib.load(
# os.path.join(BASE_DIR,"models","attrition_model.pkl")
# )

# scaler = joblib.load(
# os.path.join(BASE_DIR,"models","scaler.pkl")
# )

# columns = joblib.load(
# os.path.join(BASE_DIR,"models","columns.pkl")
# )

# # ======================
# # PREDICTION
# # ======================

# if page=="Prediction":

#     st.subheader("Employee Risk Prediction")

#     col1,col2,col3,col4 = st.columns(4)

#     age = col1.slider("Age",18,60,30)

#     income = col2.number_input(
#     "Monthly Income",
#     1000,20000,5000
#     )

#     job_level = col3.selectbox(
#     "Job Level",
#     [1,2,3,4,5]
#     )

#     years = col4.slider(
#     "Years at Company",
#     0,40,5
#     )

#     col1,col2,col3,col4 = st.columns(4)

#     job_sat = col1.selectbox(
#     "Job Satisfaction",
#     [1,2,3,4]
#     )

#     worklife = col2.selectbox(
#     "Work Life Balance",
#     [1,2,3,4]
#     )

#     overtime = col3.selectbox(
#     "Overtime",
#     ["Yes","No"]
#     )

#     department = col4.selectbox(

#     "Department",

#     ["Sales",
#     "Research & Development",
#     "Human Resources"]

#     )

#     if st.button("Predict"):

#         data = {

#         "Age":age,
#         "DailyRate":800,
#         "DistanceFromHome":5,
#         "Education":3,
#         "EnvironmentSatisfaction":3,
#         "HourlyRate":60,
#         "JobInvolvement":3,
#         "JobLevel":job_level,
#         "JobSatisfaction":job_sat,
#         "MonthlyIncome":income,
#         "MonthlyRate":15000,
#         "NumCompaniesWorked":2,
#         "PercentSalaryHike":13,
#         "PerformanceRating":3,
#         "RelationshipSatisfaction":3,
#         "StockOptionLevel":1,
#         "TotalWorkingYears":10,
#         "TrainingTimesLastYear":2,
#         "WorkLifeBalance":worklife,
#         "YearsAtCompany":years,
#         "YearsInCurrentRole":3,
#         "YearsSinceLastPromotion":1,
#         "YearsWithCurrManager":3,

#         "BusinessTravel":"Travel_Rarely",
#         "Department":department,
#         "EducationField":"Life Sciences",
#         "Gender":"Male",
#         "JobRole":"Sales Executive",
#         "MaritalStatus":"Single",
#         "OverTime":overtime

#         }

#         response = requests.post(
#         "http://127.0.0.1:8000/predict",
#         json=data
#         )

#         result=response.json()

#         st.divider()

#         col1,col2,col3 = st.columns(3)

#         if result["Prediction"]=="Attrition Risk":

#             col1.error("High Risk")

#         else:

#             col1.success("Low Risk")

#         col2.metric(
#         "Probability",
#         result["Probability"]
#         )

#         col3.metric(
#         "Risk Level",
#         result["Risk Level"]
#         )

# # ======================
# # ANALYTICS
# # ======================

# if page=="Analytics Dashboard":
    
#     st.subheader("Workforce Analytics")

#     file = st.file_uploader(
#     "Upload HR Dataset",
#     type=["csv"]
#     )

#     if file:

#         df = pd.read_csv(file)

#         st.subheader("Dataset Preview")

#         st.dataframe(df.head())

#         st.write("Dataset Shape:",df.shape)

#         if model:

#             df_original = df.copy()

#             df_encoded = pd.get_dummies(df)

#             df_encoded = df_encoded.reindex(
#             columns=columns,
#             fill_value=0
#             )

#             df_scaled = scaler.transform(df_encoded)

#             df_original['Prediction']=model.predict(df_scaled)

#             df_original['Probability']=model.predict_proba(df_scaled)[:,1]

#             df_original['Prediction']=df_original[
#             'Prediction'
#             ].map({

#             0:"No Attrition",
#             1:"Attrition"

#             })

#             st.subheader("Prediction Results")

#             st.dataframe(df_original.head())

#             # KPI

#             col1,col2,col3,col4 = st.columns(4)

#             col1.metric(
#             "Employees",
#             len(df_original)
#             )

#             col2.metric(
#             "Attrition",
#             (df_original['Prediction']=="Attrition").sum()
#             )

#             col3.metric(

#             "Attrition Rate",

#             str(

#             round(

#             (df_original['Prediction']=="Attrition")
#             .mean()*100,2

#             ))+"%"

#             )

#             col4.metric(

#             "Avg Salary",

#             int(df_original['MonthlyIncome'].mean())

#             )

#             st.divider()

#             # Charts

#             fig = px.histogram(

#             df_original,

#             x="Prediction",

#             color="Prediction",

#             title="Attrition Distribution"

#             )

#             st.plotly_chart(fig,
#             use_container_width=True)

#             fig2 = px.box(

#             df_original,

#             x="Prediction",

#             y="MonthlyIncome",

#             color="Prediction",

#             title="Income Impact"

#             )

#             st.plotly_chart(fig2,
#             use_container_width=True)

#             fig3 = px.histogram(

#             df_original,

#             x="Department",

#             color="Prediction",

#             title="Department Impact"

#             )

#             st.plotly_chart(fig3,
#             use_container_width=True)

#             st.divider()

#             st.subheader("Insights")

#             st.info("""

# Overtime strongly impacts attrition.

# Lower salary employees are higher risk.

# Job satisfaction affects retention.

# """)

#             st.subheader("Recommendations")

#             st.success("""

# Reduce overtime.

# Improve engagement.

# Review salary structure.

# Provide career growth.

# """)

#             st.download_button(

#             "Download Results",

#             df_original.to_csv(index=False),

#             "attrition_results.csv"

#             )


import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import joblib
import os

st.set_page_config(
    page_title="HR Attrition Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("HR Attrition Analytics Platform")

st.caption(
"AI driven workforce analytics and attrition prediction system"
)

st.divider()

# Sidebar

st.sidebar.title("Dashboard")

page = st.sidebar.radio(
"Navigation",
["Prediction","Analytics Dashboard"]
)

st.sidebar.divider()

st.sidebar.success("Model Active")
st.sidebar.info("Algorithm: Logistic Regression")

# Load model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(
os.path.join(BASE_DIR,"models","attrition_model.pkl")
)

scaler = joblib.load(
os.path.join(BASE_DIR,"models","scaler.pkl")
)

columns = joblib.load(
os.path.join(BASE_DIR,"models","columns.pkl")
)

# ======================
# PREDICTION
# ======================

if page=="Prediction":

    st.subheader("Employee Risk Prediction")

    container = st.container(border=True)

    with container:

        col1,col2,col3,col4 = st.columns(4)

        age = col1.slider("Age",18,60,30)

        income = col2.number_input(
        "Monthly Income",
        1000,20000,5000
        )

        job_level = col3.selectbox(
        "Job Level",
        [1,2,3,4,5]
        )

        years = col4.slider(
        "Years at Company",
        0,40,5
        )

        col1,col2,col3,col4 = st.columns(4)

        job_sat = col1.selectbox(
        "Job Satisfaction",
        [1,2,3,4]
        )

        worklife = col2.selectbox(
        "Work Life Balance",
        [1,2,3,4]
        )

        overtime = col3.selectbox(
        "Overtime",
        ["Yes","No"]
        )

        department = col4.selectbox(

        "Department",

        ["Sales",
        "Research & Development",
        "Human Resources"]

        )

    if st.button("Predict Risk"):

        with st.spinner("Running prediction model..."):

            data = {

            "Age":age,
            "DailyRate":800,
            "DistanceFromHome":5,
            "Education":3,
            "EnvironmentSatisfaction":3,
            "HourlyRate":60,
            "JobInvolvement":3,
            "JobLevel":job_level,
            "JobSatisfaction":job_sat,
            "MonthlyIncome":income,
            "MonthlyRate":15000,
            "NumCompaniesWorked":2,
            "PercentSalaryHike":13,
            "PerformanceRating":3,
            "RelationshipSatisfaction":3,
            "StockOptionLevel":1,
            "TotalWorkingYears":10,
            "TrainingTimesLastYear":2,
            "WorkLifeBalance":worklife,
            "YearsAtCompany":years,
            "YearsInCurrentRole":3,
            "YearsSinceLastPromotion":1,
            "YearsWithCurrManager":3,

            "BusinessTravel":"Travel_Rarely",
            "Department":department,
            "EducationField":"Life Sciences",
            "Gender":"Male",
            "JobRole":"Sales Executive",
            "MaritalStatus":"Single",
            "OverTime":overtime

            }

            try:

                response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data
                )

                result=response.json()

                st.divider()

                st.subheader("Prediction Result")

                col1,col2,col3 = st.columns(3)

                if result["Prediction"]=="Attrition Risk":

                    col1.error("High Risk Employee")

                else:

                    col1.success("Low Risk Employee")

                col2.metric(
                "Attrition Probability",
                result["Probability"]
                )

                col3.metric(
                "Risk Level",
                result["Risk Level"]
                )

            except:

                st.error("API not running")

# ======================
# ANALYTICS
# ======================

if page=="Analytics Dashboard":
    
    st.subheader("Workforce Analytics Dashboard")

    file = st.file_uploader(
    "Upload HR Dataset",
    type=["csv"]
    )

    if file:

        df = pd.read_csv(file)

        required_cols=[
        'Age',
        'MonthlyIncome',
        'Department'
        ]

        missing=[]

        for col in required_cols:

            if col not in df.columns:

                missing.append(col)

        if missing:

            st.error(
            "Missing columns: "+str(missing)
            )

            st.stop()

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        st.write("Dataset Shape:",df.shape)

        if model:

            with st.spinner("Analyzing workforce data..."):

                df_original = df.copy()

                df_encoded = pd.get_dummies(df)

                df_encoded = df_encoded.reindex(
                columns=columns,
                fill_value=0
                )

                df_scaled = scaler.transform(df_encoded)

                df_original['Prediction']=model.predict(df_scaled)

                df_original['Probability']=model.predict_proba(df_scaled)[:,1]

                df_original['Prediction']=df_original[
                'Prediction'
                ].map({

                0:"No Attrition",
                1:"Attrition"

                })

            st.success("Analysis Completed")

            # KPI

            st.subheader("HR Summary")

            col1,col2,col3,col4 = st.columns(4)

            col1.metric(
            "Total Employees",
            len(df_original)
            )

            col2.metric(
            "Attrition Count",
            (df_original['Prediction']=="Attrition").sum()
            )

            col3.metric(

            "Attrition Rate",

            str(

            round(

            (df_original['Prediction']=="Attrition")
            .mean()*100,2

            ))+"%"

            )

            col4.metric(

            "Average Salary",

            int(df_original['MonthlyIncome'].mean())

            )

            st.divider()

            # Risk indicator

            high_risk = (
            df_original['Prediction']=="Attrition"
            ).sum()

            if high_risk>50:

                st.error(
                "High Attrition Risk Workforce"
                )

            else:

                st.success(
                "Workforce Stability Good"
                )

            # Charts

            st.subheader("Attrition Insights")

            col1,col2 = st.columns(2)

            fig = px.histogram(
            df_original,
            x="Prediction",
            color="Prediction",
            title="Attrition Distribution"
            )

            col1.plotly_chart(
            fig,
            use_container_width=True
            )

            fig2 = px.box(
            df_original,
            x="Prediction",
            y="MonthlyIncome",
            color="Prediction",
            title="Income Impact"
            )

            col2.plotly_chart(
            fig2,
            use_container_width=True
            )

            fig3 = px.histogram(
            df_original,
            x="Department",
            color="Prediction",
            title="Department Impact"
            )

            st.plotly_chart(
            fig3,
            use_container_width=True
            )

            st.divider()

            # Expandable table

            with st.expander("View Full Prediction Data"):

                st.dataframe(df_original)

            # Insights

            st.subheader("Key Insights")

            st.info("""

Employees working overtime show higher attrition.

Lower salary employees show higher risk.

Job satisfaction affects retention.

Early tenure employees show higher turnover.

""")

            # Recommendations

            st.subheader("HR Recommendations")

            st.success("""

Reduce overtime workload.

Improve employee engagement.

Review salary structure.

Provide career growth.

Improve work life balance.

""")

            # Download

            st.subheader("Export Results")

            st.download_button(

            "Download Predictions",

            df_original.to_csv(index=False),

            "attrition_results.csv"

            )

st.divider()

st.caption(
"Employee Attrition Analytics Platform | Built with FastAPI & Streamlit"
)