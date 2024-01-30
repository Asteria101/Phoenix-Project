from behaviour import Behaviour
import threading

class Player():
    def __init__(self, name : str = "Leticia", number : int = 21, position : tuple[int] = (0, 0)) -> None:
        self.name = name
        self.number = number
        self.position = position
        self.behaviour = Behaviour()

        self.print_intro()
        
        self.target = threading.Thread(target=self.get_info)
        self.target.start()

    def kick(self, distance_ball : float):
        if distance_ball <= 0.6 and self.behaviour.ball_owner():
            print("Dá pra chutar a bola.")
        else:
            self.run()

    def run(self):
        print(f"Estou correndo. E estou {self.behaviour.mood}")
        
    def print_intro(self):
        if self.name == "Leticia":
            print(f"A jogadora {self.name}", end="")
        else:
            print(f"O jogador {self.name}", end="")

        print(f", cujo número é {self.number}, está na posição {self.position}.")

    def get_info(self):
        while True:
            info = []
            info.append(self.run)
            