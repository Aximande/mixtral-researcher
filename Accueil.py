import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="Mistral AI Hackathon",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto",
)

# Load the Mistral AI logo
logo_path = os.path.join("static", "mistral_ai_logo.png")
mistral_logo = Image.open(logo_path)

# Create the homepage layout
st.title("Welcome to the Mistral AI Hackathon!")
st.write("Explore our custom GPT Researcher application built for researchers and scientists.")

left_col, center_col, right_col = st.columns(3)

with left_col:
    st.header("About the Hackathon")
    st.write(
        "This hackathon is a collaboration between our team (david, alex, félix and Emin) and Mistral AI (+Groq!). Our goal is to develop a powerful research tool that leverages Mistral's advanced language models to run GPT Researcher."
    )
    st.write(
        "We're excited to showcase our custom adaptation of the GPT Researcher code, designed to empower researchers and scientists in their work."
    )

with center_col:
    st.image(mistral_logo, width=200)

with right_col:
    st.header("Key Features")
    st.write("- **Comprehensive Research Report Generation on Mistral Models**")
    st.write("- **Diverse Web Source Aggregation with Domain-Specific and Exclusion Capabilities**")
    st.write("- **Intuitive Web Interface**")
    st.write("- **Contextual Web Source Tracking**")
    st.write("- **Seamless Export Options**")
    st.write("- **Enhanced Verification Tool for Information Reliability**")

st.write("---")
st.write("Our custom GPT Researcher application leverages Mistral AI's advanced language models to provide researchers and scientists with powerful capabilities, including:")

with st.expander("Run GPT Researcher on Mistral Models"):
    st.write(
        "By integrating our application with Mistral AI's models, we can ensure that GPT Researcher operates on the latest and most advanced language processing capabilities. This allows for more accurate and reliable research generation, with reduced risks of hallucinations or outdated information."
    )

with st.expander("Domain-Specific and Exclusion Search"):
    st.write(
        "Our application enables researchers to focus their web searches on specific domains, such as arXiv or Google Scholar, to ensure they are accessing the most relevant and authoritative sources for their research. Additionally, they can exclude certain domains to avoid biased or unreliable information."
    )

with st.expander("Local Search and Enhanced Verification"):
    st.write(
        "Alongside the web-based search capabilities, our custom GPT Researcher also supports local document search and analysis. This allows researchers to seamlessly integrate their own materials into the research process. Furthermore, we've implemented enhanced verification tools to help researchers assess the reliability and credibility of the information they've gathered, ensuring the integrity of their research."
    )

st.write("Navigate to the other pages to explore the different functionalities of our custom GPT Researcher application.")
