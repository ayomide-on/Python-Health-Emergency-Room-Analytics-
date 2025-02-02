import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import plotly.express as px

print("Libraries imported successfully!")

df = pd.read_csv('/content/Hospital ER_Data.csv')
df.head()

#create Age Groups
df['Age Group'] = pd.cut(df['Patient Age'], bins = [0, 18, 35, 50, 100], labels= ['0-18', '19-35', '36-50', '51+'])
df.head()

#Wait Time Analysis
Wait_time = df.groupby(['Department Referral', 'Age Group'])['Patient Waittime'].mean().reset_index()
print(Wait_time)

min_wait_row = df.loc[df['Patient Waittime'].idxmin()]
print("Fastest wait time :")
min_wait_row

max_wait_row = df.loc[df['Patient Waittime'].idxmax()]
print("\nMost delayed Patient Waittime:")
max_wait_row

#PatientSatisfaction Vs Wait Time
correlation = df['Patient Satisfaction Score'].corr(df['Patient Waittime'])
print("Correlation between Patient Satisfaction and Wait Time:", correlation)

#Visualization

sns.scatterplot(data = df,x = 'Patient Waittime',  y = 'Patient Satisfaction Score',)
plt.title('Patient Satisfaction vs. Wait Time')
plt.show()

#Demographic and Department Referrals
Demograhic_analysis = df.groupby(['Department Referral', 'Patient Gender', 'Patient Race']).size().reset_index(name = 'Referral Count')
print(Demograhic_analysis)

# Group by demographics and department, then calculate admission rates
admission_analysis = df.groupby(['Patient Race', 'Patient Gender', 'Department Referral'])['Patient Admission Flag'].mean().reset_index()

# Display the results
print(admission_analysis)





