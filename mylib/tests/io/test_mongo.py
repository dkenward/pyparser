import unittest
import mylib


class MongoTest(unittest.TestCase):
    
    def test_init(self):
        db = mylib.mongo_manager()
        db.connect("test")
        
        

    
    
if __name__ == "__main__":
    unittest.main()