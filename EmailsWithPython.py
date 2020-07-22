#****************To Send Emails*************

# import smtplib

# #For Hidig The passwords
# import getpass

# #Creates The object
# smtp_obj=smtplib.SMTP('smtp.gmail.com',587)

# #Greets and establishes connection with the server
# smtp_obj.ehlo()

# #Since we are using Port 587,we are using TLS Encrytion,So we need to initilaize it
# smtp_obj.starttls()


# email=input("Email: ")
# password=input("Password: ")

# #Authentication
# smtp_obj.login(email,password)

# from_address=email
# to_address=email
# subject=input("Enter the Subject")
# message=input("Enter the Message")
# msg="Subject: " + subject +"\n" + message

# smtp_obj.sendmail(from_address,to_address,msg)

#****************To Recieve Emails*************
import imaplib
import email

#Creating Instance of Imaplib
M=imaplib.IMAP4_SSL('imap.gmail.com')

email=input("Email: ")
password=input("Password: ")
M.login(email,password)
M.list()




