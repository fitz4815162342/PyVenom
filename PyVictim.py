class Victim:

    def __init__(self):
        self.metadata = "Simple test class to test malicious code"

    def add(self, x, y):
        return x+y

x,y=1,1
z = Victim().add(1,1)
print(Victim().metadata)
print(f"{x} + {y} = {z}")
