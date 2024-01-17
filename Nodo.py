class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left_child = None
        self.right_child = None
    
    def __str__(self):
        return self.valor.__str__()
