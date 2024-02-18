# DATA SOURCE CLASS

import pandas as pd


class DataSource:
    
    def fetch_data(self):
        
        
        # <TODO> implement me:
        # Fetch historical XAU/USD DATA
        file = ('./XAUUSD_052021_022024.csv')
        df = pd.read_csv(file)
        # later make it automatic
        # RETURN DATA IN DATAFRAME FORMAT


