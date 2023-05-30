import numpy as np
from sklearn.linear_model import LinearRegression

future_percent=[]
future_warm_gas=[]
# 历年能源转型排放数据
percent = np.array([0.18316956741246357, 0.1781364681206328, 0.17732370882482298, 0.1726964821093604, 0.17684448442331235, 0.17823691921755308, 0.17981764684693297, 0.17733650005370624, 0.1845841946834824, 0.19218822958613022, 0.193944251917869, 0.1971490302583734, 0.20797338898710158, 0.21421946345036372, 0.22217247272948892, 0.22662988799500208, 0.23583479874116556, 0.2422537913008507, 0.24813723956615705, 0.25859704334961187, 0.2766947218939881])

# 构建特征矩阵和目标向量
X = np.arange(1, len(percent)+1).reshape(-1, 1)
y = percent.reshape(-1, 1)

# 创建线性回归模型并进行拟合
model = LinearRegression()
model.fit(X, y)

# 预测未来三年的数据
future_X = np.array([[len(percent)+1], [len(percent)+2], [len(percent)+3]])
future_forecast = model.predict(future_X)

# 打印未来三年的预测数据
print("未来三年能源转型排放预测：")
for i in range(len(future_X)):
    year = int(future_X[i])
    forecast = float(future_forecast[i])
    future_percent.append(forecast)
    print(f"{year}年预测能源转型排放：{forecast}")

# 历年温室气体排放数据
warm_gas = np.array([45512.83033, 46823.61819, 47545.52433, 48157.58948, 48640.85987, 48462.70094, 48565.79311, 49392.2332, 50389.95422, 50564.0993, 48936.97075, 51061.06518])

# 构建特征矩阵和目标向量
X = np.arange(1, len(warm_gas)+1).reshape(-1, 1)
y = warm_gas.reshape(-1, 1)

# 创建线性回归模型并进行拟合
model = LinearRegression()
model.fit(X, y)

# 预测未来三年的数据
future_X = np.array([[21],[22],[23]])
future_forecast = model.predict(future_X)

# 打印未来三年的预测数据
print("未来三年温室气体排放预测：")
for i in range(len(future_X)):
    year = int(future_X[i])
    forecast = float(future_forecast[i])
    future_warm_gas.append(forecast)
    print(f"{year}年预测温室气体排放：{forecast}")

import numpy as np
from sklearn.linear_model import LinearRegression

# 历年温度变化数据
temper = np.array([0.22797156398104265, 0.2064306220095694, 0.6108038277511961, 0.6300094786729858, 0.2877061611374408, 0.5422019230769232, 0.9828018867924528, 0.7521, 0.6747867298578198, 0.8624258373205742, 0.9297264150943395, 0.8450093023255815, 0.7737476635514018, 0.8474225352112676, 0.8562638888888889, 1.011589861751152, 0.7962394366197183, 0.9020654205607477, 1.0877906976744185, 0.8039953917050691, 0.8874205607476636, 0.917185185185185, 1.0961203703703704, 1.2529814814814815, 1.4279906976744186, 1.2699392523364488, 1.2881018518518519, 1.4276279069767441, 1.538565420560748, 1.3170093457943928])

#线性回归预测
# 构建特征矩阵和目标向量
temper1=temper[:-1]
X = np.arange(1, len(temper1)+1).reshape(-1, 1)
y = temper1.reshape(-1, 1)

# 创建线性回归模型并进行拟合
model = LinearRegression()
model.fit(X, y)

# 预测未来三年的数据
future_X = np.array([[21],[22],[23]])
future_forecast = model.predict(future_X)

# 打印未来三年的预测数据
print("未来三年温度变化预测：")
for i in range(len(future_X)):
    year = int(future_X[i])
    forecast = float(future_forecast[i])
    print(f"{year}年预测温度变化：{forecast}")

#温室气体排放和能源转型数据做特征值,当年数据对应当年数据
print(len(percent))#2000-2020
print(len(warm_gas))#2010-2021
print(len(temper))#1991-2021
# 创建线性回归模型
model = LinearRegression()

# 构建特征矩阵
X = np.column_stack((warm_gas[:-1], percent[10:]))
y = temper[18:-1]

# 拟合模型
model.fit(X, y)

# 预测未来三年温度变化
future_X = np.column_stack((future_warm_gas, future_percent))
future_temper = model.predict(future_X)

print("未来三年温度变化预测：")
for i in range(len(future_temper)):
    print(f"第{i+1}年预测温度变化：{future_temper[i]}")

#温室气体排放和能源转型数据做特征值,两个特征值对温度影响具有延迟性，今年预测明年
print(len(percent))#2000-2020
print(len(warm_gas))#2010-2021
print(len(temper))#1991-2021
# 创建线性回归模型
model = LinearRegression()

# 构建特征矩阵
X = np.column_stack((warm_gas[1:], percent[10:]))
y = temper[18:-1]

# 拟合模型
model.fit(X, y)

# 预测未来三年温度变化
future_X = np.column_stack((future_warm_gas, future_percent))
future_temper = model.predict(future_X)

print("未来三年温度变化预测：")
for i in range(len(future_temper)):
    print(f"第{i+1}年预测温度变化：{future_temper[i]}")