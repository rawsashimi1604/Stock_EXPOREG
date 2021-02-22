import yfinance as  yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

class LinReg:
    def __init__(self):
        pass

    def reg_stock(self, stock_ticker, period_years=1, show_plot=False):
        # Define ticker
        ticker = f'{stock_ticker}'

        # Draw data from yfinance
        stock = yf.Ticker(f"{ticker}")
        hist = stock.history(period=f'{period_years}y', interval='1d')['Close']

        # Get Data of ticker
        ticker_data = hist
        df = pd.DataFrame({'Date': ticker_data.index, 'Price': ticker_data.values})
        
        # Drop Rows from Dataframe which contains NaN values from price.
        df = df.dropna()

        # Get ordinal Dates into new column
        df['date_ordinal'] = pd.to_datetime(df['Date']).apply(lambda date: date.toordinal())

        # Get Ordinal Date Plots ( x axis )
        date_plot = df['date_ordinal'].tolist()
        date_numpy = np.array(date_plot)

        # Get Price Plots ( y axis )
        price_plot = df['Price'].tolist()
        price_array = np.array(price_plot)
        price_numpy = price_array

        # Get Date Plots ( x axis renamed )
        # convert series timestamps using pandas date time format string, then send to a new list
        rename_date_plot = df['Date'].dt.strftime('%Y-%m-%d').tolist()
        rename_date_array = np.array(rename_date_plot)

        # unshaped Ordinal Date Plot
        unshaped_date_numpy = date_plot = np.array(df['date_ordinal'].tolist())

        # Create Linear Regression Object
        linreg = LinearRegression()

        # Reshape date array to fit linear regression model
        date_numpy = date_numpy.reshape(-1, 1)

        # Fit linear regression model into data points.
        linreg.fit(date_numpy, price_numpy)

        # Predict linear regression y values
        price_numpy_pred = linreg.predict(date_numpy)

        # Create plot
        plt.plot(date_numpy, price_numpy, markevery=5)

        # Plot regression line on scatter plot
        plt.plot(date_numpy, price_numpy_pred, color='red', markevery=5)

        # Labels for x and y axis.
        plt.xlabel('Dates')
        plt.ylabel('Close Price [$]')

        # y = mx + c
        # Find gradient of lin reg
        gradient = round(float(linreg.coef_[0]), 5)

        # Find intercept of lin reg
        intercept = round(linreg.intercept_, 2)

        # Find score/ RSquare for linear regression model
        r_squared = round(linreg.score(date_numpy, price_numpy, sample_weight=None), 3)

        # Set title
        plt.title(f'{ticker} Linear Regression')

        # Get Scored linear regression
        score_val = round(((1 + gradient)**250 * r_squared) * 250, 2)

        print(f'''{ticker} Linear Regression - RSquared : {r_squared}, Score : {score_val}
---
            ''')

        # Add text of r squared, and gradient on plot, change font size to fit the plot.
        font_dict = {'size': 7.5}
        props = dict(boxstyle='round', facecolor='lightblue', alpha=0.9)
        plt.text(date_numpy[-1], price_numpy[-1], f" Slope = {gradient} \n R^2 = {r_squared} \n Score = {score_val}",
                fontdict=font_dict,
                bbox=props)

        # Set new x labels
        # Get unshaped date ord array index, then replace with new dates, followed by rotation for visual effect
        plt.xticks(unshaped_date_numpy, rename_date_array, rotation=45)
        # Show only 15 dates for visual effect.
        plt.locator_params(axis="x", nbins=15)
        # Lower font size so it fits in one window
        plt.tick_params(axis="x", labelsize=6)

        # Show plot on another window yes/no
        if show_plot:
            # Show plot if true
            plt.show()
        else:
            # Do not show plot if false
            pass

        # Function returns score value of linear regression
        return score_val
