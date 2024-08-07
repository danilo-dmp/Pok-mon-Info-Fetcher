import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(to_email, subject, body, attachment_path):
    from_email = "USER EMAIL (CHANGE)"
    password = "USER APP PASSWORD (CHANGE)"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    filename = os.path.basename(attachment_path)
    attachemnt = open(attachment_path,"rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachemnt.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit

    print("Email send sucessfully")