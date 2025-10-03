import streamlit as st
import difflib

# --- Configuration (FAQs Data) ---
# Add your questions and answers here. 
faq_data = {
    "what is artificial intelligence": "AI is the simulation of human intelligence processes by machines, especially computer systems.",
    "what is machine learning": "ML is a subset of AI that enables systems to automatically learn and improve from experience without being explicitly programmed.",
    "what is python used for": "Python is a high-level language widely used for web development, data science, machine learning, and scripting.",
    "where can i learn dsa": "You can learn Data Structures and Algorithms (DSA) on platforms like LeetCode, HackerRank, GeeksforGeeks, and Coursera."
}
# ---------------------------------

st.title("💬 FAQ Chatbot - CodeAlpha Internship")
st.markdown("Ask a question about AI/ML or tech basics.")

# User input text box
user_input = st.text_input("Enter your question here:")

# Chatbot logic
if st.button("Get Answer"):
    if user_input:
        question = user_input.lower()
        
        # Find the closest matching FAQ question (at least 60% similar)
        # We don't need to install 'difflib' as it's a standard Python module
        match = difflib.get_close_matches(question, faq_data.keys(), n=1, cutoff=0.6)
        
        if match:
            st.success(f"**Answer:** {faq_data[match[0]]}")
        else:
            st.warning("⚠️ Sorry, I don't have a direct answer for that. Please try asking about AI, ML, or Python basics.")
    else:
        st.error("❌ Please enter a question to get an answer.")