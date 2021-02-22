from index import IndexReg

# Get list of trades
i = IndexReg(regtype="ExpoReg")
df = i.get_list(r'C:\Users\Gavin\Desktop\Stock_EXPOREG', years=1,export_format="csv")

print(df)