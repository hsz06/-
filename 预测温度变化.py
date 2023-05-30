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
#根据21年数据判断模型，最终选择根据当年数据预测温度变化比较契合
'''
线性回归预测温度变化
通过基于历年温度变化数据的线性回归模型，可以捕捉到历史温度变化的趋势和模式，从而预测未来的变化趋势。
但是温度变化有很多其他因素影响，例如气体排放、能源转型、政策变化等外部因素，这些因素可能会对未来温度变化产生重大影响，但线性回归模型无法捕捉到这些复杂的非线性关系。

根据当年的温室气体排放和能源转型预测当年温度变化：
优点：

直接关联：温室气体排放和能源转型是影响气候变化的关键因素，直接使用当年数据进行预测能够更准确地反映其对温度变化的影响。
实时性：使用最新的当年数据进行预测，能够及时反映当年的温度变化情况。
缺点：

复杂性：温室气体排放和能源转型的影响因素众多，包括经济、政策、技术等多个方面，因此预测模型的建立可能较为复杂，需要考虑多个变量和其相互作用。
不确定性：温室气体排放和能源转型的数据本身可能存在不确定性，如统计误差、数据收集的局限性等，这些因素可能影响预测结果的准确性。
根据当年的温室气体排放和能源转型预测明年温度变化：
优点：

趋势延续：当年的温室气体排放和能源转型对温度变化具有一定的延续性，明年的温度变化可能受到当年因素的影响，因此可以借助当年数据预测明年的温度变化趋势。
提前预警：通过提前预测明年的温度变化，可以为决策者和相关利益方提供及时的信息，以便采取应对措施或制定政策。
缺点：

短期预测：仅基于当年数据进行预测，对于明年的温度变化只能提供短期预测，无法预测较长时间范围内的变化趋势。
系统动态性：温度变化受多种因素影响，不仅仅取决于当年的温室气体排放和能源转型，还与其他因素如天气、自然灾害等有关，因此仅凭当年数据预测明年温度变化可能存在一定的局限性。
综上所述，根据当年的温室气体排放和能源转型预测当年温度变化和明年温度变化具有直接关联和实时性的优势，能够及时反映当年的温度变化趋势，所以最终选择第一种方法
'''