
import pandas as pd
import datetime

def get_newbill():
    now = datetime.datetime.now()
    
    choice_year = input("Enter Year: ")
    choice_year = int(choice_year)
    
    while(choice_year>now.year):
        print("This is not a valid input")
        print("Please enter a year up until the current year")
        choice_year = input("Enter Year: ")
        Year = choice_year
        break
    else:
        Year = choice_year
    
    choice_month = input("Enter Month: ")
    choice_month = int(choice_month)
    if 0 < choice_month <= 12:
        Month = choice_month
    else:
        print("This is not a valid input")
    
    choice_day = input("Enter Day: ")
    choice_day = int(choice_day)
    if (choice_month == 2) & (1 <= choice_day <= 28):
        Day = choice_day
    elif (choice_month == 4 or choice_month == 6 or choice_month == 9 or 
          choice_month == 11) & (0 < choice_day <= 30):
        Day = choice_day
    elif (choice_year % 4 == 0 & choice_year % 100 != 0 & 
          choice_year % 400 == 0) & (choice_month == 2) & (0 < choice_day <= 29):
        Day = choice_day
    elif (choice_month == 1 or choice_month == 3 or choice_month == 5 or 
          choice_month == 7 or choice_month == 8 or choice_month == 10 or 
          choice_month == 12) & (0 < choice_day <= 31):
        Day = choice_day
    else:
        print("This is not a valid input")
        
    choice_value = input("Enter bill value: ")
    choice_value = float(choice_value)
    
    choice_debcred = input("Enter 1 for credit. Enter 2 for debit.\n")
    choice_debcred = int(choice_debcred)
    if choice_debcred == 1:
        Type = " credit"
    elif choice_debcred == 2:
        Type = " debit"
        
    billsold = pd.read_csv('bills.csv')
    billsnew = billsold.append(pd.Series([input("Company: "), input("Account Name: " ), Year,Month,Day, choice_value ,Type], index=billsold.columns), ignore_index=True)
    billsnew.to_csv('bills.csv', index=False)
    return billsnew
