from math import ceil

class FechaHora:
    __Dia = 0
    __Mes = 0
    __Anio = 0
    __Hora = 0
    __Minuto = 0
    __Segundo = 0

    def __init__(self, dia = 1, mes = 1, anio = 2020, hora = 0, minuto = 0, segundo = 0):
        if (anio > 0):
            if (mes in range(1,13)):
                if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
                    if (dia in range(1,31)):
                        if (hora in range(24)):
                            if (minuto in range(60)):
                                if (segundo in range(60)):
                                    self.__Anio = anio
                                    self.__Mes = mes                    #genera el objeto si es un mes de 30 dias
                                    self.__Dia = dia                    #y los datos ingresados son correctos
                                    self.__Hora = hora
                                    self.__Minuto = minuto
                                    self.__Segundo = segundo
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 59.')
                        else:
                            print('El rango de valores válidos es de 0 a 23.')
                    else:
                        print('El mes ' + str(mes) + ' solo tiene 30 días.')
                elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
                    if (dia in range(1,32)):
                        if (hora in range(24)):
                            if (minuto in range(60)):
                                if (segundo in range(60)):
                                    self.__Anio = anio
                                    self.__Mes = mes                    #genera el objeto si es un mes de 31 dias
                                    self.__Dia = dia                    #y los datos ingresados son correctos
                                    self.__Hora = hora
                                    self.__Minuto = minuto
                                    self.__Segundo = segundo
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 59.')
                        else:
                            print('El rango de valores válidos es de 0 a 23.')
                    else:
                        print('El mes ' + str(mes) + ' solo tiene 31 días.')
                else:
                    if ((anio%4 == 0) & (anio%100 != 0)) or (anio%400 == 0):
                        if (dia in range(1,30)):
                            if (hora in range(24)):
                                if (minuto in range(60)):
                                    if (segundo in range(60)):
                                        self.__Anio = anio              #genera el objeto si es que es un año bisiesto,
                                        self.__Mes = mes                #es el mes de febrero y los datos ingresados son correctos
                                        self.__Dia = dia
                                        self.__Hora = hora
                                        self.__Minuto = minuto
                                        self.__Segundo = segundo
                                    else:
                                        print('El rango de valores válidos es de 0 a 59.')
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 23.')
                        else:
                            print('El mes ' + str(mes) + ' solo tiene 29 días por ser año bisiesto.')
                    else:
                        if (dia in range(1,29)):
                            if (hora in range(24)):
                                if (minuto in range(60)):
                                    if (segundo in range(60)):
                                        self.__Anio = anio
                                        self.__Mes = mes                #genera el objeto si es que no es un año bisiesto,
                                        self.__Dia = dia                #es el mes de febrero y los datos ingresados son correctos
                                        self.__Hora = hora
                                        self.__Minuto = minuto
                                        self.__Segundo = segundo
                                    else:
                                        print('El rango de valores válidos es de 0 a 59.')
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 23.')
                        else:
                            print('El mes ' + str(mes) + ' solo tiene 28 días.')
            else:
                print('Los años solo tienen 12 meses.')
        else:
            print('Año inválido.')

    def Mostrar(self):
        print('Año:{} Mes:{} Día:{} Hora:{} Minuto:{} Segundo:{}'.format(self.__Anio,self.__Mes,self.__Dia,self.__Hora,self.__Minuto,self.__Segundo))

    def PonerEnHora(self, nuevaHora = 0, nuevoMinuto = 0, nuevoSegundo = 0):
        if (nuevaHora in range(24)):
            if (nuevoMinuto in range(60)):
                if (nuevoSegundo in range(60)):
                    self.__Hora = nuevaHora
                    self.__Minuto = nuevoMinuto
                    self.__Segundo = nuevoSegundo
                else:
                    print('El rango de valores válidos es de 0 a 59.')
            else:
                print('El rango de valores válidos es de 0 a 59.')
        else:
            print('El rango de valores válidos es de 0 a 23.')

    def AdelantarHora(self, h = 0, m = 0):
        if (h >= 0):
            if (m >= 0):
                    self.__Hora += h
                    self.__Minuto += m
            else:
                print('El valor para minuto es inválido.')
        else:
            print('El valor para hora es inválido.')
        #Actualiza Hora
        if (self.__Minuto >= 60):
            self.__Hora += self.__Minuto // 60
            self.__Minuto = self.__Minuto - ((self.__Minuto//60)* 60)
        #Actualiza Dia
        if(self.__Hora >= 24):
            self.__Dia += self.__Hora // 24
            self.__Hora = self.__Hora - ((self.__Hora//24)*24)
        #Actualiza Mes
        if (self.__Mes == 4) or (self.__Mes == 6) or (self.__Mes == 9) or (self.__Mes == 11):
            if (self.__Dia > 30):
                self.__Mes += self.__Dia // 30
                self.__Dia = self.__Dia - ((self.__Dia // 30)* 30)
        elif (self.__Mes == 1) or (self.__Mes == 3) or (self.__Mes == 5) or (self.__Mes == 7) or (self.__Mes == 8) or (self.__Mes == 10) or (self.__Mes == 12):
            if (self.__Dia > 31):
                self.__Mes += self.__Dia // 31
                self.__Dia = self.__Dia - ((self.__Dia // 31)* 31)
        else:
            if ((self.__Anio%4 == 0) & (self.__Anio%100 != 0)) or (self.__Anio%400 == 0): #Mes Bisiesto
                if (self.__Dia > 29):
                    self.__Mes += self.__Dia // 29
                    self.__Dia = self.__Dia - ((self.__Dia // 29)* 29)
            elif (self.__Dia > 28):
                self.__Mes += self.__Dia // 28
                self.__Dia = self.__Dia - ((self.__Dia // 28)* 28)
        #Actualiza Año
        if (self.__Mes > 12):
            self.__Anio += self.__Mes // 12
            self.__Mes = self.__Mes - ((self.__Mes // 12)* 12)

    def getDia (self):
        return self.__Dia

    def getMes (self):
        return self.__Mes

    def getAnio (self):
        return self.__Anio

    def getHora (self):
        return self.__Hora

    def getMinuto (self):
        return self.__Minuto

    def getSegundo (self):
        return self.__Segundo

    def __add__ (self, otroFH):
        d = self.getDia() + otroFH.getDia()
        mes = self.getMes() + otroFH.getMes()
        a = self.getAnio()            #Dejo el año del primer elemento
        h = self.getHora() + otroFH.getHora()
        m = self.getMinuto() + otroFH.getMinuto()
        s = self.getSegundo() + otroFH.getSegundo()
        #Verificar Minutos
        if (s >= 60):
            m += s // 60
            s = s - ((s//60)* 60)
        #Verificar Hora
        if (m >= 60):
            h += m // 60
            m = m - ((m//60)* 60)
        #Verificar Dia
        if(h >= 24):
            d += h // 24
            h = h - ((h//24)*24)
        #Verificar Mes
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if (d > 30):
                mes += d // 30
                d = d - ((d // 30)* 30)
        elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if (d > 31):
                mes += d // 31
                d = d - ((d // 31)* 31)
        else:
            if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0): #Mes Bisiesto
                if (d > 29):
                    mes += d // 29
                    d = d - ((d // 29)* 29)
            elif (d > 28):
                mes += d // 28
                d = d - ((d // 28)* 28)
        #Verificar Año
        if (mes > 12):
            a += mes // 12
            mes = mes - ((mes // 12)* 12)

        return FechaHora(d,mes,a,h, m, s)

    def __sub__(self, otroFH):
        d = self.getDia() - otroFH.getDia()
        mes = self.getMes() - otroFH.getMes()
        a = self.getAnio()            #Dejo el año del primer elemento
        h = self.getHora() - otroFH.getHora()
        m = self.getMinuto() - otroFH.getMinuto()
        s = self.getSegundo() - otroFH.getSegundo()
        #Verificar Minutos
        if (s < 0):
            m -= ceil((-s)/60)
            s = s + (ceil((-s)/60) * 60)
        #Verificar Hora
        if (m < 0):
            h -= ceil((-m)/60)
            m = m + (ceil((-m)/60) * 60)
        #Verificar Dia
        if (h < 0):
            d -= ceil((-h)/24)
            h = h + (ceil((-h)/24) * 24)
        #Verificar Mes
        if (mes == 0):
            mes = 1
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if (d < 0):
                mes -= ceil((-d)/30)
                d = d + (ceil((-d)/30) * 30)
        elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if (d < 0):
                mes -= ceil((-d)/31)
                d = d + (ceil((-d)/31) * 31)
        else:
            if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0): #Mes de febrero en año Bisiesto
                if (d < 0):
                    mes -= ceil((-d)/29)
                    d = d + (ceil((-d)/29) * 29)
            else:
                if (d < 0):
                    mes -= ceil((-d)/28)
                    d = d + (ceil((-d)/28) * 28)
        if (d == 0):
            d = 1
        #Verificar Año
        if (mes < 0):
            a -= ceil((-mes)/12)
            mes = mes + (ceil((-mes)/12) * 12)

        return FechaHora(d,mes,a,h, m, s)

    def __gt__ (self, otroFH):
        if (self.getHora() > otroFH.getHora()):
            return True
        elif (self.getHora() == otroFH.getHora()) & (self.getMinuto() > otroFH.getMinuto()):
            return True
        elif (self.getHora() == otroFH.getHora()) & (self.getMinuto() == otroFH.getMinuto()) & (self.getSegundo() > otroFH.getSegundo()):
            return True
        else:
            return False
