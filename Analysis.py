import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import plotly.express as px

print("Libraries imported successfully!")

df = pd.read_csv('/content/Hospital ER_Data.csv')
df['Patient Admission Date'] = pd.to_datetime(df['Patient Admission Date'], dayfirst=True)
df.fillna({'Patient Satisfaction Score': df['Patient Satisfaction Score'].mean()}, inplace=True)
df.head()

#create Age Groups
df['Age Group'] = pd.cut(df['Patient Age'], bins = [0, 18, 35, 50, 100], labels= ['0-18', '19-35', '36-50', '51+'])
df.head(10)

#Wait Time Analysis
Wait_time = df.groupby(['Department Referral', 'Age Group'])['Patient Waittime'].mean().reset_index()
print(Wait_time)

#PatientSatisfaction Vs Wait Time
correlation = df['Patient Satisfaction Score'].corr(df['Patient Waittime'])
print("Correlation between Patient Satisfaction and Wait Time:", correlation)

#Visualization
sns.scatterplot(data=df, x='Patient Waittime', y='Patient Satisfaction Score', hue='Patient Gender', alpha=0.7)
plt.title("Patient Satisfaction vs. Wait Time")
plt.xlabel("Wait Time (Minutes)")
plt.ylabel("Satisfaction Score")
plt.legend(title='Gender')
plt.show()

#Demographic and Department Referrals
Demograhic_analysis = df.groupby(['Department Referral', 'Patient Gender', 'Patient Race']).size().reset_index(name = 'Referral Count')
print(Demograhic_analysis)

## Visualization
# Gender Distribution
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.countplot(data=df, x='Patient Gender', ax=axes[0], palette='pastel')
axes[0].set_title("Patient Gender Distribution")

# Race Distribution
sns.countplot(data=df, y='Patient Race', ax=axes[1], palette='coolwarm', order=df['Patient Race'].value_counts().index)
axes[1].set_title("Patient Race Distribution")

# Department Referral Analysis
plt.figure(figsize=(12,6))
sns.countplot(data=df, y='Department Referral', palette='viridis', order=df['Department Referral'].value_counts().index)
plt.title("Department Referrals")
plt.xlabel("Count")
plt.ylabel("Department")

plt.show()
plt.figure(figsize=(10, 6))
df['Department Referral'].value_counts().plot.pie(autopct='%1.1f%%', cmap='viridis', startangle=90, explode=[0.05]*df['Department Referral'].nunique())
plt.title("Department Referral Distribution")
plt.show()



# Group by demographics and department, then calculate admission rates
admission_analysis = df.groupby(['Patient Race', 'Patient Gender', 'Department Referral'])['Patient Admission Flag'].mean().reset_index()

# Display the results
print(admission_analysis)

fig, axes = plt.subplots(1,2, figsize= (15,6))

#Admission by Race 
sns.countplot(data=df, y= 'Patient Race', hue = 'Patient Admission Flag', ax= axes[0])
axes[0].set_title('Admissions by Race')


#Admission by Gender
sns.countplot(data=df, y= 'Patient Gender', hue = 'Patient Admission Flag', ax = axes [1])
axes[1].set_title('Admissions by Gender')

plt.show()

# Admissions by Department Referral
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='Department Referral', hue='Patient Admission Flag', palette='Set2')
plt.xticks(rotation=45)
plt.title("Admissions by Department")
plt.xlabel("Department")
plt.ylabel("Number of Admissions")
plt.legend(title="Admission Flag")
plt.show()


# Additional Insight: Age Group Distribution
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Age Group', palette='husl', order=['0-18', '19-35', '36-50', '51+'])
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()

