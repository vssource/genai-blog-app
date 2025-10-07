# 📝 GenAI Blog Generator

Generate long-form blog posts using **Groq’s Llama 3.3 70B Versatile model** with a simple **Streamlit UI**.  
Enter a topic, get a blog preview in the app, and receive the generated blog via email.

![Demo Screenshot](demo.png) <!-- Replace with an actual screenshot or GIF -->

---

## ✨ Features
- 🌐 **Streamlit UI** for an easy, minimal interface  
- ⚡ **Groq API (Llama 3.3 70B Versatile)** for fast, high-quality blog generation  
- 📧 **Email delivery** — receive generated blog as an email  
- 🛠️ **Future-ready**: model dropdown (add more models/providers later)  
- ☁️ **Free deployment** on Streamlit Community Cloud

---

## 📂 Project Structure
genai-blog-app/
│── app.py # Main Streamlit app
│── blog_generator.py # LLM integration with Groq API
│── email_service.py # Email sending logic
│── requirements.txt # Python deps
│── README.md # This file
│── LICENSE # MIT License (create separately)
│── .gitignore # Ignore unnecessary files

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/genai-blog-app.git
    cd genai-blog-app
    ```
## Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
## Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Set up environment variables:
   Create a `.env` file in the project root with:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   SENDER_EMAIL=your_email_address
   SENDER_PASSWORD=your_email_password_or_app_specific_password
   ```
## Run the app:
   ```bash
   streamlit run app.py
   ```
## Deployment
1. Push your code to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in.
3. Click "New app", connect your GitHub repo, and select the main branch.
4. Set the environment variables in the Streamlit Cloud settings.
5. Click "Deploy".  Your app will be live in a few minutes!

## Usage
1. Open the deployed app in your browser.
2. Enter a blog topic and your email address.
3. Click "Generate Blog".
4. Preview the generated blog in the app.
5. Check your email for the full blog post.

## Author
- [Vaibhav Shah]

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Thanks to [Groq](https://www.groq.com/) for their powerful LLMs and API.
- Inspired by the amazing capabilities of Llama 3.3 and Streamlit.
