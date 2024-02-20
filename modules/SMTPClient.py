from email.mime.text import MIMEText
from email.header import Header
import smtplib

class SMTPClient:
    def __init__(self, login, password,
                 host='smtp.yandex.ru',
                 port=587):
        self.__login, self.__password = login, password
        self.__host = host
        self.__port = port

    def send_mail(self, emails, title, text):
        self.__msg = MIMEText(f'{text}', 'plain', 'utf-8')
        self.__msg['Subject'] = Header(title, ' utf-8')
        self.__msg['From'] = self.__login
        self.__msg['To'] = ', '.join(emails)

        s = smtplib.SMTP(self.__host, self.__port, timeout=10)

        try:
            s.starttls()
            s.login(self.__login, self.__password)
            s.sendmail(self.__msg['From'], emails, self.__msg.as_string())
        except Exception as error:
            print(error)
        finally:
            s.quit()
