import numpy as np
import statsmodels.tsa.stattools as ts
from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn
import csv

def hurst(ts):
    #Returns the Hurst Exponent of the time series vector ts
    # Create the range of lag values
    lags = range(1, 9)
    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]
    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)
    # Return the Hurst exponent from the polyfit output
    return poly[0]*2.0

def buyorsell(pricesarr):
	result = ts.adfuller(pricesarr, 1)
	avg = np.average(pricesarr)

	pvals = result[4]
	reject = pvals['5%']
	teststat = result[0]

	if reject < teststat:
	    accept = True
	    #Accept null, so random
	else:
	    accept = False
	    #Reject null, so not random

	stock = hurst(pricesarr)
	return stock

def recommendation(stock, currprice, avg):
	#mean reverting
	if stock < .40 and currprice < avg:
	    return "Buy"
	elif stock < .40 and currprice >= avg:
	    return "Sell"
	#geometric brownian mean
	elif .40 <= stock <= .60:
	    return "Hold"
	#trending
	elif stock > .60 and currprice < avg:
	    return "Sell"
	elif stock > .60 and currprice >= avg:
	    return "Buy"


with open('C:\Users\Anya\Desktop\companydata2.txt', 'rU') as csvfile:
  reader = csv.reader(csvfile, delimiter='\t', quotechar='|', dialect=csv.excel_tab)
  writer = open('C:\Users\Anya\Desktop\output.txt', 'w')

  c = 0 # row counter in csv
  
  for row in reader:
    # print column names
    temparr = []
    r = 5
    if c > 11 and c <= 4040:
      company_data = row[1:]
      currprice = company_data[14]
      symbol = company_data[1]
      country = company_data[23]
      if company_data[0] == 'Median':
      	break;
      found_bad_data = False
      for col_num in range(0, len(company_data)):
        if company_data[col_num] == "NA" and ((col_num > 2 and col_num < 23) or (col_num > 30)):
          found_bad_data = True
      if found_bad_data:
        continue # skip row
      for r in range(5, 13):
      	temparr.append(float(currprice) - float(company_data[r]))
      	r += 1 
      val = buyorsell(temparr)
      avg = np.average(temparr)
      bos = recommendation(val, currprice, avg)
      writer.write("%s, %s, %f, %s\n" % (symbol, country, val, bos))
      
    c += 1




  



