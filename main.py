import random
from Paciente import Paciente
from SalaEmergencias import SalaEmergencias

IMPRIMIR_POR_CONSOLA = True
IMPRIMIR_EN_FICHERO = True

IMPRIMIR_VERSION_DETALLADA = True
IMPRIMIR_VERSION_SIMPLE = True

NUM_PACIENTES = 20
MININMO_URGENCIA, MAXIMO_URGENCIA = 0, 10
MINIMO_ESPERA, MAXIMO_ESPERA = 0, 12

# Descomentar para obtener los mismos resultados cada vez que se ejecute
# SEMILLA = 7
# random.seed(SEMILLA)


sala_emergencias = SalaEmergencias()

pacientes_agregados = []
for i in range(NUM_PACIENTES):
    identificador = i + 1
    nivel_urgencia = random.randint(MININMO_URGENCIA, MAXIMO_URGENCIA)
    horas_espera = random.randint(MINIMO_ESPERA, MAXIMO_ESPERA)
    
    paciente = Paciente(identificador, nivel_urgencia, horas_espera)
    sala_emergencias.agregar_paciente(paciente)

    pacientes_agregados.append(paciente)

pacientes_atendidos = []
while not sala_emergencias.sala_vacia():
    paciente_atendido = sala_emergencias.atender_paciente()
    pacientes_atendidos.append(paciente_atendido)



##########################
### MOSTRAR RESULTADOS ###
##########################
    
def str_titulo_pacientes_agregados():
    return "LISTA DE PACIENTES POR ORDEN DE ENTRADA EN LA SALA DE EMERGENCIAS\n"

def str_titulo_pacientes_atendidos():
    return "LISTA DE PACIENTES POR ORDEN EN EL QUE SON ATENDIDOS\n"

def str_pacientes(lista_pacientes):
        str_return = ""
        for p in lista_pacientes:
            str_return += str(p)+ "\n"
        return str_return

def str_atributos_pacientes(lista_pacientes, atributo, separador = " | "):
        return separador.join([str(p[atributo]).zfill(2) for p in lista_pacientes])

if IMPRIMIR_POR_CONSOLA:
    if IMPRIMIR_VERSION_DETALLADA:    
        print(str_titulo_pacientes_agregados())

        print(str_pacientes(pacientes_agregados))

        print("\n")

        print(str_titulo_pacientes_atendidos())

        print(str_pacientes(pacientes_atendidos))

    if IMPRIMIR_VERSION_SIMPLE:
        if IMPRIMIR_VERSION_DETALLADA:
            print("\n\n\n" + ("#" * 50) + "\n\n\n\n")

        print(str_titulo_pacientes_agregados())

        print("ID\t\t| " + str_atributos_pacientes(pacientes_agregados, "identificador"))
        print("Nivel urgencia\t| " + str_atributos_pacientes(pacientes_agregados, "nivel_urgencia"))
        print("Horas espera\t| " + str_atributos_pacientes(pacientes_agregados, "horas_espera"))

        print("\n\n")

        print(str_titulo_pacientes_atendidos())

        print("ID\t\t| " + str_atributos_pacientes(pacientes_atendidos, "identificador"))
        print("Nivel urgencia\t| " + str_atributos_pacientes(pacientes_atendidos, "nivel_urgencia"))
        print("Horas espera\t| " + str_atributos_pacientes(pacientes_atendidos, "horas_espera"))

if IMPRIMIR_EN_FICHERO:
    if IMPRIMIR_VERSION_DETALLADA:
        ruta_archivo_detallado = "pacientes_detallado.txt"

        with open(ruta_archivo_detallado, "w") as archivo_detallado:
            archivo_detallado.write(str_titulo_pacientes_agregados() + "\n")

            archivo_detallado.write(str_pacientes(pacientes_agregados) + "\n")

            archivo_detallado.write("\n" + "\n")

            archivo_detallado.write(str_titulo_pacientes_atendidos() + "\n")

            archivo_detallado.write(str_pacientes(pacientes_atendidos) + "\n")

    if IMPRIMIR_VERSION_SIMPLE:
        ruta_archivo_simple = "pacientes_simple.txt"

        with open(ruta_archivo_simple, "w") as archivo_simple:
            archivo_simple.write(str_titulo_pacientes_agregados() + "\n")

            archivo_simple.write("ID\t\t| " + str_atributos_pacientes(pacientes_agregados, "identificador") + "\n")
            archivo_simple.write("Nivel urgencia\t| " + str_atributos_pacientes(pacientes_agregados, "nivel_urgencia") + "\n")
            archivo_simple.write("Horas espera\t| " + str_atributos_pacientes(pacientes_agregados, "horas_espera") + "\n")

            archivo_simple.write("\n\n" + "\n")

            archivo_simple.write(str_titulo_pacientes_atendidos() + "\n")

            archivo_simple.write("ID\t\t| " + str_atributos_pacientes(pacientes_atendidos, "identificador") + "\n")
            archivo_simple.write("Nivel urgencia\t| " + str_atributos_pacientes(pacientes_atendidos, "nivel_urgencia") + "\n")
            archivo_simple.write("Horas espera\t| " + str_atributos_pacientes(pacientes_atendidos, "horas_espera") + "\n")