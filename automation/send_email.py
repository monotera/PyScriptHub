import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from python!"
sender_email = "sende3000@gmail.com"
receiver_email = "sende3000@gmail.com"

password = input("Enter a password")

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

# Secure connection
context = ssl.create_default_context()

# Connecting to gmail
print("Sendinf email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
print("Success!")
