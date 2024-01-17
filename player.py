from behaviour import Behaviour

class Player():
    def __init__(self, name : str, number : int, position : tuple[int]) -> None:
        self.name : str = "Leticia"
        self.number : int = 21
        self.position : tuple[int] = (0, 0)
        self.ball_own = Behaviour.ball_owner

        print(f"A jogadora {self.name}, cujo número é {self.number}, está na posição {self.position}.")

    def kick(self, distance_ball : float):
        if distance_ball <= 0.6 and self.ball_own:
            print("Dá pra chutar a bola.")

        