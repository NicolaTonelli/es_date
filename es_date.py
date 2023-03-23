#inizio
import datetime

now = datetime.datetime.now()
print(f"Data corrente: {now}")

birthday = datetime.datetime(2006, 1, 30)
print(f"Data di nascita: {birthday}")

print(birthday.strftime("%A" " " "%d" " " "%B" " " "%Y"))
#fine