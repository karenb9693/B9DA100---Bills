
import pandas as pd 
import seaborn as sns
from collections import Counter
from writebills import get_newbill

def read_bills():
    bills = pd.read_csv('bills.csv', names=["Company", "Account Name", "Year",\
                                            "Month", "Day", "Value", "Type"])
    bills["Value"] = pd.to_numeric(bills["Value"])
    bills['Period'] = bills['Year'].astype(str) +"."+ \
        bills['Month'].astype(str)+"."+ bills['Day'].astype(str)
    bills["Period"] = pd.to_datetime(bills['Period'])
    return bills
 
def write_bills():
    get_newbill()

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\nx: Exit'

def get_submenu_message():
    return 'The report options are as follows:' + \
    '\nx: Exit to main menu\na: Count of bills/companies \nb: Credit vs Debit \
    \nc: Most popular \nd: Bills sorted \ne: Average spent \
    \nf: Average time between bill'
        
#Function for getting the cred and debit total       
def get_value_CredDeb(bills):
    print('The largest value of credit and debit bills is as follows:',
          bills.groupby('Type')['Value'].max())
   
def get_creddeb_year(bills):
    print('Value of credit and debit per year is:', \
          bills.groupby(['Year','Type'])['Value'].sum())

def display_menu():
    print(get_message())
    
def display_submenu():
    print(get_submenu_message())
    
def display_unique_companies(bills):
    print('# of unique companies:', bills['Company'].nunique())
    return bills['Company'].nunique()

def display_bill_count(bills):
    print('# of bills in file:', bills['Company'].count())
    return bills['Company'].count()

def display_sortedbydate(bills):
    print(bills.sort_values(by='Period'))

#Function to print comopany with most amount of bills
def get_Companies(bills):
    print('most popular company is:', Counter(bills['Company']).most_common(1))

def get_bills_forall_Companies(bills):
    print('Count of bills for all companies is as follows:', \
          Counter(bills['Company']).most_common(100))
    
def display_average_spent(bills):
    billstime = bills.loc[(bills['Month'] >= int(input("Start Month ")))]
    billstime = billstime.loc[(billstime['Month'] <= int(input("End Month ")))]
    print("the average bill cost between these months is: ", \
          round(billstime.sort_values(by='Period')['Value'].mean()))
    
def avg_time_between_bills(bills):
    bills = bills.sort_values(by='Period')
    print("Avg time between a bill is: ",\
          (round(bills['Period'].diff().sum().days/(bills['Company'].count()))), "days")
    return (round(bills['Period'].diff().sum().days/(bills['Company'].count())))

def get_visualisations(bills):
    my_colors = list(['k', 'm', 'b', 'y'])
    bills['Company'].value_counts().plot.barh(color=my_colors).\
    set_title("Count of bills per customer")
    sns.boxplot(bills['Year'], bills['Value']).\
    set_title("Value of bills per year")
    sns.countplot(x="Account Name", hue="Company", data=bills).\
    set_title('Count of bills per customer and company')
    
def get_terms_and_conditions():
    return '1. All bills entered should be honest and accurate. \
        \n2. The Bills Management Co. take no responsibility for bills added incorrectyly'
    
def view_bills(bills):
    print(bills)
        
def view_terms_and_conditions():
    print(get_terms_and_conditions())
    
def process_choice(bills):
    choice = input('Please enter an option: ')
    while choice != 'x':
        if choice == '1':
            view_bills(bills)
        elif choice == '2':
            print("you can insert a new bill here: ")
            bills.iloc[0:0]
            write_bills()
            print("To provide an analysis including the new reports"
                  " added you must exit and re-enter the program")
        elif choice == '3':
            display_submenu()
            choice2 = input('Please select requested report: ')
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
                elif choice2 == 'e':
                    display_average_spent(bills)
                    break
                elif choice2 == 'f':
                    avg_time_between_bills(bills)
                    break
        elif choice == '4':
            print('The terms of the billing management company are as follows:')
            view_terms_and_conditions()
        choice = input('Please enter an option: ')

def main():
    bills = read_bills()
    display_menu()
    process_choice(bills)
    #write_bills(bills)
    
if __name__ == '__main__':
    main()