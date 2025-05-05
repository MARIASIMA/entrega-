try:
    import networkx as nx
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print(f"Error: {e}. Instalando bibliotecas necesarias...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx", "matplotlib"])
    import networkx as nx
    import matplotlib.pyplot as plt

# 1. Entrada de datos
def leer_datos():
    """
    Leer la red de ciudades y conexiones desde un archivo o entrada manual.
    Retorna un grafo dirigido ponderado.
    """
    # Ejemplo de datos: lista de aristas con pesos
    datos = [
        ("Central", "CiudadA", 5),
        ("Central", "CiudadB", 10),
        ("CiudadA", "CiudadC", 3),
        ("CiudadB", "CiudadC", 1),
        ("CiudadC", "CiudadD", 8)
    ]
    grafo = nx.DiGraph()
    for origen, destino, peso in datos:
        grafo.add_edge(origen, destino, weight=peso)
    return grafo

# 2. Construcción del grafo
def construir_grafo():
    """
    Construye el grafo a partir de los datos de entrada.
    """
    return leer_datos()

# 3. Algoritmo de Dijkstra
def calcular_rutas_mas_eficientes(grafo, origen):
    """
    Calcula las rutas más eficientes desde el nodo origen a todos los demás nodos.
    Retorna un diccionario con las distancias mínimas y las rutas.
    """
    distancias, rutas = nx.single_source_dijkstra(grafo, source=origen, weight='weight')
    return distancias, rutas

# 4. Cálculo de pérdidas
def calcular_perdidas(distancias):
    """
    Simula la pérdida de energía en función de la distancia.
    Retorna un diccionario con las pérdidas calculadas.
    """
    perdidas = {nodo: distancia * 0.1 for nodo, distancia in distancias.items()}  # Ejemplo: 10% de pérdida por unidad de distancia
    return perdidas

# 5. Visualización
def visualizar_red(grafo, rutas):
    """
    Muestra gráficamente la red de distribución y las rutas seleccionadas.
    """
    pos = nx.spring_layout(grafo)
    plt.figure(figsize=(10, 8))
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=nx.get_edge_attributes(grafo, 'weight'))
    plt.title("Red de Distribución de Energía")
    plt.show()

# Programa principal
if __name__ == "__main__":
    grafo = construir_grafo()
    origen = "Central"
    distancias, rutas = calcular_rutas_mas_eficientes(grafo, origen)
    perdidas = calcular_perdidas(distancias)
    
    print("Distancias desde la central:", distancias)
    print("Pérdidas de energía:", perdidas)
    visualizar_red(grafo, rutas)
