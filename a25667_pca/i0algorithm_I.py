import numpy as np
from sklearn.datasets import fetch_covtype
from sklearn.preprocessing import StandardScaler
from scipy.stats import norm

import matplotlib.pyplot as plt
import seaborn as sns


def local_gaussian_mechanism(data, epsilon, sensitivity):
    print("#" * 20, "local_gaussian_mechanism\n")
    # 计算噪声标准差
    sigma = sensitivity / epsilon

    # 生成高斯噪声
    noise = np.random.normal(loc=0, scale=sigma, size=len(data))

    # 将噪声加到数据上
    noisy_data = data + noise

    return noisy_data


def main():
    # 加载 covtype 数据集
    covtype = fetch_covtype()
    X, y = covtype.data, covtype.target

    # 对数据进行标准化
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 取第一列数据作为例子进行隐私保护处理
    data = X[:, 0]

    # 计算数据敏感度
    sensitivity = np.max(data) - np.min(data)

    # Define a list of epsilon values
    epsilon_values = [0.1, 0.2, 0.5, 0.8, 1]

    # Loop through the epsilon values and run the local_gaussian_mechanism function
    for epsilon in epsilon_values:
        # 对数据进行隐私保护处理
        noisy_data = local_gaussian_mechanism(data, epsilon, sensitivity)

        # 打印原始数据和处理后的数据
        print(f"当隐私预算为{epsilon}时：")
        print("原始数据：", data)
        print("处理后的数据：", noisy_data)

        plt.hist(data, bins=50, alpha=0.5, label="Original")
        plt.hist(noisy_data, bins=50, alpha=0.5, label="Noisy")
        plt.legend(loc="upper right")
        plt.title("Histogram of Original and Noisy Data")
        plt.show()

        print("直方图可见#局部高斯机制算法#添加的噪声怎么改变了数据的分布")

        sns.boxplot(data=[data, noisy_data], width=0.3)
        plt.xticks([0, 1], ["Original", "Noisy"])
        plt.title("Box Plot of Original and Noisy Data")
        plt.show()

        print("箱形图可以向我们展示数据在 #局部高斯机制算法# 前后的分布、异常值的存在以及添加噪声后中位数的变化")

        # 打印原始数据和处理后的数据
        print("原始数据：", data)
        print("处理后的数据：", noisy_data)

        # 计算MSE
        mse = np.mean(np.square(noisy_data - data))
        print("MSE:", mse)

        # 计算ER
        er = np.sum(np.abs(noisy_data - data)) / np.sum(np.abs(data))
        print("ER:", er)

        snr = 10 * np.log10(
            np.sum(np.square(data)) / np.sum(np.square(noisy_data - data))
        )
        print("SNR:", snr)

        mae = np.mean(np.abs(noisy_data - data))
        print("MAE:", mae)

        rmse = np.sqrt(np.mean(np.square(noisy_data - data)))
        print("RMSE:", rmse)


if __name__ == "__main__":
    main()
