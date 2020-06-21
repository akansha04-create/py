import pandas as pd

df=pd.read_csv("pandas/1_intro/nyc_weather.csv")
#print(df)
print(df['Temperature'].max())
print(df['EST'][df['Events'] == 'Rain'])
df.fillna(0,inplace=True)
#print(df)
print(df["WindSpeedMPH"].mean())
