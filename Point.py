class Point:
    """
    Classe para representar um point em N dimensoes
    """

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __repr__(self):
        return 'Coordenadas: ' + str(self.coordinates) + \
               ' -> Dimensao: ' + str(self.dimension)