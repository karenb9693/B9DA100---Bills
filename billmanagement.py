
import pandas as pd 
from collections import Counter
import datetime as dt

def read_bills():
    bills = pd.read_csv('bills1.csv', names=["Company", "Account Name", 
                    "Year","Month", "Day", "Value", "Type"])    
    bills["Value"] = pd.to_numeric(bills["Value"])
    bills['Period'] = bills['Year'].astype(str) + "." + bills['Month'].astype(str)+"."+ bills['Day'].astype(str)
    bills["Period"] = pd.to_datetime(bills['Period'])
    return bills
 
def write_bills(bills,Year, Month, Day, Type):
    billsnew = bills.append(pd.Series([input("Company: "), input("Account Name: " ), Year,Month,Day,Type], index=bills.columns), ignore_index=True)
    billsnew.to_csv('bills.csv')

def get_input_year(bills):
    choice_year = int(input("Enter Year:"))    
    if(choice_year > dt.datetime.now().year):
        print("This is not a valid input")
    else: 
        Year = choice_year
    return Year

def get_input_month(bills):
    choice_month = int(input("Enter Month:"))
    if 1 <= choice_month <= 12:
        Month = choice_month
    else:
        print("This is not a valid input")
    return Month

def get_input_day(bills,Month,Year):
    choice_day = int(input("Enter Day:"))
    if Month == 2 & (1 <= choice_day <= 28):
        Day = choice_day
    elif (Month == 4 or Month == 6 or Month == 9 or Month == 11) & (1 <= choice_day <= 30):
        Day = choice_day
    elif (Year % 4 == 0 & Year % 100 != 0 & Year % 400 == 0) & (Month == 2) & (1 <= choice_day <= 29):
        Day = choice_day
    elif (Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 11) & (1 <= choice_day <= 31):
        Day = choice_day
    else:
        print("This is not a valid input")
    return Day

def get_input_type(bills):
    choice_debcred = input("Enter 1 for credit.\nEnter 2 for debit.\n")
    choice_debcred = int(choice_debcred)
    if choice_debcred == 1: 
        Type = " credit"
    elif choice_debcred == 2: 
        Type = " debit"
    return Type

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\nx: Exit'

def get_submenu_message():
    return 'The report options are as follows:' + \
    '\nx: to go back to main menu\na: information about dataset\nb: credit vs debit \nc: companies \nd: date sort \ne visualisation'
        
def display_menu():
    print(get_message())
    
def display_submenu():
    print(get_submenu_message())
    
#Function for getting the cred and debit total       
def get_value_CredDeb(bills):
    print('The largest value of credit and debit bills is as follows:',bills.groupby('Type')['Value'].max())
   
def get_creddeb_year(bills):
    print('Value of credit and debit per year is:', bills.groupby(['Type','Year'])['Value'].sum())

def display_unique_companies(bills):
    print('# of unique companies:', bills['Company'].nunique())

def display_bill_count(bills):
    print('# of bills in file:', bills['Company'].count())

def display_sortedbydate(bills):
    print(bills.sort_values(by='Period'))

#Function to print comopany with most amount of bills
def get_Companies(bills):
    print('most popular company is:', Counter(bills['Company']).most_common(1))

def get_bills_forall_Companies(bills):
    print('Count of bills for all companies is as follows:', Counter(bills['Company']).most_common(100))

def get_avg_time_between_bills(bills):
    print('Bills sorted in order of the date received:', display_sortedbydate(bills))

#def get_visualisations(bills):
 #   my_colors = list(['k', 'm', 'b', 'y'])
  #  bills['Company'].value_counts().plot.barh(color=my_colors).set_title("Count of bills per customer")
   # sns.boxplot(bills['Year'], bills['Value']).set_title("Value of bills per year")
    #sns.countplot(x="Account Name", hue="Company", data=bills).set_title('Count of bills per customer and company')
    
def view_bills(bills):
        print(bills)
    
def process_choice(bills):
    choice = input('Please enter an option:')
    while choice != 'x':
        if choice == '1':
            view_bills(bills)
        elif choice == '2':
            print("you can insert a new bill here:")
            write_bills(bills)
        elif choice == '3':
            display_submenu()
            choice2 = input('Please select requested report:')
            while choice2 != 'x':
                if choice2 == 'a':
                    display_bill_count(bills)
                    display_unique_companies(bills)
                    break
                elif choice2 == 'b':
                    get_value_CredDeb(bills)
                    get_creddeb_year(bills)
                    break
                elif choice2 == 'c':
                    get_Companies(bills)
                    get_bills_forall_Companies(bills)
                    break
                elif choice2 == 'd':
                    display_sortedbydate(bills)
                    break
                #elif choice2 == 'e':
                    #get_visualisations(bills)
                 #   break      
        elif choice == '4':
            print('The terms of the billing management company are:')
        choice = input('Please enter an option:')

def main():
    bills = read_bills()
    Year = get_input_year()
    Month = get_input_month()
    Day = get_input_day()
    Type = get_input_type()
    display_menu()
    process_choice(bills)
    write_bills(bills,Year, Month, Day,Type)
    
if __name__ == '__main__':
    main()

