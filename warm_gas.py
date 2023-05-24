import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
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
#查看各行业温室气体排放的变化
#农业林业和渔业
list1=dt1['Industry']=='Agriculture, Forestry and Fishing'
Agriculture_Forestry_Fishing=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
#Agriculture_Forestry_Fishing.plot()
##plt.show()
#温室气体
Agriculture_Forestry_Fishing3=Agriculture_Forestry_Fishing.loc[:,1211]
Agriculture_Forestry_Fishing3.plot(label="农业林业和渔业")
plt.title("农业林业和渔业")
##plt.show()

#建设业
list1=dt1['Industry']=='Construction'
Construction=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Construction1=Construction.loc[:,1216]
Construction1.plot(label="建设业")
plt.title("建设业")
##plt.show()
#电力燃气空调及蒸汽
list1=dt1['Industry']=='Electricity, Gas, Steam and Air Conditioning Supply'
Electricity_Gas_Steam_Air_Conditioning_Supply=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Electricity_Gas_Steam_Air_Conditioning_Supply1=Electricity_Gas_Steam_Air_Conditioning_Supply.loc[:,1221]
Electricity_Gas_Steam_Air_Conditioning_Supply1.plot(label="电力燃气空调及蒸汽")
plt.title("电力燃气空调及蒸汽")
#plt.show()

#制造业
list1=dt1['Industry']=='Manufacturing'
Manufacturing=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Manufacturing1=Manufacturing.loc[:,1226]
Manufacturing1.plot(label="制造业")
plt.title("制造业")
#plt.show()

#矿业
list1=dt1['Industry']=='Mining'
Mining=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Mining1=Mining.loc[:,1231]
Mining1.plot(label="矿业")
plt.title("矿业")
#plt.show()

#其他服务行业
list1=dt1['Industry']=='Other Services Industries'
Other_Services_Industries=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Other_Services_Industries1=Other_Services_Industries.loc[:,1236]
Other_Services_Industries1.plot(label="其他服务行业")
plt.title("其他服务行业")
#plt.show()

#所有家庭

list1=dt1['Industry']=='Total Households'
Total_Households=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Total_Households1=Total_Households.loc[:,1241]
Total_Households1.plot(label="全部家庭")
plt.title("全部家庭")
#plt.show()



#运输和存储
list1=dt1['Industry']=='Transportation and Storage'
Transportation_Storage=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Transportation_Storage1=Transportation_Storage.loc[:,1251]
Transportation_Storage1.plot(label="运输和存储")
plt.title("运输和存储")
#plt.show()

#供水；下水道，废物管理和补救活动
list1=dt1['Industry']=='Water supply; sewerage, waste management and remediation activities'
Watersupply_sewerage_wastemanagement_remediationactivities=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Watersupply_sewerage_wastemanagement_remediationactivities1=Watersupply_sewerage_wastemanagement_remediationactivities.loc[:,1256]
Watersupply_sewerage_wastemanagement_remediationactivities1.plot(label='供水；下水道，废物管理和补救活动')
plt.title("各行业温室气体的排放")
plt.legend(prop = {'size':7},bbox_to_anchor=(1,1))
plt.show()

#全部行业和家庭
list1=dt1['Industry']=='Total Industry and Households'
Total_Industry_Households=dt1[list1].drop(labels=["Industry","Gas_Type"],axis=1).T
Total_Industry_Households1=Total_Industry_Households.loc[:,1246]
Total_Industry_Households1.plot(label="全部行业和家庭")
plt.title("全部行业和家庭")
plt.show()
