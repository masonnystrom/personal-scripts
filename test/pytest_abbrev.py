# name of tests and functions matters with pytest
from data_wrangling.abbreviations import CustomFrame 

def test_name_conversion():
    custom_df = CustomFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    #self.assertEqual(custom_df.columns.tolist(), ["abbrev"])
    assert custom_df.columns.tolist() == ["abbrev"]

    custom_df.convert_names()
    #self.assertEqual(custom_df.columns.tolist(), ["abbrev", "state_name"])
    assert custom_df.columns.tolist() == ["abbrev", "state_name"]

    # todo: consider also testing the actual values (perhaps the first row)
