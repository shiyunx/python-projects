import calendar

while True:
    input_year = int(input("Search calendar year: "))
    input_month = int(input("Search calendar month: "))
    print(calendar.month(input_year, input_month))