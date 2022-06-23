import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587) # or 456

print(smtp_object.ehlo()) #Checking if it works

print(smtp_object.starttls())

# password = input('What is your password')

import getpass # With this password is invisible

# Gmail account should be using 2-step verification. It can be activate in google account -> security
# Then you should genetate an App Password from google account -> security
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')
smtp_object.login(email, password)

from_address = email
to_address = email
subject = input('enter the subject line: ')
message = input('enter the body message: ')
msg = "Subject: " + subject +'\n' + message

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()

