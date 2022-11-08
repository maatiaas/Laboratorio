from docente import Docente

class Adjunto(Docente):
    
    def __init__(self,horas,montopagar,grado, tipo,contrato, rut, nombre):
        super().__init__(montopagar,grado,tipo,contrato,rut,nombre)
        self.__horas = horas 

    def __str__(self):
        return "Nombre: {} Rut: {} Grado: {} Tipo de docente: {} Contrato: {} Horas: {} Monto a Pagar: {}".format(self.GetNombre(),self.GetRut(),self.GetGrado(),self.GetTipo(),self.GetContrato(),self.GetHoras(),self.GetMontoPagar())

    def GetHoras(self):
        return self.__horas

    def SetHoras(self,horas):
        self.__horas = horas