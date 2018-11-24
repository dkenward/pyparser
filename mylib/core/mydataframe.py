'''
Created on Nov 10, 2018

@author: Dusten Kenward
'''
from mylib.core.generic import Container_Template
import mylib


class MyDataFrame(Container_Template):
    '''
    A Container to hold multiple SubContainers
    
    >>> cont = AContainer(data)
    >>> cont.frames()
    {("set1",frame1),
     ("set2",frame2)}
    '''
    frames = {}
    groups = []
    
    def __init__(self,data):
        ''' Creates a new container 
        :param data: data to be parsed
        '''
        frames = mylib.read_mydata(data)
        pass
    
    
    
