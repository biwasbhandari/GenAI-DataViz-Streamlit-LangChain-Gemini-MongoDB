import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# Load environment variables
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

# Streamlit app
st.title('CSV Address Query App')

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("CSV file uploaded successfully!")
    st.write(df)

    temperature = st.slider("Set the temperature", min_value=0.0, max_value=1.0, value=0.5)
    
    # Create the agent with error handling
    agent = create_pandas_dataframe_agent(
        GoogleGenerativeAI(api_key=google_api_key, model='gemini-pro', temperature=temperature), 
        df,
    )

    query = st.text_input("Enter your query:")
    
    if st.button("Run Query"):
        if query:
            try:
                # Ensure the correct input format with 'input' key
                result = agent.invoke({"input": {"query": query}})
                output = result.get("output")
                st.write("Query Result:")
                st.write(output)
            except Exception as e:
                st.write(f"An error occurred: {e}")
        else:
            st.write("Please enter a query.")
else:
    st.write("Please upload a CSV file.")
