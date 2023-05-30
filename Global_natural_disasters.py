import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

df = pd.read_csv('Disaster.csv', encoding='utf-8', index_col=0)
a = df.describe()
# 统计各年自然灾害总数
count1 = df['Year'].value_counts(sort=False)
count1 = list(count1)
theYear = []
i = 0
nowYear = 2000

while i < len(count1):
    theYear.append(nowYear)
    i += 1
    nowYear += 1
print(theYear)
y1_min = np.argmin(count1)
y1_max = np.argmax(count1)

plt.figure(figsize=(20, 10), dpi=100)
plt.plot(theYear, count1, c='red')
plt.scatter(theYear, count1, c='red')
y_ticks = range(1)
show_min = '[' + str(y1_min + 2000) + ',' + str(count1[y1_min]) + ']'
show_max = '[' + str(y1_max + 2000) + ',' + str(count1[y1_max]) + ']'
plt.plot(y1_min + 2000, count1[y1_min], 'ko')
plt.plot(y1_max + 2000, count1[y1_max], 'ko')
plt.annotate(show_min, xy=((y1_min + 2000), count1[y1_min]), xytext=((y1_min + 2000), count1[y1_min]))
plt.annotate(show_max, xy=((y1_max + 2000), count1[y1_max]), xytext=((y1_max + 2000), count1[y1_max]))
plt.xlabel("year", fontdict={'size': 16})
plt.ylabel("total number", fontdict={'size': 16})
plt.title("Total number of natural disasters per year ", fontdict={'size': 20})
plt.show()


# demo = df.describe()

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
        2018, 2019, 2020, 2021, 2022]
damages = []
for i in year:
    test1 = df[df["Year"] == i]
    damages.append(test1['Total Damages (\'000 US$)'].mean())

y1_min = np.argmin(damages)
y1_max = np.argmax(damages)

plt.figure(figsize=(20, 10), dpi=100)
plt.plot(year, damages, c='red')
plt.scatter(year, damages, c='blue')
y_ticks = range(1)
show_min = '[' + str(y1_min + 2000) + ',' + str(damages[y1_min]) + ']'
show_max = '[' + str(y1_max + 2000) + ',' + str(damages[y1_max]) + ']'
plt.plot(y1_min + 2000, damages[y1_min], 'ko')
plt.plot(y1_max + 2000, damages[y1_max], 'ko')
plt.annotate(show_min, xy=((y1_min + 2000), damages[y1_min]), xytext=((y1_min + 2000), damages[y1_min]))
plt.annotate(show_max, xy=((y1_max + 2000), damages[y1_max]), xytext=((y1_max + 2000), damages[y1_max]))
plt.xlabel("year", fontdict={'size': 16})
plt.ylabel("amount", fontdict={'size': 16})
plt.title("Average total loss ", fontdict={'size': 20})
plt.show()