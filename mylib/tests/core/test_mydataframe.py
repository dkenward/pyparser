import unittest
import numpy as np
from mylib import MyDataFrame

class MyDataFrameTest(unittest.TestCase):
    def test_frames_empty(self):
        """
        When the dataframe is initiated the data should be empty
        """
        mdf = MyDataFrame("test")
        self.assertFalse(mdf.frames)
        
    def test_update_frames(self):
        test_data = np.random.randint(0,256,size=(100,4))
        mdf=MyDataFrame("test",test_data)
        self.assertEqual((100,4), mdf.frames.shape)
        
        
        
if __name__=="__main__":
    unittest.main()