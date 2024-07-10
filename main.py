import streamlit as st
from langchain.llms import OpenAI
import os
from openai_api import openai_keys

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = openai_keys

# Initialize the LLM
llm = OpenAI(temperature=0.7)

def get_credit_score_tips(credit_score):

    response = llm(f"Provide personalized tips to improve a credit score of {credit_score}")
    return response

def get_credit_utilization(balance, limit):

    utilization = (balance / limit) * 100
    response = llm(f"Give advice on a credit utilization of {utilization}% for a balance of {balance} and limit of {limit}")
    return response

def get_credit_report_education():

    response = llm("Explain the different sections of a credit report and how they impact credit scores")
    return response

def get_debt_management_plan(debt_amount, income):

    response = llm(f"Create a debt management plan for a debt of {debt_amount} with an income of {income}")
    return response

# Streamlit UI
st.title("Smart Credit Management Assistant")

menu = ["Credit Score Tips", "Credit Utilization", "Credit Report Education", "Debt Management Plan"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Credit Score Tips":

    credit_score = st.number_input("Enter your credit score")

    if st.button("Get Tips"):
        tips = get_credit_score_tips(credit_score)
        st.write(tips)

elif choice == "Credit Utilization":

    balance = st.number_input("Enter your credit card balance")
    limit = st.number_input("Enter your credit card limit")

    if st.button("Get Utilization Advice"):
        advice = get_credit_utilization(balance, limit)
        st.write(advice)

elif choice == "Credit Report Education":

    if st.button("Learn About Credit Reports"):
        education = get_credit_report_education()
        st.write(education)

elif choice == "Debt Management Plan":

    debt_amount = st.number_input("Enter your total debt amount")
    income = st.number_input("Enter your monthly income")
    
    if st.button("Get Debt Management Plan"):
        plan = get_debt_management_plan(debt_amount, income)
        st.write(plan)
