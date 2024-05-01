class game:
    def __init__(self, ID="", level=0):
        self.ID = ID
        self.lev = level

game1 = game()
game2 = game()

game1.ID = "codetree"
game1.lev = 10

ID, level = input().split()

game2.ID = ID
game2.lev = int(level)

print(f"user {game1.ID} lv {game1.lev}")
print(f"user {game2.ID} lv {game2.lev}")