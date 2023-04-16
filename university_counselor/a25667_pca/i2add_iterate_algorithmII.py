import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_covtype
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import norm
import os
import joblib


"""
保护数据隐私的同时，找到一个低维空间，我们可以将数据投影到这个空间
最大化保留原始数据结构的情况下降低数据维度
"""

def soft_thresholding_operator(x, lmbda):
    return np.sign(x) * np.maximum(np.abs(x) - lmbda, 0)

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

    # 计算稀疏程度参数 s
    s = np.mean(np.count_nonzero(data, axis=0))

    # 检查输入的 k 是否满足 k ≤ s ≤ p 的条件

    if not (k <= s <= p):
        raise ValueError("k must satisfy the condition k ≤ s ≤ p")
    else:
        print(k,s,p, "==> satisfy the condition k ≤ s ≤ p")

    X = np.zeros_like(cov_matrix)
    Y = np.zeros_like(cov_matrix)
    U = np.zeros_like(cov_matrix)

    # 增加迭代部分
    max_iter = 5000
    tol = 1e-5  
    # Iterate until convergence or max_iter reached
    for t in range(max_iter):
        X_prev = X.copy()


        X = np.linalg.inv(np.eye(p) + rho * np.eye(p)) @ (Y - U + rho * cov_matrix)


        Y = soft_thresholding_operator(X + U, 1 / rho)


        U = U + X - Y
        
        diff_norm = np.linalg.norm(X - X_prev)
        if diff_norm < tol:
            print(f"Converged at iteration {t+1}, diff_norm: {diff_norm:.6f}")
            break
        else:
            print(f"Iteration {t+1}, diff_norm: {diff_norm:.6f}")

    return Y


def load_local_covtype_data(local_folder):
    samples_path = os.path.join(local_folder, "samples_py3")
    targets_path = os.path.join(local_folder, "targets_py3")

    if os.path.exists(samples_path) and os.path.exists(targets_path):
        X = joblib.load(samples_path)
        y = joblib.load(targets_path)
        return X, y
    else:
        raise FileNotFoundError("Local COVERTYPE 数据集文件未找到。")

# covtype = fetch_covtype()
# X, y = covtype.data, covtype.target

# Load the COVERTYPE dataset
covtype = fetch_covtype()
X, y = covtype.data, covtype.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

n_samples = 1000
indices = np.random.choice(X.shape[0], n_samples, replace=False)
X_sampled = X[indices].T

epsilon = 1.0
delta = 1e-5
rho = 0.1

# Test different k
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

# Compare original and privacy-protected data
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