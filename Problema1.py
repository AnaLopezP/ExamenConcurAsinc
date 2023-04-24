from queue import Queue 
from multiprocessing import Pool

'''Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:

40 procesos que ingresan 100

20 procesos que ingresan 50

60 que ingresen 20.

De la misma manera se desean lo siguientes procesos que retiran cantidades.

40 procesos que retiran 100

20 procesos que retiran 50

60 que retiran 20.

'''



class Banco():
    def __init__(self):
        self.dinero = 100
        #operacion = 1

    def ingresar(self, cantidad):
        self.dinero = self.dinero + int(cantidad)
        print(self.dinero)
        return self.dinero
    
        #self.operacion += 1
    
    def retirar(self, cantidad):
            '''cola.join()#Paramos la cola hasta que se hayan hecho todas las operaciones
            cola.put(self.operacion)'''
            self.dinero = self.dinero - int(cantidad)
            return self.dinero
            #self.operacion -= 1


def piscina(proc, func, dinero):
    piscina = Pool(processes = proc)
    piscina.map(func, dinero)
    piscina.close()


if __name__ == '__main__':
    c1 = []
    for i in range(40):
        c1.append(100)
    c2 = []
    for i in range(20):
        c2.append(50)
    c3 = []
    for i in range(60):
         c3.append(20)
    cuenta = Banco()
    print("Dinero inicial: " + str(cuenta.dinero))

    piscina(40, cuenta.ingresar, c1)
    #print(cuenta.dinero)
    piscina(20, cuenta.ingresar, c2)
    #print(cuenta.dinero)
    piscina(60, cuenta.ingresar, c3)
    #print(cuenta.dinero)
    piscina(40, cuenta.retirar, c1)
    #print(cuenta.dinero)
    piscina(20, cuenta.retirar, c2)
    #print(cuenta.dinero)
    piscina(60, cuenta.retirar, c3)
    #print(cuenta.dinero)

    print("Dinero final: " + str(cuenta.dinero))
