import pandas as pd 
from collections import Counter

def read_bills():
    return [[col.strip() for col in row.strip().split(',')]
             for row in open('bills.csv') if len(row) > 1]

def write_bills(bills):
    bill_file = open('bills.csv', 'w')
    for bill in bills:
        bill_file.write(', '.join(bill) + '\n')

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit'

#Function for getting the most popular company
def get_topComp(bills):
    for bill in bills:
        df = pd.DataFrame(bills[0])
        df[0].value_counts().argmax()
        #use mode to return the most common company
        print(df.mode)
        
#Function for getting the cred and debit total       
def get_value_CredDeb(bills):
   #df = pd.DataFrame(bills)
   #df.rename(columns={[0]:"Company", [1]: "Account Name", [2]:"Year",[3]:"Month",[4]: "Day", [5]:"Value", [6]:"Type"}, 
              #   inplace=True)
            
   #df.groupby([6]).sum()[5]
   #print(df)
    
   for bill in bills:
       list2 = list()
       list3 = list()
       if bill[6] == "credit":
           list2.append(float(bill[5]))
       elif bills[6] == "debit":
           list3.append(float(bill[5]))
   print("total value of credit is:", sum(list2))
   print("total value of debit is:", sum(list3))

def display_menu():
    print(get_message())

#Function to print comopany with most amount of bills
def get_Companies(bills):
    list1 = list()
    for bill in bills:
        list1.append(bill[0])
    print(Counter(list1).most_common(1))

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
            get_Companies(bills)
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