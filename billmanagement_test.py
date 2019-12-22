import unittest
#import pandas as pd 


from billmanagement import read_bills, display_unique_companies, display_bill_count, get_message, get_submenu_message, avg_time_between_bills

class TestBillManagement(unittest.TestCase):

    def test_read_bills(self):
        bills = read_bills()
        self.assertEqual(20, len(bills))

    def test_get_message(self):
        self.assertEqual('Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\nx: Exit',
            get_message())       
        
    def test_get_submenu_message(self):
        self.assertEqual('The report options are as follows:' + \
    '\nx: to go back to main menu\na: information about dataset\nb: credit vs debit \nc: companies \nd: bills sorted \ne average time between bills',
            get_submenu_message())

    def test_display_unique_companies(self):
        bills = read_bills()
        self.assertEqual(3, display_unique_companies(bills))
        
    def test_display_bill_count(self):
        bills = read_bills()
        self.assertEqual(20, display_bill_count(bills))
    
    def test_avg_time_between_bills(self):
        bills = read_bills()
        self.assertEqual(57.2, avg_time_between_bills(bills))

if __name__ == '__main__':
    unittest.main()