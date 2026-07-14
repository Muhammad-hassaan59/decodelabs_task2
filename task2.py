import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Dataset for Data Analytics.xlsx")

# print(df.head(20)) Print first 20 rows

# print(df.tail(20)) This will print last 20 rows

info = df.info()
# print(info)  Print information about null values, data types , how many entries have in table and how many row and columns are there

statistic_info = df.describe(include="all")
# print(statistic_info) Printing info about meadian, mean, max, std, min stc 

# print(df.shape) How many rows and columns

# print(df.isna().sum()) # All null values in columns with heading or column names
# coupon_null = df[df["CouponCode"].isnull()]
# print(coupon_null)   How tO find null values in colum

# null_rows = df[df.isnull().any(axis=1)]
# print(null_rows) Fining Null values in a rows

df["CouponCode"] = df["CouponCode"].fillna("Unknown")
# print(df["CouponCode"])     Converting nulls or nan into unkown



df = df.map(lambda x : x.capitalize() if isinstance(x,str) else x)
# print(df.head(10))  Capitalize all entries
  
df["TotalPrice"] = df["TotalPrice"].round(2)
values = df["TotalPrice"]
# print(values)    Rounding values

duplicates = df[df.duplicated()]
# print(duplicates)

dup_order = df[df["OrderID"].duplicated()]
# print(dup_order)

# print(df["OrderID"].is_unique)
df["CalculatedPrice"] = df["Quantity"] * df["UnitPrice"]
# print(df[["CalculatedPrice", "TotalPrice"]])   

# print((df["TotalPrice"] < 0).any())   Checkig for negative values 

# print(df[["Quantity", "UnitPrice", "TotalPrice"]].describe())    #Look at distributions of numeric columns like Quantity, UnitPrice, TotalPrice

mean_price = df["UnitPrice"].mean()
median_price = df["UnitPrice"].median()

# print(f"Mean_Price : {mean_price}")
# print(f"Median_Price{median_price}")

# if mean_price > median_price:
#     print("Prices are right skewed(Expensive items raise mean)")
# elif mean_price < median_price:
#     print("Prices are left skewed(Cheap items lower mean)")
# else:
#     print("Prices are symmetric")    Compare mean vs median to check skewness

df["UnitPrice"].hist(bins=30)
plt.title("UnitPrice Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")


df[["Quantity","UnitPrice","TotalPrice"]].plot(kind="box")
plt.title("Boxplot Of Numeric Columns")
# plt.show()

# 5 Number summary for UnitPrice
summary = {
    "Minimum" : df["UnitPrice"].min(),
    "Q1 (25%)" : df["UnitPrice"].quantile(0.25),
    "Median": df["UnitPrice"].median(),
    "Q2 (75%)" : df["UnitPrice"].quantile(0.75),
    "Maximum" : df["UnitPrice"].max()
}

# print(summary)

df["Date"] = df["Date"].dt.strftime("%Y-%m-%d") # Changing DatTime Into Date 

#Correlation matrix for numeric columns
correlation = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].corr(method='pearson')
# print(correlation)

cancel_summary = df.groupby("PaymentMethod")["OrderStatus"].value_counts(normalize=True).unstack().fillna(0)
# print(cancel_summary)
cancel_summary.plot(kind="bar", stacked=True)
plt.title("Order Status By Payment Method")
plt.ylabel("Proportion")
# plt.show()

sales_summary = df.groupby("ReferralSource")["TotalPrice"].mean().sort_values(ascending = False)
print(sales_summary)
sales_summary.plot(kind="bar")
plt.title("Average TotalPrice By Referral Source")
plt.ylabel("Average Sales")
plt.show()