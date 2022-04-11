
import smtplib as smtp
from email.message import EmailMessage
from parse_daily_tracker import find_phq_contact
from docx import Document

sender = ""
password = ""
  
# content
def compose_email(siteID, subjID): 
   # find the recipients and site name
  receiver, site_name = find_phq_contact(siteID)
  full_text = []
  document = Document('PHQ-9 Email Alert Template.docx')
  
  for para in document.paragraphs:
    new_para = para.text
    if '< number >' in para.text:
      new_para = new_para.replace('< number >' ,subjID)
    if '< Coordinator >' in para.text:
      new_para = new_para.replace('< Coordinator >' ,site_name)
    full_text.append(new_para)
  
  msg_body = '\n'.join(full_text)
   
  # compile the email
  msg = EmailMessage()
  msg['subject'] = f'subject # {subjID} Suicidality Alert'   
  msg['from'] = sender
  msg['to'] = receiver
  msg.set_content(msg_body)
  return msg

def send_smtp_email(msg):
  # send the message
  try:
    server_ssl = smtp.SMTP_SSL('smtp.gmail.com', 465)
    #server_ssl = smtplib.SMTP_SSL('mail.nyumc.org', 465)
    server_ssl.ehlo()
    server_ssl.login(sender, password)
    server_ssl.sendmail(sender,  msg['to'] ,msg.as_string())
              
    # close the connection
    server_ssl.quit() 
  except Exception as ex:
      print ('Something went wrong...', ex)

