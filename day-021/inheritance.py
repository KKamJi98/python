class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
        
    def breathe(self) -> None:
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def swim(self) -> None:
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()