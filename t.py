import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generate_verification_code():
    return str(random.randint(1000, 9999))


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'kirill.smirnov.spb@gmail.com'
smtp_password = 'ztoj ehgq apmm vrxv'

recipient_email = input("Введите адрес электронной почты: ")

verification_code = generate_verification_code()

msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = recipient_email
msg['Subject'] = 'Код подтверждения'

message = f'Ваш код подтверждения: {verification_code}'
msg.attach(MIMEText(message, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, recipient_email, msg.as_string())
    server.quit()
    print("Письмо с кодом подтверждения отправлено успешно.")
except Exception as e:
    print("Ошибка при отправке письма: ", str(e))
