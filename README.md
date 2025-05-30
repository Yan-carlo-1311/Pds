# 📊 Proyecto de Señales - Tareas 1 y 2

Este proyecto permite graficar y analizar diferentes tipos de señales **continuas** y **discretas**, incluyendo:

- Señales senoidales
- Señales exponenciales
- Señales triangulares
- Señales cuadradas

Está dividido en dos tareas principales, las cuales pueden ejecutarse desde el archivo `main.py`.

---

## 📁 Estructura del Proyecto

├── main.py
├── README.md
├── requirements.txt
└── src/
├── Tarea_1.py
├── Tarea_2.py
└── utils/
└── grapher.py

yaml
Copiar
Editar

---

## 🧠 Tarea 1: Graficar señales continuas y discretas

Ejecuta una señal específica, tanto en su versión continua como discreta.

```bash
python main.py Tarea_1 [tipo_de_senal]
Tipos de señal disponibles:
seno

exponencial

triangular

cuadrada

Ejemplo:
bash
Copiar
Editar
python main.py Tarea_1 seno
📈 Tarea 2: Señal senoidal continua con frecuencia personalizada
Genera una señal senoidal continua entre 0 y 5 segundos con la frecuencia que indiques.

Sintaxis:
bash
Copiar
Editar
python main.py Tarea_2 [frecuencia]
Ejemplo:
bash
Copiar
Editar
python main.py Tarea_2 2.5
⚙️ Requisitos
Python 3.7 o superior

Librerías necesarias:

numpy

matplotlib

scipy

Puedes instalarlas ejecutando:

bash
Copiar
Editar
pip install -r requirements.txt
Si estás usando un entorno virtual, asegúrate de activarlo antes de instalar los paquetes o ejecutar el script.

⚠️ Notas importantes
Ejecuta el script desde la raíz del proyecto para evitar errores de importación.

El programa utiliza matplotlib para mostrar gráficas, por lo que necesita acceso a una interfaz gráfica.

En sistemas con entorno gráfico limitado (como algunos servidores o WSL), puede ser necesario configurar el entorno adecuadamente para mostrar las ventanas de las gráficas.