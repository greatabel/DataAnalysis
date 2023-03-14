import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_covtype
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import norm

"""
保护数据隐私的同时，找到一个低维空间，我们可以将数据投影到这个空间
最大化保留原始数据结构的情况下降低数据维度
"""


def local_gaussian_mechanism_high_dimension(data, epsilon, delta, rho, k):
    # 计算噪声标准偏差
    sigma = np.sqrt(2 * np.log(1.25 / delta))

    # 生成高斯噪音
    p, n = data.shape
    noise = np.random.normal(loc=0, scale=sigma, size=(p, p, n))
    for i in range(n):
        noise[:, :, i] = np.triu(noise[:, :, i]) + np.triu(noise[:, :, i], 1).T

    # 给数据添加噪音
    noisy_data = data + noise

    # 计算协方差矩阵
    cov_matrix = np.zeros((p, p))
    for i in range(n):
        cov_matrix += np.einsum(
            "ij, kj -> ik", noisy_data[:, :, i], noisy_data[:, :, i]
        )
    cov_matrix /= n

    # 使用 PCA 主成分分析
    pca = PCA(n_components=k)
    pca.fit(cov_matrix)
    # 主成分是带噪声数据的最佳线性投影
    principal_components = pca.components_.T

    return principal_components


covtype = fetch_covtype()
X, y = covtype.data, covtype.target


scaler = StandardScaler()
X = scaler.fit_transform(X)

# 买家自己定义数据集使用量（上次他要求）
n_samples = 1000
indices = np.random.choice(X.shape[0], n_samples, replace=False)
X_sampled = X[indices].T

# 设置选项，买家可以自己调整这块
epsilon = 1.0
delta = 1e-5
rho = 0.1

# 测试不同k
print("\n\n")
print("----1.测试不同k和方差 ----")

k_values = range(1, 6)
explained_variances = []

for k in k_values:
    noisy_data = local_gaussian_mechanism_high_dimension(
        X_sampled, epsilon, delta, rho, k
    )
    pca = PCA(n_components=k)
    pca.fit(X_sampled.T)
    explained_variance = pca.explained_variance_ratio_.sum()
    explained_variances.append(explained_variance)

plt.plot(k_values, explained_variances, marker="o")
plt.xlabel("Number of Principal Components (k)")
plt.ylabel("Variance")
plt.title("Variance vs. k")
plt.grid()
plt.show()

# 随着选择更多的主成分，累积数据方差会逐渐增加

print("\n\n")
print("----2.选择一种k=2情况比较原始数据和隐私化后数据分类----")

k = 2
pca = PCA(n_components=k)
X_pca = pca.fit_transform(X_sampled.T)

noisy_data = local_gaussian_mechanism_high_dimension(X_sampled, epsilon, delta, rho, k)
X_noisy = np.dot(X_sampled.T, noisy_data)
pca_noisy = PCA(n_components=k)
X_pca_noisy = pca_noisy.fit_transform(X_noisy)

plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.5, label="Original Data")
plt.scatter(
    X_pca_noisy[:, 0], X_pca_noisy[:, 1], alpha=0.5, label="Privacy-Protected Data"
)
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.legend()
plt.title("First 2 Principal Components of Original and Privacy-Protected Data")
plt.show()


print("\n\n")
