import random
import threading
import time

class Ruleta:
    def __init__(self):
        self.numero = None
        self.banca = 50000
        self.jugadores = []

    def girar(self):
        self.numero = random.randint(0, 36)
        print("Ha salido el número", self.numero)
        if self.numero == 0:
            self.banca += sum(jugador.apuesta for jugador in self.jugadores)
            for jugador in self.jugadores:
                jugador.saldo -= jugador.apuesta
            print("La banca se queda con todo el dinero.")
        else:
            ganadores = [jugador for jugador in self.jugadores if jugador.apuesta_ganadora(self.numero)]
            perdedores = [jugador for jugador in self.jugadores if jugador not in ganadores]
            ganancia_banca = sum(jugador.apuesta for jugador in perdedores)
            perdida_banca = sum(jugador.apuesta * 36 for jugador in ganadores)
            self.banca += ganancia_banca - perdida_banca
            for jugador in ganadores:
                jugador.saldo += jugador.apuesta * 36
            for jugador in perdedores:
                jugador.saldo -= jugador.apuesta
            print("La banca gana", ganancia_banca - perdida_banca, "euros.")
    
    def add_jugador(self, jugador):
        self.jugadores.append(jugador)
        
