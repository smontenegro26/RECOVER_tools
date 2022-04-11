
import csv 
import pandas as pd
from parse_daily_tracker import load_tracker_data
from pathlib import Path
from tkinter import Tk     
from tkinter.filedialog import askopenfilename

def find_idx(data_array):
  return list(filter(lambda c: data_array[c], range(len(data_array))))

def find_matches(csc_info, rise_info, column_index): 

  for j in range(len(csc_info)):
    if any(csc_info.Email.iloc[j] == rise_info.Email):
      csc_info.iloc[j,column_index] = 'Yes'
 
    elif any(rise_info['Last Name'] == csc_info['Last Name'].iloc[j]):
      idx = find_idx((rise_info['Last Name'] == csc_info['Last Name'].iloc[j]).to_numpy())

      if (rise_info['First Name'].iloc[idx].to_string(index=False)) == (csc_info['First Name'].iloc[j]):
        csc_info.iloc[j,column_index] = 'Yes'

Tk().withdraw()
rise_file = askopenfilename(title='Select a Rise Report') 
data_in = pd.read_csv(rise_file)

Tk().withdraw()
site_file = askopenfilename(title='Select the daily tracker')
csc_data = load_tracker_data(site_file)

rise_data = pd.DataFrame(data_in, columns= ['Email','First Name','Last Name','Course','Passed'])
trainings = ['protocol', 'biorepository', 'redcap']

# now look at the emails that passed in rise
for training in trainings:
  if 'redcap' in training:
    #redcap training has no quiz so take all the names
    passed = rise_data.loc[rise_data.Course.str.contains(training, case=False)]
    training = 'edc'
  else:
    #for all trainings with quizzes...
    passed = rise_data.loc[rise_data.Course.str.contains(training, case=False) & rise_data.Passed == True]
   
  columns = csc_data.columns.str.contains(training,case=False)
  column_index = find_idx(columns)

  find_matches(csc_data, passed, column_index) 

# write it out
filepath = Path('outputs/riseTraining/riseTrainingList.csv') 
filepath.parent.mkdir(parents=True, exist_ok=True)  
csc_data.to_csv(filepath)