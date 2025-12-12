import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Couples AI Mediator", layout="centered")

st.title("💬 Couples AI Mediator")
st.write("Enter both perspectives below to get a neutral, AI-generated mediation summary.")

partner_a = st.text_area("Partner A's Perspective:", height=180)
partner_b = st.text_area("Partner B's Perspective:", height=180)

if st.button("Mediate the Conflict"):
    if not partner_a or not partner_b:
        st.error("Both perspectives are required.")
    else:
        prompt = f"""
Act as a neutral and emotionally intelligent relationship mediator.
Two partners have presented their perspectives on a disagreement.

Partner A says:
{partner_a}

Partner B says:
{partner_b}

Your task:
1. Summarize the disagreement neutrally.
2. Identify the core issue behind the conflict.
3. Highlight what each person is *really* trying to express (needs, fears, expectations).
4. Point out any misunderstandings or miscommunications.
5. Identify areas of agreement or shared goals.
6. Suggest practical steps to move toward resolution without taking sides.

Respond in a calm, structured, and supportive tone.
"""

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600
        )

        output = response.choices[0].message.content
        st.subheader("Mediator Response")
        st.write(output)
