#!/usr/bin/env python
# coding: utf-8

# In[20]:


from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

# 可视化用户画像
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
import pandas as pd
from pyspark.ml.clustering import KMeans


# In[21]:


# 获取已安装字体的路径
font_path = 'SourceHanSansCN-Regular.otf'

# 创建字体属性对象
font = FontProperties(fname=font_path)
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# In[22]:


# 创建SparkSession
spark = SparkSession.builder.appName("UserPortrait").getOrCreate()

# 加载用户数据
user_df = spark.read.csv("data/user_data.csv", header=True, inferSchema=True)

# 加载用户行为数据
behavior_df = spark.read.csv("data/user_behavior_data.csv", header=True, inferSchema=True)



# In[23]:


# 统计用户数据中的记录数量
user_count = user_df.count()

# 统计用户行为数据中的记录数量
behavior_count = behavior_df.count()

# 打印结果
print("用户数据中的记录数量：", user_count)
print("用户行为数据中的记录数量：", behavior_count)


# In[24]:


# 计算用户数据中各特征之间的相关系数
# Convert the Spark DataFrame to a Pandas DataFrame
user_df_pd = user_df.toPandas()

# 将性别从分类变量转换为数值变量
user_df_pd['gender_numeric'] = user_df_pd['gender'].map({'Male': 0, 'Female': 1})

# 重新计算相关性矩阵
corr_matrix = user_df_pd.corr()

# 可视化相关性矩阵
sns.heatmap(corr_matrix, annot=True)
plt.show()





# In[25]:


# 训练ALS模型，用于商品推荐
# 协同过滤算法
als = ALS(rank=10, maxIter=15, regParam=0.01, userCol="userId", itemCol="itemId", ratingCol="rating")
model = als.fit(behavior_df)

# 针对每个用户生成推荐列表
user_recs = model.recommendForAllUsers(10)

print('#'*20)


# In[26]:


# 将用户画像和推荐结果连接起来
user_recs_with_profile = user_recs.join(user_df, on="userId", how="left")




# 将 PySpark DataFrame 转换为 Pandas DataFrame
user_df_pd = user_df.toPandas()

# 绘制用户年龄分布图
sns.histplot(data=user_df_pd, x="age")


# 绘制用户地理位置云图
# 绘制散点图

plt.xlabel('年龄', fontproperties=font)
plt.ylabel('频数', fontproperties=font)
plt.title('年龄分布直方图', fontproperties=font)
plt.show()





# In[27]:


sns.countplot(data=user_df_pd, x="gender")
plt.xlabel('性别', fontproperties=font)
plt.ylabel('频数', fontproperties=font)
plt.title('性别分布', fontproperties=font)
plt.show()


# In[28]:


# 用户行为数据转换为 Pandas DataFrame
behavior_df_pd = behavior_df.toPandas()

# 合并用户数据和行为数据
user_behavior_df_pd = pd.merge(user_df_pd, behavior_df_pd, on="userId")

# 绘制年龄与评分的关系
sns.scatterplot(data=user_behavior_df_pd, x="age", y="rating", hue="gender")
plt.xlabel('年龄', fontproperties=font)
plt.ylabel('评分', fontproperties=font)
plt.title('年龄与评分关系', fontproperties=font)
plt.show()


# In[ ]:





# In[29]:


sns.histplot(data=behavior_df_pd, x="rating", bins=5)
plt.xlabel('评分', fontproperties=font)
plt.ylabel('频数', fontproperties=font)
plt.title('评分分布', fontproperties=font)
plt.show()


# In[ ]:





# In[ ]:





# In[30]:


# 绘制用户地理位置云图
sns.scatterplot(data=user_df_pd, x="longitude", y="latitude", hue="city")

# 设置图例字体
current_legend = plt.legend()
plt.legend(title=current_legend.get_title().get_text(), labels=[t.get_text() for t in current_legend.texts], 
           loc=current_legend._loc, prop=font)

# 设置坐标轴标签和标题
plt.xlabel('经度', fontproperties=font)
plt.ylabel('纬度', fontproperties=font)
plt.title('城市分布图', fontproperties=font)

plt.show()


# In[31]:


