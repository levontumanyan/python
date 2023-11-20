import monthly_invoice
import unittest

class TestMonthlyInvoice(unittest.TestCase):
    def test_validate_year(self):
        self.assertTrue(monthly_invoice.validate_year("2021"))
        self.assertFalse(monthly_invoice.validate_year("202"))
        self.assertFalse(monthly_invoice.validate_year("20212"))
        self.assertFalse(monthly_invoice.validate_year("2021a"))
        self.assertFalse(monthly_invoice.validate_year("2021 "))

    def test_validate_month(self):
        self.assertTrue(monthly_invoice.validate_month("01"))
        self.assertTrue(monthly_invoice.validate_month("12"))
        self.assertFalse(monthly_invoice.validate_month("1"))
        self.assertFalse(monthly_invoice.validate_month("13"))
        self.assertFalse(monthly_invoice.validate_month("a"))
        self.assertFalse(monthly_invoice.validate_month(" "))
        self.assertFalse(monthly_invoice.validate_month(""))
        self.assertFalse(monthly_invoice.validate_month("  "))
    
    def test_generate_filename(self):
        self.assertEqual(monthly_invoice.generate_filename("01", "2021"), "Levon_Tumanyan_01_2021.xlsx")
        self.assertEqual(monthly_invoice.generate_filename("12", "2021"), "Levon_Tumanyan_12_2021.xlsx")
        self.assertEqual(monthly_invoice.generate_filename("01", "2022"), "Levon_Tumanyan_01_2022.xlsx")
        self.assertEqual(monthly_invoice.generate_filename("12", "2022"), "Levon_Tumanyan_12_2022.xlsx")
        self.assertEqual(monthly_invoice.generate_filename("01", "2023"), "Levon_Tumanyan_01_2023.xlsx")