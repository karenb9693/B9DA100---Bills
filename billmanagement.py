
import pandas as pd 
from collections import Counter
#from writebills import get_newbill
#import datetime as dt

def read_bills():
    bills = pd.read_csv('bills.csv', names=["Company", "Account Name", "Year","Month", "Day", "Value", "Type"])   
    bills["Value"] = pd.to_numeric(bills['Value'],errors='ignore')
    bills['Period'] = bills['Year'].astype(str) + "." + bills['Month'].astype(str)+"."+ bills['Day'].astype(str)
    bills["Period"] = pd.to_datetime(bills['Period'])
    return bills

#def write_bills(bills1):
 #   #get_newbill()
  #  billsnew = bills1.append(pd.Series([input("Company: "), input("Account Name: " ), input("Year: "),input("Month: "),
   #                                       input("Day: "), input("value: ") ,input("Type: ")], index=bills1.columns), ignore_index=True)
   # billsnew.to_csv('bills.csv')
   # bills = pd.read_csv('bills.csv')   
   # return bills

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
            #choice3 = input("do you wish to insert a new bill?")
            #if choice3 == "1":
            #    write_bills(bills)
        #elif choice == '2':
         #   print("you can insert a new bill here:")
          #  write_bills(bills)
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
    bills = read_bills
   # bills = write_bills()
    display_menu()
    process_choice(bills)
    
if __name__ == '__main__':
    main()

