from behaviour import Behaviour

class Player():
    def __init__(self, name : str = "Leticia", number : int = 21, position : tuple[int] = (0, 0)) -> None:
        self.name : str = name
        self.number : int = number
        self.position : tuple[int] = position
        self.behaviour = Behaviour

        self.print_intro()

    def kick(self, distance_ball : float):
        if distance_ball <= 0.6 and self.behaviour.ball_owner():
            print("Dá pra chutar a bola.")

    def run(self):
        print(f"Estou correndo e estou {}")

    def print_intro(self):
        if self.name == "Leticia":
            print(f"A jogadora {self.name}, cujo número é {self.number}, está na posição {self.position}.")
        else:
            print(f"O jogador {self.name}, cujo número é {self.number}, está na posição {self.position}.")
            
