from adjunto import Adjunto 
from regular import Regular
from io import open

adjuntos = []
regulares = []

def main():
        bandera = 1
        while bandera == 1:
                IngresoDatos()
                bandera = int(input("\n¿Desea volver agregar un docente?\n1.Sí\n2.No\n>>> "))
                bandera = bandera
        MontoPago()
        MostrarDatos()
        registro_docentes()

def IngresoDatos():
        nombre = input("\nIngrese su nombre\n>>> ")
        rut = input("\nIngrese su rut sin puntos, guión y dígito verificador\n>>> ")
        digitoverificador = (input("\nIngrese su código verificador\n>>> ").capitalize())
        digito_verificador(rut)
        while digitoverificador != digito_verificador(rut):
                print("\nEl digito verificador ingresado no es válido\n")
                digitoverificador = (input("Ingrese nuevamente su dígito verificador\n>>> ").capitalize())
        if digitoverificador == digito_verificador(rut):
                print("\nRUT Válido")
        cont = input("\nIngrese la fecha de inicio de su contrato (DD/MM/AA)\n>>> ")
        grado = (input("\nIngrese su Grado Obtenido (L = Licenciado, M = Magister, D = Doctorado)\n>>> ").capitalize())
        while grado != "L" and grado != "M" and grado != "D":
                grado = (input("Ingrese un Grado Obtenido válido (L = Licenciado, M = Magister, D = Doctorado)\n>>> ").capitalize())
        tipo_docente = (input("\nIngrese tipo de docente al que corresponde (R = Regular, A = Adjunto)\n>>> ").capitalize())
        while tipo_docente != "R" and tipo_docente != "A":
                tipo_docente = (input("Ingrese un tipo de docente válido\n>>> ").capitalize())
        if tipo_docente == "R":
                tipo_jornada = (input("\nIngrese su tipo de jornada (C = Completa, M = Media)\n>>> ").capitalize())
                while tipo_jornada != "C" and tipo_jornada != "M":
                        tipo_jornada = (input("\nIngrese un tipo de jornada válida (C = Completa, M = Media)\n>>> ").capitalize())
                sueldo_base = int(input("\nIngrese su sueldo base\n>>> "))
                docente_Regular = Regular(tipo_jornada,sueldo_base," ",grado,tipo_docente,cont,rut+"-"+digitoverificador,nombre)
                regulares.append(docente_Regular)
        else:
                horas_trabajadas = int(input("\nIngrese la cantidad de horas trabajadas\n>>> "))
                docente_Adjunto = Adjunto(horas_trabajadas," ",grado,tipo_docente,cont,rut+"-"+digitoverificador,nombre)
                adjuntos.append(docente_Adjunto)

def MostrarDatos():
        contador_regulares = 1
        contador_adjuntos = 1
        print("\nLista de Docentes Regulares:\n")
        for docentes in regulares:
                print("Docente Regular "+str(contador_regulares)+":",docentes)
                contador_regulares += 1
        print("\nLista de Docentes Adjuntos:\n")
        for docentes in adjuntos:
                print("Docente Adjunto "+str(contador_adjuntos)+":",docentes)
                contador_adjuntos += 1

def digito_verificador(rut)-> str:
        value = 11 - sum([int(a)*int(b) for a,b in zip(str(rut).zfill(8),"32765432")])%11
        return {10 : "K", 11 : "0"}.get(value,str(value))

def MontoPago():
        contador_regulares = 1
        print("\nDOCENTES REGULARES")
        for docente in regulares:
                print("\nDocente Regular "+str(contador_regulares))
                j = docente.GetJornada() 
                g = docente.GetGrado()
                if j == "C":
                        if g == "L":
                                totalpagar = 200000 + docente.GetSueldo()
                                print("Monto a Pagar: $"+str(totalpagar))
                                docente.SetMontoPagar(totalpagar)
                        elif g == "M":
                                totalpagar = 500000 + docente.GetSueldo()
                                print("Monto a Pagar: $"+str(totalpagar))
                                docente.SetMontoPagar(totalpagar)
                        else:
                                totalpagar = 800000 + docente.GetSueldo()
                                print("Monto a Pagar: $"+str(totalpagar))
                                docente.SetMontoPagar(totalpagar)
                else:
                        if g == "L":
                                totalpagar = 100000 + docente.GetSueldo()
                                print("Monto a Pagar: $"+str(totalpagar))
                                docente.SetMontoPagar(totalpagar)
                        elif g == "M":
                                totalpagar = 300000 + docente.GetSueldo()
                                print("Monto a Pagar: $"+str(totalpagar))
                                docente.SetMontoPagar(totalpagar)
                        else:
                                totalpagar = 700000 + docente.GetSueldo()
                                print("Monto a Pagar: $"+str(totalpagar))
                                docente.SetMontoPagar(totalpagar)
                contador_regulares += 1
        contador_adjuntos = 1
        print("\nDOCENTES ADJUNTOS")
        for docente in adjuntos:
                print("\nDocente Adjunto "+str(contador_adjuntos))
                g = docente.GetGrado()
                if g == "L":
                        totalpagar = docente.GetHoras() * 16000
                        print("Monto a Pagar: $"+str(totalpagar))
                        docente.SetMontoPagar(totalpagar)
                elif g == "M":
                        totalpagar = docente.GetHoras() * 19000
                        print("Monto a Pagar: $"+str(totalpagar))
                        docente.SetMontoPagar(totalpagar)
                else:
                        totalpagar = docente.GetHoras() * 25000
                        print("Monto a Pagar: $"+str(totalpagar))
                        docente.SetMontoPagar(totalpagar)
                contador_adjuntos += 1

def registro_docentes():
        registro = open('docentes.txt','w')
        for docentes in regulares:
                registro.writelines("\n"+str(docentes))
        for docentes in adjuntos:
                registro.writelines("\n"+str(docentes))
        registro.close()

main()