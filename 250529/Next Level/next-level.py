user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self, Id, lev):
        self.Id = Id
        self.lev = lev

user1 = User("codetree", 10)
user2 = User(user2_id, user2_level)

print(f"user {user1.Id} lv {user1.lev}")
print(f"user {user2.Id} lv {user2.lev}")