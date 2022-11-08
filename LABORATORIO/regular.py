from docente import Docente

class Regular(Docente):

    def __init__(self,jornada,sueldo,montopagar,grado, tipo, contrato, rut, nombre):
        super().__init__(montopagar,grado, tipo, contrato, rut, nombre)
        self.__jornada = jornada
        self.__sueldo = sueldo

    def __str__(self):
        return "Nombre: {} Rut: {} Grado: {} Tipo de docente: {} Contrato: {} Tipo de Jornada: {} Sueldo Base: {} Monto a Pagar: {}".format(self.GetNombre(),self.GetRut(),self.GetGrado(),self.GetTipo(),self.GetContrato(),self.__jornada,self.__sueldo,self.GetMontoPagar())

    def GetJornada(self):
        return self.__jornada

    def GetSueldo(self):
        return self.__sueldo

    def SetJornada(self,jornada):
        self.__jornada = jornada

    def SetSueldo(self,sueldo):
        self.__sueldo = sueldo