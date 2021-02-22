from expo_reg import ExpoReg
from lin_reg import LinReg
import pandas as pd
import numpy as np
import datetime

# Import dataframe from csv file
class IndexReg:
    pd.set_option('display.max_columns', None)
    
    def __init__(self, regtype="ExpoReg"):
        self.regtype = regtype

    def get_list(self, components_dir, years=1, export_format="csv"):
        print('''
---
Initializing Regression Ranking System...
    # made by rawsashimi1604 #
Uses Andreas Clenow's Exponential Regression System to rank stocks by price momentum.
---
        ''')
        with open(f'{components_dir}', 'r') as f:

            if self.regtype == "ExpoReg":
                reg = ExpoReg()
            
            elif self.regtype == "LinReg":
                reg = LinReg()

            else:
                print("Error selecting reg_type. Please input either 'ExpoReg' or 'LinReg'.")

            # Import csv
            df = pd.read_csv(f)

            # Set index labels as ticker symbol
            df = df.set_index('Ticker')
            print
            # Create new list for scoring and removed tickers
            score = []
            removed = []
            # Append scoring list with exponential regression
            for ticker in df.index:
                try:
                    score_val = reg.reg_stock(f'{ticker}', years, show_plot=False)
                    score.append(score_val)
                except AttributeError:
                    try:
                        # If Ticker cannot be found, try replacing "." to "-" for yfinance compatibility
                        ticker = ticker.replace(".", "-")
                        score_val = reg.reg_stock(f'{ticker}', years, show_plot=False)
                        score.append(score_val)
                    except AttributeError:
                        # If ticker still cannot be found, drop the ticker and continue with next line of code.
                        df = df.drop(f'{ticker}')
                        print(f'{ticker}"s data cannot be accessed from yfinance library. Shall remove from dataframe now')
                        removed.append(ticker)

            # Print out list of tickers that are removed
            print(f'''List of tickers that are removed \nErrorList = {removed}''')

            # Add new column "Score" to dataframe
            df['Score'] = score

            # Sort dataframe by score
            df = df.sort_values('Score', ascending=False)

            # Get Date today for file naming
            today = datetime.datetime.today().strftime("%d-%m-20%y")

            if export_format == "csv":
                # Export dataframe to csv file
                df.to_csv(f'{today} Exponential Regression Ranking.csv')
            
            elif export_format == "txt":
                # Export dataframe to txt file
                df.to_csv(f"{today} Exponential Regression Ranking.txt")

            # Output to run window.
            print(f'''Finished running program, new csv file created with ranking of stocks by exponential regression.
Sample of csv file:
        ''')
            print(df)
