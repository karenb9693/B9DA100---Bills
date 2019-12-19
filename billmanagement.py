
import pandas as pd 
from collections import Counter

def read_bills():
    return [[col.strip() for col in row.strip().split(',')]
             for row in open('bills1.csv') if len(row) > 1]
    

def write_bills(bills):
    bill_file = open('bills.csv', 'w')
    for bill in bills:
        bill_file.write(', '.join(bill) + '\n')

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit'

def get_submenu_message():
    return 'The report options are as follows:' + \
    '\nx: to go back to main menu\na: information about dataset\nb: credit vs debit \nc: companies'

#Function for getting the most popular company
#def get_topComp(bills):
 #   for bill in bills:
  #      df = pd.DataFrame(bills[0])
   #     df[0].value_counts().argmax()
        #use mode to return the most common company
      #  print(df.mode)
        
#Function for getting the cred and debit total       
def get_value_CredDeb(bills):
   df = pd.DataFrame(bills)
   df.columns = ["Company", "Account Name", "Year", "Month", "Day", "Value", "Type"]
   print("The largest value of a credit/debit bill is:", df.groupby('Type')['Value'].max())
   
def get_creddeb_year(bills):
   df = pd.DataFrame(bills)
   df.columns = ["Company", "Account Name", "Year", "Month", "Day", "Value", "Type"]
   df["Value"] = pd.to_numeric(df["Value"])
   print("The value of Debit and Credit per year", df.groupby(['Type','Year'])['Value'].sum())

def display_menu():
    print(get_message())
    
def display_submenu():
    print(get_submenu_message())
    
def display_info(bills):
   df = pd.DataFrame(bills)
   df.columns = ["Company", "Account Name", "Year", "Month", "Day", "Value", "Type"]
   print("The amount of bills listed is:", df['Company'].count())
   print("The number of unique companies are:", df['Company'].nunique())

#Function to print comopany with most amount of bills
def get_Companies(bills):
    list1 = list()
    for bill in bills:
        list1.append(bill[0])
    print()
    print("The company with the most amount of bills is:", Counter(list1).most_common(1))

def view_bills(bills):
    for bill in bills:
        print(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6])
    
def process_choice(bills):
    choice = input('Please enter an option:')
    while choice != '5':
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
                    print('Information about companies and the amount of bills in the dataset')
                    display_info(bills)
                    break
                elif choice2 == 'b':
                    print('Information regarding credit vs debit')
                    get_value_CredDeb(bills)
                    get_creddeb_year(bills)
                    break
                elif choice2 == 'c':
                    get_Companies(bills)
                    break
            choice2 = input('Please select requested report:')
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

