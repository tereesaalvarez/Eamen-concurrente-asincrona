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
        
class Jugador(threading.Thread):
    def __init__(self, ruleta):
        threading.Thread.__init__(self)
        self.ruleta = ruleta
        self.saldo = 1000
        
    def run(self):
        while self.saldo > 0:
            time.sleep(3)
            self.apostar()
            
    def apostar(self):
        tipo_apuesta = random.choice(["numero", "par_impar", "martingala"])
        if tipo_apuesta == "numero":
            numero_elegido = random.randint(1, 36)
            self.apuesta = 10
            self.numero_apostado = numero_elegido
            print("El jugador", self.ident, "apuesta", self.apuesta, "euros al número", self.numero_apostado)
        elif tipo_apuesta == "par_impar":
            par_impar_elegido = random.choice(["par", "impar"])
            self.apuesta = 10
            self.par_impar_apostado = par_impar_elegido
            print("El jugador", self.ident, "apuesta", self.apuesta, "euros a", self.par_impar_apostado)
        else:
            if not hasattr(self, "numero_anterior"):
                self.numero_anterior = random.randint(1, 36)
            self.apuesta = 10 if self.numero_anterior == self.ruleta.numero else self.apuesta * 2
            self.numero_apostado = self.numero_anterior
            print("El jugador", self.ident, "apuesta", self.apuesta, "euros al número", self.numero_apostado)
        self.ruleta.add_jugador(self)
        
    def apuesta_ganadora(self, numero):
        if hasattr(self, "numero_apostado"):
            return self.numero_apostado == numero
        else:
            return (self.par_impar_apostado == "par" and numero % 2 == 0) or (self.par_impar_apostado == "impar" and numero % 2 == 1)

if __name__ == "__main__":
    ruleta = Ruleta()
    jugadores = [Jugador(ruleta) for _ in range(10)]
    for jugador in jugadores:
        jugador.start()
    while True:
        time.sleep(10)
        ruleta.girar()
