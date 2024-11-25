from datetime import datetime, timezone, timedelta

# Get current UTC time
# print('Israel', datetime.now())
# print('UTC   ', datetime.now(timezone.utc))
# print(datetime.now().strftime("%H:%M:%S.%f %d/%m/%Y"))
# print(datetime.now().strftime("%H:%M:%S.%f %Y-%B-%d %A"))
# print( (datetime.now() + timedelta(days=1)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))
# print( (datetime.now() + timedelta(days=30)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))
# print( (datetime.now() + timedelta(hours=90)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))

# create a new list
# input names from the user until 'done'
# append each name to a list with a timestamp as tuple
# danny
#    0                        ,  1
# [ (datetime.now(), 'danny') , ( )]
# print all the time+name and index
# for key, value ...
#  0: danny 18:55  1: sharon 18:56

# list_enter: list [tuple] = []
# SENTINEL: str = "done"
# while True:
#     name: str = str(input(" Enter name :"))
#     if SENTINEL == name:
#         break
#     else:
#         list_enter.append((name, datetime.now().strftime("%H:%M:%S %d/%m/%Y")))
#
# for index ,value in enumerate(list_enter):
#     print(f" {index} {value}")
#----------------------------------------------

# abc = 0
# if abc == 0 and (abc := 1):  # בדוק קודם אם abc שווה ל-0 ואז עשה השמה ל-1
#     print(True, f"{abc}")
# else:
#     print(False, f"{abc}")

#-------------------------------------------------

titanic = {3, 2, 6,0, 4, 5}
oscar = {3, 11, 6,12, 4, 13}

print(f" actor which no win in oscar: {titanic - oscar}")
