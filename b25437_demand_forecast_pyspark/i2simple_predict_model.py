from pyspark.sql import SparkSession

from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# 创建SparkSession
spark = SparkSession.builder.appName('Demand Prediction').getOrCreate()

from pyspark.sql.functions import col



# Rest of your code goes here...

# 导入数据
data = spark.read.format("csv").option("header", "true").load("data.csv")

# Convert the 'demand' column to a numeric type
data = data.withColumn("demand", col("demand").cast("double"))
# 数据清洗和准备
data = data.dropna()
data = data.withColumn("timestamp", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss"))
data = data.withColumn("year", year(col("timestamp")))
data = data.withColumn("month", month(col("timestamp")))
data = data.withColumn("day", dayofmonth(col("timestamp")))

# 特征工程
assembler = VectorAssembler(inputCols=["year", "month", "day"], outputCol="features")
data = assembler.transform(data)

# 划分训练和测试数据集
(train_data, test_data) = data.randomSplit([0.7, 0.3], seed=100)

# 定义线性回归模型
lr = LinearRegression(featuresCol="features", labelCol="demand")

# 训练模型
lr_model = lr.fit(train_data)

# 预测未来需求
predictions = lr_model.transform(test_data)

# 展示预测结果
predictions.select("year", "month", "day", "demand", "prediction").show()


# 
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

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


# ###

from pyspark.ml.regression import GBTRegressor
from pyspark.ml.evaluation import RegressionEvaluator

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


# 组合

# from pyspark.ml.linalg import Vectors
# from pyspark.ml.feature import VectorAssembler
# from pyspark.ml.regression import LinearRegression, GBTRegressor
# from pyspark.ml.evaluation import RegressionEvaluator

# # Split the data into training and test sets
# train_data, test_data = data.randomSplit([0.7, 0.3])

# # Train the linear regression model
# lr = LinearRegression(featuresCol="features", labelCol="demand")
# lr_model = lr.fit(train_data)

# # Train the gradient boosting tree model
# gbt = GBTRegressor(featuresCol="features", labelCol="demand")
# gbt_model = gbt.fit(train_data)

# Combine the models using weighted averaging

'''
1. PySpark：Apache Spark的Python API，用于分布式数据处理和计算。它提供了广泛的算法和工具，包括机器学习和数据处理。
https://spark-reference-doc-cn.readthedocs.io/zh_CN/latest/programming-guide/quick-start.html

2. 线性回归：一种广泛使用的机器学习算法，用于建立线性模型并预测连续变量。在本例中，我们使用线性回归来预测未来的需求。
https://aws.amazon.com/cn/what-is/linear-regression/

3. 随机森林回归：一种集成学习算法，将多个决策树组合起来，以提高预测准确性。在本例中，我们使用随机森林回归来预测未来的需求。
https://help.aliyun.com/document_detail/439734.html

4. 梯度提升树回归：一种集成学习算法，通过迭代地训练多个决策树来提高预测准确性。
https://zh.wikipedia.org/wiki/%E6%A2%AF%E5%BA%A6%E6%8F%90%E5%8D%87%E6%8A%80%E6%9C%AF

'''