#!/usr/bin/env python
# coding: utf-8

# In[81]:


from pyspark.sql import SparkSession

from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.ml.regression import GBTRegressor
from pyspark.ml.evaluation import RegressionEvaluator

import matplotlib.pyplot as plt
import pandas as pd


# In[82]:


# 创建SparkSession
spark = SparkSession.builder.appName('Demand Prediction').getOrCreate()

from pyspark.sql.functions import col


# In[83]:


# 导入数据

# 1.骨料的情况
# data = spark.read.format("csv").option("header", "true").load("data/Aggregate/daily_demand_totals.csv")
# 2.水泥的情况
data = spark.read.format("csv").option("header", "true").load("data/Concrete/daily_demand_totals.csv")


# In[84]:


# Convert the 'demand' column to a numeric type
data = data.withColumn("demand", col("demand").cast("double"))
# 数据清洗和准备
data = data.dropna()
data = data.withColumn("timestamp", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss"))
data = data.withColumn("year", year(col("timestamp")))
data = data.withColumn("month", month(col("timestamp")))
data = data.withColumn("day", dayofmonth(col("timestamp")))


# In[85]:


# consider more human common sense
data = data.withColumn("day_of_week", dayofweek(col("timestamp")))
data = data.withColumn("is_weekend", when(col("day_of_week").isin([1, 7]), 1).otherwise(0))


# In[86]:


# 特征工程
assembler = VectorAssembler(inputCols=["year", "month", "day", "day_of_week", "is_weekend"], outputCol="features")
data = assembler.transform(data)


# In[87]:


# 划分训练和测试数据集
(train_data, test_data) = data.randomSplit([0.7, 0.3], seed=100)


# # 数据探索

# In[88]:


# 绘制demand的直方图
demand = pd.DataFrame(train_data.select('demand').rdd.map(lambda x: x[0]).collect(), columns=['demand'])
demand.plot(kind='hist', bins=20)
plt.xlabel('Demand')
plt.show()


# In[89]:


# 绘制demand和时间的散点图
data = train_data.select('timestamp', 'demand').toPandas()
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.plot(x='timestamp', y='demand', kind='scatter', s=1)
plt.xlabel('Time')
plt.ylabel('Demand')
plt.show()


# In[90]:


# 用箱线图来检测异常值和数据分布的形状
demand = pd.DataFrame(train_data.select('demand').rdd.map(lambda x: x[0]).collect(), columns=['demand'])
demand.plot(kind='box')
plt.xlabel('Demand')
plt.show()


# In[91]:


# 定义线性回归模型
lr = LinearRegression(featuresCol="features", labelCol="demand")

# 训练模型
lr_model = lr.fit(train_data)

# 预测未来需求
predictions = lr_model.transform(test_data)

# 展示预测结果
predictions.select("year", "month", "day", "day_of_week", "is_weekend", "demand", "prediction").show()



# In[92]:


# 创建随机森林回归模型
rf = RandomForestRegressor(featuresCol="features", labelCol="demand", numTrees=10)

# 训练模型
rf_model = rf.fit(train_data)

# 预测未来需求
predictions = rf_model.transform(test_data)

# 计算模型的评估指标（均方误差）
evaluator = RegressionEvaluator(labelCol="demand", predictionCol="prediction", metricName="mse")
mse = evaluator.evaluate(predictions)

# 展示预测结果
predictions.select("year", "month", "day", "demand", "prediction").show()

# 输出均方误差
print("Mean Squared Error (MSE) on test data = %g" % mse)


# In[93]:


# 创建梯度提升树回归模型
gbt = GBTRegressor(featuresCol="features", labelCol="demand", maxIter=10)

# 训练模型
gbt_model = gbt.fit(train_data)

# 预测未来需求
predictions = gbt_model.transform(test_data)

# 计算模型的评估指标（均方误差）
evaluator = RegressionEvaluator(labelCol="demand", predictionCol="prediction", metricName="mse")
mse = evaluator.evaluate(predictions)

# 展示预测结果
predictions.select("year", "month", "day", "demand", "prediction").show()

# 输出均方误差
print(" 3 Mean Squared Error (MSE) on test data = %g" % mse)


# In[94]:


print('#'*20)
import matplotlib.pyplot as plt

# 使用三种不同的模型进行预测
lr_predictions = lr_model.transform(test_data)
rf_predictions = rf_model.transform(test_data)
gbt_predictions = gbt_model.transform(test_data)

# 使用均方误差评估每个模型的预测效果
lr_evaluator = RegressionEvaluator(labelCol="demand", predictionCol="prediction", metricName="mse")
lr_mse = lr_evaluator.evaluate(lr_predictions)
rf_evaluator = RegressionEvaluator(labelCol="demand", predictionCol="prediction", metricName="mse")
rf_mse = rf_evaluator.evaluate(rf_predictions)
gbt_evaluator = RegressionEvaluator(labelCol="demand", predictionCol="prediction", metricName="mse")
gbt_mse = gbt_evaluator.evaluate(gbt_predictions)



# In[95]:


# 选取 lr_model作为例子 预测误差分布图来观察模型的预测误差是否符合正态分布
# 计算预测误差
lr_predictions = lr_model.transform(test_data)
lr_errors = lr_predictions.select("demand", "prediction").rdd.map(lambda x: x[0] - x[1]).collect()

# 绘制预测误差分布图
pd.DataFrame(lr_errors, columns=['error']).plot(kind='hist', bins=20)
plt.xlabel('Error')
plt.show()


# In[96]:


# 创建一个时间序列的数组
time_series = test_data.select("timestamp").rdd.flatMap(lambda x: x).collect()

# Create a matplotlib chart and plot the actual demand and predictions from each model
fig, ax = plt.subplots()
ax.plot(time_series, test_data.select("demand").collect(), label="Actual")
ax.plot(time_series, rf_predictions.select("prediction").collect(), label="RF Prediction")
ax.plot(time_series, gbt_predictions.select("prediction").collect(), label="GBT Prediction")
ax.scatter(time_series, lr_predictions.select("prediction").collect(), label="LR Prediction")
ax.set_xlabel("Time")
ax.set_ylabel("Demand")
ax.set_title("Comparison of Demand Prediction Models")
ax.legend()

# Show the chart
plt.show()


# 输出评估结果
print("Linear Regression Mean Squared Error (MSE) on test data = %g" % lr_mse)
print("Random Forest Mean Squared Error (MSE) on test data = %g" % rf_mse)
print("Gradient Boosting Tree Mean Squared Error (MSE) on test data = %g" % gbt_mse)


# In[97]:


print('在预测结果可视化图表中，随机森林(Random Forest)模型和梯度提升树(Gradient Boosting Tree)\
模型的预测结果比线性回归(Linear Regression)模型的预测结果更接近实际需求值，\
选择均方误差最小的模型，也就是梯度提升树模型，作为最终的库存预测模型')


# In[98]:


import calendar
from datetime import datetime

# 生成2023年的特征数据
features_2023 = []
for month in range(1, 13):
    for day in range(1, calendar.monthrange(2023, month)[1] + 1):
        day_of_week = datetime(2023, month, day).weekday()
        is_weekend = 1 if day_of_week in (5, 6) else 0
        features_2023.append((2023, month, day, day_of_week, is_weekend))




# In[99]:


# 将特征数据转换为DataFrame
features_2023_df = spark.createDataFrame(features_2023, ["year", "month", "day", "day_of_week", "is_weekend"])

# 使用特征工程生成特征向量
features_2023_df = assembler.transform(features_2023_df)

# 使用梯度提升树模型进行预测
predictions_2023 = gbt_model.transform(features_2023_df)

# 将预测结果转换为Pandas DataFrame
predictions_2023_df = predictions_2023.select("year", "month", "day", "prediction").toPandas()

# 保留2位小数
predictions_2023_df['prediction'] = predictions_2023_df['prediction'].round(2)

# 保存预测结果到CSV文件
# 骨料保存1
# predictions_2023_df.to_csv("data/Aggregate/predictions_2023.csv", index=False)
# 水泥保存2
predictions_2023_df.to_csv("data/Concrete/predictions_2023.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:




