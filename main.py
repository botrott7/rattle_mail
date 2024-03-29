import os

from modules.SMTPClient import SMTPClient
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

mailer = SMTPClient(LOGIN, PASSWORD)

mailer.send_mail(emails=['x1@yandex.ru', 'x2@gmail.com'],
                 title='First Test Title',
                 text='This is first SMTP email')
