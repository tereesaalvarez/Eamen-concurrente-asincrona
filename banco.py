import threading
import unittest

class CuentaBancaria:
    def __init__(self):
        self.saldo = 100
    
    def ingresar_dinero(self,cantidad):
        self.saldo += cantidad

    def retirar_dinero(self,cantidad):
        self.saldo -= cantidad

