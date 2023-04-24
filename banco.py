import threading
import unittest

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
        threads= []
#ingreso
        for i in range(40):
            t = threading.Thread(target=self.cuenta.ingresar_dinero, args=(100,))
            threads.append(t)
        for i in range(20):
            t = threading.Thread(target=self.cuenta.ingresar_dinero, args=(50,))
            threads.append(t)
        for i in range(60):
            t = threading.Thread(target=self.cuenta.ingresar_dinero, args=(20,))
            threads.append(t)
#retiro
        for i in range(40):
            t = threading.Thread(target=self.cuenta.retirar_dinero, args=(100,))
            threads.append(t)
        for i in range(20):
            t = threading.Thread(target=self.cuenta.retirar_dinero, args=(50,))
            threads.append(t)
        for i in range(60):
            t = threading.Thread(target=self.cuenta.retirar_dinero, args=(20,))
            threads.append(t)

        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        self.assertEqual(self.cuenta.saldo, 100)