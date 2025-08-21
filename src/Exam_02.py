def exam_p2():
    import numpy as np
    import matplotlib.pyplot as plt
    from src.utils.functions import mi_DFT

    fs = 256
    T = 6
    N = 1536
    n = np.arange(N)

    f1, f2 = 8, 20
    X_n = np.sin(2*np.pi*f1*n/fs) + 0.5*np.sin(2*np.pi*f2*n/fs)
    Xm1 = mi_DFT(X_n)

    tol = 1e-14
    Xm1.real[abs(Xm1.real) < tol] = 0
    Xm1.imag[abs(Xm1.imag) < tol] = 0

    fan = n * fs / N

    plt.figure(figsize=(10,6))
    plt.subplot(2,1,1)
    plt.plot(n/fs, X_n)
    plt.title("Señal discreta limpia en el tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid()

    plt.subplot(2,1,2)
    plt.stem(fan[:N//2], np.abs(Xm1[:N//2])/N)
    plt.title("Espectro DFT de la señal limpia")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid()
    plt.tight_layout()

    noise = 0.5*np.random.randn(N)
    Signal_final = X_n + noise
    Xm2 = mi_DFT(Signal_final)
    Xm2.real[abs(Xm2.real) < tol] = 0
    Xm2.imag[abs(Xm2.imag) < tol] = 0

    plt.figure(figsize=(10,6))
    plt.subplot(2,1,1)
    plt.plot(n/fs, Signal_final)
    plt.title("Señal con ruido en el tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid()

    plt.subplot(2,1,2)
    plt.stem(fan[:N//2], np.abs(Xm2[:N//2])/N)
    plt.title("Espectro DFT de la señal con ruido")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid()
    plt.tight_layout()

    plt.show()
