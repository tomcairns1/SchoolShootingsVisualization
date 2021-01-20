'''
This file is to clean the data from the K-12 SSDB (Public) Excel file into manageable
files to be used later for visualizations
'''

import pandas as pd

#############
# Import Data
#############

# Import data
df = pd.read_excel('Data/K-12 SSDB (Public).xlsx', skiprows=[0])

# Remove Unnecessary columns
columns_to_drop = ['Gender of Victims (M/F/Both)', 'Victim\'s age(s) ',
                   'Victims Race', 'Victim Ethnicity',
                   'Shooter\'s actions immediately after shots fired', 'Summary',
                   'Narrative (Detailed Summary/ Background)', 'Sources',
                   'Time Period', 'During a Sporting Event (Y/N)',
                   'During a school sponsored event (school dance, concert, play, activity)',
                   'Location', 'Shooter Name', 'Shooter Ethnicity',
                   'Shooter had an accomplice who did not fire gun (Y/N)']

df.drop(columns_to_drop, axis=1)


############
# Clean Data
############

# Remove the specific rows that are not reliable (Reliability Score == 1) 
# Anything with a score of 1 means it was a blog post or something unreliable
# that referenced the incident
unreliable_rows = []
for index, row in df.iterrows():
    if row['Reliability Score (1-5)'] == 1:
        unreliable_rows.append(index)

df.drop(unreliable_rows)

# Group by state
overview_df = df.groupby(['State']).count()

# Count the dates to find the number of shootings in each state
overview_df = overview_df[['Date']]
overview_df.rename(columns={'Date': 'Number of shootings'}, inplace=True)
overview_df.sort_values(['Number of shootings'], inplace=True)
overview_df = overview_df[1:]


#############
# Export Data
#############

overview_df.to_csv('Data/Shootings_per_state.csv', index=True)
