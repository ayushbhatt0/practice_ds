                        # pratice - 2    (with crime data)

'''
1. Data Loading & Overview
Load the CSV into a pandas DataFrame.

Display the first few rows to understand the dataset structure.

Check for missing values and data types of each column.

2. Basic Statistics
Calculate the total population for each year across all states.

Compute the mean, median, and standard deviation for selected crime rates (e.g., "TOTAL IPC CRIMES(per_100k)").

3. Grouping and Aggregation
Group data by "STATE/UT" and find the average number of crimes per 100,000 for each state.

Group by "YEAR" to observe nationwide crime rate trends over time.

4. Filtering and Sorting
Sort states by the highest "TOTAL IPC CRIMES(per_100k)" in a given year.

Filter rows for a specific state (e.g., "Uttar Pradesh") or crime (e.g., "RAPE(per_100k)") for trend analysis.

5. Visualization
Plot a line chart showing the trend of a specific crime type (e.g., "MURDER(per_100k)") over several years for selected states.

Create bar charts comparing total crimes per 100,000 population across states for a particular year.

6. Data Transformation
Create a new column for "CRIME DIFFERENCE" between two years for selected states.

Normalize crime values by population to compare large and small states on an equal footing.

7. Advanced Analysis
Identify top 5 states with the lowest and highest "RAPE(per_100k)" rates for each year.

Correlate demographic variables (e.g., gender distribution) with specific crime rates.

8. Exporting Results
Save aggregated results, such as annual crime summaries by state, to a new CSV file for reporting.

These tasks will help you become familiar with pandas and gain actionable insights from your dataset. Let me know if you’d like step-by-step code for any specific task!
'''



################################################################################################################################################################################################################################################


#                         # 1. Data Loading & Overview

# # Load the CSV into a pandas DataFrame.
# # Display the first few rows to understand the dataset structure.
# # Check for missing values and data types of each column.


import pandas as pd

crime= pd.read_csv(r"C:\Users\acer\Documents\practice data\final.csv",encoding="utf-8")
print(crime.head())

print(crime.isnull().sum())
print(crime.dtypes)




#                         # 2. Basic Statistics

# # Calculate the total population for each year across all states.
# # Compute the mean, median, and standard deviation for selected crime rates (e.g., "TOTAL IPC CRIMES(per_100k)").


print(crime.columns)
population_grp = crime.groupby('STATE/UT')['POPULATION'].sum()
print(population_grp)


print('mean \n',crime['TOTAL IPC CRIMES(per_100k)'].mean())
print('median \n',crime['TOTAL IPC CRIMES(per_100k)'].median())
print('standard deviation \n',crime['TOTAL IPC CRIMES(per_100k)'].std())




#                         3. Grouping and Aggregation
# Group data by "STATE/UT" and find the average number of crimes per 100,000 for each state.
# Group by "YEAR" to observe nationwide crime rate trends over time.



grp_data= crime.groupby('STATE/UT')['TOTAL IPC CRIMES(per_100k)'].mean()
print(grp_data)

grp_trend= crime.groupby('YEAR')['TOTAL IPC CRIMES(per_100k)'].mean()
print(grp_trend)





# #                         4. Filtering and Sorting

# # Sort states by the highest "TOTAL IPC CRIMES(per_100k)" in a given year.
# # Filter rows for a specific state (e.g., "Uttar Pradesh") or crime (e.g., "RAPE(per_100k)") for trend analysis.


state_bY_crime= crime.sort_values(by="TOTAL IPC CRIMES(per_100k)",ascending=False)
print(state_bY_crime[['STATE/UT','TOTAL IPC CRIMES(per_100k)']].head(10))

up_crime= crime[crime['STATE/UT']=='Uttar Pradesh']
print(up_crime[['STATE/UT','RAPE(per_100k)']])







