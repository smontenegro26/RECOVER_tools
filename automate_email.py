
import compose_send_email as cse
import imaplib
import email
from email.header import decode_header
import webbrowser
import os

username = []
password = []
# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 3
# total number of emails
messages = int(messages[0])
# #check emails coming in
# messages = inbox.Items
# messages.Sort("[ReceivedTime]", True)

# for message in messages:
#     if message.subject.startswith('Company UK Cash Movement'):
#         print("Found message")
#     else:
#         print("not found")

#find the subjid from the incoming email
subjID = 'RA11601_00000'

# parse the subjID to get the siteID
tmp_str = subjID.split('_')
siteID = tmp_str[0]

# figure out site and key contacts using the site ID
siteID = cse.find_RECOVER_contacts(siteID)

# compose the email body using a template email, the subjID and site ID
msg = cse.compose_email(siteID, subjID)

# send the email
cse.send_smtp_email(msg)


