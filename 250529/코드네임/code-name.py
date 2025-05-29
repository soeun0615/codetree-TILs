MAX_N = 5

# Please write your code here.
class Agent:
    def __init__(self, codename="null", score=0):
        self.codename = codename
        self.score = score

agents = []
for _ in range(MAX_N):
    codename, score = input().split()
    score = int(score)
    agents.append(Agent(codename, score))

agents_score = [score for _ in range(MAX_N)]

ind = agents_score.index(min(agents_score))
print(agents[ind].codename, agents[ind].score)