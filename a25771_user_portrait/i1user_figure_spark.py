#!/usr/bin/env python
# coding: utf-8

# In[42]:


from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

# 可视化用户画像
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
import pandas as pd


# In[43]:


# 获取已安装字体的路径
font_path = 'SourceHanSansCN-Regular.otf'

# 创建字体属性对象
font = FontProperties(fname=font_path)
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# In[44]:


# 创建SparkSession
spark = SparkSession.builder.appName("UserPortrait").getOrCreate()

# 加载用户数据
user_df = spark.read.csv("data/user_data.csv", header=True, inferSchema=True)

# 加载用户行为数据
behavior_df = spark.read.csv("data/user_behavior_data.csv", header=True, inferSchema=True)



# In[45]:


# 训练ALS模型，用于商品推荐
# 协同过滤算法
als = ALS(rank=10, maxIter=15, regParam=0.01, userCol="userId", itemCol="itemId", ratingCol="rating")
model = als.fit(behavior_df)

# 针对每个用户生成推荐列表
user_recs = model.recommendForAllUsers(10)

print('#'*20)


# In[46]:


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





# In[56]:


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


# In[57]:


# 生成特征列和标签列
feature_cols = ["age", "longitude", "latitude"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
user_recs_with_profile = assembler.transform(user_recs_with_profile)
user_recs_with_profile = user_recs_with_profile.withColumn("label", 
                                            user_recs_with_profile["gender"].isin(["Male"]).cast("double"))


# In[62]:


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


# In[63]:


# 显示用户
print("用户：")
user_df.show()




# In[64]:


# 显示推荐结果
print("推荐结果：")
print('user_recs中的recommendations列包含了为每个用户推荐的商品ID及其对应的预测评分')
user_recs_with_profile.show()



# In[65]:


# 显示标签结果
print("标签结果：")
new_user_labels.show()


# In[ ]:





# In[ ]:





# In[ ]:




