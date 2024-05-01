class Secret:
    def __init__(self, code, spot, time):
        self.c = code
        self.s = spot
        self.t = time

s_code, m_point, time = tuple(input().split())

s = Secret(s_code, m_point, int(time))
print(f"secret code : {s.c}\nmeeting point : {s.s}\ntime : {s.t}")