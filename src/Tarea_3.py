import numpy as np
from src.utils.grapher import double_plotter, double_discrete_plotter

def compare_sine_signals(A, f, phi):
    # Tiempo continuo
    t = np.linspace(-1, 5, 1000)

    # Tiempo discreto
    Ts = 0.01
    n = np.arange(int(-1/Ts), int(5/Ts))
    t_disc = n * Ts

    # Señal continua
    ref_cont = np.sin(2 * np.pi * 1 * t)
    mod_cont = A * np.sin(2 * np.pi * f * t + phi)

    # Señal discreta
    ref_disc = np.sin(2 * np.pi * 1 * t_disc)
    mod_disc = A * np.sin(2 * np.pi * f * t_disc + phi)

    # Gráfica continua (líneas)
    double_plotter(
        t, ref_cont, mod_cont,
        title="Comparación de Señales Senoidales (Continuo)",
        ref_label="Referencia (A=1, f=1Hz, ϕ=0)",
        new_label=f"Modificada (A={A}, f={f}Hz, ϕ={phi} rad)",
        x_label="Tiempo (s)",
        y_label="Amplitud"
    )

    # Gráfica discreta (puntitos)
    double_discrete_plotter(
        t_disc, ref_disc, mod_disc,
        title="Comparación de Señales Senoidales (Discreta)",
        ref_label="Referencia (A=1, f=1Hz, ϕ=0)",
        mod_label=f"Modificada (A={A}, f={f}Hz, ϕ={phi} rad)",
        x_label="Tiempo (s)",
        y_label="Amplitud"
    )
