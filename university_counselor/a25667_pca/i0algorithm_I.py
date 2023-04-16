import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_covtype
import matplotlib.pyplot as plt
import os
import joblib


def load_local_covtype_data(local_folder):
    samples_path = os.path.join(local_folder, "samples_py3")
    targets_path = os.path.join(local_folder, "targets_py3")

    if os.path.exists(samples_path) and os.path.exists(targets_path):
        X = joblib.load(samples_path)
        y = joblib.load(targets_path)
        return X, y
    else:
        raise FileNotFoundError("Local COVERTYPE 数据集文件未找到。")


def local_gaussian_mechanism(X, epsilon, delta, k):
    n, p = X.shape

    # 计算 sigma
    sigma = np.sqrt(2 * np.log(1.25 / delta)) / epsilon

    # 为每个数据点生成 Zi
    X_tilde = []
    for x_i in X:
        Zi = np.zeros((p, p))
        for i in range(p):
            for j in range(i, p):
                noise = np.random.normal(0, sigma**2)
                Zi[i, j] = noise
                Zi[j, i] = noise

        x_i_tilde = x_i @ x_i.T + Zi
        X_tilde.append(x_i_tilde)

    # 计算 S_tilde
    S_tilde = np.sum(X_tilde, axis=0) / n

    # 在 S_tilde 上执行 PCA 并提取主要的 the principal k-subspace of S ̃ .
    pca = PCA(n_components=k)
    pca.fit(S_tilde)
    V_tilde_k = pca.components_.T

    return V_tilde_k, S_tilde


def visualize_data(X, X_noisy, title):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    X_noisy_pca = pca.fit_transform(X_noisy)

    plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.5, label="source_data")
    plt.scatter(
        X_noisy_pca[:, 0], X_noisy_pca[:, 1], alpha=0.5, label="with_noise_data"
    )
    plt.legend(loc="best")
    plt.title(title)
    plt.show()


def main():
    # 加载 covtype 数据集
    covtype = fetch_covtype()

    # X, _ = covtype.data, covtype.target
    local_data_folder = "covertype"

    try:
        # 尝试加载 COVERTYPE 数据集
        covtype = fetch_covtype()
        print("----from internent---")
        X, _ = covtype.data, covtype.target
    except Exception as e:
        print("无法下载 COVERTYPE 数据集，尝试从本地加载数据集。")
        X, _ = load_local_covtype_data(local_data_folder)

    # 跑全集，就注释掉这里
    subset_size = int(len(X) * 0.001)
    X = X[:subset_size]

    # 标准化数据
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 设置隐私参数
    epsilon = 0.5
    delta = 0.001

    # 为不同的 k 值运行实验
    for k in range(1, 4):
        # 应用局部高斯机制
        V_tilde_k, S_tilde = local_gaussian_mechanism(X, epsilon, delta, k)
        print(f"S_tilde {k}-sub：\n", V_tilde_k)

        if k == 2:
            # 对于其他维度，我认为可视化没有意义
            visualize_data(X, S_tilde, f"visual:k = {k}")


if __name__ == "__main__":
    main()
