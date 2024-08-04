import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def simular_canica(niveles):
    """
    Simula el recorrido de una canica a través de la máquina de Galton.
    :param niveles: Número de niveles de obstáculos
    :return: Posición final de la canica
    """
    posicion = 0
    for _ in range(niveles):
        # Decidir si la canica va a la izquierda (-1) o a la derecha (+1)
        posicion += random.choice([-1, 1])
    return posicion

def crear_histograma(resultados):
    """
    Crea y muestra un histograma de los resultados.
    :param resultados: Lista de posiciones finales de las canicas
    """
    plt.figure(figsize=(12, 6))
    n, bins, patches = plt.hist(resultados, bins=range(min(resultados), max(resultados) + 2, 1), 
             align='left', rwidth=0.8)
    plt.title('Simulación de la Máquina de Galton')
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.xticks(range(min(resultados), max(resultados) + 1))
    max_y = int(np.ceil(max(n) / 200) * 200)
    plt.yticks(range(0, max_y + 200, 200))
    plt.grid(True, alpha=0.3)
    plt.show()

def animar_canicas(num_canicas, niveles):
    fig, ax = plt.subplots(figsize=(12, 8))
    contenedores = [0] * (2 * niveles + 1)

    def actualizar(frame):
        ax.clear()
        if frame < num_canicas:
            posicion = simular_canica(niveles)
            contenedores[posicion + niveles] += 1

        # Dibujar los obstáculos
        for nivel in range(niveles):
            y = (niveles - nivel) / niveles
            x_positions = [i/(nivel+1) - 0.5 for i in range(nivel+2)]
            ax.scatter(x_positions, [y]*len(x_positions), color='red', s=50)

        # Dibujar los contenedores
        ax.bar(range(-niveles, niveles+1), contenedores, align='center')
        ax.set_title('Simulación de la Máquina de Galton')
        ax.set_xlabel('Distribución de canicas')
        ax.set_ylabel('Cantidad de canicas')
        ax.set_ylim(0, max(contenedores) + 100)

    ani = animation.FuncAnimation(fig, actualizar, frames=num_canicas+50, interval=10, repeat=False)
    plt.show()

if __name__ == "__main__":
    num_canicas = 3000
    niveles = 12
    # Simular las canicas
    resultados = [simular_canica(niveles) for _ in range(num_canicas)]
    # Crear y mostrar el histograma
    crear_histograma(resultados)
    # Animar la caída de las canicas
    animar_canicas(num_canicas, niveles)
