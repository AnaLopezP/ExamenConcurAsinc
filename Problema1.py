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
        self.dinero = self.dinero + cantidad
        print()
        #self.operacion += 1
    
    def retirar(self, cantidad):
            '''cola.join()#Paramos la cola hasta que se hayan hecho todas las operaciones
            cola.put(self.operacion)'''
            self.dinero = self.dinero - cantidad
            #self.operacion -= 1


def piscina(proc, func, dinero):
    piscina = Pool(processes = proc)
    d = piscina.map(func, dinero)
    piscina.close()


if __name__ == '__main__':
    c1 = 100
    c2 = 50
    c3 = 20 
    cuenta = Banco()
    print("Dinero inicial: " + str(cuenta.dinero))

    piscina(40, cuenta.ingresar, 100)
    print(cuenta.dinero)
    piscina(20, cuenta.ingresar, 50)
    print(cuenta.dinero)
    piscina(60, cuenta.ingresar, 20)
    print(cuenta.dinero)
    piscina(40, cuenta.retirar, 100)
    print(cuenta.dinero)
    piscina(20, cuenta.retirar, 50)
    print(cuenta.dinero)
    piscina(60, cuenta.retirar, 20)
    print(cuenta.dinero)


