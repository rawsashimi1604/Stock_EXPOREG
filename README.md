# Exponential Regression Ranking System
*Made by rawsashimi1604*

*example Exponential Regression AAPL*
<img width="589" alt="aapl exporeg" src="https://user-images.githubusercontent.com/75880261/108709562-d7e56a00-754d-11eb-9512-df4b4becf032.PNG">

### Introduction
Hey everyone! :wave: This project will help you rank stocks by momentum. It uses Andreas Clenow's Exponential Regression Ranking method. 
Personally, I used Python to program the exponential ranking, then exported it to the CSV.

My stock universe is the *S&P500 Index* Stocks.

### Required Modules
- yfinance
- sklearn.linear_model
- matplotlib.pyplot
- numpy
- pandas

### Usage
```python
# Import classes
from index import IndexReg
from expo_reg import ExpoReg
from lin_reg import LinReg

# Get list of stocks ranked
i = IndexReg(regtype="ExpoReg")
df = i.get_list(r'C:\Users\Gavin\Desktop\Stock_EXPOREG\S&P500 Components.csv', years=1,export_format="csv") # returns pandas DataFrame, exports to CSV

# Individual stock exporeg
e = ExpoReg()
e.reg_stock("AAPL", show_plot=True)

# Indivudual stock linear regression
i = LinReg()
i.reg_stock("AAPL", show_plot=True)
```








