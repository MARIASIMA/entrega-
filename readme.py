"""
# Simulador de Energía Eléctrica en una Red de Distribución

## Descripción
Este programa modela la distribución de energía eléctrica en una red de ciudades conectadas. Utiliza un grafo dirigido ponderado para representar las conexiones entre ciudades y calcula las rutas más eficientes desde una central eléctrica a cada ciudad, considerando pérdidas de energía en las rutas largas.

## Requisitos
- Python 3.8 o superior
- Bibliotecas necesarias:
  - `networkx`
  - `matplotlib`

## Instalación
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install networkx matplotlib
   ```

## Ejecución
1. Asegúrate de que todos los archivos del proyecto estén en el mismo directorio.
2. Ejecuta el archivo principal del programa:
   ```bash
   python simulador_red_distribucion.py
   ```
3. El programa mostrará:
   - Las distancias desde la central eléctrica a cada ciudad.
   - Las pérdidas de energía calculadas para cada ciudad.
   - Una visualización gráfica de la red de distribución.

## Documentación
- **Algoritmo de Dijkstra**: Se utiliza para calcular las rutas más eficientes desde el nodo origen.
- **Simulación de pérdidas**: Se calcula un 10% de pérdida de energía por unidad de distancia.
- **Visualización**: Se utiliza `matplotlib` para graficar la red y las rutas seleccionadas.

## Referencias
- [Algoritmo de Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
"""

