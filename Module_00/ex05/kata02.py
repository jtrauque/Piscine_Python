import datetime

t = (3,30,2019,9,25)

tm = datetime.datetime(t[2], t[3], t[4], t[0], t[1])
print(tm.strftime("%m/%d/%Y %H:%M"))
