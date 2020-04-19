# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:24:50 2020

@author: hari

Omega Curve

The following scripts allows you to call dynamic stock prices
from yahoo finance and plot Omega Curves of the stocks.

All you have to do is call the class and input your list of stocks and 
the lookback period.

Call many stocks as you want.


#Calling function:
    
    plotOmegaCurve(stocklist,historyPeriod,thresholdStart,thresholdEnd)    

    eg: plotOmegaCurve(['AAPL','AMZN','IBM','MSFT'],'1000d',0,1.5)

    Call list of stocks from yahoo finance. Check yahoo finance for ticker
    symbols.
    
    'd' is for daily data.
    
    thresholdStart and thresholdEnd are the range of threshold axis to plot
    the omega curve.


You are welcome to edit and improve the efficiency of the model.

If you find the object oriented code below difficult to understand
just request for functional code.
"""

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


class plotOmegaCurve:
    def __init__(self,stocklist,period,thresholdStart,thresholdEnd):
        self.stocklist = stocklist
        self.period = period
        self.thresholdStart = thresholdStart
        self.thresholdEnd = thresholdEnd
        self.callPrices()
        self.thresholds = np.linspace(self.thresholdStart,
                                      self.thresholdEnd,50)
        self.allVals = {}
        self.OmegaCurve()
        self.plotCurve()

    def callPrices(self):
        
        # Calling the prices from yahoo finance
        listOfStocks = [yf.Ticker(i).history(period=self.period
                                             ) for i in self.stocklist]
        
        # Zipping the stock names as keys of a dictionary
        self.listOfStocks = dict(zip(self.stocklist,listOfStocks))
        
        return self.listOfStocks
    
    def Omega(self,df,threshold):
        
        # Get daily threshold from annualised threshold value
        dailyThreshold = (threshold + 1) ** np.sqrt(1/252) - 1
        
        df['Daily Return'] = df['Close'].pct_change(1)
        
        # Get excess return
        df['Excess'] = df['Daily Return'] - dailyThreshold
        
        # Get sum of all values excess return above 0
        dfPositiveSum = (df[df['Excess'] > 0].sum())['Excess']
        
        # Get sum of all values excess return below 0
        dfNegativeSum = (df[df['Excess'] < 0].sum())['Excess']
    
        omega = dfPositiveSum/(-dfNegativeSum)
        
        return omega
    
    def OmegaCurve(self): 
        for i in self.stocklist:
            omegaValues = []
            for j in self.thresholds:
                val = round(self.Omega(self.listOfStocks[i],j),10)
                omegaValues.append(val)
            self.allVals[i] = omegaValues 
        
    def plotCurve(self):
        
        plt.figure(figsize=(12,6),dpi=150)
        for i in self.stocklist:
            plt.plot(self.thresholds,self.allVals[i],label=i)
        plt.title("Omega Curve - over last {}'s period".format(self.period))
        plt.ylabel('Omega Ratio')
        plt.xlabel('Threshold (%)')
        plt.legend()
        plt.ylim(0,1.5)

plt.style.use('seaborn')      
plotOmegaCurve(['MSFT','AMZN','KO','GS','NFLX','^GSPC'],'504d',0,1.5)
        
