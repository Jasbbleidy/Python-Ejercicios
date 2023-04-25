("reservacion")
print("reservacion en linea para un restaurante")
print("llamar para hacer lareservacion el dia martes")
reserva = input().upper()
if reserva == "NO":
    print("entrar a un sitio web para hacer la reserva")
else:
    print("pedir la mesa")
    mesa = input()
print("esta disponible la mesa con vista a Bogotà")
vista = input().upper()
if vista == "NO":
    print("pedir una mesa que este disponible")
    mesaDisponible = input()
else:
    print("escoger una hora para la reservaciòn")
    hora = input()
print("a las 11:00 p.m esta disponible la mesa")
horaDisponible = input().upper()
if horaDisponible == "SI":
    print("confirmar la hora")
    confirmarLaHora = input()
else:
    print("preguntar la hora disponible y confirmar")
    confirmarLaHora = input()
print("resalizar un cambio en la reservaciòn")
cambio = input().upper()
if cambio == "SI":
    print("hacer el cambio de los datos")
    cambioDeDatos = input()
else:
    print("verificar los datos")
    cambioDeDatos = input()
    print("realizar reservaciòn")