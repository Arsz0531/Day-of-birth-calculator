year = 0
month = 0
day = 0
weekday_dictionary = {
    0: "saturday",
    1: "sunday",
    2: "monday",
    3: "tuesday",
    4: "wednesday",
    5: "thursday",
    6: "friday"
}


def is_leapyear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

while True:
    year = (int(input("Year: ")))
    if year < 1583 or year > 9999:
        print("Out allowed range 1583 - 9999")
    else:
        break

while True:
    month = (int(input("Month: ")))
    if month < 1 or month > 12:
        print("Out of allowed range 1 - 12")
    else:
        break

while True:
    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]
    day = (int(input("Day: ")))
    """ Parenthases around the if statements fix issue
    when the wrong input is send and all four prints print."""
    if ((month in day31) and (day < 1 or day > 31)):
        print("Out of allowed range 1 - 31")
    if ((month in day30) and (day < 1 or day > 30)):
        print("Out of allowed range 1 - 30")
    if ((month == 2 and is_leapyear(year)) and (day < 1 or day > 29)):
        print("Out of allowed range 1 - 29")
    if ((month == 2 and not is_leapyear(year)) and (day < 1 or day > 28)):
        print("Out of allowed ranged 1- 28")
    else:
        break

if month == 1 or month == 2:
    month += 12
    year -= 1

weekday = (day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7

print("It is a " + weekday_dictionary.get(weekday))


