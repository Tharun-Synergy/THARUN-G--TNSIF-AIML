import pandas as pd

prod={
    "Product Name": ["Laptop","Mobile","Shirt","Pant","Chocolate","Milk"],
    "Category": ["Electronics", "Electronics","Clothing","Clothing", "Food Products","Food Products"],
    "Price": [50000, 25000, 500, 800, 90,25],
    "Quantity Sold": [30, 70,100, 90,60,700]
}
df= pd.DataFrame(prod)
df["Total Sales"] = df["Price"] * df["Quantity Sold"]
print("Product DataFrame:","\n", df)
print("\nProduct with highest sales:","\n", df.loc[df["Total Sales"].idxmax()])
print("\nAverage Product Price:",df["Price"].mean())
print("\nProducts with quantity sold greater than 50:","\n", df[df["Quantity Sold"] > 50])
print("\nProducts sorted by total sales:","\n", df.sort_values("Total Sales"))
