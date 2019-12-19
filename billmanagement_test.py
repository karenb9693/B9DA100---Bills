import unittest

from billmanagement import get_message,read_bills, write_bills, display_bill_count,display_unique_companies
    #get_value_CredDeb, get_display_info,get_creddeb_year

class TestBillManagement(unittest.TestCase):

    def test_read_bills(self):
        bills = read_bills()
        self.assertEqual(20, len(bills))
        self.assertEqual('Electric Ireland', bills[0][0])
        self.assertEqual('credit', bills[19][6])

    def test_write_bills(self):
        bills = read_bills()
        write_bills(bills)
        self.assertEqual(20, len(bills))
        self.assertEqual('Electric Ireland', bills[0][0])
        self.assertEqual('credit', bills[19][6])

    def test_get_message(self):
        self.assertEqual('Hello, Welcome to the Bill Management Company\n' + \
                         '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit',
            get_message())
        
    def test_display_info(self):
        bills = read_bills()
        self.assertEqual(20, len(bills))
     #   self.assertEqual(None, display_info(bills))
        
    def test_display_bill_count(self):
        bills = read_bills()
        self.assertEqual(20, len(bills))

    def test_display_unique_companies(self):
        bills = read_bills()
        self.assertEqual(3, display_unique_companies(bills))

        
    #def test_display_info(self):
     #   self.assertEqual()      

#    def test_display_info(self):
 #       self.assertEqual()  

if __name__ == '__main__':
    unittest.main()