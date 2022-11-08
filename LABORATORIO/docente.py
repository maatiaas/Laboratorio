from persona import Persona

class Docente(Persona):
    def __init__(self,montopagar,grado,tipo,contrato,rut,nombre):
        super().__init__(rut,nombre)
        self.__montopagar = montopagar
        self.__grado = grado
        self.__tipo = tipo
        self.__contrato = contrato
    
    def __str__(self):
        return "Grado obtenido: {} Tipo de Docente: {} Fecha inicio de contrato: {}".format(self.__grado,self.__tipo,self.__contrato)

    def GetGrado(self):
        return self.__grado
    
    def GetMontoPagar(self):
        return self.__montopagar

    def GetTipo(self):
        return self.__tipo

    def GetContrato(self):
        return self.__contrato

    def SetGrado(self,grado):
        self.__grado = grado

    def SetTipo(self,tipo):
        self.__tipo = tipo

    def SetContrato(self,contrato):
        self.__contrato = contrato
    
    def SetMontoPagar(self,montopagar):
        self.__montopagar = montopagar
