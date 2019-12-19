
import pandas as pd 
import seaborn as sns
from collections import Counter

def read_bills():
    bills = pd.read_csv('bills1.csv', names=["Company", "Account Name", "Year", "Month", "Day", "Value", "Type"])
    bills["Value"] = pd.to_numeric(bills["Value"])
    bills['Period'] = bills['Year'].astype(str) +"."+ bills['Month'].astype(str)+"."+ bills['Day'].astype(str)
    bills["Period"] = pd.to_datetime(bills['Period'])
    return bills
 
def write_bills(bills):
    bill_file = open('bills.csv', 'w')
    for bill in bills:
        bill_file.write(', '.join(bill) + '\n')

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\nx: Exit'

def get_submenu_message():
    return 'The report options are as follows:' + \
    '\nx: to go back to main menu\na: information about dataset\nb: credit vs debit \nc: companies \nd: visualisation'
        
#Function for getting the cred and debit total       
def get_value_CredDeb(bills):
    print(bills.groupby('Type')['Value'].max())
   
def get_creddeb_year(bills):
    print(bills.groupby(['Type','Year'])['Value'].sum())

def display_menu():
    print(get_message())
    
def display_submenu():
    print(get_submenu_message())
    
def display_unique_companies(bills):
    print(bills['Company'].nunique())

def display_bill_count(bills):
    print(bills['Company'].count())

#Function to print comopany with most amount of bills
def get_Companies(bills):
    print(Counter(bills['Company']).most_common(1))

def get_bills_forall_Companies(bills):
    print(Counter(bills['Company']).most_common(100))

def get_visualisations(bills):
    my_colors = list(['k', 'm', 'b', 'y'])
    bills['Company'].value_counts().plot.barh(color=my_colors).set_title("Count of bills per customer")
    sns.boxplot(bills['Year'], bills['Value']).set_title("Value of bills per year")
    sns.countplot(x="Account Name", hue="Company", data=bills).set_title('Count of bills per customer and company')
    
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
                    print('# of bills in file')
                    display_bill_count(bills)
                    print('# of unique companies')
                    display_unique_companies(bills)
                    break
                elif choice2 == 'b':
                    print('The largest value of credit and debit bills is as follows:')
                    get_value_CredDeb(bills)
                    print('Value of credit and debit per year is:')
                    get_creddeb_year(bills)
                    break
                elif choice2 == 'c':
                    print('most popular company is:')
                    get_Companies(bills)
                    print('Count of bills for all companies is as follows:')
                    get_bills_forall_Companies(bills)
                    break
                elif choice2 == 'd':
                    get_visualisations(bills)
                    break
        elif choice == '4':
            print('The terms of the billing management company are:')
        choice = input('Please enter an option:')

def main():
    bills = read_bills()
    display_menu()
    process_choice(bills)
    write_bills(bills)
    
if __name__ == '__main__':
    main()

