# filepath: data_wrangling/abbreviations.py

import pandas as pd 

# Goal: Use inherit form DatFrame and creat our own custom DF class 

class CustomFrame(pd.DataFrame):
    """
    Params my_df (pd.DataFrame) with column called "abbrev" which has state abbrevs
    """

    def convert_names(self):
        """
        Creates a new column called "state_name" which has the corresponding state name
        """
        
        names_map = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
            }
        # print(type(self.df["abbrev"])) #> <class 'pandas.core.series.Series'>
        self["state_name"] = self["abbrev"].map(names_map)
        # return self.df


if __name__ == "__main__":
    
    custom_df = CustomFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    print(custom_df.head())
    
    custom_df.convert_names()
    print(custom_df.head())
    
    # transformer = DataTransformer(df)
    # print(transformer.df.head())
    # transformer.convert_names() # mutate df in place
    # print(transformer.df.head())

    # to initialize two dfs follow same method on a new df. 


