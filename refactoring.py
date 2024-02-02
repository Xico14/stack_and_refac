import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailClient:
    """
    Класс для работы с почтой.

    Атрибуты:
    login (str): Логин для доступа к почте.
    password (str): Пароль для доступа к почте.
    subject (str): Тема письма.
    recipients (list): Список получателей письма.
    message (str): Текст письма.
    header (str): Заголовок письма.
    """

    def __init__(self, login, password, subject, recipients, message, header):
        """
        Инициализирует класс EmailClient с указанными атрибутами.
        """
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        """
        Отправляет письмо.
        """
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def receive_message(self):
        """
        Получает письмо.
        """
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'Писем с указанным заголовком не найдено'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':
    client = EmailClient('login@gmail.com', 'qwerty', 'Subject', ['vasya@email.com', 'petya@email.com'], 'Message', None)
    client.send_message()
    client.receive_message()