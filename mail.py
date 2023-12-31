import re
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from typing import Union

from pywhatsnow.core.exceptions import UnsupportedEmailProvider


def send_mail(
    email_sender: str,
    password: str,
    subject: str,
    message: Union[str, MIMEText],
    email_receiver: str,
) -> None:
    """Enviar un correo electrónico"""

    domain = re.search("(?<=@)[^.]+(?=\\.)", email_sender)

    hostnames = {
        "gmail": "smtp.gmail.com",
        "yahoo": "smtp.mail.yahoo.com",
        "outlook": "smtp.live.com",
        "aol": "smtp.aol.com",
    }

    hostname = None
    for x in hostnames:
        if x == domain.group():
            hostname = hostnames[x]
            break

    if hostname is None:
        raise UnsupportedEmailProvider(f"{domain.group()} no es compatible actualmente!")

    with smtplib.SMTP_SSL(hostname, 465) as smtp:
        smtp.login(email_sender, password)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content(message)

        smtp.send_message(msg)
        print("Correo electrónico enviado correctamente!")


def send_hmail(
    email_sender: str, password: str, subject: str, html_code: str, email_receiver: str
) -> None:
    """Enviar un correo electrónico con código HTML"""

    message = MIMEText(html_code, "html")
    send_mail(email_sender, password, subject, message, email_receiver)
