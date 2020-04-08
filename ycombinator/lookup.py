import pandas as pd 


class yc_company(object):
    def __init__(self, yc_cohort, company, website,exit_value, total_funding):
        self.yc_cohort = yc_cohort
        self.company = company
        self.website = website
        self.exit_value = exit_value 
        self.total_funding = total_funding

#define some companies 
yc = pd.read_csv('yc.csv')

# def lookup(company):