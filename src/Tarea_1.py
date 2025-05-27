# src/tarea1.py

import numpy as np
from scipy.signal import square, sawtooth
from src.utils.grapher import graficar_senal

def escalon_unitario(t):
    return np.where(t >= 0, 1, 0)

def ejecutar_tarea():
    f = 2  # frecuencia en Hz
    T_s = 0.01  # periodo de muestreo
    t_cont = np.linspace(-1, 5, 1000)
    n = np.arange(0, int((5 + 1) / T_s))  # desde 0 hasta cubrir [–1, 5]
    t_disc = n * T_s - 1  # ajustar para cubrir el mismo intervalo

    # Señal 1: senoidal
    x1_cont = np.sin(2 * np.pi * f * t_cont)
    x1_disc = np.sin(2 * np.pi * f * t_disc)
    graficar_senal(t_cont, x1_cont, t_disc, x1_disc, "x₁(t) = sin(2π·f·t)")

    # Señal 2: exponencial * escalón
    x2_cont = np.exp(-2 * t_cont) * escalon_unitario(t_cont)
    x2_disc = np.exp(-2 * t_disc) * escalon_unitario(t_disc)
    graficar_senal(t_cont, x2_cont, t_disc, x2_disc, "x₂(t) = e^(–2t) · u(t)")

    # Señal 3: triangular periódica
    x3_cont = sawtooth(2 * np.pi * f * t_cont, width=0.5)
    x3_disc = sawtooth(2 * np.pi * f * t_disc, width=0.5)
    graficar_senal(t_cont, x3_cont, t_disc, x3_disc, "x₃(t) = tri(t, f)")

    # Señal 4: cuadrada periódica
    x4_cont = square(2 * np.pi * f * t_cont)
    x4_disc = square(2 * np.pi * f * t_disc)
    graficar_senal(t_cont, x4_cont, t_disc, x4_disc, "x₄(t) = sq(t, f)")
