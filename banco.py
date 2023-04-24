import threading
import unittest
from multiprocessing import Pool
import multiprocessing

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

if __name__ == '__main__':
    unittest.main()
    cuenta = multiprocessing.Value('i', 100)
    
    tareas_ingreso = [(cuenta, 100)] * 40 + [(cuenta, 50)] * 20 + [(cuenta, 20)] * 60
    tareas_retiro = [(cuenta, 100)] * 40 + [(cuenta, 50)] * 20 + [(cuenta, 20)] * 60
    
    with multiprocessing.Pool(processes=4) as pool:
        pool.starmap(CuentaBancaria.ingresar_dinero, tareas_ingreso)
        pool.starmap(CuentaBancaria.retirar_dinero, tareas_retiro)
        
    assert cuenta.value == 100, f"La cuenta bancaria no tiene el saldo esperado ({cuenta.value} euros)."