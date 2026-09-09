import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ibm_final.csv')

# Check encoding
print(df['Attrition'].unique())
print(df['Attrition'].dtype)

# Chart 1 - Department
plt.figure()
df.groupby('Department')['Attrition'].mean().mul(100).plot(kind='bar', color='steelblue')
plt.title('Attrition Rate by Department')
plt.ylabel('Attrition %')
plt.tight_layout()
plt.savefig('dept_Attrition.png')
plt.close()

# Chart 2 - Overtime
plt.figure()
df.groupby('OverTime')['Attrition'].mean().mul(100).plot(kind='bar', color=['green','red'])
plt.title('OverTime VS Attrition')
plt.ylabel('Attrition %')
plt.tight_layout()
plt.savefig('OverTime_Attrition.png')
plt.close()

# Chart 3 - Salary
plt.figure()
df.groupby('Attrition')['MonthlyIncome'].mean().plot(kind='bar', color=['green','red'])
plt.title('Avg Salary: Stayed vs Left')
plt.ylabel('Monthly Income')
plt.tight_layout()
plt.savefig('salary_Attrition.png')
plt.close()

print("EDA Done! Check your folder for 3 PNG files")