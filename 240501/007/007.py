class Secret:
    def __init__(self, code, spot, time):
        self.c = code
        self.s = spot
        self.t = time

secret1 = Secret("codetree", "L", 13)
print(f"secret code : {secret1.c}\nmeeting point : {secret1.s}\ntime : {secret1.t}")