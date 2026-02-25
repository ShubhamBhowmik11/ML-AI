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


#Transforming Data  part 2  16/jan/2026
# through this we can change the name of all coulmns,just should know with number  of columns
df.columns = ["id","name","age","gender","email","phone","address","city","state","country","nexAge"] 

# if you to changes specfic column name then 
df.rename(columns={"id":"ID"})

# sort values
res_df = df.sort_values(by="age")
res_df = df.sort_values(by=["age","address"])



#sort_index
res_df = df.sort_index(ascending=False)
#reset_index
res_df = df.reset_index()
#rank or reorder columns
#res_df = df.rank()


#task practice - task is that id  will swift to right most side of  dataset
new_df = df.copy()
new_index = [col for col in  df.columns if col != "id"] + ["id"]
print(new_df[new_index])

# write in csv file
transform_data = df.dropna()
transform_data = df.drop_duplicates()
transform_data = df.sort_values(by="age",ascending=False)
transform_data.to_csv("output.csv")


#17/jan/2026
# Grouping and Aggregating Data
#groupy()  #mean()   #min()  #max()
print(transform_data.groupby("country")["age"].mean())
print(transform_data.groupby("country")["age"].min())
print(transform_data.groupby("country")["age"].max())

#pivot and melt


#hist plot
#print(transform_data["Age"])
print(transform_data.plot(kind="scatter",x="Age",y="new_Age"))



#merge 
# by default it is innner join , if you want to use other join then you have to declation like left,right;


#21/jan/2026
#concontination



# transaction
#Atomicity - tasa will be complete or not at all 
#Consistency - data will be in consistent state
#isolation - transaction will be isolated from other transaction
#durability - once transaction is committed it will be permenant


#28/jan/2026
#commit - save changes to the database


#rollback - if face any kind of isssu duraing transaction it will rollback current state to previous stable state



# savepoint - it is use to break a transaction in smaller parts so if any issues occur we can rollback to savepoint instead of entire transtaction
  
                     #Savepoint

                     #Transcation
                     #UPDATE accounts SET balance  = balance + 1000  WHERE id = 1;