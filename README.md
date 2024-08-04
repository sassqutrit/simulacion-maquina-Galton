Este proyecto proporciona una guía clara sobre el proceso de creación del programa, y ofrece reflexiones personales sobre el aprendizaje y las habilidades desarrolladas durante el bootcamp.
# Simulación de la Máquina de Galton
## Descripción
Este proyecto simula una máquina de Galton, diseñada por Francis Galton en el siglo XIX para demostrar cómo una distribución binomial con una muestra suficientemente grande se aproxima a una distribución normal. La simulación incluye la generación de números aleatorios, la animación de la caída de las canicas, y la graficación del histograma de resultados.
## Requisitos
- Python 3.x
- Bibliotecas: `numpy`, `matplotlib`
Puedes instalar las bibliotecas necesarias utilizando pip:
pip install numpy matplotlib

# Detalles del Programa
## Funcionamiento de la Simulación
Nuestra simulación recrea digitalmente el comportamiento de una Máquina de Galton:

1. **Generación de canicas**: Simulamos 3000 canicas.
2. **Recorrido de las canicas**: Cada canica pasa por 12 niveles de obstáculos. En cada nivel, la canica tiene igual probabilidad de desviarse a la izquierda o a la derecha.
3. **Registro de posiciones**: La posición final de cada canica se registra.
4. **Visualización**: 
   - Se crea un histograma que muestra la distribución final de las canicas.
   - Se genera una animación que muestra el proceso de las canicas cayendo y acumulándose en los contenedores.

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema (preferiblemente Python 3.7+).
2. Instala las bibliotecas necesarias.
3. El programa utiliza la biblioteca `numpy` para generar números aleatorios que simulan la caída de las canicas. Cada canica tiene igual probabilidad de moverse a la derecha o a la izquierda en cada nivel de obstáculos.

### Simulación de la Caída de las Canicas

La función `simular_caida_canica(n_niveles)` simula la trayectoria de una canica a través de los obstáculos. La función `simular_caida(n_canicas, n_niveles)` llama repetidamente a `simular_caida_canica` para simular la caída de todas las canicas y almacena los resultados.

### Graficación del Histograma

La función `graficar_histograma(resultados)` utiliza `matplotlib` para graficar un histograma de la distribución de las canicas en los contenedores. Los ejes están etiquetados como "Distribución de canicas" y "Cantidad de canicas", y el gráfico tiene el título "Simulación de la Máquina de Galton".

### Animación de la Caída de las Canicas

La función `animar_caida(resultados, n_niveles)` crea una animación que visualiza la caída de las canicas y su acumulación en los contenedores. Utiliza `FuncAnimation` de `matplotlib` para actualizar el histograma en cada frame de la animación.

## Reflexiones sobre el Bootcamp

Este proyecto ha sido una experiencia enriquecedora, permitiéndome aplicar una variedad de conceptos aprendidos durante el bootcamp, incluyendo:

- **Probabilidad y Estadística**: La máquina de Galton es una excelente herramienta para entender la relación entre la distribución binomial y la distribución normal.
- **Programación en Python**: La implementación de la simulación y la animación reforzó mis habilidades en Python, especialmente en el uso de bibliotecas como `numpy` y `matplotlib`.
- **Visualización de Datos**: La creación de histogramas y animaciones me ayudó a mejorar mis habilidades en la visualización de datos, una competencia crucial en muchos campos de la ciencia y la ingeniería.
- **Pensamiento Crítico y Resolución de Problemas**: Diseñar y implementar el programa desde cero, asegurando que cumple con todos los requisitos, fue un ejercicio excelente de resolución de problemas y pensamiento crítico.

## Agradecimientos

Agradezco a mi coach y compañeros del bootcamp por su apoyo y colaboración a lo largo de este proyecto. La experiencia ha sido invaluable y ha fortalecido significativamente mis habilidades técnicas y analíticas.
