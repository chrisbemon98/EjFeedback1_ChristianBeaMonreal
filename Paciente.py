class Paciente:
    def __init__(self, identificador, nivel_urgencia, horas_espera):
        self.identificador = identificador
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera
    
    def __eq__(self, paciente):
        return (self.identificador == paciente.identificador)
    
    def __gt__(self, paciente):
        return (12 - self.horas_espera) > (12 - paciente.horas_espera)

    def __lt__(self, paciente):
        return self.nivel_urgencia < paciente.nivel_urgencia

    def __getitem__(self, item):
        if item == "identificador":
            return self.identificador
        elif item == "nivel_urgencia":
            return self.nivel_urgencia
        elif item == "horas_espera":
            return self.horas_espera
        else:
            return None

    def __str__(self):
        strReturn = "ID: {0}\n\tNivel de urgencia (0-10): {1}\n\tHoras de espera (0-12h): {2}"
        strReturn = strReturn.format(self.identificador, self.nivel_urgencia, self.horas_espera)
        return strReturn
