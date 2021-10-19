# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("\n\n################################ De A a B ################################")

print("\n----- Búsqueda ramificación y acotación -----")
print(search.ramificacion_acotacion(ab).path())       #30 nodos expandidos

print("\n----- Búsqueda ramificación y acotación con subestimación -----")
print(search.ramificacion_acotacion_con_heuristica(ab).path())       #15 nodos expandidos



oe = search.GPSProblem('O', 'E'
                       , search.romania)
print("\n\n################################ De O a E ################################")

print("\n----- Búsqueda ramificación y acotación -----")
print(search.ramificacion_acotacion(oe).path())       #30 nodos expandidos

print("\n----- Búsqueda ramificación y acotación con subestimación -----")
print(search.ramificacion_acotacion_con_heuristica(oe).path())       #15 nodos expandidos




df = search.GPSProblem('D', 'F'
                       , search.romania)
print("\n\n################################ De D a F ################################")

print("\n----- Búsqueda ramificación y acotación -----")
print(search.ramificacion_acotacion(df).path())       #30 nodos expandidos

print("\n----- Búsqueda ramificación y acotación con subestimación -----")
print(search.ramificacion_acotacion_con_heuristica(df).path())       #15 nodos expandidos





ut = search.GPSProblem('U', 'T'
                       , search.romania)
print("\n\n################################ De U a T ################################")

print("\n----- Búsqueda ramificación y acotación -----")
print(search.ramificacion_acotacion(ut).path())       #30 nodos expandidos

print("\n----- Búsqueda ramificación y acotación con subestimación -----")
print(search.ramificacion_acotacion_con_heuristica(ut).path())       #15 nodos expandidos





cz = search.GPSProblem('C', 'Z'
                       , search.romania)
print("\n\n################################ De C a Z ################################")

print("\n----- Búsqueda ramificación y acotación -----")
print(search.ramificacion_acotacion(cz).path())       #30 nodos expandidos

print("\n----- Búsqueda ramificación y acotación con subestimación -----")
print(search.ramificacion_acotacion_con_heuristica(cz).path())       #15 nodos expandidos


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
