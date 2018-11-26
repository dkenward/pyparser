'''
Created on Nov 10, 2018

@author: Dusten Kenward
'''
from mylib.core.generic import Container_Template


class MyDataFrame(Container_Template):
    '''
    A Container to hold multiple SubContainers
    
    >>> cont = AContainer(data)
    >>> cont.frames()
    {("set1",frame1),
     ("set2",frame2)}
    '''
    _frames = {}
    _groups = []
    _name = None
    
    def __init__(self,name='DefaultFrame',data=None):
        ''' Creates a new container 
        :param data: data to be parsed
        '''
        self.name = name
        self.frames=data
        pass
    
    
    @property
    def frames(self):
        return self._frames
    
    @frames.setter
    def frames(self, data):
        self._frames = data
    
    @property
    def shape(self):
        #TODO: have this return the row,col (or other dim) from individual getters
        #e.g. return (self._frame_count,self._col_count)
        return self._frames.shape