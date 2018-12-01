import numpy as np
import pandas as pd

class AParser():
    def __init__(self,data):
        pass
        
    
    
    def parse(self,data):
        df = pd.DataFrame(data)
        return df
    
def read_mydata(data):
    from io import BytesIO
    a=BytesIO(b"01:00:00.100Z 2 3 4 \n 02:00:00.010Z 6 7 8")
    def dateparse(time):
        import dateutil
        return dateutil.parser.parse("2018-01-01"+"T"+time)
    data=pd.read_csv(BytesIO(data),delim_whitespace=True,parse_date={"date":0},date_parser=dateparse,index_col='date')
    
    return data

def read_table(table):
    return table