import smtplib
from email.message import EmailMessage
import socket
socket.getaddrinfo('127.0.0.1', 8080)

email = EmailMessage()
email['from'] = 'Simanta karki'
email['to'] = 'sirishtitaju@gmail.com'
email['subject'] = 'k hudai xa ho bro'

email.set_content('yo message python bata code bata pahako ho')

with smtplib.SMTP(host = 'smptp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('karkisim33@gmail.com','waibapratap1')
	smtp.send_message(email)
	print('all good boss!')



