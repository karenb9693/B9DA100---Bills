import unittest
#import pandas as pd 


from billmanagement import (read_bills, display_unique_companies, 
display_bill_count, get_message, get_submenu_message, display_sortedbydate,
avg_time_between_bills, get_terms_and_conditions)

class TestBillManagement(unittest.TestCase):

    def test_read_bills(self):
        bills = read_bills()
        self.assertEqual(43, len(bills))

    def test_get_message(self):
        self.assertEqual('Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\nx: Exit',
            get_message())       
        
    def test_get_submenu_message(self):
        self.assertEqual('The report options are as follows:' + \
    '\nx: Exit to main menu\na: Count of bills/companies \nb: Credit vs Debit \
    \nc: Most popular \nd: Bills sorted \ne: Average spent \
    \nf: Average time between bill',
            get_submenu_message())
        
    def test_get_terms_and_conditions(self):
        self.assertEqual('1. All bills entered should be honest and accurate. \
        \n2. The Bills Management Co. take no responsibility for bills added incorrectyly',
        get_terms_and_conditions())

    def test_display_sortedbydate(self):
        bills = read_bills()
        bills1 = display_sortedbydate(bills)
        self.assertEqual('Tesco Mobile', bills1['Company'].values[0])
        self.assertEqual('Karen Byrne', bills1['Account Name'].values[10])


    def test_display_unique_companies(self):
        bills = read_bills()
        self.assertEqual(10, display_unique_companies(bills))
        
    def test_display_bill_count(self):
        bills = read_bills()
        self.assertEqual(43, display_bill_count(bills))
    
    def test_avg_time_between_bills(self):
        bills = read_bills()
        self.assertEqual(439.0, avg_time_between_bills(bills))

if __name__ == '__main__':
    unittest.main()