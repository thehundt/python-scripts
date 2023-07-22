from datetime import datetime
import pickle

theday = input('Enter a date (MMDD): ')
startyear = input('Enter starting year: ')
years = input('Enter number of years: ')

month = int(str(theday)[:2])
day = int(str(theday)[2:4])

print('For the Date: ', theday)

for year in range(int(startyear), int(startyear) + int(years) + 1):
    fulldate = datetime(year, month, day)
    print(fulldate.year, fulldate.strftime('%A'))