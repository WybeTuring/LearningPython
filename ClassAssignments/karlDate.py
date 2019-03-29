# Author: Lemfon Karl Ndze'dzenyuy
# Purpose: This program returns the day on which any day is returned
days = {1:"Monday",2:"Tuesday",3:"Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
# Function that caclculates the number of days by years, this is for the full years that are inbetween
def numberOfDaysByYear(y):
    days = 0
    todayYear = 2019
    years = y - todayYear
    if y > 2019:
        for i in range(2020, y+1):
            if i % 4 == 0:
                days += 366
            else:
                days += 365
    else:
        for i in range(y+1,2019):
            if i % 4 == 0:
                days += 366
            else:
                days += 365
    return days
# Function that calculates the number of days between full months
def numberofDaysByMonth(m,y):
    normalYear = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 30, 31]
    leapYear = [31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 30, 31]
    days = 0
    todayMonth = 1
    if y % 4 == 0:
        for i in range(2,m+1):
            days += leapYear[i]
    else:
        for i in range(2,m+1):
            days += normalYear[i]
    return days
# This function returns the number of days if the month is in january
def numberofDaysByDays(d):
    return d-25

day, month, year = eval(input("Enter the day, month and date in that order. Please seperate with spaces: "))
print(numberofDaysByMonth(month) + numberOfDaysByYear(year))
