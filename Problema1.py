from queue import Queue 
import threading

'''Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:

40 procesos que ingresan 100

20 procesos que ingresan 50

60 que ingresen 20.

De la misma manera se desean lo siguientes procesos que retiran cantidades.

40 procesos que retiran 100

20 procesos que retiran 50

60 que retiran 20.

'''

cola = Queue(100) 

class Banco(threading.Thread):
    def __init__(self, dinero):
        dinero = dinero

    def ingresar(cantidad):
        dinero = dinero + cantidad
        return dinero
    
    

