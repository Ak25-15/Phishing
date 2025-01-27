"""
Educational Script: Simulating a Phishing Email Structure
This script demonstrates how phishing emails are structured for educational purposes only.
DO NOT use this code for malicious activities.
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_phishing_email(to_email, subject, body):
    from_email = "example@example.com"
    password = "password123"  # Placeholder for educational purposes

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Simulated message creation (not sent)
    print("Email created successfully:")
    print(msg)

# Simulated phishing email body (for demonstration purposes)
email_body = """
<html>
  <body>
    <p>Dear Employee,<br>
       This is a simulated phishing email for educational purposes. Do not click on any suspicious links.<br>
       <a href="http://educational-phishing-example.com">Verify Account</a>
    </p>
  </body>
</html>
"""

# Simulate the creation of a phishing email
create_phishing_email("example@domain.com", "Security Update Required", email_body)
