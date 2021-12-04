import requests
import pandas as pd
from datetime import date
import os

url = 'https://tradingeconomics.com/calendar'
home_path = os.getcwd()
path = 'macro_data'

def get_data(verbose=True, export=False):
    r = requests.get(url).text
    df = pd.read_html(r)[1]
    df.columns = [df.columns[0][0], 'Country', 'Event', 'Actual', 
                  'Previous', 'Consensus', 'Forecast', 'drop', 'drop']
    if verbose == True:
        pd.set_option('display.max_row', None)
    if export == True:
        f_name = date.today()
        os.chdir(path)
        df.to_csv(f'Macro_{f_name}.csv')
        os.chdir(home_path)
    return df

    
    