# 生成特征列和标签列
feature_cols = ["age", "longitude", "latitude"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
user_recs_with_profile = assembler.transform(user_recs_with_profile)
user_recs_with_profile = user_recs_with_profile.withColumn("label", 
                                            user_recs_with_profile["gender"].isin(["Male"]).cast("double"))


# In[40]:


# 生成特征列和标签列
feature_cols = ["age", "longitude", "latitude"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
user_df = assembler.transform(user_df)
user_df = user_df.withColumn("label", user_df["gender"].isin(["Male"]).cast("double"))

# 划分训练集和测试集
train, test = user_df.randomSplit([0.7, 0.3], seed=1)
# 计算用户标签，使用逻辑回归算法
lr = LogisticRegression(featuresCol="features", labelCol="label", regParam=0.1, elasticNetParam=0.5)
lr_model = lr.fit(user_recs_with_profile)

# 使用用户画像和推荐结果生成新用户的标签
new_user_df = pd.DataFrame({"userId": [80], "age": [25], "gender": ["Male"],
                            "city": ["上海"], "longitude": [121.4737], "latitude": [31.2304]})
new_user_df = spark.createDataFrame(new_user_df)

new_user_recs = model.recommendForUserSubset(new_user_df, 10)
new_user_recs_with_profile = new_user_recs.join(new_user_df, on="userId", how="left")
new_user_recs_with_profile = assembler.transform(new_user_recs_with_profile)
new_user_recs_with_profile = new_user_recs_with_profile.withColumn("label", 
                                            new_user_recs_with_profile["gender"].isin(["Male"]).cast("double"))

new_user_labels = lr_model.transform(new_user_recs_with_profile)


# In[33]:


# 显示用户
print("用户：")
user_df.show()




# In[34]:


# 显示推荐结果
print("推荐结果：")
print('user_recs中的recommendations列包含了为每个用户推荐的商品ID及其对应的预测评分')
user_recs_with_profile.show()



# In[35]:


# 显示标签结果
print("标签结果：")
new_user_labels.show()


# In[43]:


# 导入项目数据 ，我们预设的电商不同房间和类别

item_data = [("75", "Room75", " Ecommerce_categoryA(娱乐)"), 
             ("76", "Room76", " Ecommerce_categoryB（学习）"), 
             ("77", "Room77", " Ecommerce_categoryC（在线虚拟产品）"),
             ("78", "Room78", " Ecommerce_categoryD（运动）"),

             ]

item_df = spark.createDataFrame(item_data, schema=["itemId", "itemName", "itemCategory"])

# 将推荐结果与项目数据关联
from pyspark.sql.functions import explode

# 展开recommendations列，使每行只包含一个推荐项目
user_recs_exploded = user_recs_with_profile.select("userId", explode("recommendations").alias("recommendation"))

# 提取项目ID和评分
user_recs_exploded = user_recs_exploded.select("userId", "recommendation.itemId", "recommendation.rating")

# 将推荐结果与项目数据关联
user_recs_with_item_info = user_recs_exploded.join(item_df, on="itemId", how="left")


user_recs_with_item_info_pd = user_recs_with_item_info.toPandas()
user_recs_with_item_info_pd.to_json('user_recommendations.json', orient='records', lines=True)


# 显示带有项目详细信息的推荐结果
user_recs_with_item_info.show()


# # part2
# # 使用KMeans算法对用户进行聚
# # 使用KMeans算法对用户进行聚类AN

# In[37]:


kmeans = KMeans(k=3, seed=1)
kmeans_model = kmeans.fit(user_recs_with_profile.select("features"))

# 添加聚类标签到用户画像数据中
user_clusters = kmeans_model.transform(user_recs_with_profile).select("userId", "prediction").withColumnRenamed("prediction", "cluster")

# 将聚类标签连接到推荐结果数据中
user_recs_with_profile = user_recs_with_profile.join(user_clusters, on="userId", how="left")

# 显示用户画像，包含聚类标签
print("用户画像：")
user_df.show()

# 显示推荐结果，包含聚类标签
print("推荐结果：")
user_recs_with_profile.show()

# 使用用户画像和推荐结果生成新用户的标签
new_user_clusters = kmeans_model.transform(new_user_recs_with_profile.select("features")).select("prediction").withColumnRenamed("prediction", "cluster")
new_user_recs_with_profile = new_user_recs_with_profile.join(new_user_clusters, how="left")

new_user_labels = lr_model.transform(new_user_recs_with_profile)

# 显示标签结果
print("标签结果：")
new_user_labels.show()

# 绘制用户画像分布图，按聚类标签分别显示
sns.scatterplot(data=user_recs_with_profile.toPandas(), x="longitude", y="latitude", hue="cluster")
plt.show()


# # part3
# # XGBoost分类器
# 

# In[41]:


from pyspark.ml.classification import GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

gbt = GBTClassifier(maxIter=10, featuresCol="features", labelCol="label")
gbt_model = gbt.fit(train)

# 在测试集上评估模型性能
evaluator = BinaryClassificationEvaluator(labelCol="label")
gbt_predictions = gbt_model.transform(test)
gbt_auc = evaluator.evaluate(gbt_predictions)

print("GBT AUC: {:.2f}".format(gbt_auc))


from pyspark.sql.functions import col
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score

# 计算预测精度
test_accuracy = gbt_predictions.filter(gbt_predictions.label == gbt_predictions.prediction).count() / float(test.count())
print("Test Accuracy: {:.2f}%".format(test_accuracy * 100))

# 获取混淆矩阵
test_prediction_labels = gbt_predictions.select("label", "prediction").rdd.map(lambda x: tuple(x)).toDF(["label", "prediction"])
test_prediction_np = test_prediction_labels.toPandas().to_numpy()
cm = confusion_matrix(test_prediction_np[:, 0], test_prediction_np[:, 1])

# 计算Jaccard相似度
jaccard_similarity = jaccard_score(test_prediction_np[:, 0], test_prediction_np[:, 1])

# 可视化混淆矩阵
plt.imshow(cm, cmap=plt.cm.Blues)
plt.title("GBT Confusion Matrix")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.xticks([0, 1], ["Female", "Male"])
plt.yticks([0, 1], ["Female", "Male"])
plt.colorbar()
for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, format(cm[i, j], "d"), ha="center", va="center")
plt.show()

# 输出Jaccard相似度
print("Jaccard Similarity: {:.2f}%".format(jaccard_similarity * 100))



# In[42]:


# 假设您有一个包含新用户画像信息的Pandas DataFrame（new_user_profile_df）
new_user_profile_df = pd.DataFrame({"userId": [5001], "age": [28], "gender": ["Female"],
                                    "longitude": [116.4074], "latitude": [39.9042]})

# 将Pandas DataFrame转换为Spark DataFrame
new_user_profile_spark_df = spark.createDataFrame(new_user_profile_df)

# 使用VectorAssembler将新用户的特征列组合为一个特征向量
new_user_assembled = assembler.transform(new_user_profile_spark_df)

# 使用训练好的GBT模型对新用户进行预测
new_user_predictions = gbt_model.transform(new_user_assembled)

# 显示新用户的预测结果
new_user_predictions.show()


# In[ ]:




