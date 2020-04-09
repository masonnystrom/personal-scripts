# test customerframe function

import unittest

from data_wrangling.abbreviations import CustomFrame 

class TestCustomFrame(unittest.TestCase):

    def test_name_conversion(self):
        # self.arrertEqual 
        custom_df = CustomFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        
        self.assertEqual(custom_df.columns.tolist(), ['abbrev'])
        custom_df.convert_names()
        self.assertEqual(custom_df.columns.tolist(), ['abbrev', 'state_name'])  


if __name__ == '__main__':
    unittest.main()
