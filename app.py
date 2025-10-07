import streamlit as st
from blog_generator import generate_blog
from email_service import send_email

st.set_page_config(page_title="GenAI Blog Generator", layout="centered")

st.title("📝 GenAI Blog Generator")
st.write("Generate professional blog posts using Llama 3.3 70B (Groq API).")

# User input
topic = st.text_input("Enter your blog topic:")
email = False #st.text_input("Enter your email to receive the blog:")

if st.button("Generate Blog"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating blog..."):
            try:
                blog_content = generate_blog(topic)
                st.subheader("Generated Blog Preview:")
                st.write(blog_content)

                if email:
                    send_email(email, blog_content)
                    st.success(f"Blog sent to {email}")
                else:
                    st.info("No email entered. Blog not sent.")
            except Exception as e:
                st.error(f"Error: {e}")
