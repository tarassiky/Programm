import smtplib
from email.mime.text import MIMEText
from email.header import Header

# Настройки SMTP сервера
smtp_server = 'smtp.mail.ru'
smtp_port = 465
email_sender = 'tarassiky.dasha5@mail.ru'
email_recipient = 'tarasova_dasha5@mail.ru'
email_password = 'gT5nnCgZaMjTufZ0XH0a'

# Создание сообщения
email_content = MIMEText('Тетке приснился собачий сон, будто за нею гонится дворник с метлой, и она проснулась от страха.', 'plain', 'utf-8')
email_content['Subject'] = Header('Важно', 'utf-8')  # Заголовок письма
email_content['From'] = email_sender
email_content['To'] = email_recipient

# Отправка письма
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_recipient, email_content.as_string())
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Произошла ошибка при отправке письма: {e}")
