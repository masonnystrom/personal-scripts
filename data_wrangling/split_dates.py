import pandas as pd 

#rename the the date column to 'date' before performing. 

# function takes a dataframe and returns the df with day, month, year columns
def split_dates(X):

    # convert to datetime format 
    X['date'] = pd.to_datetime(X['date'], infer_datetime_format=True)

    # split into day, month, year columns
    X['day'] = X['date'].dt.day 
    X['month'] = X['date'].dt.month
    X['year'] = X['date'].dt.year 

    # drop original date column
    X = X.drop(columns = 'date')

    # return the dataframe 
    return X

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    X = (input("Please choose a dataframe with the DD/MM/YYYY labeled as date"))
    result = split_dates(X)
    print(result)
