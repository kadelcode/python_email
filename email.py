from email import message
import smtplib
'''
host: hostname of the machine running your SMTP.
port: port number on which the host machine is listening to the SMTP connections.
local_hostname: hostname of your local machine.

sendmail(): This method is used to send the mail to the desired machine
'''
sender_mail = 'ayodelekadiri.ak@gmail.com'
receivers_mail = ['kadelcode@gmail.com']

message = """
From: %s
To: %s
Subject: Sending SMTP E-mail
"""%(sender_mail, receivers_mail)

try:
    #gmail server requires the sender's password
    password = input('Input your email password:')
    #create an smtp object
    smtpobj = smtplib.SMTP('gmail.com',587)
    #login the sender
    smtpobj.login(sender_mail,password)
    smtpobj.sendmail(sender_mail, receivers_mail, message)
    print("E-mail successfully sent")

except Exception:
    print("E-mail not sent!")