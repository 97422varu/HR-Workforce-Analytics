import pandas as pd
df=pd.read_csv("ibm.csv")
print(df)
print(df.isnull().sum())

import pandas as pd
df=pd.read_csv("ibm.csv")
df.drop(columns=['EmployeeCount', 'Over18', 'StandardHours'], inplace=True)
df["Attrition"] = df["Attrition"].map({"Yes":1,"No":0})
df.to_csv("ibm_cleaned.csv",index=False)
print("Done!",df.shape)
print(df.info())

import pandas as pd
df = pd.read_csv('ibm_final.csv')
print(df['Attrition'].unique())
print(df['Attrition'].dtype)