from Heap import MaxHeap, MinHeap
# from Heap2 import MaxHeap, MinHeap
from Nodo import Nodo

class SalaEmergencias:
    def __init__(self):
        self.heap_nivel_urgencia = MaxHeap()
        self.heap_horas_espera = MinHeap()

    def sala_vacia(self):
        return self.heap_horas_espera.is_empty()

    def agregar_paciente(self, paciente):
        nodo = Nodo(paciente)
        self.heap_nivel_urgencia.push(nodo)
        self.heap_horas_espera.push(nodo)

    def atender_paciente(self):
        nivel_urgencia_maxima = self.heap_nivel_urgencia.peek().valor.nivel_urgencia
        horas_espera_maxima = self.heap_horas_espera.peek().valor.horas_espera

        pop_nivel_urgencia = nivel_urgencia_maxima == 10 or horas_espera_maxima <= 5

        if pop_nivel_urgencia:
            paciente_atendido = self.heap_nivel_urgencia.pop().valor
            self.heap_horas_espera.delete_node(paciente_atendido)
        else:
            paciente_atendido = self.heap_horas_espera.pop().valor
            self.heap_nivel_urgencia.delete_node(paciente_atendido)

        return paciente_atendido
    
    def agregar_pacientes(self, lista_pacientes):
        for paciente in lista_pacientes:
            self.agregar_paciente(paciente)

    def atender_pacientes(self):
        pacientes_atendidos = []

        while not self.sala_vacia():
            pacientes_atendidos.append(self.atender_paciente())

        return pacientes_atendidos
