import threading
import unittest
from multiprocessing import Pool
import multiprocessing
import concurrent.futures

class CuentaBancaria:
    def __init__(self):
        self.saldo = 100
    
    def ingresar_dinero(self,cantidad):
        self.saldo += cantidad

    def retirar_dinero(self,cantidad):
        self.saldo -= cantidad

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaBancaria()

    def test_ingreso_y_retiro(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            #ingresos
            ingresos= [executor.sumbit(self.cuenta.ingresar_dinero, 100) for i in range(40)]
            ingresos += [executor.sumbit(self.cuenta.ingresar_dinero, 50) for i in range(20)]
            ingresos += [executor.sumbit(self.cuenta.ingresar_dinero, 20) for i in range(60)]
            #retiros


    #def test_ingreso_y_retiro(self):
        #threads= []
        #ingreso
        #for i in range(40):
        #    t = threading.Thread(target=self.cuenta.ingresar_dinero, args=(100,))
        #    threads.append(t)
        #for i in range(20):
        #    t = threading.Thread(target=self.cuenta.ingresar_dinero, args=(50,))
        #    threads.append(t)
        #for i in range(60):
        #    t = threading.Thread(target=self.cuenta.ingresar_dinero, args=(20,))
        #    threads.append(t)
        #retiro
        #for i in range(40):
        #    t = threading.Thread(target=self.cuenta.retirar_dinero, args=(100,))
        #    threads.append(t)
        #for i in range(20):
        #    t = threading.Thread(target=self.cuenta.retirar_dinero, args=(50,))
        #    threads.append(t)
        #for i in range(60):
        #    t = threading.Thread(target=self.cuenta.retirar_dinero, args=(20,))
        #    threads.append(t)

        #for t in threads:
        #    t.start()
        #for t in threads:
        #    t.join()
        #self.assertEqual(self.cuenta.saldo, 100)

if __name__ == '__main__':
    unittest.main()
