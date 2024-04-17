import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns




survey_df = pd.read_csv('survey.csv')
print(survey_df.head())

#Summary for each disaster, dropping crime as its not a natural disaster
#Seperate worry scores
columns_to_drop = ['Gender', 'Family_Status',
                   'Migrant_Status', 'Residential_Status', 'Insurance',
                   'ND_Experience', 'Above_Poverty_Line', 'Employment_Status', 'Crime']
survey_worry_df = survey_df.drop(columns_to_drop, axis=1)

#Summarise worry and export
worry_summary = survey_worry_df.describe()

# Create a box plot for multiple columns
plt.figure(figsize=(10, 10))
sns.boxplot(data=survey_worry_df.drop('Respondent', axis = 1))

# Add labels and title
plt.xlabel('Natural Disaster')
plt.ylabel('Worry Score')
plt.title('Distribution of Worry Scores by Natural Disaster Type')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.show()

worry_summary.to_csv('summary_ND_worry.csv', index=False)

#Summarise for cohorts

# Group by demographic categories and calculate the average worry scores for each type of natural disaster

gender_summary_df = survey_df.groupby(['Gender']).mean()
family_summary_df= survey_df.groupby(['Family_Status']).mean()
migrant_summary_df = survey_df.groupby(['Migrant_Status']).mean()
residential_summary_df = survey_df.groupby(['Residential_Status']).mean()
insurance_summary_df = survey_df.groupby(['Insurance']).mean()
nd_exp_summary_df = survey_df.groupby(['ND_Experience']).mean()
above_pov_line_summary_df = survey_df.groupby(['Above_Poverty_Line']).mean()
employment_summary_df = survey_df.groupby(['Employment_Status']).mean()

# Concatenate the individual summary tables into a single DataFrame
combined_summary_df = pd.concat([gender_summary_df,
                                 family_summary_df,
                                 migrant_summary_df,
                                 residential_summary_df,
                                 insurance_summary_df,
                                 nd_exp_summary_df,
                                 above_pov_line_summary_df,
                                 employment_summary_df],
                                axis=0)

# Reset index to make demographic categories as columns
combined_summary_df.reset_index(inplace=True)

# Rename the index column to 'Demographic_Category'
combined_summary_df.rename(columns={'index': 'Demographic_Category'}, inplace=True)

# Display and export the combined summary DataFrame
print(combined_summary_df)
combined_summary_df.to_csv('summary_demo_worry.csv', index=False)

#Box plots suggest most worry exists around Floods and Cyclones

#Summarise Demos vs Floods and Cyclones

columns_to_drop = ['Floods', 'Bushfire','Tsunami','Earthquake','Landslide','Crime']
cyclone_summary_df = survey_df.drop(columns_to_drop, axis=1)
print(cyclone_summary_df.head())

columns_to_drop = ['Cyclone', 'Bushfire','Tsunami','Earthquake','Landslide','Crime']
flood_summary_df = survey_df.drop(columns_to_drop, axis=1)
print(flood_summary_df.head())

# Group by demographic categories and calculate the summary stats for worry scores for floods

gender_f_summary_df = flood_summary_df.groupby(['Gender']).describe()
family_f_summary_df= flood_summary_df.groupby(['Family_Status']).describe()
migrant_f_summary_df = flood_summary_df.groupby(['Migrant_Status']).describe()
residential_f_summary_df = flood_summary_df.groupby(['Residential_Status']).describe()
insurance_f_summary_df = flood_summary_df.groupby(['Insurance']).describe()
nd_exp_f_summary_df = flood_summary_df.groupby(['ND_Experience']).describe()
above_pov_line_f_summary_df = flood_summary_df.groupby(['Above_Poverty_Line']).describe()
employment_f_summary_df = flood_summary_df.groupby(['Employment_Status']).describe()

gender_f_summary_df['Group'] = 'Gender'
family_f_summary_df['Group']= 'Family Status'
migrant_f_summary_df['Group'] = 'Migrant Status'
residential_f_summary_df['Group'] = 'Home Ownership'
insurance_f_summary_df['Group'] = 'Home Insurance'
nd_exp_f_summary_df['Group'] = 'Experienced Natural Disaster'
above_pov_line_f_summary_df['Group'] = 'Income Above Poverty Line'
employment_f_summary_df['Group'] = 'Employment Status'
q

# Group by demographic categories and calculate the summary stats for worry scores for cyclones

gender_c_summary_df = cyclone_summary_df.groupby(['Gender']).describe()
family_c_summary_df= cyclone_summary_df.groupby(['Family_Status']).describe()
migrant_c_summary_df = cyclone_summary_df.groupby(['Migrant_Status']).describe()
residential_c_summary_df = cyclone_summary_df.groupby(['Residential_Status']).describe()
insurance_c_summary_df = cyclone_summary_df.groupby(['Insurance']).describe()
nd_exp_c_summary_df = cyclone_summary_df.groupby(['ND_Experience']).describe()
above_pov_line_c_summary_df = cyclone_summary_df.groupby(['Above_Poverty_Line']).describe()
employment_c_summary_df = cyclone_summary_df.groupby(['Employment_Status']).describe()

gender_c_summary_df['Group'] = 'Gender'
family_c_summary_df['Group']= 'Family Status'
migrant_c_summary_df['Group'] = 'Migrant Status'
residential_c_summary_df['Group'] = 'Home Ownership'
insurance_c_summary_df['Group'] = 'Home Insurance'
nd_exp_c_summary_df['Group'] = 'Experienced Natural Disaster'
above_pov_line_c_summary_df['Group'] = 'Income Above Poverty Line'
employment_c_summary_df['Group'] = 'Employment Status'