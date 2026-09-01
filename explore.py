import pandas as pd 

df = pd.read_csv("data/SGO-2021-01_Incident_Reports_ADS.csv", low_memory = False)

print(df.shape)
print()
print(df.columns.tolist())

print(df["Reporting Entity"].value_counts())
print()
print(df["Highest Injury Severity Alleged"].value_counts(dropna=False))
print()
print("total rows:", len(df))
print("unique incidents:", df["Same Incident ID"].nunique())
print()
print(df["Incident Date"].head(10))