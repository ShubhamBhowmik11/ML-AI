import pandas as pd

df = pd.read_csv("synthetic_large_data.csv")
# dtypes
# astype
# to_timestamp



# - handle String
# str.lower
# str.contains
# str.upper()
# str.capitalize
df["Gender"] = df["Gender"].str.lower()
df["Gender"] = df["Gender"].str.upper()
df["Gender"] = df["Gender"].str.capitalize()

print(df["Gender"].str.contains("female", case=False))
print(df)


#Transforming Data - Feature Engineering
#apply
#assign
#map
#replace
df["Gender"] = df["Gender"].apply(lambda x : "m" if x == "male" else "f")

mp = {"m" : "mather" , "f" : "fatther"}
df["Gender"] = df["Gender"].map(mp)
df = df.assign(new_Age = df["Age"] + 10)
df["State"] = df["State"].replace("CA","JS")
print(df)

#Transforming Data  part 2



