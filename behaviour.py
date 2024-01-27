class Behaviour():
    def __init__(self) -> None:
        self.mode : str = "Atacante"
        self.mood : str = "Feliz"

    def ball_owner(self) -> bool:
        if self.mode == "Atacante":
            return True
        
        else:
            self.mode = "Defensivo"
            self.mood = "Triste"
            return False
