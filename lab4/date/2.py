import datetime

print("Yesterday -",(datetime.datetime.today() - datetime.timedelta(days = 1)).strftime("%A"))

print("Today -",datetime.datetime.today().strftime("%A"))

print("Tomorow -",(datetime.datetime.today() + datetime.timedelta(days = 1)).strftime("%A"))