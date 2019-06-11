import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from Point import Point
from Cluster import Cluster

DATASET1 = "./dataSet/DS_3Clusters_999Points.txt"
NUM_CLUSTERS = 3
ITERATIONS = 1000
COLORS = ['red', 'blue', 'green', 'yellow', 'gray', 'pink', 'violet', 'brown',
          'cyan', 'magenta']


def dataset_to_list_points(dir_dataset):
    """
    Le um arquivo txt com um conjunto de pontos e retorne uma lista de objetos Point
    """
    points = list()
    with open(dir_dataset, 'rt') as reader:
        for point in reader:
            points.append(Point(np.asarray(map(float, point.split("::")))))
    return points


def get_nearest_cluster(clusters, point):
    """
    Calcular o cluster mais proximo
    """
    dist = np.zeros(len(clusters))
    for i, c in enumerate(clusters):
        dist[i] = distance.euclidean(point.coordinates, c.centroid)
    return np.argmin(dist)


def print_clusters_status(it_counter, clusters):
    print '\Interacao %d' % it_counter
    for i, c in enumerate(clusters):
        print '\tCentroide Cluster %d: %s' % (i + 1, str(c.centroid))


def print_results(clusters):
    print '\n\n Resultado Final:'
    for i, c in enumerate(clusters):
        print '\tCluster %d' % (i + 1)
        print '\t\Pontos em Cluster %d' % len(c.points)
        print '\t\tCentroide: %s' % str(c.centroid)


def plot_results(clusters):
    plt.plot()
    for i, c in enumerate(clusters):
        # Plotando pontos
        x, y = zip(*[p.coordinates for p in c.points])
        plt.plot(x, y, linestyle='None', color=COLORS[i], marker='.')
        # Plotando centroides
        plt.plot(c.centroid[0], c.centroid[1], 'o', color=COLORS[i],
                 markeredgecolor='k', markersize=10)
    plt.show()


def k_means(dataset, num_clusters, iterations):
    # Ler Data Set
    points = dataset_to_list_points(dataset)

    # Selecionar N pontos aleatorios pra iniciar os N Clusters
    initial = random.sample(points, num_clusters)

    # Criar N Clusters iniciais
    clusters = [Cluster([p]) for p in initial]

    # Iniciar lista de listas para salvar os novos pontos do cluster
    new_points_cluster = [[] for i in range(num_clusters)]

    converge = False
    it_counter = 0
    while (not converge) and (it_counter < iterations):
        # Atribuir pontos no centroide mais proximo
        for p in points:
            i_cluster = get_nearest_cluster(clusters, p)
            new_points_cluster[i_cluster].append(p)

        # Definir novos pontos em clusters e calcular novos centroides
        for i, c in enumerate(clusters):
            c.update_cluster(new_points_cluster[i])

        # Verifique se convergem todos os Clusters
        converge = [c.converge for c in clusters].count(False) == 0

        # Contador de incrementos e listas de exclusao de pontos de agrupamentos
        it_counter += 1
        new_points_cluster = [[] for i in range(num_clusters)]

        # Printar status de clusters
        print_clusters_status(it_counter, clusters)

    # Printar resultado final
    print_results(clusters)

    # Plotar resultado final
    plot_results(clusters)


if __name__ == '__main__':
    k_means(DATASET1, NUM_CLUSTERS, ITERATIONS)
