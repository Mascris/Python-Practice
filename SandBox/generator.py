class SimpleRandom:
    def __init__(self, seed=0):
        self.s = seed
    
    def next(self):
        self.s = (self.s * 9301 + 49297) % 233280
        return self.s

    def next_float(self):
        return self.next() / 233280.0

for i in range(100):
    rng = SimpleRandom(seed=i)
    print(rng.next_float())
