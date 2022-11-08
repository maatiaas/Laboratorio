class Persona():

    def __init__(self,rut,nombre):
        self.__rut = rut
        self.__nombre = nombre
    
    def __str__(self):
        return "Nombre: {} Rut: {}".format(self.__rut,self.__nombre)
    
    def GetRut(self):
        return self.__rut

    def GetNombre(self):
        return self.__nombre

    def SetRut(self,rut):
        self.__rut = rut

    def SetNombre(self,nombre):
        self.__nombre = nombre