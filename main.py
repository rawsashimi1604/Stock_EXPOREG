from index import IndexReg
from expo_reg import ExpoReg
from lin_reg import LinReg

# Get list of trades
i = IndexReg(regtype="ExpoReg")
df = i.get_list(r'C:\Users\Gavin\Desktop\Stock_EXPOREG\S&P500 Components.csv', years=1,export_format="csv")

print(df)

