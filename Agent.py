class Agent:
    def __init__(self, type, pos) -> None:
        if type == "pacman":
            self.type = 2
            self.pos = pos
        elif type == "ghost":
            self.type = 3
            self.pos = pos

    def __str__(self) -> str:
        return f"{self.type} >  {self.pos}"
