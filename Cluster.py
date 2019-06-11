import numpy as np


class Cluster:
    """
    Class para representar um Cluster: seta os pontos e seus centroides
    """

    def __init__(self, points):
        if len(points) == 0:
            raise Exception("Cluster nao pode ter 0 Pontos")
        else:
            self.points = points
            self.dimension = points[0].dimension

        # Checa que todos os elementos do cluster tem a mesma dimensao
        for p in points:
            if p.dimension != self.dimension:
                raise Exception(
                    "Ponto %s tem dimensao %d diferente com %d de resto "
                    "de pontos") % (p, len(p), self.dimension)

        # Calcula Centroide
        self.centroid = self.calculate_centroid()
        self.converge = False

    def calculate_centroid(self):
        sum_coordinates = np.zeros(self.dimension)
        for p in self.points:
            for i, x in enumerate(p.coordinates):
                sum_coordinates[i] += x

        return (sum_coordinates / len(self.points)).tolist()

    def update_cluster(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculate_centroid()
        self.converge = np.array_equal(old_centroid, self.centroid)

    def __repr__(self):
        cluster = 'Centroide: ' + str(self.centroid) + '\nDimensao: ' + str(
            self.dimension)
        for p in self.points:
            cluster += '\n' + str(p)

        return cluster + '\n\n'