import streamlit as st
from my_open_key import openapi_key
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = openapi_key

OPENAI_API_KEY = openapi_key
client = OpenAI(api_key = OPENAI_API_KEY)

def AI_code_reviewer(prompt):
    
    response = client.chat.completions.create(
          model = "gpt-4o-mini",
          messages = [
                  {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Review the following code and identify potential bugs or improvements. Provide the issues as a numbered list. Return only the list of issues with no extra text or explanations:\n\n{prompt}"
            },
            {
                "role": "user",
                "content": f"Here is the original code:\n\n{prompt}\n\nReturn only the issues in the format '1. Issue one; 2. Issue two;'. Do not include any additional information."
            },
              
            ]
                            
          
    )
   
    return response.choices[0].message.content

def fixed_code(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
                {"role":"system",
                    "content": "You are a helpful assistant."},
                 { "role": "user", 
                   "content":f"Here is the original code:\n\n{prompt}\n\nBased on the following bug report:\n\n{prompt}\n\n Please provide the fixed code snippets directly without any additional text or code blocks:"}
        ]
    )
    return response.choices[0].message.content


st.image("D:\Solmon projects\GEN AI APP\Innomatics-Logo1.webp")
st.title("💬 An AI Code Reviewer")
code_input = st.text_area("Enter your Python code here:", height=150)

if st.button("Generate"):
    if code_input:
        with st.spinner('Reviewing code...'):
            review_output = AI_code_reviewer(code_input)
            output_code = fixed_code(code_input)
            st.subheader("Code Review")

            st.write("**Bug Report**")
            st.text(review_output)
            
            st.write("**Fixed Code**")
            st.code(output_code)
    else:
        st.error("Please enter some code to review.")
             
        
        

        
           