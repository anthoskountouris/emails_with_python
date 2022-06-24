import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

emaill = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

M.login(emaill, password)

M.list() #shows the catefories of emails

M.select('inbox')

typ, data = M.search(None, 'SUBJECT "Python Script"')

print(typ)
print(data)

email_id = data[0] # getting email id
result, email_data = M.fetch(email_id, 'RFC822') # fetching the email id with the protocol RFC822

# email_data
raw_email = email_data[0][1] # fetting the message

raw_email_string = raw_email.decode('utf-8') # decoding the message

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():

    if part.get_content_type() == 'text/plain': #means is a plain text
        body = part.get_payload(decode=True)
        print(body)






