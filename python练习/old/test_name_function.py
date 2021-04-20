# coding = utf-8
# author = mochacha
# date = 2020.12.15

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('liu', 'xuyang')
        self.assertEqual(formatted_name, 'Liu Xuyang')
    
    def test_full_name(self):
        formatted_name = get_formatted_name('liu', 'yang', middle='xu')
        self.assertEqual(formatted_name, 'liu xu yang')
        self.assertEqual(a, b)  # 核实 a == b
        self.assertNotEqual(a, b) # 核实 a != b
        self.assertTrue(x) # 核实x为True
        self.assertFalse(x) # 核实x为false
        self.assertIn(item, list) # 核实item在list中
        self.assertNotIn(item, list) #核实item不在list中 
        

if __name__ == "__main__":
    unittest.main()
    
