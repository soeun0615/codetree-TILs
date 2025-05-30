import datetime as dt

n = int(input())

# Please write your code here.
class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

# dt.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M")
forecasts = []
for _ in range(n):
    date, day, weather = input().split()
    forecasts.append(Forecast(date, day, weather))

ind = 0
for i in range(n):
    i_date = dt.datetime.strptime(forecasts[i].date, "%Y-%m-%d")
    ind_date = dt.datetime.strptime(forecasts[ind].date, "%Y-%m-%d")

    #ind 초기조건 
    if (forecasts[ind].weather != "Rain") & (forecasts[i].weather == "Rain"):
        ind = i

    if (forecasts[i].weather == "Rain") & (i_date < ind_date):
        ind = i


print(forecasts[ind].date, forecasts[ind].day, forecasts[ind].weather)