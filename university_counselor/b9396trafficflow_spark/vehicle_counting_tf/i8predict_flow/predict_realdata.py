import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.naive_bayes as nb

import pickle
from predict_train import MyEncoder

filename = "finalized_model.sav"

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
encoders = pickle.load(open('myencoders.pkl', 'rb'))


def flow_predict(input_data):
	print('input_data=', input_data, type(input_data), '*'*10)
	# 真实数据预测
	# 数据整理 input_data = ["Tuesday", "13:35", "placeid0", "down"]
	# data = [["Tuesday", "13:35", "placeid0", "down"]]
	data = [input_data]
	data = np.array(data).T
	x = []
	for row in range(len(data)):
	    encoder = encoders[row]
	    x.append(encoder.transform(data[row]))
	x = np.array(x).T

	# 真实数据预测
	prd_y = loaded_model.predict(x)
	print("真实数据预测结果:", int(prd_y))
	return int(prd_y)

if __name__ == "__main__":
	flow_predict(["Tuesday", "13:35", "placeid0", "down"])