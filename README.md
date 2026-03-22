# PeopleIQ – AI Workforce Intelligence Platform

AI-powered HR analytics platform for predicting employee attrition and generating workforce insights using Machine Learning and Large Language Models.

---

## Project Overview

PeopleIQ is an end-to-end AI workforce analytics platform designed to help HR teams proactively identify employee attrition risks and make data-driven retention decisions.

The system combines Machine Learning prediction models, an AI insights engine, and an interactive analytics dashboard to transform raw HR data into actionable workforce intelligence.

This project demonstrates the integration of:

* Machine Learning prediction systems  
* AI powered insights generation  
* Backend API deployment  
* Interactive analytics dashboards  
* Business decision intelligence  

---

## Key Features

### Machine Learning Prediction
* Predict employee attrition risk using Logistic Regression  
* Feature engineered HR dataset  
* Model evaluation using ROC curves and confusion matrices  
* Risk probability scoring

### AI Workforce Intelligence
* AI generated HR insights from workforce data
* Automated HR recommendations
* Business impact summaries
* Dataset driven strategy suggestions

### HR Analytics Dashboard
* Interactive workforce analytics dashboard
* Department wise attrition analysis
* Salary vs attrition insights
* Risk distribution visualization
* High risk employee identification

### Production Style System
* FastAPI backend model deployment
* Streamlit frontend dashboard
* Modular project architecture
* Scalable ML pipeline structure

---

## Tech Stack

### Machine Learning
Scikit-learn  
Pandas  
NumPy  

### Backend
FastAPI  
Python  

### Frontend
Streamlit  
Plotly  

### AI Integration
LLM powered insights engine  

### Tools
Git  
GitHub  
Jupyter Notebook  

---

## System Architecture
The PeopleIQ platform follows a modular AI architecture that transforms raw HR data into actionable workforce intelligence through Machine Learning prediction and AI insight generation.

### Architecture Flow

```text
HR Dataset
   ↓
Data Cleaning & Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
ML Model Training
(Logistic Regression / Decision Tree / Random Forest)
   ↓
Model Evaluation
   ↓
Model Serialization
(Joblib)
   ↓
FastAPI Prediction API
   ↓
Streamlit Analytics Dashboard
   ↓
AI Insights Engine
   ↓
HR Decision Support System
```


---

## Model Performance Comparison

| Model | Accuracy | Key Observation |
|------|---------|----------------|
| Logistic Regression | 87% | Best overall performance |
| Decision Tree | 75% | Lower generalization |
| Random Forest | 87% | Good but less recall on attrition |

Final model selected:
**Logistic Regression** due to stability and interpretability.

---

## Business Problem Addressed

Employee attrition causes:

* Loss of talent
* Hiring costs
* Productivity decline
* Knowledge drain

Companies need proactive systems to detect attrition risk early.

**PeopleIQ helps HR teams:**

* Identify high risk employees
* Understand attrition drivers
* Generate retention strategies
* Improve workforce stability

---

## Business Impact

PeopleIQ can help organizations:

* Reduce employee turnover
* Improve retention strategy planning
* Identify workforce risk trends
* Enable proactive HR decision making
* Improve employee engagement

**Potential outcomes:**

* Reduced hiring costs
* Improved retention rate
* Better workforce planning
* Data driven HR strategy

---

## Screenshots

### Employee Risk Prediction Module

![Prediction](screenshots/prediction.png)

### Workforce Analytics Dashboard

![Dashboard](screenshots/dashboard.png)

### AI Workforce Intelligence

![AI](screenshots/ai_insights.png)

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/yourusername/PeopleIQ-AI-Workforce-Intelligence
```

### Move into Project Directory

```bash
cd PeopleIQ-AI-Workforce-Intelligence
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Run Backend API

```bash
uvicorn backend.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

---

### Run Frontend Dashboard

```bash
streamlit run app.py
```

Dashboard will be available at:

```
http://localhost:8501
```

---

## API Example

### POST Request

```
/predict
```

### Input Example

```json
{
  "Age": 41,
  "MonthlyIncome": 5993,
  "JobLevel": 2,
  "WorkLifeBalance": 1,
  "OverTime": "Yes"
}
```

### Output

```text
Prediction: Attrition Risk
Probability: 0.78
Risk Level: High
```


---

## Key Insights Generated

Example insights produced:

• Overtime employees show higher attrition probability  
• Low salary band employees show higher risk  
• Early tenure employees have elevated exit probability  
• Low satisfaction employees require engagement actions  

---

## HR Recommendations Generated

Example recommendations:

• Reduce overtime workload
• Conduct satisfaction reviews
• Improve compensation policies
• Strengthen onboarding programs

---

## Project Structure

```text id="h6o0il"
PeopleIQ-AI-Workforce-Intelligence/
│
├── backend/
│   ├── main.py
│   ├── ai.py
│   ├── models/
│       ├── attrition_model.pkl
│       ├── scaler.pkl
│       └── columns.pkl
│
│
├── frontend/
│   ├── app.py
│   └── style.css
│
├── notebook/
│   └── Employee-Attrition.ipynb
│
├── data/
│   └── HR_Analytics.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```


---

## Future Improvements

Planned enhancements:

* SHAP feature importance explanation
* AI HR chatbot assistant
* Employee risk explanation module
* Cloud deployment
* Docker containerization
* Role based HR dashboard
* Real time database integration

---

## Learning Outcomes

Through this project I gained experience in:

* End-to-end ML pipeline development
* Model evaluation techniques
* Backend API deployment
* AI integration with ML systems
* Dashboard development
* Business analytics thinking
* Product level project structuring

---

## Author

**Shashank**

---

## License

MIT License

---

## Project Status

Production ready portfolio project.

Actively improving with AI capabilities.

---

## Acknowledgements

HR Analytics dataset inspiration from IBM HR Analytics dataset.

---

## Contact

For collaboration or questions:

**GitHub:**
https://github.com/shashank-g2100
