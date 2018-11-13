class Interval():
    ''' 
    File with start and stop times of an event/series of events.
    '''
    @classmethod
    def from_csv(cls):
        '''
        JSON:
        {
            Intervals : {
                Interval : {
                    Start:Datetime,
                    Stop:Datetime
                }
            }
        }