# Omega_Curve
Omega performance measure using python

The following scripts allows you to call dynamic stock prices
from yahoo finance and plot Omega Curves of the stocks.

All you have to do is call the class and input your list of stocks and 
the lookback period.

Call many stocks/instruments as you like.


#Calling function:
    
    plotOmegaCurve(stocklist,historyPeriod,thresholdStart,thresholdEnd)    

    eg: plotOmegaCurve(['AAPL','AMZN','IBM','MSFT'],'1000d',0,1.5)

    Call list of stocks from yahoo finance. Check yahoo finance for ticker
    symbols.
    
    'd' is for daily data.
    
    thresholdStart and thresholdEnd are the range of threshold axis to plot
    the omega curve.

# Sample output
![Omega Curve](/Figure_1.png)


# Libraries
  
  Numpy == 1.18.1
  YFinance == 0.1.54
  Matplotlib == 3.1.3

You are welcome to edit and improve the efficiency of the model.

If you find the object oriented code below difficult to understand
just request for functional code.
