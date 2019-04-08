import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random

fromaddr = "cyberbot1502@gmail.com"
toaddr = "hj101998@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'OTP'
otp = ""
while len(otp) < 6:
    otp += chr(random.randrange(48, 58))
body = "OTP-" + otp
msg.attach(MIMEText(body, 'plain'))
attachment = open("output2.xlsx", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "Hexadecimalqwertyuiop")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
print("Mail Sent Successfully to:", toaddr)
