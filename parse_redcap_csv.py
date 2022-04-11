site_file = ''
redcap_template = ''

import csv
from email.headerregistry import UniqueSingleAddressHeader 
import pandas as pd
from parse_daily_tracker import load_tracker_data
from pathlib import Path
# from tkinter import Tk    
# from tkinter.filedialog import askopenfilename
from datetime import date

# Tk().withdraw()
# redcap_template = askopenfilename(title='Select a Redcap Template') 
rc_template = pd.read_csv(redcap_template)
# Tk().withdraw()
# site_file = askopenfilename(title='Select the daily tracker')
tracker_data = load_tracker_data(site_file)
counter = 0

all_sites = tracker_data['Site ID'].unique()
for site in all_sites:
  for j in range(len(tracker_data)):
    if tracker_data['Site ID'].iloc[j] == site:
      # first add a blank row
      empty_row = pd.DataFrame(columns=[rc_template.columns]) #not working yet
      df1 = pd.concat([rc_template,empty_row],axis=1, ignore_index=True)
      
      # now write in all the data
      rc_template['site_id'] = site
      rc_template['redcap_repeat_instrument'] = "Study Team Documents"
      rc_template['redcap_repeat_instance'] = counter
      rc_template['First Name'] = tracker_data['First Name'].iloc[j]
      rc_template['Last Name']  = tracker_data['Last Name'].iloc[j]
      rc_template['Role'] = tracker_data['First Name'].iloc[j]
      #rc_template["Is this staff member the main site contact (outside of the PI)?"] = tracker_data['First Name'].iloc[j]
      rc_template['Is this staff member delegated as the trained MINI assessor?'] = tracker_data['Requires MINI Training?'].iloc[j]
      rc_template['Staff Email'] = tracker_data['Email'].iloc[j]
      rc_template['Date of HSP Training'] = tracker_data['HSP Training Expiration Date'].iloc[j]
      rc_template['CV / Resume'] = tracker_data[ 'CV/Biosketch submitted?'].iloc[j]
      rc_template['License (If applicable)'] = tracker_data['License Expiration Date'].iloc[j]
      rc_template['Listed on Delegation Log'] = tracker_data['Included in Delegation Log?'].iloc[j]
      rc_template['Rise Certificate - CSC/Protocol'] = tracker_data['Completed Protocol Training via RISE?'].iloc[j]
      rc_template['Rise Certificate - DRC/REDCap'] = tracker_data['Completed EDC Training via RISE?'].iloc[j]
      rc_template['Rise Certificate - PBC/Biospecimens'] = tracker_data['Completed Biorepository Training via RISE?'].iloc[j]
      
# write it out
filepath = Path(f'outputs/REDCapUpload/REDCap_Upload{date.today()}.csv') 
filepath.parent.mkdir(parents=True, exist_ok=True)  
rc_template.to_csv(filepath)