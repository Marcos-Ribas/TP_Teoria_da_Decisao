import print_resultados

fronteiras = [
    [(3, 3), (1, 5), (2, 2), (4, 4), (5, 1), (6, 3), (7, 7), (2, 6), (2, 1)],
    [(1, 4), (2, 8), (3, 2), (4, 1), (5, 3), (6, 2)],
    [(1, 7), (2, 5), (3, 3), (4, 6), (5, 4)]
]

print_resultados.print_fronteiras_pareto(fronteiras)