import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
data=pd.read_csv('Greenhouse_Gas.csv',index_col=0)
#查看前5行
#国家地区，ISO2国际标准，指示，单位，来源，...行业，气体类型，年份
print(data.head())
print(data.shape)
print(data.info())
#全球的气体排放
dt=data.loc[data['Country/Region']=='World']
print(dt.shape)
print(dt.info())
#去除无意义的值,只要行业，气体类型，排放量
print(type(dt))
dt1=dt.drop(labels=["Indicator","Unit","Scale",'ISO2',"ISO3","Source","CTS_Code","CTS_Name","CTS_Full_Descriptor","Country/Region"],axis=1)
print(dt1.info())
#查看各行业气体排放的变化
#农业林业和渔业
list1=dt1['Industry']=='Agriculture, Forestry and Fishing'
Agriculture_Forestry_Fishing1=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
print(Agriculture_Forestry_Fishing1)
Agriculture_Forestry_Fishing1.plot()
plt.show()
#农业林业和渔业
list1=dt1['Industry']=='Agriculture, Forestry and Fishing'
Agriculture_Forestry_Fishing1=dt1[list1].drop(labels=["Industry"],axis=1).T
print(list(Agriculture_Forestry_Fishing1))
#Agriculture_Forestry_Fishing1.plot()
#plt.show()
#农业林业和渔业
list1=dt1['Industry']=='Agriculture, Forestry and Fishing'
Agriculture_Forestry_Fishing1=dt1[list1].drop(labels=["Industry"],axis=1).T
print(list(Agriculture_Forestry_Fishing1))
#Agriculture_Forestry_Fishing1.plot()
#plt.show()
#农业林业和渔业
list1=dt1['Industry']=='Agriculture, Forestry and Fishing'
Agriculture_Forestry_Fishing1=dt1[list1].drop(labels=["Industry"],axis=1).T
print(list(Agriculture_Forestry_Fishing1))
#Agriculture_Forestry_Fishing1.plot()
#plt.show()
#农业林业和渔业
list1=dt1['Industry']=='Agriculture, Forestry and Fishing'
Agriculture_Forestry_Fishing1=dt1[list1].drop(labels=["Industry"],axis=1).T
print(list(Agriculture_Forestry_Fishing1))
<<<<<<<<< Temporary merge branch 1
#plt.show()
=========
plt.show()
>>>>>>>>> Temporary merge branch 2


