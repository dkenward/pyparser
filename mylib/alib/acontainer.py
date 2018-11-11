'''
Created on Nov 10, 2018

@author: Dusten Kenward
'''
from mylib.alib import *

class AContainer():
    '''
    A Container to hold multiple ASubContainers
    
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
        frames = AParser.parse(data)
        pass
    
    
    