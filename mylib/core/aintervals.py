from mylib.io.parsers import *

class Interval():
    
    def __init__(self):
        pass
    
    
    ''' 
    File with start and stop times of an event/series of events.
    '''
    @classmethod
    def from_csv(cls):
        '''
        JSON:
        {
            
            Intervals : [
                {
                    ID:int [number in sequence],
                    Name: String, 
                    Start:Datetime,
                    Stop:Datetime
                }, ...
            
        }
        '''
        
