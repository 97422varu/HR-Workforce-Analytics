import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# Load cleaned data
df = pd.read_csv('ibm_cleaned.csv')
df_original = pd.read_csv('ibm_cleaned.csv')

# Encode categorical columns
cat_cols = ['BusinessTravel','Department','EducationField',
            'Gender','JobRole','MaritalStatus','OverTime']

le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# Features & Target
X = df.drop(columns=['Attrition'])
y = df['Attrition']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Add predictions to original dataframe (with real department names)
df_original['AttritionProbability'] = model.predict_proba(X)[:,1].round(3)
df_original['RiskLevel'] = pd.cut(df_original['AttritionProbability'],
                                   bins=[0, 0.3, 0.6, 1.0],
                                   labels=['Low','Medium','High'])
df_original['AttritionCost'] = df_original['MonthlyIncome'] * 12 * 0.5
df_original['RiskLevel'] = df_original['RiskLevel'].astype(str)

# Save for Power BI
df_original.to_csv('ibm_final.csv', index=False)
print("Done! ibm_final.csv saved")

df_original['JobSatisfaction'] = df_original['JobSatisfaction'].map({
    1: '1-Low',
    2: '2-Medium', 
    3: '3-High',
    4: '4-Very High'
})