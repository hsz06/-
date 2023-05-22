import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

df = pd.read_csv('data/Temp (1).csv', encoding='utf-8')
a = df.describe()
b = df.drop(labels=['ObjectId', 'Country/Region', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 'CTS_Code', 'CTS_Name',
                    'CTS_Full_Descriptor'], axis=1)
AvgAnTemperature = b.mean()
theAvg = list(AvgAnTemperature)
theYear = []
nowYear = 1961
i = 0
while i < len(theAvg):
    theYear.append(nowYear)
    i += 1
    nowYear += 1
print(theAvg)
y1_min = np.argmin(theAvg)
y1_max = np.argmax(theAvg)


plt.figure(figsize=(20, 10), dpi=100)
plt.plot(theYear, theAvg, c='red')
plt.scatter(theYear, theAvg, c='red')
y_ticks = range(1)


show_min = '[' + str(y1_min+1961) + ' ' + str(theAvg[y1_min]) + ']'
show_max = '[' + str(y1_max+1961) + ' ' + str(theAvg[y1_max]) + ']'
plt.plot(y1_min+1961, theAvg[y1_min], 'ko')
plt.plot(y1_max+1961, theAvg[y1_max], 'ko')

plt.annotate(show_min, xy=((y1_min+1961), theAvg[y1_min]), xytext=((y1_min+1961), theAvg[y1_min]))
plt.annotate(show_max, xy=((y1_max+1961), theAvg[y1_max]), xytext=((y1_max+1961), theAvg[y1_max]))


plt.xlabel("year", fontdict={'size': 16})
plt.ylabel("avg", fontdict={'size': 16})
plt.title("Global average of changes in surface temperature", fontdict={'size': 20})
plt.show()
