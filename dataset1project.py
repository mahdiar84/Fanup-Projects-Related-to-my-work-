import pandas as pd

data = pd.read_csv(r"C:\Users\saraye tel\OneDrive\Desktop\ARCH_Roadmap\Fanupcanvas\Dataset1")
df = pd.DataFrame(data)

# For checking
#print(df.head())

# Remove non essential column from our dataset
if "id" in df.columns:
    df = df.drop("id", axis=1)

# Total sum for sales
print("Total sale:")
print(f"{df["Sale"].sum().round(1)}$")

# Sale's mean
print("Sale mean:")
print(f"{df["Sale"].mean().round(1)}$")

# Most sales on a day
print("Most sale on a day:")
print(f"{max(df["Sale"].round(1))}$")