import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
data=pd.read_csv('Energy_Transition.csv',index_col=0)

#查看前5行
#国家地区，ISO2国际标准，指示，技术，能源类型，单位，来源，...年份
print(data.head())
print(data.info())

#选取世界的能源转型数据
dt=data.loc[data['Country/Region']=='World']
#查看缺失值
print(dt.info())
#去除空值及无用数据，
dt1=dt.drop(labels=['ISO2',"ISO3","Source","CTS_Code","CTS_Name","CTS_Full_Descriptor","Country/Region","Unit"],axis=1)
print(dt1.info())

#筛选发电数据
list1=dt1['Indicator']=="Electricity Generation"

#筛选可再生能源和不可再生能源
Electricity_Generation=dt1[list1]
list2=Electricity_Generation['Energy_Type']=="Total Renewable"
Total_Renewable=Electricity_Generation[list2].drop(labels=["Energy_Type","Technology","Indicator"],axis=1).T

print(Total_Renewable)
Total_Renewable.plot()
plt.legend(prop = {'size':7},bbox_to_anchor=(1,1),labels=['生物能源','地热能','水电','海洋能源','太阳能','风能'])
plt.title('可再生能源总量')
plt.show()



#不可再生能源
Electricity_Generation=dt1[list1]
list2=Electricity_Generation['Energy_Type']=="Total Non-Renewable"
Total_NoneRenewable=Electricity_Generation[list2].drop(labels=["Energy_Type","Technology","Indicator"],axis=1).T

print(Total_NoneRenewable)
Total_NoneRenewable.plot()
plt.legend(prop = {'size':7},bbox_to_anchor=(1,1),labels=['化石燃料','核','其他不可再生能源','抽水蓄能'])
plt.title('不可再生能源总量')
plt.show()

#可再生总量
Total_Renewable_all=Total_Renewable.T
Total_Renewable_all.loc['Col_sum'] = Total_Renewable_all.apply(lambda x: x.sum()) # 各列求和，添加新的行
print(Total_Renewable_all)
all=Total_Renewable_all.T
all=all["Col_sum"]
print(all)
all.plot(label='可再生能源总量')
plt.title("可再生能源总量变化")
#plt.show()

#不可再生总量
Total_NoneRenewable_all=Total_NoneRenewable.T
Total_NoneRenewable_all.loc['Col_sum'] = Total_NoneRenewable_all.apply(lambda x: x.sum()) # 各列求和，添加新的行
print(Total_NoneRenewable_all)
all1=Total_NoneRenewable_all.T
all1=all1["Col_sum"]
print(all1)
all1.plot(label='不可再生能源总量')
plt.legend(prop = {'size':7},bbox_to_anchor=(1,1))

plt.title("可再生能源与不可再生能源总量变化")
plt.show()

list1=list(all)
list2=list(all1)
list3=[list1[i]+list2[i] for i in range(len(list1))]
print(list1)
print(list3)
percent=[list1[i]/list3[i] for i in range(len(list1))]
print(percent)
percent=DataFrame(percent)
percent.plot(label='百分比')
#plt.xticks([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
plt.title('可再生能源在能源总量中的占比')
plt.legend(prop = {'size':7},bbox_to_anchor=(1,1))
plt.show()