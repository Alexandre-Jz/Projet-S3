import itertools

def independant(graph, subset):
    for u in subset:
        for v in subset:
            if v != u and v in graph[u]:  # Si une arrete (u,v) existe
                return False
    return True


def brute_force_mis(graph):
    n = len(graph)
    MIS = set()

    # Parcourt tous les sous-ensembles de sommets possibles
    for taille in range(1, n+1):
        for subset in itertools.combinations(list(graph.keys()), taille):
            if independant(graph, subset):
                if len(subset) > len(MIS):
                    MIS = set(subset)

    return MIS

La commande itertools.combinations(iterable,n) permet de générer tous les sous-ensembles de taille n de l'itérable pris en entrée, sans répétitions.

Pour l'ensemble ['A','B','C'], la commande itertools.combinations([1, 2, 3], 2) renvoie [('A', 'B'), ('A', 'C'), ('B', 'C')].
