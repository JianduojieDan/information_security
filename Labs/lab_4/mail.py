import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = "smtp.gmail.com" 
smtp_port = 587
sender_email = "yourownemail@gmail.com"
password = "yourpassword"         


receiver_email = "victemsemail@example.com"


subject = "account abnormal acitivity occured - please verify your account immediately"

phishing_link = "http://yourseverIP:5000" 

body = f"""
Dear user,

We detected an abnormal login activity on your account.
To protect your account security, please click the link below to verify your identity:

{phishing_link}

If you don't verify your account within 24 hours, your account will be temporarily locked.

Instagram Team
"""


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


try:
    print(f"[*] Connecting to {smtp_server}...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    
    print("[*] Logging in...")
    server.login(sender_email, password)
    
    print(f"[*] Sending phishing email to {receiver_email}...")
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    
    print("[+] Email sent successfully!")
except Exception as e:
    print(f"[-] Failed to send email: {e}")
finally:
    server.quit()
