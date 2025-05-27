# src/utils/grapher.py

import matplotlib.pyplot as plt

def graficar_senal(t_cont, x_cont, t_disc, x_disc, titulo):
    plt.figure()
    plt.plot(t_cont, x_cont, label="Señal continua", linewidth=2)
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt='k-', 
             label="Señal muestreada", use_line_collection=True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
