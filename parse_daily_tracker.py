
import csv
import pandas as pd

def load_tracker_data(site_file): 
  
  data = pd.read_excel(site_file, sheet_name="Study Team")
  
  tracker_data = pd.DataFrame(data, columns= ['Site ID','First Name','Last Name',
  'Email', 'Site Name','Study Cohort', 'CV/Biosketch submitted?','HSP Training Expiration Date',
  'License Expiration Date','PHQ-9 Contact', 'Completed Protocol Training via RISE?',
  'Completed Biorepository Training via RISE?','Included in Delegation Log?',
  'Completed EDC Training via RISE?','Requires MINI Training?'])  
  
  return tracker_data
  

def find_phq_contact(tracker_data,siteID):

  phq_contacts = []

  for j in range(len(tracker_data)):
    if tracker_data['Site ID'].iloc[j] == siteID:
      if str(tracker_data['PHQ-9 Contact'].iloc[j]).lower() == 'yes':
        phq_contacts.append(tracker_data['Email'].iloc[j])
        site_name = tracker_data['Site Name'].iloc[j]
    
  return phq_contacts, site_name