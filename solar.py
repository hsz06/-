import netCDF4 as nc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 读取.nc文件
plt.rcParams['font.sans-serif'] = ['SimHei']
dataset = nc.Dataset('tsi_v02r01_yearly_s1610_e2022_c20230120.nc')
print(dataset.variables)  # 变量
print(99)
print(dataset.dimensions)  # 维度
print(dataset.__dict__)  # 全局属性
# 获取变量数据
data = dataset.variables['TSI'][:]
data1= dataset.variables['time'][:]
# 将数据转换为DataFrame
df = pd.DataFrame(data)
df.plot(label='百万')
#plt.xlim((1961, 2023))
#my_x_ticks = np.arange(1961, 2023, 1)
#plt.xticks(my_x_ticks)
plt.title('地球的太阳总辐射变化')
plt.show()
df1=pd.DataFrame(data1)
# 保存为.csv文件
df.to_csv('solar.csv', index=False)
#df1.to_csv('solar.csv', index=False)