import datetime

def writeWeekReport ():
  today = datetime.date.today()
  mon = 0 - today.weekday()
  fri = 4 - today.weekday()
  Monday = str(today + datetime.timedelta(days=mon)).replace("-","/")[5:]
  Friday = str(today + datetime.timedelta(days=fri)).replace("-","/")[5:]
  week = Monday+"~"+Friday
  write = "の週報書け"
  return print(week+write)

writeWeekReport()