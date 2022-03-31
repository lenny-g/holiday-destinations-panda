import pandas as pd
destinations=pd.read_csv("Holidays.csv")
print(destinations)

data=pd.read_csv("Holidays.csv")
print (data.loc[3:8])

mean=data["Num of all-inclusive htls"].mean()
print(f"The mean of the number of all-inclusive hotels is {mean}.")

min=data["Score"].min()
print(f"The minimum score of all destinations is {min}.")

max=data["Score"].max()
print(f"The maximum score of all destinations is {max}.")

df= pd.read_csv("Holidays.csv") 
condition = df["Num of all-inclusive htls"] >= 9
print(df.loc[condition])

condition = df["Score"] >= 8
print(df.loc[condition])

condition = df["Score"] <= 2
print(df.loc[condition])


column_1 = df["Score"]
column_2 = df["Num of all-inclusive htls"]
correlation = column_1.corr(column_2)
print(correlation)
if (correlation >0.5):
  print("There is a strong colleration between the score and number of all inclusive hotels.")
elif (correlation >=0):
  print("There may be a correlation between the score and number of all inclusive hotels but not a strong one.")
else:
  print("There doesn't seem to be a correlation between the score and number of  all inclusive hotels.")
