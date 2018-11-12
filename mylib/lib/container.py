'''
Created on Nov 10, 2018

@author: Dusten Kenward
'''
import mylib.lib.container_template
import mylib.io

class Container(container_template):
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
        frames = io.read_data()(data)
        pass
    
    