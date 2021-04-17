import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.naive_bayes as nb

import pickle

class MyEncoder:
    """
    数字与字符串互转
    """

    def fit_transform(self, y):
        return y.astype(float)

    def transform(self, y):
        return y.astype(float)

    def inverse_transform(self, y):
        return y.astype(str)





def load_and_preprocess_dataset(history_file_path):
    global x, y, encoders
    # 读取数据集 整理数据集
    lines = np.loadtxt(history_file_path, delimiter=",", dtype="str")
    print(lines.shape)

    # 读取数据
    lines = np.array(lines)

    # 整理样本空间 并编码 （对列执行标签编码）
    x, y = [], []
    encoders = []  # 标签编码数组
    for index, row in enumerate(lines.T):
        rowStr = row[index]
        if rowStr.isdigit():
            encoder = MyEncoder()  # 数字编码
        else:
            encoder = sp.LabelEncoder()  # 标签编码

        if index < (len(lines.T) - 1):  # 训练样本 X
            x.append(encoder.fit_transform(row))
        else:
            y = encoder.fit_transform(row)  # 训练样本结果 Y
        encoders.append(encoder)

    # 转置
    x = np.array(x).T  
    y = np.array(y)

    print(x.shape, y.shape)
    print(x[0], y[0])

if __name__ == "__main__":
    history_file_path = "history_traffic_measurement.txt"
    print('-'*20, '1. start load_and_preprocess_dataset')
    x, y, encoders  = None, None, None
    load_and_preprocess_dataset(history_file_path)

    train_x, test_x, train_y, test_y = ms.train_test_split(
        x, y, test_size=0.25, random_state=7
    )

    print('-'*20, '2. training')
    # 选择模型 训练模型
    model = svm.SVR(kernel="rbf", C=10, epsilon=0.1, gamma="auto")
    model.fit(train_x, train_y)

    print('-'*20, '3. test on test-dataset')
    # 测试数据集预测
    prd_test_y = model.predict(test_x)
    print(sm.r2_score(test_y, prd_test_y))

    print('-'*20, '4. test on test-dataset')
    filename = "finalized_model.sav"
    pickle.dump(model, open(filename, 'wb'))

    print('encoders', encoders)
    pickle.dump(encoders, open('myencoders.pkl', 'wb'))


