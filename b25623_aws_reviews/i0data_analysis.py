#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Sports_and_Outdoors.csv
# from https://nijianmo.github.io/amazon/index.html#code
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Load the Amazon review dataset into a pandas dataframe
import pandas as pd
import matplotlib.pyplot as plt



# In[43]:


df = pd.read_csv('Sports_and_Outdoors.csv', header=None, names=['product_id', 'user_id', 'rating', 'timestamp'])


# In[44]:


df.head()


# In[45]:


print("Length of the DataFrame:", len(df))


# In[46]:


df = df.drop('timestamp', axis=1) #Dropping timestamp

df_copy = df.copy(deep=True)


# In[47]:


# Convert the user_id column from string to integer
# Map the user_id column to integers
df['user_id'] = pd.factorize(df['user_id'])[0]

df['product_id'] = pd.factorize(df['product_id'])[0]


# In[48]:


#Check Data types
df.dtypes


# In[49]:


df.head()


# In[50]:


# Plot the distribution of user ratings
plt.hist(df['rating'], bins=[0.5,1.5,2.5,3.5,4.5,5.5])
plt.title('Distribution of User Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Plot the distribution of product ratings
product_rating_counts = df.groupby('product_id')['rating'].count().values
plt.hist(product_rating_counts, bins=range(1,50))
plt.title('Distribution of Product Rating Counts')
plt.xlabel('Number of Ratings per Product')
plt.ylabel('Count')
plt.show()


# In[51]:


# Calculate the average rating for each product
average_rating = df.groupby('product_id')['rating'].mean()
# Calculate the count of ratings for each product
count_rating = df.groupby('product_id')['rating'].count()

# Create a dataframe with calculated average and count of ratings
product_ratings = pd.DataFrame({'Average Rating':average_rating, 'Rating Count':count_rating})

# Sort the dataframe by average of ratings
product_ratings_sorted = product_ratings.sort_values(by='Average Rating', ascending=False)

# Plot the distribution of average product ratings
plt.hist(product_ratings_sorted['Average Rating'], bins=np.arange(2.5, 5.1, 0.1))
plt.title('Distribution of Average Product Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Count')
plt.show()

# Plot the distribution of product rating counts
plt.hist(product_ratings_sorted['Rating Count'], bins=range(1, 100, 5))
plt.title('Distribution of Product Rating Counts')
plt.xlabel('Number of Ratings per Product')
plt.ylabel('Count')
plt.show()

# Plot the top 20 products by average rating
product_ratings_top20 = product_ratings_sorted.head(20)
product_ratings_top20.plot(kind='bar', y='Average Rating', legend=False)
plt.title('Top 20 Products by Average Rating')
plt.xlabel('Product ID')
plt.ylabel('Average Rating')
plt.show()


# In[52]:


counts = df['user_id'].value_counts()
df_final = df[df['user_id'].isin(counts[counts >= 50].index)]

print('The number of observations in the final data =', len(df_final))
print('Number of unique USERS in the final data = ', df_final['user_id'].nunique())
print('Number of unique PRODUCTS in the final data = ', df_final['product_id'].nunique())


# In[53]:


# Calculate some basic statistics about the dataset

# Convert the 'user_id' column to a string data type
# df['user_id'] = df['user_id'].astype(str)

n_users = df['user_id'].nunique()
n_products = df['product_id'].nunique()
print('Number of unique users:', n_users)
print('Number of unique products:', n_products)
print('Average rating:', np.mean(df['rating']))


# In[54]:


#Calculate the average rating for each product 
average_rating = df_final.groupby(['product_id']).mean().rating
print(average_rating.head())
#Calculate the count of ratings for each product
count_rating = df_final.groupby(['product_id']).count().rating

#Create a dataframe with calculated average and count of ratings
final_rating = pd.DataFrame(pd.concat([average_rating,count_rating], axis = 1))
final_rating.columns=["Average Rating", "Ratings Count"]

#Sort the dataframe by average of ratings
final_rating = final_rating.sort_values(by='Average Rating', ascending=False)

final_rating.head()


# In[55]:


def my_top_n_products(final_rating, n, min_interaction):
    
    #Finding movies with minimum number of interactions
    recommendations = final_rating[final_rating['Ratings Count'] >= min_interaction]
    
    #Sorting values w.r.t average rating 
    recommendations = recommendations.sort_values(by='Average Rating', ascending=False)
    
    return recommendations.index[:n]


# In[56]:


list(my_top_n_products(final_rating, 5, 50))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




