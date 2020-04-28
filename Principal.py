from FechaHora import FechaHora

def opcion0(r1,r2):
    print("Adiós")

def opcion1(fechaHora1,fechaHora2):
    f3 = fechaHora1 + fechaHora2
    f3.Mostrar()

def opcion2(fechaHora1,fechaHora2):
    f3 = fechaHora1 - fechaHora2
    f3.Mostrar()

def opcion3(fechaHora1,fechaHora2):
    print(fechaHora1 > fechaHora2)

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument,r1,r2):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(r1,r2)

if __name__ == '__main__':

    d=int(input("Ingrese Dia r1: "))
    mes=int(input("Ingrese Mes r1: "))
    a=int(input("Ingrese Año r1: "))
    h=int(input("Ingrese Hora r1: "))
    m=int(input("Ingrese Minutos r1: "))
    s=int(input("Ingrese Segundos r1: "))
    r1= FechaHora(d,mes,a,h, m, s)
    d=int(input("Ingrese Dia r2: "))
    mes=int(input("Ingrese Mes r2: "))
    a=int(input("Ingrese Año r2: "))
    h=int(input("Ingrese Hora r2: "))
    m=int(input("Ingrese Minutos r2: "))
    s=int(input("Ingrese Segundos r2: "))
    r2= FechaHora(d,mes,a,h, m, s)

    band = False
    while not band:
        print("")
        print("0 Salir")
        print("1 r1 + r2")
        print("2 r1 - r2")
        print("3 r1 > r2")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion,r1,r2)
        band = int(opcion)==0
