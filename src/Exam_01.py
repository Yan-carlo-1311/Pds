import numpy as np
import matplotlib.pyplot as plt

def exam_p1():
    # Parámetros de la señal
    fm = 0.5   # frecuencia moduladora (Hz)
    fc = 8     # frecuencia portadora (Hz)
    m  = 0.5   # índice de modulación
    fs = 100   # frecuencia de muestreo (Hz)
    N  = 1024  # número de puntos para la DFT

    # Vector de tiempo
    t = np.arange(0, N/fs, 1/fs)

    # Señal: x(t) = [1 + m*cos(2πfmt)] * sin(2πfct)
    x = (1 + m*np.cos(2*np.pi*fm*t)) * np.sin(2*np.pi*fc*t)

    # Calcular la DFT
    X = np.fft.fft(x, N)
    X_mag = np.abs(X) / N   # magnitud normalizada

    # Frecuencias
    freqs = np.fft.fftfreq(N, 1/fs)
    mask = freqs >= 0
    freqs_pos = freqs[mask]
    X_mag_pos = X_mag[mask]

    # Resolución en frecuencia
    delta_f = fs / N
    print(f"\nResolución en frecuencia Δf = {delta_f:.4f} Hz")

    # Detectar picos (umbral sencillo)
    umbral = 0.05
    picos = [(freqs_pos[i], X_mag_pos[i]) for i in range(len(freqs_pos)) if X_mag_pos[i] > umbral]

    # Ordenar por amplitud y quedarnos con los 3 más grandes
    picos_principales = sorted(picos, key=lambda x: x[1], reverse=True)[:3]

    print("\nPicos principales (frecuencia y amplitud):")
    for f, A in picos_principales:
        print(f"f = {f:.2f} Hz , Amplitud = {A:.3f}")

    # Gráficas
    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    plt.plot(t, x)
    plt.title("Señal en el tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")

    plt.subplot(1,2,2)
    plt.stem(freqs_pos, X_mag_pos)  
    plt.title("Espectro (DFT)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")

    plt.tight_layout()
    plt.show()
