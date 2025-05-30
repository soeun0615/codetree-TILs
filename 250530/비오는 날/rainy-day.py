n = int(input())

# Please write your code here.
class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


ans = Forecast("9999-99-99", "", "")

for _ in range(n):
    date, day, weather = input().split()
    f = Forecast(date, day, weather)

    #ind 초기조건 
    if (f.weather == "Rain"):
        if (f.date < ans.date):
            ans = f

print(ans.date, ans.day, ans.weather)