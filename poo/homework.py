#crear una clase banco
# sus atributos seran nombre,apellido,dni,numero de cuenta y saldo inicial.
# como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.
#crear una clase  banco sus atributos seran nombre apellidos deni numero de cuenrta
#y saldo inicial
#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta
class banco:
    #atributos
    def __init__(self,nombre,apellidos,dni,numero_de_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_de_cuenta=numero_de_cuenta
        self.saldo_inicial=saldo_inicial
    #metodos
    def deposito(self):
        print("estoy depositando 500")
    def retirar(self):
        print("estoy retirando 500")
    def get_status(self):
        print("estoy viendo el estado  actual de mi cuenta")
carlos=banco("carlos","condori vasques",7894561,1220763,5485466)
print(carlos.retirar())

#ejercicio 2
#crear una clase agencia 
# con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje.
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje.

class agencia:
    #atributos
    def _init_(self,nombre,apellidos,dni,numero_asiento,fecha_viaje):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_asiento=numero_asiento
        self.fecha_viaje=fecha_viaje
    #metodos
    def ingresar_origen(self,lugar):
        print("estoy ingresando de donde viajo:",lugar)
    def ingresar_destino(self):
        print("estoy ingresando de donde voy")
    def cancelar_viaje(self):
        print("estoy cancelando mi viaje ")
    def ver_estado_pasaje(self):
        print("estoy viendo el estado de mi pasaje")
eulalia=agencia("eulalia","tito olivares",7446489,122,"2024/12/22")
print(eulalia.ingresar_destino())
eulalia.ingresar_origen("puquio")


