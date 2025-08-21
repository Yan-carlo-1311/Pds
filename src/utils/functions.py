import numpy as np

def mi_DFT(x):
    N = len(x)
    Xm = np.zeros(N, dtype=complex)
    for m in range(N):
        suma = 0.0
        for n in range(N):
            arg = (2 * np.pi * m * n) / N
            suma += x[n] * np.exp(-1j * arg)
        Xm[m] = suma
    return Xm