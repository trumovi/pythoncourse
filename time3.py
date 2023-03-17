import time

year = input("Year of birth: ")
month = input("Month of birth: ")
day = input("Day of birth: ")
birth = day + "." + month + "." + year
print(f"Вы прожили {round((time.time() - time.mktime(time.strptime(birth,'%d.%m.%Y')))/86400)} дней")
