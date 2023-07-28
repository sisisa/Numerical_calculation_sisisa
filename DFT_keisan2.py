import numpy as np

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex64)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return X
