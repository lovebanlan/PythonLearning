from datetime import datetime, timedelta
now = datetime.now()
print(now)

dt = datetime(2015, 4, 20, 12, 20, 20, 99)
print(dt)
t = dt.timestamp()
print(dt + timedelta(hours=1, days=20))