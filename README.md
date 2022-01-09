# Practica1_FSI

La primera práctica ha consistido en crear la estrategia de búsqueda de ramificación y acotación (búsqueda no informada) y la estrategia de búsqueda de ramificación y acotación con subestimación (búsqueda informada). Para la primera estrategia a la hora de extender un nodo, ordenábamos la lista abierta según el coste acumulado de cada trayectoria parcial. Asimismo, la estrategia con subestimación además de utilizar el coste se utiliza la estimación de la heurística, que se basa en la distancia en línea recta entre el estado inicial y el final.

Para mostrar la diferencia entre ambas estrategias, se ha contabilizado los nodos expandidos en cada estrategia y para diferentes recorridos, obteniendo que siempre la estrategia con subestimación obtiene un menor número de nodos expandidos que la estrategia de la búsqueda no informada.

