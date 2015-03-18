days = 2
dayt = "!mtwrfs"
sundays = 0
def leap(year):
    return (year % 400 == 0) or (year%4 == 0 and not year%100==0)

for year in range(1901,2001):
    months = [31, 29 if leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(12):
        days+=months[month]
        if days%7==0:
            sundays+=1

print sundays

