import matplotlib.pyplot as plt

def continuous_plotter(x, y, title="", xlabel="Tiempo [s]", ylabel="Amplitud", legend=None):
    """Grafica una señal continua (ej: tiempo vs amplitud)."""
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend:
        plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def discrete_plotter(x, y, title="", xlabel="Muestras [n]", ylabel="Amplitud", legend=None):
    """Grafica una señal discreta (ej: muestras vs amplitud)."""
    plt.figure(figsize=(8, 4))
    plt.stem(x, y, basefmt=" ", use_line_collection=True, label=legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend:
        plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def spectrum_plotter(freqs, mag, title="", xlabel="Frecuencia [Hz]", ylabel="Magnitud", legend=None):
    """Grafica espectros en frecuencia."""
    plt.figure(figsize=(8, 4))
    plt.plot(freqs, mag, label=legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend:
        plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
