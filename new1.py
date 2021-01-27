# send an email through GMAIL
#Author : Conor McCaffrey

import smtplib
print('in testEmail')

username = 'conor.mccaffrey7@mail.dcu.ie'
password = 'Blacklioncrewpython .\1.'
toEmail = 'cmcaff@outlook.com'
message = 'Hello'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(username, toEmail, message)


