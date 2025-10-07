'''
import os
import smtplib
from email.mime.text import MIMEText

def send_email(to_email: str, blog_content: str):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    if not sender_email or not sender_password:
        raise ValueError("Missing email credentials in environment variables")

    msg = MIMEText(blog_content, "plain", "utf-8")
    msg["Subject"] = "Your Generated Blog"
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
    except Exception as e:
        raise RuntimeError(f"Failed to send email: {e}")
'''